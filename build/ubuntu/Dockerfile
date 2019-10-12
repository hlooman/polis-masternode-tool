FROM ubuntu:17.10
MAINTAINER \
[Bertrand256 <bertrand256gh@protonmail.com>]
RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get -y install libudev-dev libusb-1.0-0-dev libfox-1.6-dev autotools-dev autoconf automake libtool libpython3-all-dev python3.6-dev python3-pip git cmake \
 && pip3 install virtualenv \
 && cd ~ \
 && mkdir pmt \
 && cd pmt \
 && virtualenv -p python3 venv \
 && . venv/bin/activate \
 && pip install --upgrade setuptools \
 && git clone https://github.com/Bertrand256/polis-masternode-tool \
 && cd polis-masternode-tool/ \
 && pip install -r requirements.txt \
 && cd ~/pmt \
 && echo "#!/bin/sh" | tee build-pmt.sh \
 && echo "cd ~/pmt" | tee -a build-pmt.sh \
 && echo ". venv/bin/activate" | tee -a build-pmt.sh \
 && echo "cd polis-masternode-tool" | tee -a build-pmt.sh \
 && echo "git fetch --all" | tee -a build-pmt.sh \
 && echo "git reset --hard origin/master" | tee -a build-pmt.sh \
 && echo "pip install -r requirements.txt" | tee -a build-pmt.sh \
 && echo "pyinstaller --distpath=../dist/linux --workpath=../dist/linux/build polis_masternode_tool.spec" | tee -a build-pmt.sh \
 && echo "cd .." | tee -a build-pmt.sh \
 && chmod +x build-pmt.sh

CMD ~/pmt/build-pmt.sh
