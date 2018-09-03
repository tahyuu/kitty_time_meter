#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program centers a window 
on the screen. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui,QtCore
#import ConfigParser 


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        #self.cf=ConfigParser.ConfigParser()
        #self.cf.read("config.ini")
        #self.icon_image=self.cf.get("system","icon_image")
        #self.icon_title=self.cf.get("system","icon_title")
        self.icon_image='Hello_Kitty.jpg'
        self.icon_title='time-meter'
        self.initUI()
        
    def initUI(self):               
        
        self.resize(1280, 800)
        self.setWindowTitle(self.icon_title)
        self.setWindowIcon(QtGui.QIcon(self.icon_image))
        self.center()
        self.welcomeMsg()
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def welcomeMsg(self):
    	#set the Msg label.
        self.widget_msg=QtGui.QWidget(self)
        self.label_msg=QtGui.QLabel(self.widget_msg)
        self.label_msg.setGeometry(QtCore.QRect(20,20,420,56))
        font=QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(100)
        font.setBold(True)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName(_fromUtf8("label"))
        self.label_msg.setText(QtGui.QApplication.translate("MainWindow","208-09-03 11:30 Monday\n Welcome home, Child",None,QtGui.QApplication.UnicodeUTF8))
    def TimerStart(self):
    	pass
    def TaskListInit(self):
    	pass
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
