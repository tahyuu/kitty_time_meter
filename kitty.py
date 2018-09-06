#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: Yong Tan
"""

import sys
from PyQt4 import QtGui,QtCore
import time
import datetime
import codecs
#reload(sys)
#sys.setdefaultencoding('utf-8')


try:
    import configparser 
except:
    import ConfigParser as configparser 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.cf=configparser.ConfigParser()
        self.tsk=configparser.ConfigParser()
        #self.cf.read("config.ini")
        self.cf.readfp(codecs.open('Config.ini', "r", "utf-8"))
        self.tsk.readfp(codecs.open('task.ini', "r", "utf-8"))
        self.language=self.cf.get('system','language')
        #self.icon_image='Hello_Kitty.jpg'
        self.icon_image=self.cf.get("system","icon_image")
        #self.icon_title='time-meter'
        self.icon_title=self.cf.get(self.language,'icon_title_text')
        self.start_text=self.cf.get(self.language,'start_text')
        self.ongoing_text=self.cf.get(self.language,'ongoing_text')
        self.finished_text=self.cf.get(self.language,'finished_text')
        self.initUI()
    def SetTaskList(self):
        self.task_list=[]
        self.task_list_str=(self.tsk.get('abc','task_list'))
        #print self.task_list_str
        for li in self.task_list_str.split(";"):
            if li:
                l2=[]
                l=li.split(",")
                for s in l:
                    s=_fromUtf8(s)
                    l2.append(s)
                l2.extend(["","","",_fromUtf8(self.start_text)])
                self.task_list.append(l2)
        #self.task_list.reverse()

    def initUI(self):               
        self.currentTaskId=-1
        self.justSender=None
        self.SetTaskList()
        self.resize(1280, 800)
        self.setWindowTitle(self.icon_title)
        self.setWindowIcon(QtGui.QIcon(self.icon_image))
        self.center()
        #self.welcomeMsg()
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
                                          background-color : Red;
                                          height : 30px;
                                          border-style: outset;
                                          font : 30px  ''')
        #updateBtn.setStyleSheet(''' text-align : center;
        #                                  background-color : NavajoWhite;
        #                                  height : 30px;
        #                                  border-style: outset;
        #                                  font : 30px  ''')

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
        self.lcdNumber.setGeometry(QtCore.QRect(10, 500, 1250, 280))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setNumDigits(8)
        self.lcdNumber.setMode(QtGui.QLCDNumber.Bin)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.setStyleSheet('''text-align : center;
                                    background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateDisplay)
    def taskStartEnd(self,i):
        self.currentIndex=i
        if self.sender().text()==self.start_text or self.sender().text()==self.finished_text:
            self.startTime=time.time()
            if self.sender().text()==self.start_text:
                self.startTime=time.time()
                self.task_list[int(i)][2]=time.strftime("%H:%M:%S", time.localtime())
            self.sender().setText(self.ongoing_text)
            self.sender().setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 30px  ''')
            self.timer.start(1000)
        else:
            self.sender().setText(self.finished_text)
            self.task_list[int(i)][3]=time.strftime("%H:%M:%S", time.localtime())
            #self.startTime=time.mktime(time.strptime(time.strftime("%Y/%m/%d ",time.localtime())+self.task_list[int(i)][2],"%Y/%m/%d %H:%M:%S"))
            #self.startTime=time.time()
            timecost=time.time()-self.startTime
            if self.task_list[int(i)][4]!="":
                timecost=timecost+int(self.task_list[int(i)][4])
            hours=int(timecost/3600)
            minutes=int((timecost-hours*3600)/60)
            seconds=timecost%60
            text = "%02d:%02d:%02d" % (hours,minutes,seconds)
            self.lcdNumber.display(text)
            self.task_list[int(i)][4]=str(int(timecost))
            self.sender().setStyleSheet(''' text-align : center;
                                          background-color : rgb(138,226,52);
                                          height : 30px;
                                          border-style: outset;
                                          font : 30px  ''')
            self.timer.stop()
            self.updateTaskList()
        self.currentTaskId=int(i)
    def updateDisplay(self):
        i=self.currentIndex
        timecost=time.time()-self.startTime
        if self.task_list[int(i)][4]!="":
            timecost=timecost+int(self.task_list[int(i)][4])
        hours=int(timecost/3600)
        minutes=int((timecost-hours*3600)/60)
        seconds=timecost%60
        text = "%02d:%02d:%02d" % (hours,minutes,seconds)
        self.lcdNumber.display(text)
        self.updateTaskList()
    def taskListInit(self):
        self.widget_task_list= QtGui.QTableWidget(self)
        self.widget_task_list.setGeometry(QtCore.QRect(10,10,1250, 490))
        self.widget_task_list.setObjectName(_fromUtf8("#table"))
        self.widget_task_list.clear()
        self.widget_task_list.setRowCount(10)
        self.widget_task_list.setColumnCount(6)
        self.widget_task_list.setHorizontalHeaderLabels([self.cf.get(self.language,'subject_text'),self.cf.get(self.language,'descrip_text'),self.cf.get(self.language,'startTime_text') ,
                self.cf.get(self.language,'endTime_text'), self.cf.get(self.language,'timeCost_text'),self.cf.get(self.language,'status_text')])
        self.widget_task_list.setAlternatingRowColors(True)
        self.widget_task_list.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.widget_task_list.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
        self.widget_task_list.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.widget_task_list.setStyleSheet(''' text-align : center;
                                          height : 30px;
                                          border-style: outset;
                                          font : 30px  ''')
        header = self.widget_task_list.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(4, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(5, QtGui.QHeaderView.ResizeToContents)
        for i in range(10):
            self.widget_task_list.setRowHeight(i,50)
        #self.widget_task_list.setRowHeight(0,40)
        stylesheet = "::section{Background-color:#A640BF;border-radius:4px;}"
        self.widget_task_list.horizontalHeader().setStyleSheet(stylesheet)
        self.updateTaskList()
    def updateTaskList(self):
        rowid=self.currentTaskId
        #self.widget_task_list.clear()
        #print(list(enumerate(self.task_list)))
        for row_number, row_data in enumerate(self.task_list):
            #self.widget_task_list.insertRow(row_number)
            #if row is -1 then update all the list
            #self.widget_task_list.setRowHeight(row_number,50)
            if rowid==-1 or rowid==row_number:
                pass
            else:
                continue
                
            for i in range(len(row_data)+1):
                if i<len(row_data)-1:
                    self.widget_task_list.setItem(row_number, i, QtGui.QTableWidgetItem(str(row_data[i])))
                if i==len(row_data)-1:
                    #when the rowid==-1, that means the first time we just need to update add the button
                    if rowid==-1:
                    	self.widget_task_list.setCellWidget(row_number, i,self.buttonForRow(str(row_number),str(row_data[-1])))
        #self.widget_task_list.resizeColumnsToContents()
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
