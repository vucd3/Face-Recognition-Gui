# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectFaceGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from skimage.feature import local_binary_pattern
import os
import cv2
import face_recognition
import imutils
import pickle
import numpy as np

class DetectFace(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)

        self.MainWindow = MainWindow

        font = QtGui.QFont('Arial', 12, QtGui.QFont.Bold)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.msg = QtWidgets.QMessageBox(self.centralwidget)
        self.msg.setWindowTitle("Message")
        self.msg.setGeometry(QtCore.QRect(230, 180, 256, 121))

        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(210, 10, 121, 31))
        self.text.setObjectName("text")
        self.text.setStyleSheet("background-color: yellow")

        self.webcam = QtWidgets.QLabel(self.centralwidget)
        self.webcam.setGeometry(QtCore.QRect(60, 50, 450, 450))
        self.webcam.setText("")
        self.webcam.setObjectName("webcam")

        self.box = QtWidgets.QGroupBox(self.centralwidget)
        self.box.setGeometry(QtCore.QRect(670, 160, 301, 221))
        self.box.setObjectName("box")
        self.box.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.box)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 51, 17))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)

        self.label_3 = QtWidgets.QLabel(self.box)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 51, 17))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.box)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 51, 17))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)

        self.time = QtWidgets.QTextBrowser(self.box)
        self.time.setGeometry(QtCore.QRect(90, 150, 181, 31))
        self.time.setObjectName("time")

        self.name = QtWidgets.QTextBrowser(self.box)
        self.name.setGeometry(QtCore.QRect(90, 50, 181, 31))
        self.name.setObjectName("name")

        self.date = QtWidgets.QTextBrowser(self.box)
        self.date.setGeometry(QtCore.QRect(90, 100, 181, 31))
        self.date.setObjectName("date")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(690, 30, 41, 17))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 80, 41, 17))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font)

        self.date_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.date_1.setGeometry(QtCore.QRect(750, 20, 161, 31))
        self.date_1.setObjectName("date1")
        self.date_1.setFont(font)

        self.time_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.time_1.setGeometry(QtCore.QRect(750, 70, 161, 31))
        self.time_1.setObjectName("time1")
        self.time_1.setFont(font)

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(60, 510, 450, 40))
        self.save.setObjectName("save")
        self.save.setStyleSheet("background-color: red")

        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(860, 470, 141, 61))
        self.quit.setObjectName("quit")
        self.quit.setStyleSheet("background-color: red")

        MainWindow.setCentralWidget(self.centralwidget)

        self.title = "<span style=\" font-size:16pt; font-weight:600; color:#ff0000;\" >"
        self.title += "WEBCAM"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.capture = cv2.VideoCapture(0)

        self.timer = QtCore.QTimer()
        self.timer.start(5)
        self.timer.timeout.connect(self.update_frame)

        self.timer_1 = QtCore.QTimer()
        self.timer_1.start(1000)
        self.timer_1.timeout.connect(self.displayTime)
        
        self.face_name = None
        self.faceEnable = None

        self.gray = None
        self.image_detected = None
        
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        self.save.clicked.connect(self.save_infor)
        self.quit.clicked.connect(self.quitGui)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DETECT FACE"))

        self.text.setText(_translate("MainWindow", self.title))
        self.box.setTitle(_translate("MainWindow", "Information"))
        self.label_2.setText(_translate("MainWindow", "NAME"))
        self.label_3.setText(_translate("MainWindow", "TIME"))
        self.label_4.setText(_translate("MainWindow", "DATE"))
        self.label_5.setText(_translate("MainWindow", "DATE"))
        self.label_6.setText(_translate("MainWindow", "TIME"))

        self.save.setText(_translate("MainWindow", "CHECK IN/CHECK OUT"))
        self.quit.setText(_translate("MainWindow", "QUIT"))

    def displayTime(self):
        current_time = QtCore.QTime.currentTime()
        current_date = QtCore.QDate.currentDate()

        self.time_1.setText(current_time.toString())
        self.date_1.setText(current_date.toString())

    def update_frame(self):
        _, self.image = self.capture.read()
        self.resize_c = cv2.resize(self.image, (1024, 600))
        self.resize = cv2.resize(self.image, (1024, 600))
        self.detect_face()
        self.displayImage(self.resize)

    def displayImage(self,img):
        outImage=QtGui.QImage(img,img.shape[1],img.shape[0],img.strides[0],QtGui.QImage.Format_RGB888)

        outImage=outImage.rgbSwapped()
      
        self.webcam.setPixmap(QtGui.QPixmap.fromImage(outImage))
        self.webcam.setScaledContents(True)
    
    def detect_face(self):
        self.gray = cv2.cvtColor(self.resize, cv2.COLOR_BGR2GRAY)
        self.faces = self.face_cascade.detectMultiScale(gray,scaleFactor = 1.1, 
            minNeighbors=5, minSize=(100, 100))
        
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.resize, (x, y), (x+w, y+h), (0, 255, 0), 5)
        
    def recognize_face(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data = pickle.loads(open("encodings.pickle", "rb").read())    

        if len(self.faces) > 0:
            self.faceEnable = True
        else:
            self.faceEnable = False

        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in self.faces]
        #boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)

        name = ""
        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
          
            name = "Unknown"
            face_distances = face_recognition.face_distance(data["encodings"], encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index] and face_distances[best_match_index] < 0.35:
                name = data["names"][best_match_index]
        return name
    
    def antispoofing(self):
        predict = ""
        lower = np.array([0, 48, 80], dtype = "uint8")
        upper = np.array([20, 255, 255], dtype = "uint8")

        for (x, y, w, h) in self.faces:
            roi = self.resize_c[y:y+h, x:x+w]
        
        converted = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        skinMask = cv2.erode(skinMask, kernel, iterations = 1)

        skinMask = cv2.dilate(skinMask, kernel, iterations = 1)

        skinMask = cv2.GaussianBlur(skinMask, (5, 5), 0)
        skin = cv2.bitwise_and(roi, roi, mask = skinMask) 
        

        if np.count_nonzero(skin) > 20000 and roi.shape[0] < 350 and roi.shape[1] < 350:
            predict = "real_face"
        else:
            predict = "fake_face"

        return predict

    def save_infor(self):
        self.name .setText("")
        self.time.setText("")
        self.date.setText("")
        
        predict = self.antispoofing()
        name = self.recognize_face(self.resize_c)

        current_date = QtCore.QDate.currentDate()
        current_time = QtCore.QTime.currentTime()
        
        if self.faceEnable:
            if predict == "real_face":
                if name != "Unknown" and name != "":
                    self.name .setText(name)
                    self.time.setText(current_time.toString())
                    self.date.setText(current_date.toString())
                    self.save_infor_to_file(name, current_date, current_time)
                    self.msg.setText("Save your information succesfully!")
                else:
                    self.msg.setText("System can not identify your face!")
            else:
                self.msg.setText("System can not identify your face!")
        else:
            self.msg.setText("System can not detect your face!")
        self.msg.exec()
    
    def save_infor_to_file(self, name, date, time):
        f = open("information.txt", "a+")
        f.write(name + "\t\t" + date.toString() + "\t" 
        + time.toString() + "\n")

    def off_webcam(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()

    def quitGui(self):
        self.off_webcam()
        self.timer_1.stop()
        self.MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DetectFace()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
