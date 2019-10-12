#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Bertrand256
# Created on: 2018-03
import collections
import logging
from typing import List

APP_NAME_SHORT = 'PolisMasternodeTool'
APP_NAME_LONG = 'Polis Masternode Tool'
APP_DATA_DIR_NAME = '.pmt'
PROJECT_URL = 'https://github.com/hlooman/polis-masternode-tool'
FEE_DUFF_PER_BYTE = 1
MIN_TX_FEE = 1000
SCREENSHOT_MODE = False
DEBUG_MODE = False
DEFAULT_LOG_FORMAT = '%(asctime)s %(levelname)s|%(name)s|%(threadName)s|%(filename)s|%(funcName)s|%(message)s'
KnownLoggerType = collections.namedtuple('KnownLoggerType', 'name external')
APP_PATH = ''
APP_IMAGE_DIR = ''


class HWType:
    trezor = 'TREZOR'
    keepkey = 'KEEPKEY'
    ledger_nano_s = 'LEDGERNANOS'

    @staticmethod
    def get_desc(hw_type):
        if hw_type == HWType.trezor:
            return 'Trezor'
        elif hw_type == HWType.keepkey:
            return 'KeepKey'
        elif hw_type == HWType.ledger_nano_s:
            return 'Ledger Nano S'
        else:
            return '???'


def get_note_url(note_symbol):
    """
    Returns an URL to a project documentation page related to the note symbol passed as an argument.
    :param note_symbol: Symbol of the note, for example: PMT00001
    :return: URL
    """
    return PROJECT_URL + f'/blob/master/doc/notes.md#note-{note_symbol.lower()}'


def get_doc_url(doc_file_name):
    """
    Returns an URL to a project documentation page.
    :return: URL
    """
    return PROJECT_URL + f'/blob/master/doc/{doc_file_name}'


__KNOWN_LOGGERS = [
    KnownLoggerType(name='pmt.wallet_dlg', external=False),
    KnownLoggerType(name='pmt.bip44_wallet', external=False),
    KnownLoggerType(name='pmt.polisd_intf', external=False),
    KnownLoggerType(name='pmt.db_intf', external=False),
    KnownLoggerType(name='pmt.proposals', external=False),
    KnownLoggerType(name='pmt.ext_item_model', external=False),
    KnownLoggerType(name='pmt.hw_intf_trezor', external=False),
    KnownLoggerType(name='pmt.reg_masternode', external=False),
    KnownLoggerType(name='pmt.transaction_dlg', external=False),
    KnownLoggerType(name='pmt.app_cache', external=False),
    KnownLoggerType(name='BitcoinRPC', external=True),
    KnownLoggerType(name='urllib3.connectionpool', external=True),
    KnownLoggerType(name='trezorlib.transport', external=True),
    KnownLoggerType(name='trezorlib.transport.bridge', external=True),
    KnownLoggerType(name='trezorlib.client', external=True),
    KnownLoggerType(name='trezorlib.protocol_v1', external=True),
]


def get_known_loggers() -> List[KnownLoggerType]:
    ll = []
    # add existing loggers which are not known: some new libraries (or new versions) can intruduce new
    # loggers
    for lname in logging.Logger.manager.loggerDict:
        l = logging.Logger.manager.loggerDict[lname]
        if isinstance(l, logging.Logger):
            if not any(lname in name for name in __KNOWN_LOGGERS):
                __KNOWN_LOGGERS.append(KnownLoggerType(name=lname, external=True))
    return __KNOWN_LOGGERS[:]
