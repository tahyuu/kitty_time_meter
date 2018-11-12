# kitty time meter system

### Introduction
the program is designed for child study time system. it can help child check how many time cost on each items of task.

### 1, install system and enviroment tools.
the program is designed on raspberry pi3. first of all we need make a raspberry system. and run below command to install enviroment.
```
sudo pip install ConfigParser
sudo pip install ps4
sudo apt-get update
sudo apt-get install python-qt4
git clone https://github.com/tahyuu/kitty_time_meter.git time_meter
```

### 2, setup enviroment
```
cd ~/time_meter
sudo inatall/install.sh
```

### 3, How to config language
update the filed language in Config/Config.ini file. you can choose chinese,english,japanese.
```
[system]
language=chinese
```

### 3, How the program looks like

![Image text](https://github.com/tahyuu/kitty_time_meter/blob/master/img/Interface.png)
