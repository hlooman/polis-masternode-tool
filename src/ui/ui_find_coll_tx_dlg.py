# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/PMT-git/src/ui/ui_find_coll_tx_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListCollateralTxsDlg(object):
    def setupUi(self, ListCollateralTxsDlg):
        ListCollateralTxsDlg.setObjectName("ListCollateralTxsDlg")
        ListCollateralTxsDlg.resize(655, 286)
        ListCollateralTxsDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListCollateralTxsDlg)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMessage = QtWidgets.QLabel(ListCollateralTxsDlg)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.collsTableView = QtWidgets.QTableView(ListCollateralTxsDlg)
        self.collsTableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.collsTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.collsTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.collsTableView.setShowGrid(True)
        self.collsTableView.setSortingEnabled(False)
        self.collsTableView.setObjectName("collsTableView")
        self.collsTableView.verticalHeader().setVisible(False)
        self.collsTableView.verticalHeader().setCascadingSectionResizes(True)
        self.collsTableView.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.collsTableView)
        self.buttonBox = QtWidgets.QDialogButtonBox(ListCollateralTxsDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ListCollateralTxsDlg)
        QtCore.QMetaObject.connectSlotsByName(ListCollateralTxsDlg)

    def retranslateUi(self, ListCollateralTxsDlg):
        _translate = QtCore.QCoreApplication.translate
        ListCollateralTxsDlg.setWindowTitle(_translate("ListCollateralTxsDlg", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListCollateralTxsDlg = QtWidgets.QDialog()
    ui = Ui_ListCollateralTxsDlg()
    ui.setupUi(ListCollateralTxsDlg)
    ListCollateralTxsDlg.show()
    sys.exit(app.exec_())

