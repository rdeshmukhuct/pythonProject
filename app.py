# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from menu import *
from modifiedHomePage import *
import ExcelVisualisation
import time_series_analysis

t= time_series_analysis.TimeSeries()


ob = ExcelVisualisation.Comparison()


class Ui_MainWindowApp(object):
    def setupUiApp(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 704)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -60, 911, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/uct_original_logo.jpg"))
        self.label.setObjectName("label")
        self.Overview = QtWidgets.QPushButton(self.centralwidget)
        self.Overview.setGeometry(QtCore.QRect(120, 250, 191, 71))
        self.Overview.setStyleSheet("font: 12pt \"Verdana\";\n"
"")
        self.Overview.setObjectName("Overview")
        self.DetailedAnlaysis = QtWidgets.QPushButton(self.centralwidget)
        self.DetailedAnlaysis.setGeometry(QtCore.QRect(100, 350, 231, 71))
        self.DetailedAnlaysis.setStyleSheet("font: 12pt \"Verdana\";")
        self.DetailedAnlaysis.setObjectName("DetailedAnlaysis")

        self.Comparison = QtWidgets.QPushButton(self.centralwidget)
        self.Comparison.setGeometry(QtCore.QRect(120, 450, 191, 71))
        self.Comparison.setStyleSheet("font: 12pt \"Verdana\";")
        self.Comparison.setObjectName("Comparison")

        self.timeSeries = QtWidgets.QPushButton(self.centralwidget)
        self.timeSeries .setGeometry(QtCore.QRect(100, 550, 231, 71))
        self.timeSeries .setStyleSheet("font: 12pt \"Verdana\";")
        self.timeSeries .setObjectName("timeSeries ")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 421, 61))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 26))
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
        self.Overview.setText(_translate("MainWindow", "Overview"))
        self.Comparison.setText(_translate("MainWindow", "Comparison"))
        self.timeSeries.setText(_translate("MainWindow", "Time Series"))
        self.DetailedAnlaysis.setText(_translate("MainWindow", "Detailed Analysis"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">Sentiment Analysis </span></p></body></html>"))
        self.DetailedAnlaysis.clicked.connect(self.analysis)
        self.Overview.clicked.connect(self.overview)
        self.Comparison.clicked.connect(self.comparison)
        self.timeSeries.clicked.connect(self.timeSeriesFunction)

    def overview(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowMenu()
        self.ui.setupUiMenu(self.window)
        self.window.show()

    def analysis(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def comparison(self):
        ob.comparison()
    def timeSeriesFunction(self):
        t.open_csv('report.csv')
        #t.plot_by_month()
        t.plot_df()
        t.main()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowApp()
    ui.setupUiApp(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
