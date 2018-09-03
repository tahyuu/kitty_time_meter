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
        self.socketStyle_w_select = "#widget_msg {border: 5px outset #BF408C;padding: 5px;border-radius: 15px;}widget *{}" 
        self.initUI()
        
    def initUI(self):               
        
        self.resize(1280, 800)
        self.setWindowTitle(self.icon_title)
        self.setWindowIcon(QtGui.QIcon(self.icon_image))
        self.center()
        self.welcomeMsg()
	self.taskListInit()
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def welcomeMsg(self):
    	#set the Msg label.
        self.widget_msg=QtGui.QWidget(self)
        self.widget_msg.setObjectName(_fromUtf8("widget_msg"))

        self.widget_msg.setStyleSheet(self.socketStyle_w_select)

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
    def taskListInit(self):
        self.widget_task_list= QtGui.QTableWidget(self)
        self.widget_task_list.setGeometry(QtCore.QRect(500,0 ,580, 340))
        self.widget_task_list.setObjectName(_fromUtf8("#table"))
        self.widget_task_list.clear()
        self.widget_task_list.setRowCount(10)
        self.widget_task_list.setColumnCount(5)
        self.widget_task_list.setHorizontalHeaderLabels(["Subject", "Descript", "Status",
                "StartTime", "Time Cost"])
        self.widget_task_list.setAlternatingRowColors(True)
        self.widget_task_list.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.widget_task_list.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.widget_task_list.setSelectionMode(QtGui.QTableWidget.SingleSelection)

        task_list=[["Englisth", "page11 to page 12 read the english documents"],["Chinese", "page 12-12 recsite the documents"],["Math", "Read all the documents"]]
        i=0
        for task in task_list:
            j=0
            for task_detail in task:
                item = QtGui.QTableWidgetItem(task_detail)
                self.widget_task_list.setItem(i, j, item)
                j=j+1
            i=i+1
        self.widget_task_list.resizeColumnsToContents()


    	pass
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
