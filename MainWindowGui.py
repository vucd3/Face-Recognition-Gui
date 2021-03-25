# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from AddFaceGui import AddFace
from DetectFaceGui import DetectFace
from DeleteFaceGui import DeleteFace

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)

        font = QtGui.QFont('Arial', 12, QtGui.QFont.Bold)

        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 320, 41, 17))
        self.label.setObjectName("label")
        self.label.setFont(font)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(380, 360, 41, 17))
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(font)

        self.date = QtWidgets.QTextBrowser(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(440, 310, 181, 31))
        self.date.setObjectName("date")
        self.date.setFont(font)

        self.time = QtWidgets.QTextBrowser(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(440, 350, 181, 31))
        self.time.setObjectName("time")
        self.time.setFont(font)

        self.add_face = QtWidgets.QPushButton(self.centralwidget)
        self.add_face.setGeometry(QtCore.QRect(100, 170, 191, 71))
        self.add_face.setObjectName("add_face")
        self.add_face.setStyleSheet("background-color: red")

        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(850, 480, 151, 61))
        self.quit.setObjectName("quit")
        self.quit.setStyleSheet("background-color: red")

        self.textBrowser = QtWidgets.QLabel(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(310, 40, 471, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: yellow")

        self.detect_face = QtWidgets.QPushButton(self.centralwidget)
        self.detect_face.setGeometry(QtCore.QRect(420, 170, 191, 71))
        self.detect_face.setObjectName("detect_face")
        self.detect_face.setStyleSheet("background-color: red")

        self.delete_face = QtWidgets.QPushButton(self.centralwidget)
        self.delete_face.setGeometry(QtCore.QRect(720, 170, 191, 71))
        self.delete_face.setObjectName("delete_face")
        self.delete_face.setStyleSheet("background-color: red")

        MainWindow.setCentralWidget(self.centralwidget)

        self.add_face_gui = QtWidgets.QMainWindow()
        self.detect_face_gui = QtWidgets.QMainWindow()
        self.delete_face_gui = QtWidgets.QMainWindow()

        self.title = "<span style=\" font-size:22pt; font-weight:600; color:#ff0000;\" >"
        self.title += "FACE DETECTION SYSTEM"
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_face.clicked.connect(self.addface)
        self.detect_face.clicked.connect(self.detectface)
        self.delete_face.clicked.connect(self.deleteface)

        self.quit.clicked.connect(self.quitGui)

        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.displayTime)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FACE DETECTION SYSTEM"))
        self.add_face.setText(_translate("MainWindow", "ADD FACE"))
        self.textBrowser.setText(_translate("MainWindow", self.title))
        self.detect_face.setText(_translate("MainWindow", "DETECT FACE"))
        self.delete_face.setText(_translate("MainWindow", "DELETE FACE"))

        self.label.setText(_translate("MainWindow", "DATE"))
        self.label_1.setText(_translate("MainWindow", "TIME"))
        self.date.setText(_translate("MainWindow", ""))
        self.time.setText(_translate("MainWindow", ""))
        self.quit.setText(_translate("MainWindow", "QUIT"))
    
    def displayTime(self):
        current_time = QtCore.QTime.currentTime()
        current_date = QtCore.QDate.currentDate()

        self.time.setText(current_time.toString())
        self.date.setText(current_date.toString())

    def addface(self):
        self.add_face_ui = AddFace()
        self.add_face_ui.setupUi(self.add_face_gui)
        self.add_face_gui.show()
    
    def detectface(self):
        self.detect_face_ui = DetectFace()
        self.detect_face_ui.setupUi(self.detect_face_gui)
        self.detect_face_gui.show()
    
    def deleteface(self):
        self.delete_face_ui = DeleteFace()
        self.delete_face_ui.setupUi(self.delete_face_gui)
        self.delete_face_gui.show()

    def quitGui(self):
        self.MainWindow.close()
        self.add_face_gui.close()
        self.detect_face_gui.close()
        self.delete_face_gui.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
