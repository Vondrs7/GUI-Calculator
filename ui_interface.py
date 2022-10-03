# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(255, 265)
        Form.setMinimumSize(QSize(255, 265))
        Form.setMaximumSize(QSize(255, 265))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"")
        self.calculator_label = QLabel(Form)
        self.calculator_label.setObjectName(u"calculator_label")
        self.calculator_label.setGeometry(QRect(10, 10, 231, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.calculator_label.setFont(font)
        self.calculator_label.setLayoutDirection(Qt.RightToLeft)
        self.calculator_label.setStyleSheet(u"color: white;")
        self.calculator_label.setTextFormat(Qt.AutoText)
        self.calculator_label.setScaledContents(False)
        self.calculator_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calculator_label.setWordWrap(False)
        self.calculator_label.setMargin(0)
        self.calculator_label.setIndent(6)
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 50, 75, 23))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;\n"
"")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 50, 75, 23))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(170, 50, 75, 23))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 80, 75, 23))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(90, 80, 75, 23))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(170, 80, 75, 23))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 110, 75, 23))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(90, 110, 75, 23))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(170, 110, 75, 23))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(90, 140, 75, 23))
        self.pushButton_0.setFont(font1)
        self.pushButton_0.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_C = QPushButton(Form)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setGeometry(QRect(10, 140, 75, 23))
        self.pushButton_C.setFont(font1)
        self.pushButton_C.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_plus = QPushButton(Form)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setGeometry(QRect(10, 170, 54, 41))
        self.pushButton_plus.setFont(font1)
        self.pushButton_plus.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_minus = QPushButton(Form)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setGeometry(QRect(70, 170, 54, 41))
        self.pushButton_minus.setFont(font1)
        self.pushButton_minus.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_multiplication = QPushButton(Form)
        self.pushButton_multiplication.setObjectName(u"pushButton_multiplication")
        self.pushButton_multiplication.setGeometry(QRect(130, 170, 54, 41))
        self.pushButton_multiplication.setFont(font1)
        self.pushButton_multiplication.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_division = QPushButton(Form)
        self.pushButton_division.setObjectName(u"pushButton_division")
        self.pushButton_division.setGeometry(QRect(190, 170, 54, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_division.sizePolicy().hasHeightForWidth())
        self.pushButton_division.setSizePolicy(sizePolicy)
        self.pushButton_division.setFont(font1)
        self.pushButton_division.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_division.setCheckable(False)
        self.pushButton_division.setAutoRepeat(False)
        self.pushButton_division.setAutoExclusive(False)
        self.pushButton_division.setAutoDefault(False)
        self.pushButton_division.setFlat(False)
        self.pushButton_result = QPushButton(Form)
        self.pushButton_result.setObjectName(u"pushButton_result")
        self.pushButton_result.setGeometry(QRect(10, 220, 234, 35))
        self.pushButton_result.setFont(font1)
        self.pushButton_result.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        self.pushButton_comma = QPushButton(Form)
        self.pushButton_comma.setObjectName(u"pushButton_comma")
        self.pushButton_comma.setGeometry(QRect(170, 140, 75, 23))
        self.pushButton_comma.setFont(font1)
        self.pushButton_comma.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")

        self.retranslateUi(Form)

        self.pushButton_division.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(accessibility)
        Form.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.calculator_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_C.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_multiplication.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_division.setText(QCoreApplication.translate("Form", u":", None))
        self.pushButton_result.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_comma.setText(QCoreApplication.translate("Form", u",", None))
    # retranslateUi

