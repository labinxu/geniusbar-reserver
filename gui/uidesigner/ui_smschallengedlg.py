# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uidesigner_res/smschallengedlg.ui'
#
# Created: Thu Dec 04 15:27:26 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SmsChallengeDialog(object):
    def setupUi(self, SmsChallengeDialog):
        SmsChallengeDialog.setObjectName(_fromUtf8("SmsChallengeDialog"))
        SmsChallengeDialog.resize(562, 429)
        SmsChallengeDialog.setSizeGripEnabled(True)
        SmsChallengeDialog.setModal(True)
        self.verticalLayout_5 = QtGui.QVBoxLayout(SmsChallengeDialog)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tWTask = QtGui.QTabWidget(SmsChallengeDialog)
        self.tWTask.setDocumentMode(False)
        self.tWTask.setObjectName(_fromUtf8("tWTask"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 486, 370))
        self.groupBox_7.setTitle(_fromUtf8(""))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.gBTaskProcessinfo = QtGui.QGroupBox(self.groupBox_7)
        self.gBTaskProcessinfo.setMaximumSize(QtCore.QSize(240, 350))
        self.gBTaskProcessinfo.setTitle(_fromUtf8(""))
        self.gBTaskProcessinfo.setObjectName(_fromUtf8("gBTaskProcessinfo"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.gBTaskProcessinfo)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_2 = QtGui.QGroupBox(self.gBTaskProcessinfo)
        self.groupBox_2.setMaximumSize(QtCore.QSize(220, 196))
        self.groupBox_2.setSizeIncrement(QtCore.QSize(5, 5))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pTSmsChallengInfo = QtGui.QPlainTextEdit(self.groupBox_2)
        self.pTSmsChallengInfo.setMinimumSize(QtCore.QSize(200, 100))
        self.pTSmsChallengInfo.setMaximumSize(QtCore.QSize(200, 100))
        self.pTSmsChallengInfo.setObjectName(_fromUtf8("pTSmsChallengInfo"))
        self.verticalLayout_3.addWidget(self.pTSmsChallengInfo)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lEPhoneNumber = QtGui.QLineEdit(self.groupBox_3)
        self.lEPhoneNumber.setEnabled(False)
        self.lEPhoneNumber.setObjectName(_fromUtf8("lEPhoneNumber"))
        self.horizontalLayout_6.addWidget(self.lEPhoneNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lEReservCode = QtGui.QLineEdit(self.groupBox_3)
        self.lEReservCode.setEnabled(False)
        self.lEReservCode.setObjectName(_fromUtf8("lEReservCode"))
        self.horizontalLayout_7.addWidget(self.lEReservCode)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(self.gBTaskProcessinfo)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 80))
        self.groupBox.setMaximumSize(QtCore.QSize(170, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lbVerifyCodePic = QtGui.QLabel(self.groupBox)
        self.lbVerifyCodePic.setMaximumSize(QtCore.QSize(161, 78))
        self.lbVerifyCodePic.setObjectName(_fromUtf8("lbVerifyCodePic"))
        self.verticalLayout_6.addWidget(self.lbVerifyCodePic)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(self.gBTaskProcessinfo)
        self.groupBox_4.setMaximumSize(QtCore.QSize(220, 42))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_10.addWidget(self.label_6)
        self.lEVerfiyCode = QtGui.QLineEdit(self.groupBox_4)
        self.lEVerfiyCode.setObjectName(_fromUtf8("lEVerfiyCode"))
        self.horizontalLayout_10.addWidget(self.lEVerfiyCode)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.horizontalLayout_23.addWidget(self.gBTaskProcessinfo)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_5.setMaximumSize(QtCore.QSize(240, 80))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_5)
        self.progressBar.setMinimumSize(QtCore.QSize(191, 30))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(True)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setTextVisible(True)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_8.addWidget(self.progressBar)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.gBTaskinfo = QtGui.QGroupBox(self.groupBox_7)
        self.gBTaskinfo.setMaximumSize(QtCore.QSize(240, 162))
        self.gBTaskinfo.setTitle(_fromUtf8(""))
        self.gBTaskinfo.setObjectName(_fromUtf8("gBTaskinfo"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.gBTaskinfo)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lebelStore = QtGui.QLabel(self.gBTaskinfo)
        self.lebelStore.setObjectName(_fromUtf8("lebelStore"))
        self.horizontalLayout.addWidget(self.lebelStore)
        self.combStore = QtGui.QComboBox(self.gBTaskinfo)
        self.combStore.setEnabled(False)
        self.combStore.setObjectName(_fromUtf8("combStore"))
        self.horizontalLayout.addWidget(self.combStore)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.gBTaskinfo)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.combServType = QtGui.QComboBox(self.gBTaskinfo)
        self.combServType.setEnabled(False)
        self.combServType.setObjectName(_fromUtf8("combServType"))
        self.horizontalLayout_2.addWidget(self.combServType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.gBTaskinfo)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.lEUserName = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEUserName.setEnabled(False)
        self.lEUserName.setObjectName(_fromUtf8("lEUserName"))
        self.horizontalLayout_3.addWidget(self.lEUserName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.gBTaskinfo)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lEPasswd = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPasswd.setEnabled(False)
        self.lEPasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.lEPasswd.setObjectName(_fromUtf8("lEPasswd"))
        self.horizontalLayout_4.addWidget(self.lEPasswd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.gBTaskinfo)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lEGovId = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEGovId.setEnabled(False)
        self.lEGovId.setObjectName(_fromUtf8("lEGovId"))
        self.horizontalLayout_5.addWidget(self.lEGovId)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addWidget(self.gBTaskinfo)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_6.setMaximumSize(QtCore.QSize(240, 80))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.pBCancel = QtGui.QPushButton(self.groupBox_6)
        self.pBCancel.setObjectName(_fromUtf8("pBCancel"))
        self.horizontalLayout_9.addWidget(self.pBCancel)
        self.pBSubmit = QtGui.QPushButton(self.groupBox_6)
        self.pBSubmit.setObjectName(_fromUtf8("pBSubmit"))
        self.horizontalLayout_9.addWidget(self.pBSubmit)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addWidget(self.groupBox_6)
        self.horizontalLayout_23.addLayout(self.verticalLayout_9)
        self.tWTask.addTab(self.tab_1, _fromUtf8(""))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.tWTask.addTab(self.tab_11, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tWTask)

        self.retranslateUi(SmsChallengeDialog)
        self.tWTask.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SmsChallengeDialog)
        SmsChallengeDialog.setTabOrder(self.combStore, self.lEPasswd)
        SmsChallengeDialog.setTabOrder(self.lEPasswd, self.lEPhoneNumber)
        SmsChallengeDialog.setTabOrder(self.lEPhoneNumber, self.lEReservCode)
        SmsChallengeDialog.setTabOrder(self.lEReservCode, self.lEUserName)
        SmsChallengeDialog.setTabOrder(self.lEUserName, self.lEGovId)
        SmsChallengeDialog.setTabOrder(self.lEGovId, self.combServType)

    def retranslateUi(self, SmsChallengeDialog):
        SmsChallengeDialog.setWindowTitle(_translate("SmsChallengeDialog", "任务查看", None))
        self.label_4.setText(_translate("SmsChallengeDialog", "手机号：", None))
        self.label_5.setText(_translate("SmsChallengeDialog", "预约码：", None))
        self.groupBox.setTitle(_translate("SmsChallengeDialog", "双击刷新", None))
        self.lbVerifyCodePic.setText(_translate("SmsChallengeDialog", "TextLabel", None))
        self.label_6.setText(_translate("SmsChallengeDialog", "验证码：", None))
        self.lebelStore.setText(_translate("SmsChallengeDialog", "零售店：", None))
        self.label_7.setText(_translate("SmsChallengeDialog", "服务类型:", None))
        self.label.setText(_translate("SmsChallengeDialog", "用户名：", None))
        self.label_2.setText(_translate("SmsChallengeDialog", "密码：", None))
        self.label_3.setText(_translate("SmsChallengeDialog", "身份证号：", None))
        self.pBCancel.setText(_translate("SmsChallengeDialog", "取消", None))
        self.pBSubmit.setText(_translate("SmsChallengeDialog", "提交", None))
        self.tWTask.setTabText(self.tWTask.indexOf(self.tab_1), _translate("SmsChallengeDialog", "任务信息", None))
        self.tWTask.setTabText(self.tWTask.indexOf(self.tab_11), _translate("SmsChallengeDialog", "预订信息", None))

