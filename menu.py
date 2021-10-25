# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import word_frequency
import article_analysis
from BarGraph import *
from summaryArticles import *

ob = word_frequency.MostCommonWords()  # MUST RENAME THESE OBJECTS TO BETTER REPRESENT THEIR FUNCTIONALITY
obj = article_analysis.GUIFunctions()


class Ui_MainWindowMenu(object):
    def setupUiMenu(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 607)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border-color: rgb(85, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonStock = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStock.setGeometry(QtCore.QRect(180, 250, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        self.pushButtonStock.setFont(font)
        self.pushButtonStock.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                           "")
        self.pushButtonStock.setObjectName("pushButtonStock")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 0, 621, 201))
        self.logo.setAutoFillBackground(True)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/uct_original_logo.jpg"))
        self.logo.setObjectName("logo")
        self.labelImageStock = QtWidgets.QLabel(self.centralwidget)
        self.labelImageStock.setGeometry(QtCore.QRect(110, 250, 71, 51))
        self.labelImageStock.setText("")
        self.labelImageStock.setPixmap(QtGui.QPixmap("images/stocks-to-buy-in-2021.png"))
        self.labelImageStock.setScaledContents(True)
        self.labelImageStock.setObjectName("labelImageStock")
        self.pushButtonVisualisation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonVisualisation.setGeometry(QtCore.QRect(180, 310, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        self.pushButtonVisualisation.setFont(font)
        self.pushButtonVisualisation.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                                   "")
        self.pushButtonVisualisation.setObjectName("pushButtonVisualisation")
        self.pushButtonBargraph = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBargraph.setGeometry(QtCore.QRect(180, 370, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        self.pushButtonBargraph.setFont(font)
        self.pushButtonBargraph.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                              "")
        self.pushButtonBargraph.setObjectName("pushButtonBargraph")
        self.pushButtonSummary = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSummary.setGeometry(QtCore.QRect(180, 430, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        self.pushButtonSummary.setFont(font)
        self.pushButtonSummary.setStyleSheet("border-color: rgb(85, 0, 255);\n"
                                             "")
        self.pushButtonSummary.setObjectName("pushButtonSummary")
        self.labelImageBar = QtWidgets.QLabel(self.centralwidget)
        self.labelImageBar.setGeometry(QtCore.QRect(110, 370, 71, 51))
        self.labelImageBar.setText("")
        self.labelImageBar.setPixmap(QtGui.QPixmap("images/3d-bar-graph-vector-114792.jpg"))
        self.labelImageBar.setScaledContents(True)
        self.labelImageBar.setObjectName("labelImageBar")
        self.labelImageSummary = QtWidgets.QLabel(self.centralwidget)
        self.labelImageSummary.setGeometry(QtCore.QRect(110, 430, 71, 51))
        self.labelImageSummary.setText("")
        self.labelImageSummary.setPixmap(QtGui.QPixmap(
            "images/How-to-Write-a-Press-Release-Summary-and-Why-It-Matters.jpg"))
        self.labelImageSummary.setScaledContents(True)
        self.labelImageSummary.setObjectName("labelImageSummary")
        self.labelImageDataVisualisation = QtWidgets.QLabel(self.centralwidget)
        self.labelImageDataVisualisation.setGeometry(QtCore.QRect(110, 310, 71, 51))
        self.labelImageDataVisualisation.setText("")
        self.labelImageDataVisualisation.setPixmap(QtGui.QPixmap("images/shutterstock_488322949.jpg"))
        self.labelImageDataVisualisation.setScaledContents(True)
        self.labelImageDataVisualisation.setObjectName("labelImageDataVisualisation")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
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
        self.pushButtonStock.setText(_translate("MainWindow", "Market Stock"))
        self.pushButtonVisualisation.setText(_translate("MainWindow", "Data Visualisation"))
        self.pushButtonBargraph.setText(_translate("MainWindow", "Bar Graph"))
        self.pushButtonSummary.setText(_translate("MainWindow", "Summary"))

        # Button clicks call methods
        self.pushButtonStock.clicked.connect(self.MarketStock)
        self.pushButtonVisualisation.clicked.connect(self.dataVisualization)
        self.pushButtonBargraph.clicked.connect(self.barGraph)
        self.pushButtonSummary.clicked.connect(self.summary)

    def MarketStock(self):
        obj.visualize()

    def dataVisualization(self):
        values = obj.read_lines()
        obj.pie_chart(values)

    def barGraph(self):
        # Code to open a new window , bar graph
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BarGraph()
        self.ui.setup(self.window)
        self.window.show()

    def summary(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowSummary()
        self.ui.setupUiSummary(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowMenu()
    ui.setupUiMenu(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
