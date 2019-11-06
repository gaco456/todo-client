# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets , QtNetwork
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import requests
import json
import sys

from main.auth.defender import Defender


class Ui_loginUi(object):

    def setupUi(self, loginUi):
        # 상속받은 Qwidget의 오브젝트네임과 사이즈 조정.
        loginUi.setObjectName("loginUi")
        loginUi.resize(395, 195)

        # Qwidget add layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(loginUi)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.loginLayOut = QtWidgets.QVBoxLayout()
        self.loginLayOut.setObjectName("loginLayOut")

        self.loginTabWidget = QtWidgets.QTabWidget(loginUi)
        self.loginTabWidget.setObjectName("loginTabWidget")

        self.loginTab = QtWidgets.QWidget()
        self.loginTab.setObjectName("loginTab")

        self.gridLayout = QtWidgets.QGridLayout(self.loginTab)
        self.gridLayout.setObjectName("gridLayout")

        self.loginTabLayout = QtWidgets.QFormLayout()
        self.loginTabLayout.setContentsMargins(10, 10, 10, -1)
        self.loginTabLayout.setHorizontalSpacing(5)
        self.loginTabLayout.setVerticalSpacing(8)
        self.loginTabLayout.setObjectName("loginTabLayout")

        self.loginidLabel = QtWidgets.QLabel(self.loginTab)
        self.loginidLabel.setObjectName("loginidLabel")

        self.loginTabLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.loginidLabel)

        self.loginidLineEdit = QtWidgets.QLineEdit(self.loginTab)
        self.loginidLineEdit.setAutoFillBackground(False)
        self.loginidLineEdit.setObjectName("loginidLineEdit")

        self.loginTabLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginidLineEdit)

        self.loginpasswdLabel = QtWidgets.QLabel(self.loginTab)
        self.loginpasswdLabel.setObjectName("loginpasswdLabel")

        self.loginTabLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.loginpasswdLabel)

        self.loginpasswdLineEdit = QtWidgets.QLineEdit(self.loginTab)
        self.loginpasswdLineEdit.setObjectName("loginpasswdLineEdit")

        self.loginTabLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.loginpasswdLineEdit)

        self.gridLayout.addLayout(self.loginTabLayout, 0, 0, 1, 1)

        self.loginTabWidget.addTab(self.loginTab, "")

        self.joinTab = QtWidgets.QWidget()
        self.joinTab.setObjectName("joinTab")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.joinTab)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.joinTabLayout = QtWidgets.QFormLayout()
        self.joinTabLayout.setContentsMargins(10, 10, 10, -1)
        self.joinTabLayout.setHorizontalSpacing(5)
        self.joinTabLayout.setObjectName("joinTabLayout")

        self.joinidLabel = QtWidgets.QLabel(self.joinTab)
        self.joinidLabel.setObjectName("joinidLabel")

        self.joinTabLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.joinidLabel)

        self.joinidLineEdit = QtWidgets.QLineEdit(self.joinTab)
        self.joinidLineEdit.setObjectName("joinidLineEdit")

        self.joinTabLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.joinidLineEdit)

        self.joinpasswdLabel = QtWidgets.QLabel(self.joinTab)
        self.joinpasswdLabel.setObjectName("joinpasswdLabel")

        self.joinTabLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.joinpasswdLabel)

        self.joinpasswdLineEdit = QtWidgets.QLineEdit(self.joinTab)
        self.joinpasswdLineEdit.setObjectName("joinpasswdLineEdit")

        self.joinTabLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.joinpasswdLineEdit)

        self.joinpasswdCheckLabel = QtWidgets.QLabel(self.joinTab)
        self.joinpasswdCheckLabel.setObjectName("joinpasswdCheckLabel")

        self.joinTabLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.joinpasswdCheckLabel)

        self.joinpasswdCheckLineEdit = QtWidgets.QLineEdit(self.joinTab)
        self.joinpasswdCheckLineEdit.setObjectName("joinpasswdCheckLineEdit")

        self.joinTabLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.joinpasswdCheckLineEdit)

        self.gridLayout_2.addLayout(self.joinTabLayout, 0, 0, 1, 1)

        self.loginTabWidget.addTab(self.joinTab, "")

        self.loginLayOut.addWidget(self.loginTabWidget)

        self.verticalLayout_2.addLayout(self.loginLayOut)

        self.okBtn = QtWidgets.QPushButton(loginUi)
        self.okBtn.setObjectName("okBtn")
        self.okBtn.clicked.connect(self.confirmClick)

        self.verticalLayout_2.addWidget(self.okBtn, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(loginUi)
        self.loginTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(loginUi)

    def confirmClick(self):

        msgPop = QMessageBox()
        msgPop.setWindowIcon(QIcon('../icon/icon.png'))
        focusTab = self.loginTabWidget.currentIndex()

        # login
        if focusTab == 0:

            msgPop.setWindowTitle("login")
            userid = self.loginidLineEdit.text()
            passwd = self.auth.encrypt(self.loginpasswdLineEdit.text())

            if not userid:
                msgPop.setText("please enter userid")
                msgPop.setStandardButtons(QMessageBox.Ok)
                ret = msgPop.exec_()
                return

            if not self.loginpasswdLineEdit.text():
                msgPop.setText("please enter passwd")
                msgPop.setStandardButtons(QMessageBox.Ok)
                ret = msgPop.exec_()
                return

            data = {
                "userid": userid,
                "passwd": passwd
            }
            headers = {'Content-type': 'application/json'}

            try:
                req = requests.patch("http://192.168.56.1:5000/user", data=json.dumps(data), headers=headers)
            except requests.exceptions.ConnectionError as e:
                msgPop.setText(e.__str__())
                msgPop.setStandardButtons(QMessageBox.Ok)
                msgPop.exec_()
                return

            if req.status_code == 200:
                res = req.json()
                msg = res['message']
                code = res['code']

                msgPop.setText(msg)
                msgPop.setStandardButtons(QMessageBox.Ok)
                ret = msgPop.exec_()

                if ret == QMessageBox.Ok and code == 1:
                    print("login btn ok!")

        # join
        elif focusTab == 1:

            msgPop.setWindowTitle("join")
            userid = self.joinidLineEdit.text()
            passwd = self.joinpasswdLineEdit.text()
            checkPasswd = self.joinpasswdCheckLineEdit.text()

            if not userid:
                msgPop.setText("please enter userid")
                msgPop.setStandardButtons(QMessageBox.Ok)
                ret = msgPop.exec_()
                return

            if not passwd:
                msgPop.setText("please enter passwd")
                msgPop.setStandardButtons(QMessageBox.Ok)
                ret = msgPop.exec_()
                return


            if passwd == checkPasswd:
                # regexp MUST !!!!!

                # bcryte
                passwdHash , passwdSalt = self.auth.genHashAndSalt(passwd.encode('utf-8'))

                # header and req data
                data = {
                    "userid": userid,
                    "passwd": passwdHash,
                    "passwdSalt" : passwdSalt
                }
                headers = {'Content-type': 'application/json'}

                try:
                    req = requests.put("http://192.168.56.1:5000/user", data=json.dumps(data), headers=headers)
                except requests.exceptions.ConnectionError as e:
                    # connection refused
                    msgPop.setText(e.__str__())
                    msgPop.setStandardButtons(QMessageBox.Ok)
                    msgPop.exec_()
                    return

                if req.status_code == 200:
                    res = req.json()
                    msg = res['message']
                    code = res['code']

                    msgPop.setText(msg)
                    msgPop.setStandardButtons(QMessageBox.Ok)
                    ret = msgPop.exec_()

                    if ret == QMessageBox.Ok and code == 1:
                        self.joinidLineEdit.setText("")
                        self.joinpasswdLineEdit.setText("")
                        self.joinpasswdCheckLineEdit.setText("")
                        self.loginTabWidget.setCurrentIndex(0)

            else:
                msgPop.setText("please Check password and password(Check)")
                msgPop.setStandardButtons(QMessageBox.Ok)
                msgPop.exec_()

                # pop up modal dialog

    def retranslateUi(self, loginUi):
        _translate = QtCore.QCoreApplication.translate
        # label init
        loginUi.setWindowTitle(_translate("loginUi", "Agile TODO"))
        loginUi.setWindowIcon(QIcon('../icon/icon.png'))

        self.loginidLabel.setText(_translate("loginUi", "id"))
        self.loginpasswdLabel.setText(_translate("loginUi", "passwd"))
        self.loginTabWidget.setTabText(self.loginTabWidget.indexOf(self.loginTab), _translate("loginUi", "login"))
        self.joinidLabel.setText(_translate("loginUi", "id"))
        self.joinpasswdLabel.setText(_translate("loginUi", "passwd"))
        self.joinpasswdCheckLabel.setText(_translate("loginUi", "passwd(Check)"))
        self.loginTabWidget.setTabText(self.loginTabWidget.indexOf(self.joinTab), _translate("loginUi", "join"))
        self.okBtn.setText(_translate("loginUi", "확인"))

        # passwd edit set echo password mode .
        self.loginpasswdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.joinpasswdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.joinpasswdCheckLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        # gen instance auth.
        self.auth = Defender("HARDMODE")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginUi = QtWidgets.QWidget()
    ui = Ui_loginUi()
    ui.setupUi(loginUi)
    loginUi.show()
    sys.exit(app.exec_())
