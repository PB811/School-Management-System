from PyQt5 import QtCore, QtGui, QtWidgets
#mport LOGIN_PAGE_GB_BG_rc
#import LOGIN_PAGE_LBL2_BG_rc
#import LOGIN_PAGE_LBL_BG_rc
#import LOGIN_PAGE_TB1_BG_rc
#import LOGIN_PAGE_TB2_BG_rc
from QRC_FILES import LOGIN_PAGE_GB_BG, LOGIN_PAGE_LBL_BG, LOGIN_PAGE_LBL2_BG, LOGIN_PAGE_TB1_BG, LOGIN_PAGE_TB2_BG
from SMS_MAIN_INTERFACE import *
import mysql.connector
import sys

global hide_power_flow
hide_power_flow = 0


mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
if mydb.is_connected():
     print("Successfully Connected")
mycursor = mydb.cursor()
mydb.close()

class Ui_LOGIN_PAGE(object):
    global icon
    def setup_login_page(self, LOGIN_PAGE):
        global icon, hide_power_flow
        LOGIN_PAGE.setObjectName("LOGIN_PAGE")
        LOGIN_PAGE.resize(870, 494)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LOGIN_PAGE.sizePolicy().hasHeightForWidth())
        LOGIN_PAGE.setSizePolicy(sizePolicy)
        LOGIN_PAGE.setMinimumSize(QtCore.QSize(870, 494))
        LOGIN_PAGE.setMaximumSize(QtCore.QSize(870, 494))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("QRC_FILES/Pictures/Main_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LOGIN_PAGE.setWindowIcon(icon)
        LOGIN_PAGE.setStyleSheet("background-color: rgb(0, 0, 0);")
        LOGIN_PAGE.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(LOGIN_PAGE)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 351, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-image: url(:/LABEL_UI/Pictures/Logo.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/LABEL_UI/Pictures/Logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 110, 141, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("background-image: url(:/LABEL_BG/Pictures/Login_C.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/LABEL_BG/Pictures/Login_C.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 110, 321, 221))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("background-image: url(:/GB_BG/Pictures/BG.jpg);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 81, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 81, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Login_bn = QtWidgets.QPushButton(self.groupBox)
        self.Login_bn.setGeometry(QtCore.QRect(110, 150, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_bn.sizePolicy().hasHeightForWidth())
        self.Login_bn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.Login_bn.setFont(font)
        self.Login_bn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Login_bn.setShortcut("")
        self.Login_bn.setObjectName("Login_bn")
        self.Login_bn.clicked.connect(self.secure_login)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 100, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setStyleSheet("background-image: url(:/TB2_BG/Pictures/password_bg.jpg);")
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 40, 251, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setStyleSheet("background-image: url(:/TB1_BG/Pictures/username_bg.jpg);")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhPreferUppercase)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        LOGIN_PAGE.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LOGIN_PAGE)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 21))
        self.menubar.setObjectName("menubar")
        LOGIN_PAGE.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LOGIN_PAGE)
        self.statusbar.setObjectName("statusbar")
        LOGIN_PAGE.setStatusBar(self.statusbar)

        self.retranslateUi(LOGIN_PAGE)
        QtCore.QMetaObject.connectSlotsByName(LOGIN_PAGE)

    def retranslateUi(self, LOGIN_PAGE):
        _translate = QtCore.QCoreApplication.translate
        LOGIN_PAGE.setWindowTitle(_translate("LOGIN_PAGE", "Login"))
        self.label_3.setText(_translate("LOGIN_PAGE", "Username"))
        self.label_4.setText(_translate("LOGIN_PAGE", "Password"))
        self.Login_bn.setText(_translate("LOGIN_PAGE", "Login"))
        self.lineEdit_3.setPlaceholderText(_translate("LOGIN_PAGE", "Enter Password"))
        self.lineEdit_2.setPlaceholderText(_translate("LOGIN_PAGE", "Enter Username"))

    def secure_login(self):
        global icon, hide_power_flow
        msg =  QtWidgets.QMessageBox()
        Username = str(self.lineEdit_2.text())
        Password = str(self.lineEdit_3.text())
        control_power_flow = 1
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
        if mydb.is_connected():
            print("Successfully Connected")
        mycursor = mydb.cursor()
        mycursor.execute("use sms")
        mycursor.execute("select *from users")
        users_credentials = mycursor.fetchall()
        for i in range(len(users_credentials)):
            _username = users_credentials[i][1]
            _password = users_credentials[i][2]
            print(_username)
            print(_password)
            if Username == _username and Password == _password:
                control_power_flow += 1
            elif Username == "" or Password == "":
                msg.setWindowTitle("School Management System")
                msg.setWindowIcon(icon)
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("All Fields sre required!")
                msg.exec_()
            else:
                pass
        mydb.close()

        '''
        def hide():
            if hide_power_flow == 9999:
                LOGIN_PAGE.close()
            else:
                pass
        '''

        if control_power_flow == 2:
            msg.setWindowTitle("School Management System")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Welcome")
            msg.exec_()
            a = LOGIN_PAGE
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MAIN_INTERFACE()
            self.ui.setup_sms_main_interface(self.window)
            self.window.show()
            a.close()
        else:
            msg.setWindowTitle("School Management System")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("The entered username or password is wrong")
            msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN_PAGE = QtWidgets.QMainWindow()
    ui = Ui_LOGIN_PAGE()
    ui.setup_login_page(LOGIN_PAGE)
    LOGIN_PAGE.show()
    sys.exit(app.exec_())
