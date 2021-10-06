# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifiedHome.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import SQLiteDBModified

from monthPage import *

db = SQLiteDBModified.SQLDbModified()





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UCTTLogo = QtWidgets.QLabel(self.centralwidget)
        self.UCTTLogo.setGeometry(QtCore.QRect(20, 10, 541, 141))
        self.UCTTLogo.setText("")
        self.UCTTLogo.setPixmap(QtGui.QPixmap("uct_original_logo.jpg"))
        self.UCTTLogo.setObjectName("UCTTLogo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 280, 131, 71))
        self.pushButton.setStyleSheet("font: 75 12pt \"Cambria\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 200, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 370, 131, 71))
        self.pushButton_2.setStyleSheet("font: 75 12pt \"Cambria\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Yearly"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#0000ff;\">Sentiment Analysis</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Monthly"))

        self.pushButton.clicked.connect(self.combined)    # Yearly Button clicked
        self.pushButton_2.clicked.connect(self.monthly)    # Monthly button clicked

    # Combined bar graph method is called from the ModifiedSqlLite
    def combined(self):
        db.combinedBarGraph()
    def monthly(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Monthly()
        self.ui.setupMonthly(self.window)
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())