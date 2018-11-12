#!/bin/bash
sudo apt-get update
sudo apt-get install python-qt4
sudo pip install ConfigParser
sudo pip install ps4
echo "/home/pi/time_meter/install/clientStart.sh start">> /home/pi/.config/lxsession/LXDE-pi/autostart
