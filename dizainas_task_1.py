# Form implementation generated from reading ui file 'dizainas_task_1.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 346)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.padidinti = QtWidgets.QPushButton(parent=self.centralwidget)
        self.padidinti.setGeometry(QtCore.QRect(190, 70, 101, 41))
        self.padidinti.setAutoFillBackground(True)
        self.padidinti.setCheckable(False)
        self.padidinti.setObjectName("padidinti")
        self.sumazinti = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sumazinti.setGeometry(QtCore.QRect(420, 70, 91, 41))
        self.sumazinti.setObjectName("sumazinti")
        self.skaicius = QtWidgets.QLabel(parent=self.centralwidget)
        self.skaicius.setGeometry(QtCore.QRect(320, 120, 71, 71))
        self.skaicius.setWordWrap(True)
        self.skaicius.setObjectName("skaicius")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.padidinti.setText(_translate("MainWindow", "Padidinti"))
        self.sumazinti.setText(_translate("MainWindow", "Sumazinti"))
        self.skaicius.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; text-decoration: underline;\">0</span></p></body></html>"))
