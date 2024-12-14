from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.CandidateTitle = QtWidgets.QTextBrowser(self.centralwidget)
        self.CandidateTitle.setGeometry(QtCore.QRect(55, 20, 200, 40))
        self.CandidateTitle.setFont(QtGui.QFont("Arial", 15))
        self.CandidateTitle.setObjectName("CandidateTitle")

        self.JohnButton = QtWidgets.QRadioButton(self.centralwidget)
        self.JohnButton.setGeometry(QtCore.QRect(30, 200, 91, 51))
        self.JohnButton.setFont(QtGui.QFont("Arial", 16))
        self.JohnButton.setObjectName("JohnButton")

        self.JaneButton = QtWidgets.QRadioButton(self.centralwidget)
        self.JaneButton.setGeometry(QtCore.QRect(170, 200, 91, 51))
        self.JaneButton.setFont(QtGui.QFont("Arial", 16))
        self.JaneButton.setObjectName("JaneButton")

        self.VoteButton = QtWidgets.QPushButton(self.centralwidget)
        self.VoteButton.setGeometry(QtCore.QRect(90, 280, 101, 31))
        self.VoteButton.setFont(QtGui.QFont("Arial", 12))
        self.VoteButton.setObjectName("VoteButton")

        self.ResultsButton = QtWidgets.QPushButton(self.centralwidget)
        self.ResultsButton.setGeometry(QtCore.QRect(90, 350, 101, 35))
        self.ResultsButton.setFont(QtGui.QFont("Arial", 12))
        self.ResultsButton.setObjectName("ResultsButton")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 100, 191, 31))
        self.textEdit.setObjectName("textEdit")

        self.IDlabel = QtWidgets.QLabel(self.centralwidget)
        self.IDlabel.setGeometry(QtCore.QRect(40, 95, 41, 41))
        self.IDlabel.setFont(QtGui.QFont("Arial", 15))
        self.IDlabel.setObjectName("IDlabel")

        self.results_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.results_display.setGeometry(QtCore.QRect(45, 420, 220, 50))
        self.results_display.setObjectName("results_display")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voting App"))
        self.CandidateTitle.setHtml(_translate("MainWindow", "<p align='center'>CANDIDATE MENU</p>"))
        self.JohnButton.setText(_translate("MainWindow", "John"))
        self.JaneButton.setText(_translate("MainWindow", "Jane"))
        self.VoteButton.setText(_translate("MainWindow", "VOTE"))
        self.ResultsButton.setText(_translate("MainWindow", "Results"))
        self.IDlabel.setText(_translate("MainWindow", "ID"))


