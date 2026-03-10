from PyQt5 import QtCore, QtGui, QtWidgets
#import CREATE_SUB_rc
from QRC_FILES import CREATE_SUB
import sys
import mysql.connector
import pickle

global l

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
if mydb.is_connected():
     print("Successfully Connected")
US_CURSOR = mydb.cursor()
US_CURSOR.execute("use sms")

def fill():
    global l, update_subject_ID, update_subject
    with open("subject_values.dat", "rb") as f:
        try:
            while True:
                l = pickle.load(f)
        except Exception as e:
            pass
    for key, value in l.items():
        update_subject_ID = key
        update_subject = value

def update_data(subid, subject, control):
    global icon
    query1 = "update subjects set Subject = %s where Subject_ID = %s"
    query2 = "update subjects set Subject_ID = %s where Subject = %s "
    msg = QtWidgets.QMessageBox()
    if control == 1:
        try:
            US_CURSOR.execute(query1, (subject, int(subid)))
            mydb.commit()
            msg.setWindowTitle("School Management System")
            msg.setText("Subject Record Updated Successfully")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
        except Exception as e:
            msg.setWindowTitle("School Management System")
            msg.setText(f"{e}")
            print(e)
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
    elif control == 2:
        try:
            US_CURSOR.execute(query2, (int(subid), subject))
            mydb.commit()
            msg.setWindowTitle("School Management System")
            msg.setText("Subject Record Updated Successfully")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.exec_()
        except Exception as e:
            msg.setWindowTitle("School Management System")
            msg.setText(f"{e}")
            print(e)
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()



class Ui_Update_Subjects(object):
    global l, update_subject_ID, update_subject
    def setup_update_subjects(self, Update_Subjects):
        global l, icon
        fill()
        Update_Subjects.setObjectName("Update_Subjects")
        Update_Subjects.resize(623, 268)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Update_Subjects.sizePolicy().hasHeightForWidth())
        Update_Subjects.setSizePolicy(sizePolicy)
        Update_Subjects.setMinimumSize(QtCore.QSize(623, 268))
        Update_Subjects.setMaximumSize(QtCore.QSize(623, 268))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        Update_Subjects.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/Pictures/Main_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Update_Subjects.setWindowIcon(icon)
        Update_Subjects.setStyleSheet("background-color: rgb(0, 0, 0);")
        Update_Subjects.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Update_Subjects)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 581, 221))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-image: url(:/PIC/Pictures/BG.jpg);")
        self.groupBox.setObjectName("groupBox")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(30, 40, 181, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setLineWidth(1)
        self.label_17.setObjectName("label_17")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 201, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("background-image: url(:/PIC/Pictures/TB_PIC.png);")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setMaxLength(30)
        self.lineEdit.setFrame(False)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        #self.lineEdit.setValidator(QtGui.QSpaceValidator())
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 70, 281, 31))
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
        self.lineEdit_2.setStyleSheet("background-image: url(:/PIC/Pictures/TB_PIC.png);")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setMaxLength(30)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(270, 40, 181, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setLineWidth(1)
        self.label_18.setObjectName("label_18")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 140, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.save_bn)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 140, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.cancel_bn)
        Update_Subjects.setCentralWidget(self.centralwidget)

        self.lineEdit.setText(update_subject_ID)
        self.lineEdit_2.setText(update_subject)

        self.retranslateUi(Update_Subjects)
        QtCore.QMetaObject.connectSlotsByName(Update_Subjects)

    def retranslateUi(self, Update_Subjects):
        _translate = QtCore.QCoreApplication.translate
        Update_Subjects.setWindowTitle(_translate("Update_Subjects", "Update Subjects"))
        self.groupBox.setTitle(_translate("Update_Subjects", "Update Subjects"))
        self.label_17.setText(_translate("Update_Subjects", "Subject ID"))
        self.label_18.setText(_translate("Update_Subjects", "Subject"))
        self.pushButton_5.setText(_translate("Update_Subjects", "Update"))
        self.pushButton_6.setText(_translate("Update_Subjects", "Cancel"))

    def cancel_bn(self):
       QtCore.QCoreApplication.quit()

    def save_bn(self):
        global icon, update_subject_ID, update_subject
        flow = 0
        control = 0
        msg = QtWidgets.QMessageBox()
        subid = self.lineEdit.text()
        subject = self.lineEdit_2.text()
        print(update_subject_ID, update_subject)
        if subid != update_subject_ID and subject != update_subject:
            msg.setWindowTitle("School Management System")
            msg.setText("Please change at most one parameter at a time")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec()
        elif subid == "" or subject == "":
            msg.setWindowTitle("School Management System")
            msg.setText("Some or all the fields are Empty, please try again")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        elif subid == update_subject_ID and subject == update_subject:
            msg.setWindowTitle("School Management System")
            msg.setText("Please change at least one parameter at a time")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            flow += 1

        #Changing one parameter at a time
        if flow == 1:
            if subid == update_subject_ID:
                control += 1
                update_data(subid, subject, control)
            elif subject == update_subject:
                control += 2
                update_data(subid, subject, control)

if __name__ == "__main__":
    global Update_Subjects
    app = QtWidgets.QApplication(sys.argv)
    Update_Subjects = QtWidgets.QMainWindow()
    ui = Ui_Update_Subjects()
    ui.setup_update_subjects(Update_Subjects)
    Update_Subjects.show()
    sys.exit(app.exec_())
