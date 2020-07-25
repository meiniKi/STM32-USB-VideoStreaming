# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoPlayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fileInputTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fileInputTextEdit.setGeometry(QtCore.QRect(10, 10, 1091, 41))
        self.fileInputTextEdit.setObjectName("fileInputTextEdit")
        self.fileInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileInputButton.setGeometry(QtCore.QRect(1120, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fileInputButton.setFont(font)
        self.fileInputButton.setObjectName("fileInputButton")
        self.optionsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.optionsGroupBox.setGeometry(QtCore.QRect(640, 80, 611, 681))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.optionsGroupBox.setFont(font)
        self.optionsGroupBox.setObjectName("optionsGroupBox")
        self.colorThresholdingGroupBox = QtWidgets.QGroupBox(self.optionsGroupBox)
        self.colorThresholdingGroupBox.setGeometry(QtCore.QRect(10, 30, 591, 251))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.colorThresholdingGroupBox.setFont(font)
        self.colorThresholdingGroupBox.setObjectName("colorThresholdingGroupBox")
        self.groupBox = QtWidgets.QGroupBox(self.colorThresholdingGroupBox)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 551, 91))
        self.groupBox.setObjectName("groupBox")
        self.blockSizeSlider = QtWidgets.QSlider(self.groupBox)
        self.blockSizeSlider.setGeometry(QtCore.QRect(110, 30, 431, 41))
        self.blockSizeSlider.setMinimum(3)
        self.blockSizeSlider.setMaximum(75)
        self.blockSizeSlider.setSingleStep(2)
        self.blockSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blockSizeSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.blockSizeSlider.setTickInterval(2)
        self.blockSizeSlider.setObjectName("blockSizeSlider")
        self.blockSizeLabel = QtWidgets.QLabel(self.groupBox)
        self.blockSizeLabel.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.blockSizeLabel.setObjectName("blockSizeLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.colorThresholdingGroupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 561, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.constantThresholdSlider = QtWidgets.QSlider(self.groupBox_2)
        self.constantThresholdSlider.setGeometry(QtCore.QRect(120, 30, 431, 41))
        self.constantThresholdSlider.setMinimum(1)
        self.constantThresholdSlider.setMaximum(50)
        self.constantThresholdSlider.setPageStep(1)
        self.constantThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.constantThresholdSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.constantThresholdSlider.setTickInterval(1)
        self.constantThresholdSlider.setObjectName("constantThresholdSlider")
        self.constantLabel = QtWidgets.QLabel(self.groupBox_2)
        self.constantLabel.setGeometry(QtCore.QRect(30, 40, 41, 31))
        self.constantLabel.setObjectName("constantLabel")
        self.progressBar = QtWidgets.QProgressBar(self.optionsGroupBox)
        self.progressBar.setGeometry(QtCore.QRect(40, 340, 561, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.errorLabel = QtWidgets.QLabel(self.optionsGroupBox)
        self.errorLabel.setGeometry(QtCore.QRect(40, 300, 531, 21))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.label = QtWidgets.QLabel(self.optionsGroupBox)
        self.label.setGeometry(QtCore.QRect(40, 370, 521, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.comPortsGroupBox = QtWidgets.QGroupBox(self.optionsGroupBox)
        self.comPortsGroupBox.setGeometry(QtCore.QRect(10, 430, 591, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comPortsGroupBox.setFont(font)
        self.comPortsGroupBox.setObjectName("comPortsGroupBox")
        self.comPortsListButton = QtWidgets.QPushButton(self.comPortsGroupBox)
        self.comPortsListButton.setGeometry(QtCore.QRect(430, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comPortsListButton.setFont(font)
        self.comPortsListButton.setObjectName("comPortsListButton")
        self.comPortsListBox = QtWidgets.QComboBox(self.comPortsGroupBox)
        self.comPortsListBox.setGeometry(QtCore.QRect(30, 30, 381, 41))
        self.comPortsListBox.setObjectName("comPortsListBox")
        self.comPortsConnectButton = QtWidgets.QPushButton(self.comPortsGroupBox)
        self.comPortsConnectButton.setGeometry(QtCore.QRect(430, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comPortsConnectButton.setFont(font)
        self.comPortsConnectButton.setObjectName("comPortsConnectButton")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(True)
        self.playButton.setGeometry(QtCore.QRect(540, 420, 80, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QtCore.QSize(80, 80))
        self.playButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.playButton.setFont(font)
        self.playButton.setObjectName("playButton")
        self.goToStartButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToStartButton.setGeometry(QtCore.QRect(540, 510, 80, 80))
        self.goToStartButton.setMinimumSize(QtCore.QSize(80, 80))
        self.goToStartButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.goToStartButton.setFont(font)
        self.goToStartButton.setObjectName("goToStartButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(19, 69, 611, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.rawVideoLabel = QtWidgets.QLabel(self.groupBox_3)
        self.rawVideoLabel.setGeometry(QtCore.QRect(10, 20, 581, 281))
        self.rawVideoLabel.setText("")
        self.rawVideoLabel.setObjectName("rawVideoLabel")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 420, 491, 251))
        self.groupBox_4.setObjectName("groupBox_4")
        self.processedVideoLabel = QtWidgets.QLabel(self.groupBox_4)
        self.processedVideoLabel.setGeometry(QtCore.QRect(20, 20, 448, 224))
        self.processedVideoLabel.setMinimumSize(QtCore.QSize(448, 224))
        self.processedVideoLabel.setMaximumSize(QtCore.QSize(448, 224))
        self.processedVideoLabel.setText("")
        self.processedVideoLabel.setObjectName("processedVideoLabel")
        self.playBackSlider = QtWidgets.QSlider(self.centralwidget)
        self.playBackSlider.setGeometry(QtCore.QRect(20, 390, 611, 21))
        self.playBackSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playBackSlider.setObjectName("playBackSlider")
        self.streamCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.streamCheckBox.setGeometry(QtCore.QRect(540, 609, 81, 21))
        self.streamCheckBox.setObjectName("checkBox")
        self.invertCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.invertCheckBox.setGeometry(QtCore.QRect(540, 636, 81, 21))
        self.invertCheckBox.setObjectName("checkBox_2")
        self.groupBox_3.raise_()
        self.fileInputTextEdit.raise_()
        self.fileInputButton.raise_()
        self.optionsGroupBox.raise_()
        self.playButton.raise_()
        self.goToStartButton.raise_()
        self.groupBox_4.raise_()
        self.playBackSlider.raise_()
        self.streamCheckBox.raise_()
        self.invertCheckBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SKEmbedded Video Player"))
        self.fileInputButton.setText(_translate("MainWindow", "Browse.."))
        self.optionsGroupBox.setTitle(_translate("MainWindow", "Options"))
        self.colorThresholdingGroupBox.setTitle(_translate("MainWindow", "Thresholding Constants"))
        self.groupBox.setTitle(_translate("MainWindow", "Block Size"))
        self.blockSizeLabel.setText(_translate("MainWindow", "BlockSize"))
        self.groupBox_2.setTitle(_translate("MainWindow", "C (subtracted from mean)"))
        self.constantLabel.setText(_translate("MainWindow", "C"))
        self.comPortsGroupBox.setTitle(_translate("MainWindow", "USB Connection"))
        self.comPortsListButton.setText(_translate("MainWindow", "List COM Ports"))
        self.comPortsConnectButton.setText(_translate("MainWindow", "Connect"))
        self.playButton.setText(_translate("MainWindow", " ▶ "))
        self.goToStartButton.setText(_translate("MainWindow", "⇐"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Raw Video"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Processed 128 × 64 Video"))
        self.streamCheckBox.setText(_translate("MainWindow", "Stream"))
        self.invertCheckBox.setText(_translate("MainWindow", "Invert"))