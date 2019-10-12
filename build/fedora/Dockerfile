FROM fedora
MAINTAINER \
[Bertrand256 <bertrand256gh@protonmail.com>]
RUN yum update -y \
 && yum group install -y "Development Tools" "Development Libraries" \
 && yum install -y redhat-rpm-config python3-devel libusbx-devel libudev-devel cmake gcc-c++ \
 && yum remove -y gmp-devel \
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
 && set +H \
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
