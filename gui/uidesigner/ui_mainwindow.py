# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uidesigner_res/mainwindow.ui'
#
# Created: Wed Dec 03 19:43:04 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(723, 735)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(9, 9, 470, 339))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setMaximumSize(QtCore.QSize(450, 71))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lebelStore_4 = QtGui.QLabel(self.groupBox_3)
        self.lebelStore_4.setMaximumSize(QtCore.QSize(116, 16777215))
        self.lebelStore_4.setObjectName(_fromUtf8("lebelStore_4"))
        self.horizontalLayout_2.addWidget(self.lebelStore_4)
        self.cbStore = QtGui.QComboBox(self.groupBox_3)
        self.cbStore.setMinimumSize(QtCore.QSize(115, 0))
        self.cbStore.setObjectName(_fromUtf8("cbStore"))
        self.horizontalLayout_2.addWidget(self.cbStore)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout.addWidget(self.label_19)
        self.cbServType = QtGui.QComboBox(self.groupBox_3)
        self.cbServType.setMinimumSize(QtCore.QSize(115, 0))
        self.cbServType.setObjectName(_fromUtf8("cbServType"))
        self.horizontalLayout.addWidget(self.cbServType)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_14.addLayout(self.verticalLayout_4)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_14)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox.setMaximumSize(QtCore.QSize(450, 200))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.gBTaskinfo_4 = QtGui.QGroupBox(self.groupBox)
        self.gBTaskinfo_4.setTitle(_fromUtf8(""))
        self.gBTaskinfo_4.setObjectName(_fromUtf8("gBTaskinfo_4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.gBTaskinfo_4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.gBTaskinfo_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.lEAccount_2 = QtGui.QLineEdit(self.gBTaskinfo_4)
        self.lEAccount_2.setObjectName(_fromUtf8("lEAccount_2"))
        self.horizontalLayout_4.addWidget(self.lEAccount_2)
        self.pBViewTask_2 = QtGui.QPushButton(self.gBTaskinfo_4)
        self.pBViewTask_2.setMaximumSize(QtCore.QSize(30, 23))
        self.pBViewTask_2.setObjectName(_fromUtf8("pBViewTask_2"))
        self.horizontalLayout_4.addWidget(self.pBViewTask_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.gBTaskinfo_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lEAccount_3 = QtGui.QLineEdit(self.gBTaskinfo_4)
        self.lEAccount_3.setObjectName(_fromUtf8("lEAccount_3"))
        self.horizontalLayout_5.addWidget(self.lEAccount_3)
        self.pBViewTask_3 = QtGui.QPushButton(self.gBTaskinfo_4)
        self.pBViewTask_3.setMaximumSize(QtCore.QSize(30, 23))
        self.pBViewTask_3.setObjectName(_fromUtf8("pBViewTask_3"))
        self.horizontalLayout_5.addWidget(self.pBViewTask_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_3 = QtGui.QLabel(self.gBTaskinfo_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lEAccount_4 = QtGui.QLineEdit(self.gBTaskinfo_4)
        self.lEAccount_4.setObjectName(_fromUtf8("lEAccount_4"))
        self.horizontalLayout_6.addWidget(self.lEAccount_4)
        self.pushButton_5 = QtGui.QPushButton(self.gBTaskinfo_4)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(self.gBTaskinfo_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lEAccount_5 = QtGui.QLineEdit(self.gBTaskinfo_4)
        self.lEAccount_5.setObjectName(_fromUtf8("lEAccount_5"))
        self.horizontalLayout_7.addWidget(self.lEAccount_5)
        self.pushButton_6 = QtGui.QPushButton(self.gBTaskinfo_4)
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_13.addWidget(self.gBTaskinfo_4)
        self.gBTaskinfo_5 = QtGui.QGroupBox(self.groupBox)
        self.gBTaskinfo_5.setTitle(_fromUtf8(""))
        self.gBTaskinfo_5.setObjectName(_fromUtf8("gBTaskinfo_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gBTaskinfo_5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_21 = QtGui.QLabel(self.gBTaskinfo_5)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_8.addWidget(self.label_21)
        self.lEAcount_6 = QtGui.QLineEdit(self.gBTaskinfo_5)
        self.lEAcount_6.setObjectName(_fromUtf8("lEAcount_6"))
        self.horizontalLayout_8.addWidget(self.lEAcount_6)
        self.pushButton_7 = QtGui.QPushButton(self.gBTaskinfo_5)
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_8.addWidget(self.pushButton_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_5 = QtGui.QLabel(self.gBTaskinfo_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lEAcount_7 = QtGui.QLineEdit(self.gBTaskinfo_5)
        self.lEAcount_7.setObjectName(_fromUtf8("lEAcount_7"))
        self.horizontalLayout_9.addWidget(self.lEAcount_7)
        self.pushButton_8 = QtGui.QPushButton(self.gBTaskinfo_5)
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_9.addWidget(self.pushButton_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_6 = QtGui.QLabel(self.gBTaskinfo_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_10.addWidget(self.label_6)
        self.lEAcount_8 = QtGui.QLineEdit(self.gBTaskinfo_5)
        self.lEAcount_8.setObjectName(_fromUtf8("lEAcount_8"))
        self.horizontalLayout_10.addWidget(self.lEAcount_8)
        self.pushButton_9 = QtGui.QPushButton(self.gBTaskinfo_5)
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_7 = QtGui.QLabel(self.gBTaskinfo_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_11.addWidget(self.label_7)
        self.lEAccount_9 = QtGui.QLineEdit(self.gBTaskinfo_5)
        self.lEAccount_9.setObjectName(_fromUtf8("lEAccount_9"))
        self.horizontalLayout_11.addWidget(self.lEAccount_9)
        self.pushButton_10 = QtGui.QPushButton(self.gBTaskinfo_5)
        self.pushButton_10.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout_11.addWidget(self.pushButton_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_8 = QtGui.QLabel(self.gBTaskinfo_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_12.addWidget(self.label_8)
        self.lEAccount_10 = QtGui.QLineEdit(self.gBTaskinfo_5)
        self.lEAccount_10.setObjectName(_fromUtf8("lEAccount_10"))
        self.horizontalLayout_12.addWidget(self.lEAccount_10)
        self.pushButton_11 = QtGui.QPushButton(self.gBTaskinfo_5)
        self.pushButton_11.setMaximumSize(QtCore.QSize(30, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_12.addWidget(self.pushButton_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addWidget(self.gBTaskinfo_5)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_2.setMaximumSize(QtCore.QSize(450, 60))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.pBOk_4 = QtGui.QPushButton(self.groupBox_2)
        self.pBOk_4.setEnabled(True)
        self.pBOk_4.setMinimumSize(QtCore.QSize(75, 23))
        self.pBOk_4.setMaximumSize(QtCore.QSize(75, 50))
        self.pBOk_4.setObjectName(_fromUtf8("pBOk_4"))
        self.horizontalLayout_15.addWidget(self.pBOk_4)
        self.pBClear_4 = QtGui.QPushButton(self.groupBox_2)
        self.pBClear_4.setMinimumSize(QtCore.QSize(75, 23))
        self.pBClear_4.setMaximumSize(QtCore.QSize(75, 50))
        self.pBClear_4.setObjectName(_fromUtf8("pBClear_4"))
        self.horizontalLayout_15.addWidget(self.pBClear_4)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_15.addWidget(self.pushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(9, 354, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_task_manage = QtGui.QMenu(self.menubar)
        self.menu_task_manage.setObjectName(_fromUtf8("menu_task_manage"))
        self.menu_account_manage = QtGui.QMenu(self.menubar)
        self.menu_account_manage.setObjectName(_fromUtf8("menu_account_manage"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(80, 45))
        self.dockWidget_2.setMaximumSize(QtCore.QSize(524287, 45))
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_2)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName(_fromUtf8("action_5"))
        self.action_new_task = QtGui.QAction(MainWindow)
        self.action_new_task.setObjectName(_fromUtf8("action_new_task"))
        self.action_10 = QtGui.QAction(MainWindow)
        self.action_10.setObjectName(_fromUtf8("action_10"))
        self.action_11 = QtGui.QAction(MainWindow)
        self.action_11.setObjectName(_fromUtf8("action_11"))
        self.action_new_task_2 = QtGui.QAction(MainWindow)
        self.action_new_task_2.setObjectName(_fromUtf8("action_new_task_2"))
        self.action_view_task = QtGui.QAction(MainWindow)
        self.action_view_task.setObjectName(_fromUtf8("action_view_task"))
        self.action_create_task = QtGui.QAction(MainWindow)
        self.action_create_task.setObjectName(_fromUtf8("action_create_task"))
        self.action_6 = QtGui.QAction(MainWindow)
        self.action_6.setObjectName(_fromUtf8("action_6"))
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName(_fromUtf8("action_7"))
        self.action_8 = QtGui.QAction(MainWindow)
        self.action_8.setObjectName(_fromUtf8("action_8"))
        self.action_add_account = QtGui.QAction(MainWindow)
        self.action_add_account.setObjectName(_fromUtf8("action_add_account"))
        self.action_13 = QtGui.QAction(MainWindow)
        self.action_13.setObjectName(_fromUtf8("action_13"))
        self.action_14 = QtGui.QAction(MainWindow)
        self.action_14.setObjectName(_fromUtf8("action_14"))
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu_2.addAction(self.action_4)
        self.menu_2.addSeparator()
        self.menu_3.addAction(self.action_11)
        self.menu_task_manage.addAction(self.action_create_task)
        self.menu_task_manage.addAction(self.action_view_task)
        self.menu_account_manage.addAction(self.action_add_account)
        self.menu_account_manage.addAction(self.action_13)
        self.menu_account_manage.addAction(self.action_14)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_task_manage.menuAction())
        self.menubar.addAction(self.menu_account_manage.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_create_task, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.newTask)
        QtCore.QObject.connect(self.action_add_account, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.addAccount)
        QtCore.QObject.connect(self.pBViewTask_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.viewTask)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lebelStore_4.setText(_translate("MainWindow", "零售店：", None))
        self.label_19.setText(_translate("MainWindow", "服务类型:", None))
        self.label.setText(_translate("MainWindow", "用户名：", None))
        self.pBViewTask_2.setText(_translate("MainWindow", "查看", None))
        self.label_2.setText(_translate("MainWindow", "用户名：", None))
        self.pBViewTask_3.setText(_translate("MainWindow", "查看", None))
        self.label_3.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_5.setText(_translate("MainWindow", "查看", None))
        self.label_4.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_6.setText(_translate("MainWindow", "查看", None))
        self.label_21.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_7.setText(_translate("MainWindow", "查看", None))
        self.label_5.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_8.setText(_translate("MainWindow", "查看", None))
        self.label_6.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_9.setText(_translate("MainWindow", "查看", None))
        self.label_7.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_10.setText(_translate("MainWindow", "查看", None))
        self.label_8.setText(_translate("MainWindow", "用户名：", None))
        self.pushButton_11.setText(_translate("MainWindow", "查看", None))
        self.pBOk_4.setText(_translate("MainWindow", "开始", None))
        self.pBClear_4.setText(_translate("MainWindow", "停止", None))
        self.pushButton.setText(_translate("MainWindow", "导入任务", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "编辑", None))
        self.menu_3.setTitle(_translate("MainWindow", "帮助", None))
        self.menu_task_manage.setTitle(_translate("MainWindow", "任务管理", None))
        self.menu_account_manage.setTitle(_translate("MainWindow", "用户管理", None))
        self.action.setText(_translate("MainWindow", "登录", None))
        self.action_2.setText(_translate("MainWindow", "注销", None))
        self.action_4.setText(_translate("MainWindow", "任务配置", None))
        self.action_5.setText(_translate("MainWindow", "新建任务", None))
        self.action_new_task.setText(_translate("MainWindow", "新建任务", None))
        self.action_10.setText(_translate("MainWindow", "查看", None))
        self.action_11.setText(_translate("MainWindow", "关于", None))
        self.action_new_task_2.setText(_translate("MainWindow", "新建任务", None))
        self.action_view_task.setText(_translate("MainWindow", "查看", None))
        self.action_create_task.setText(_translate("MainWindow", "新建任务", None))
        self.action_6.setText(_translate("MainWindow", "添加用户", None))
        self.action_7.setText(_translate("MainWindow", "删除用户", None))
        self.action_8.setText(_translate("MainWindow", "修改", None))
        self.action_add_account.setText(_translate("MainWindow", "添加账号", None))
        self.action_13.setText(_translate("MainWindow", "删除账号", None))
        self.action_14.setText(_translate("MainWindow", "修改账号", None))

