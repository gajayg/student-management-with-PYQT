# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Delete.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 613)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 20, 131, 20))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 60, 311, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 497, 311, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setAcceptDrops(False)
        self.label_8.setLineWidth(0)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(110)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(60, 120, 311, 361))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setSizeIncrement(QtCore.QSize(10, 10))
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.textEdit = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2.setLayout(7, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Delete Menu"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter RollNumber"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.label_8.setText(_translate("Dialog", "StatusBar:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "show status  "))
        self.label_2.setText(_translate("Dialog", "student Details"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Enter the name"))
        self.label_4.setText(_translate("Dialog", "Department"))
        self.label_5.setText(_translate("Dialog", "Year"))
        self.label_6.setText(_translate("Dialog", "Gender"))
        self.radioButton.setText(_translate("Dialog", "Male"))
        self.radioButton_2.setText(_translate("Dialog", "Female"))
        self.label_7.setText(_translate("Dialog", "Address"))
        self.pushButton_2.setText(_translate("Dialog", "Delete Details"))
        self.comboBox.setItemText(0, _translate("Dialog", "---SelectDepartment----"))
        self.comboBox.setItemText(1, _translate("Dialog", "Computer Science"))
        self.comboBox.setItemText(2, _translate("Dialog", "Mechcanical"))
        self.comboBox.setItemText(3, _translate("Dialog", "Electranics and Electrical "))
        self.comboBox.setItemText(4, _translate("Dialog", "Elecronic and communication "))
        self.comboBox.setItemText(5, _translate("Dialog", "Mechtronics"))
        self.comboBox.setItemText(6, _translate("Dialog", "Information Tecnology"))
        self.comboBox.setItemText(7, _translate("Dialog", "Textile "))
        self.comboBox.setItemText(8, _translate("Dialog", "Aeronatical"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "--Select Year--"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "First "))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Second"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Third"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Final"))
        self.label_9.setText(_translate("Dialog", "RollNumber"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Enter RollNumber"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

