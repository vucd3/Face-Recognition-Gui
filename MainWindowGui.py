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
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: blue")
        
        self.add_face = QtWidgets.QPushButton(self.centralwidget)
        self.add_face.setGeometry(QtCore.QRect(100, 220, 131, 41))
        self.add_face.setObjectName("add_face")
        self.add_face.setStyleSheet("background-color: red")

        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(620, 460, 151, 61))
        self.quit.setObjectName("quit")
        self.quit.setStyleSheet("background-color: red")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 100, 400, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: yellow")

        self.detect_face = QtWidgets.QPushButton(self.centralwidget)
        self.detect_face.setGeometry(QtCore.QRect(340, 220, 131, 41))
        self.detect_face.setObjectName("detect_face")
        self.detect_face.setStyleSheet("background-color: red")

        self.delete_face = QtWidgets.QPushButton(self.centralwidget)
        self.delete_face.setGeometry(QtCore.QRect(580, 220, 131, 41))
        self.delete_face.setObjectName("delete_face")
        self.delete_face.setStyleSheet("background-color: red")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.title = "<span style=\" font-size:22pt; font-weight:600; color:#ff0000;\" >"
        self.title += "FACE DETECTION SYSTEM"
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_face.clicked.connect(self.addface)
        self.detect_face.clicked.connect(self.detectface)
        self.delete_face.clicked.connect(self.deleteface)

        self.quit.clicked.connect(self.quitGui)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FACE DETECTION SYSTEM"))
        self.add_face.setText(_translate("MainWindow", "ADD FACE"))
        self.textBrowser.setText(_translate("MainWindow", self.title))
        self.detect_face.setText(_translate("MainWindow", "DETECT FACE"))
        self.delete_face.setText(_translate("MainWindow", "DELETE FACE"))
        self.quit.setText(_translate("MainWindow", "QUIT"))

    def addface(self):
        self.add_face_gui = QtWidgets.QMainWindow()
        self.add_face_ui = AddFace()
        self.add_face_ui.setupUi(self.add_face_gui)
        self.add_face_gui.show()
    
    def detectface(self):
        self.detect_face_gui = QtWidgets.QMainWindow()
        self.detect_face_ui = DetectFace()
        self.detect_face_ui.setupUi(self.detect_face_gui)
        self.detect_face_gui.show()
    
    def deleteface(self):
        self.delete_face_gui = QtWidgets.QMainWindow()
        self.delete_face_ui = DeleteFace()
        self.delete_face_ui.setupUi(self.delete_face_gui)
        self.delete_face_gui.show()

    def quitGui(self):
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())