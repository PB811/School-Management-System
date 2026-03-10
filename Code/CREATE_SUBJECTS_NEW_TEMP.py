from PyQt5 import QtCore, QtGui, QtWidgets
#import CREATE_SUB_rc
from QRC_FILES import CREATE_SUB
import sys
import pickle
import mysql.connector
import os
from UPDATE_SUBJECTS import *

mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
if mydb.is_connected():
     print("Successfully Connected")
CS_CURSOR = mydb.cursor()
CS_CURSOR.execute("use sms")

def add_data(subid, subject):
    query = "insert into subjects(Subject_ID, Subject) values(%s, %s)"
    global icon
    msg = QtWidgets.QMessageBox()
    try:
        CS_CURSOR.execute(query, (subid, subject))
        mydb.commit()
        msg.setWindowTitle("School Management System")
        msg.setText("New subject added Successfully")
        msg.setWindowIcon(icon)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()
    except Exception as e:
        msg.setWindowTitle("School Management System")
        msg.setText(f"{e}")
        msg.setWindowIcon(icon)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

class Ui_Create_Subjects(object):
    def setup_create_subjects(self, Create_Subjects):
        global icon
        Create_Subjects.setObjectName("Create_Subjects")
        Create_Subjects.resize(623, 830)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Create_Subjects.sizePolicy().hasHeightForWidth())
        Create_Subjects.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        Create_Subjects.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/Pictures/Main_logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Create_Subjects.setWindowIcon(icon)
        Create_Subjects.setStyleSheet("background-color: rgb(0, 0, 0);")
        Create_Subjects.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Create_Subjects)
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
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QtGui.QIntValidator())
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
        self.pushButton_6.clicked.connect(self.clear_bn)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 260, 261, 541))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 330, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_7.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.delete_selected_subject)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 460, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_8.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.update_record)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 590, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.load_db)
        Create_Subjects.setCentralWidget(self.centralwidget)
        self.tableWidget.cellClicked.connect(self.cell_clicked)


        self.retranslateUi(Create_Subjects)
        QtCore.QMetaObject.connectSlotsByName(Create_Subjects)

    def retranslateUi(self, Create_Subjects):
        _translate = QtCore.QCoreApplication.translate
        Create_Subjects.setWindowTitle(_translate("Create_Subjects", "Create Subjects"))
        self.groupBox.setTitle(_translate("Create_Subjects", "Create Subjects"))
        self.label_17.setText(_translate("Create_Subjects", "Subject ID"))
        self.lineEdit.setPlaceholderText(_translate("Create_Subjects", "Enter the subject ID"))
        self.lineEdit_2.setPlaceholderText(_translate("Create_Subjects", "Enter the subject"))
        self.label_18.setText(_translate("Create_Subjects", "Subject"))
        self.pushButton_5.setText(_translate("Create_Subjects", "Create"))
        self.pushButton_6.setText(_translate("Create_Subjects", "Clear"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Create_Subjects", "Subject ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Create_Subjects", "Subject"))
        self.pushButton_7.setText(_translate("Create_Subjects", "Delete Selected Subject"))
        self.pushButton_8.setText(_translate("Create_Subjects", "Update Record"))
        self.pushButton_9.setText(_translate("Create_Subjects", "Refresh List"))

    def load_db(self):
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
        if mydb.is_connected():
            print("Successfully Connected")
        CS_CURSOR = mydb.cursor()
        CS_CURSOR.execute("use sms")
        self.tableWidget.setRowCount(0)
        CS_CURSOR.execute("use sms")
        CS_CURSOR.execute("select *from subjects")
        records = CS_CURSOR.fetchall()
        print(records)
        for row_number, row_record in enumerate(records):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_record):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        mydb.close()

    def clear_bn(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def save_bn(self):
        global icon
        flow = 0
        subid = self.lineEdit.text()
        subject = self.lineEdit_2.text()     
        if subid == "" or subject == "":
            msg.setWindowTitle("School Management System")
            msg.setText("Some or all the fields are Empty, please try again")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        else:
            flow +=1

        if flow == 1:
            add_data(subid, subject)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
        

    def delete_selected_subject(self):
        global icon
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
        if mydb.is_connected():
            print("Successfully Connected")
        CS_CURSOR = mydb.cursor()
        selected_Id = self.tableWidget.currentItem().text()
        current_column = self.tableWidget.currentColumn()
        current_row = self.tableWidget.currentRow()
        msg = QtWidgets.QMessageBox()
        control = 0
        try:
            del_ID = int(selected_Id)
            control += 1
            if current_column != 0:
                pass
            else:
                control += 1
        except Exception as e:
            if selected_Id == None and current_column == None:
                msg.setText("Please select an Subject ID to delete the subject's record")
                msg.setWindowIcon(icon)
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("School Management System")
                msg.exec_()
            else:
                msg.setText("Error! Please select an Subject ID to delete the subject's record")
                msg.setWindowIcon(icon)
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowTitle("School Management System")
                msg.exec_()

        print(control)
        if control == 2:
            if type(del_ID) == int and current_column == 0:
                CS_CURSOR.execute("use sms")
                CS_CURSOR.execute(f"delete from subjects where Subject_ID = {int(del_ID)}")
                mydb.commit()
                self.tableWidget.removeRow(current_row)
                msg.setText("Subject Record Successfully Deleted!")
                msg.setWindowTitle("School Management System")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowIcon(icon)
                msg.exec_()
        elif control == 1:
            msg.setText("Error! Please select an Subject ID to delete the subject's record")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("School Management System")
            msg.exec_()
        mydb.close()

    def update_record(self):
        global icon
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "ilkr1475")
        if mydb.is_connected():
            print("Successfully Connected")
        CS_CURSOR = mydb.cursor()
        msg = QtWidgets.QMessageBox()
        try:
            current_row = self.tableWidget.currentRow()
            subject_ID = self.tableWidget.item(current_row, 0).text()
            subject = self.tableWidget.item(current_row, 1).text()
            l = {subject_ID: subject}
            os.remove("subject_values.dat")
            with open("subject_values.dat", "wb") as f:
                pickle.dump(l, f)
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Update_Subjects()
            self.ui.setup_update_subjects(self.window)
            self.window.show()
        except Exception as e:
            msg.setWindowTitle("School Management System")
            msg.setText("Please select a record first")
            msg.setWindowIcon(icon)
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.exec_()
        mydb.close()

    def cell_clicked(self):
        selected_Id = self.tableWidget.currentItem().text()
        current_column = self.tableWidget.currentColumn()
        try:
            del_ID = int(selected_Id)
        except Exception as e:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Create_Subjects = QtWidgets.QMainWindow()
    ui = Ui_Create_Subjects()
    ui.setup_create_subjects(Create_Subjects)
    Create_Subjects.show()
    sys.exit(app.exec_())
