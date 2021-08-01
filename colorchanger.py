from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(702, 557)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 80, 101, 81))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.red)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 80, 101, 81))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.blue)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 80, 101, 81))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.yellow)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 220, 101, 81))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.green)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 220, 101, 81))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.black)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 220, 101, 81))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.white)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 360, 101, 81))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.purple)
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 360, 101, 81))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.orange)
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 360, 101, 81))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.pink)
        self.pushButton.setStyleSheet("""
            background-color: white;
            color: red;
            """)
        self.pushButton_2.setStyleSheet("""
            background-color: white;
            color: blue;
            """)
        self.pushButton_3.setStyleSheet("""
            background-color: white;
            color: yellow;
            """)
        self.pushButton_4.setStyleSheet("""
            background-color: white;
            color: green;
            """)
        self.pushButton_5.setStyleSheet("""
            background-color: white;
            color: black;
            """)
        self.pushButton_6.setStyleSheet("""
            background-color: white;
            color: red;
            """)
        self.pushButton_7.setStyleSheet("""
            background-color: white;
            color: purple;
            """)
        self.pushButton_8.setStyleSheet("""
            background-color: white;
            color: orange;
            """)
        self.pushButton_9.setStyleSheet("""
            background-color: white;
            color: pink;
            """)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "colorchanging"))
        self.pushButton.setText(_translate("Dialog", "red"))
        self.pushButton_2.setText(_translate("Dialog", "blue"))
        self.pushButton_3.setText(_translate("Dialog", "yellow"))
        self.pushButton_4.setText(_translate("Dialog", "green"))
        self.pushButton_5.setText(_translate("Dialog", "black"))
        self.pushButton_6.setText(_translate("Dialog", "white"))
        self.pushButton_7.setText(_translate("Dialog", "purple"))
        self.pushButton_8.setText(_translate("Dialog", "orange"))
        self.pushButton_9.setText(_translate("Dialog", "pink"))
    def red(self):
        Dialog.setStyleSheet("background-color: red;")
    def blue(self):
        Dialog.setStyleSheet("background-color: blue;")
    def yellow(self):
        Dialog.setStyleSheet("background-color: yellow;")
    def green(self):
        Dialog.setStyleSheet("background-color: green;")
    def black(self):
        Dialog.setStyleSheet("background-color: black;")
    def white(self):
        Dialog.setStyleSheet("background-color: white;")
    def purple(self):
        Dialog.setStyleSheet("background-color: purple")
    def orange(self):
        Dialog.setStyleSheet("background-color: orange;")
    def pink(self):
        Dialog.setStyleSheet("background-color: pink;")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
