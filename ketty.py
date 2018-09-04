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
import time
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
    def SetTaskList(self):
        self.task_list=[["Englisth", "page11 to page 12 ","","Start"],\
		        ["Chinese", "page 12-12 recsite ","","Start"],\
		        ["Math", "Read all the documents","","Start"],\
		        ["Math", "Read all the documents","","Start"],\
		        ["Math", "Read all the documents","","Start"],\
		        ["Math", "Read all the documents","","Start"],\
		       ]

        
    def initUI(self):               
	self.currentTaskId=-1
        self.SetTaskList()
        self.resize(1280, 800)
        self.setWindowTitle(self.icon_title)
        self.setWindowIcon(QtGui.QIcon(self.icon_image))
        self.center()
        self.welcomeMsg()
        self.taskListInit()
        self.TimerStart()
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def buttonForRow(self,id,name):
        widget=QtGui.QWidget()
        updateBtn = QtGui.QPushButton(name)
        updateBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        updateBtn.clicked.connect(lambda:self.taskStartEnd(id))

        viewBtn = QtGui.QPushButton('view')
        viewBtn.setStyleSheet(''' text-align : center;
                                  background-color : DarkSeaGreen;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')

        viewBtn.clicked.connect(lambda: self.viewTable(id))

        deleteBtn = QtGui.QPushButton('delete')
        deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')
        hLayout = QtGui.QHBoxLayout()
        hLayout.addWidget(updateBtn)
        #hLayout.addWidget(viewBtn)
        #hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)
        return widget
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
        self.lcdNumber = QtGui.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(600, 600, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setNumDigits(8)
        self.lcdNumber.setMode(QtGui.QLCDNumber.Bin)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.display("00:00:00")
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateDisplay)
    def taskStartEnd(self,i):
        self.startTime=time.time()
        self.timer.start(1000)
        print(self.sender().text())
        if self.sender().text()=="Start":
            self.sender().setText("Stop")
            self.task_list[int(i)][3]="Stop"
        else:
            self.sender().setText("Start")
            self.task_list[int(i)][3]="Start"
        self.task_list[int(i)][2]=time.strftime("%m/%d %H:%M:%S", time.localtime())
	self.currentTaskId=int(i)
    def SetTaskList(self):
        self.task_list=[["Englisth", "page11 to page 12 ","","Start"],\
		        ["Chinese", "page 12-12 recsite ","","Start"],\
		        ["Math", "Read all the documents","","Start"],\
		        ["Math", "Read all the documents","","Start"],\
			]
    def updateDisplay(self):
        timecost=time.time()-self.startTime
        hours=int(timecost/3600)
        minutes=int((timecost-hours*3600)/60)
        seconds=timecost%60
        text = "%02d:%02d:%02d" % (hours,minutes,seconds)
        self.lcdNumber.display(text)
        self.timer = QtCore.QTimer(self)
        self.updateTaskList()
        self.timer.timeout.connect(self.updateDisplay)
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
        self.updateTaskList()
    def updateTaskList(self):
	rowid=self.currentTaskId
        #self.widget_task_list.clear()
        print(list(enumerate(self.task_list)))
        for row_number, row_data in enumerate(self.task_list):
            #self.widget_task_list.insertRow(row_number)
            #if row is -1 then update all the list
	    if rowid==-1 or rowid==row_number:
		pass
            else:
                continue
                
            for i in range(len(row_data)+1):
                if i<len(row_data):
                    self.widget_task_list.setItem(row_number, i, QtGui.QTableWidgetItem(str(row_data[i])))
                if i==len(row_data):
                    self.widget_task_list.setCellWidget(row_number, i,self.buttonForRow(str(row_number),str(row_data[-1])))
        #self.widget_task_list.resizeColumnsToContents()
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
