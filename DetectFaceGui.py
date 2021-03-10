# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetectFaceGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import face_recognition
import imutils
import time
import pickle

class DetectFace(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 621)

        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 551, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(6)
        self.frame.setObjectName("frame")

        self.text = QtWidgets.QTextBrowser(self.frame)
        self.text.setGeometry(QtCore.QRect(180, 10, 151, 51))
        self.text.setObjectName("text")

        self.webcam = QtWidgets.QLabel(self.frame)
        self.webcam.setGeometry(QtCore.QRect(50, 90, 431, 371))
        self.webcam.setText("")
        self.webcam.setObjectName("webcam")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(610, 20, 301, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(90, 10, 111, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 51, 17))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 51, 17))
        self.label_3.setObjectName("label_3")

        self.time = QtWidgets.QTextBrowser(self.frame_2)
        self.time.setGeometry(QtCore.QRect(90, 100, 181, 31))
        self.time.setObjectName("time")

        self.name = QtWidgets.QTextBrowser(self.frame_2)
        self.name.setGeometry(QtCore.QRect(90, 50, 181, 31))
        self.name.setObjectName("name")

        self.detect = QtWidgets.QPushButton(self.centralwidget)
        self.detect.setGeometry(QtCore.QRect(30, 530, 551, 31))
        self.detect.setObjectName("detect")
        self.detect.setStyleSheet("background-color: red")

        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(820, 520, 111, 41))
        self.quit.setObjectName("quit")
        self.quit.setStyleSheet("background-color: red")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.title = "<span style=\" font-size:22pt; font-weight:600; color:#ff0000;\" >"
        self.title += "WEBCAM"

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.capture=cv2.VideoCapture(0)
        self.timer=QtCore.QTimer()
        self.timer.start(2)
        self.timer.timeout.connect(self.update_frame)
        
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        self.face_Enabled = False

        self.detect.setCheckable(True)
        self.detect.toggled.connect(self.detect_webcam_face)
        self.quit.clicked.connect(self.quitGui)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DETECT FACE"))
        self.text.setHtml(_translate("MainWindow", self.title))
        self.label.setText(_translate("MainWindow", "INFORMATION"))
        self.label_2.setText(_translate("MainWindow", "NAME"))
        self.label_3.setText(_translate("MainWindow", "TIME"))
        self.detect.setText(_translate("MainWindow", "DETECT FACE"))
        self.quit.setText(_translate("MainWindow", "QUIT"))

    def detect_webcam_face(self,status):
        if status:
            self.detect.setText('STOP DETECTION')
            self.face_Enabled = True
        else:
            self.detect.setText('DETECT FACE')
            self.face_Enabled = False

    def update_frame(self):
        _, self.image=self.capture.read()
        if self.face_Enabled:
            image_detected = self.detect_face(self.image)
            self.displayImage(image_detected)
        else:
            self.displayImage(self.image)

    def displayImage(self,img):
        outImage=QtGui.QImage(img,img.shape[1],img.shape[0],img.strides[0],QtGui.QImage.Format_RGB888)

        outImage=outImage.rgbSwapped()
      
        self.webcam.setPixmap(QtGui.QPixmap.fromImage(outImage))
        self.webcam.setScaledContents(True)

    def detect_face(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        data = pickle.loads(open("encodings.pickle", "rb").read())

        faces = self.face_cascade.detectMultiScale(gray,scaleFactor = 1.1, 
        minNeighbors=5, minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE)

        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in faces]

        encodings = face_recognition.face_encodings(rgb, boxes)

        names = []
        name  = ""
        
        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
            
            name = "Unknown"

            if True in matches:
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                name = max(counts, key=counts.get)

            names.append(name)

        for ((top, right, bottom, left), name) in zip(boxes, names):
            cv2.rectangle(img, (left, top), (right, bottom),
                (0, 255, 0), 5)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(img, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 5)

        self.name.setText(name)

        return img
 
    def quitGui(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()
        self.MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DetectFace()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
