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
        Form.resize(255, 335)
        Form.setMinimumSize(QSize(255, 335))
        Form.setMaximumSize(QSize(255, 335))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"")
        self.calculator_label_input = QLabel(Form)
        self.calculator_label_input.setObjectName(u"calculator_label_input")
        self.calculator_label_input.setGeometry(QRect(10, 10, 235, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.calculator_label_input.setFont(font)
        self.calculator_label_input.setLayoutDirection(Qt.RightToLeft)
        self.calculator_label_input.setStyleSheet(u"color: rgb(218, 218, 218);\n"
"background-color:rgb(45, 45, 45);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;")
        self.calculator_label_input.setTextFormat(Qt.AutoText)
        self.calculator_label_input.setScaledContents(False)
        self.calculator_label_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calculator_label_input.setWordWrap(False)
        self.calculator_label_input.setMargin(0)
        self.calculator_label_input.setIndent(6)
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 120, 75, 23))
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon = QIcon()
        icon.addFile(u"pictures/one_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setIconSize(QSize(20, 20))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 120, 75, 23))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon1 = QIcon()
        icon1.addFile(u"pictures/two_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(170, 120, 75, 23))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon2 = QIcon()
        icon2.addFile(u"pictures/three_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 150, 75, 23))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon3 = QIcon()
        icon3.addFile(u"pictures/four_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 20))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(90, 150, 75, 23))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon4 = QIcon()
        icon4.addFile(u"pictures/five_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(20, 20))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(170, 150, 75, 23))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon5 = QIcon()
        icon5.addFile(u"pictures/six_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 180, 75, 23))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon6 = QIcon()
        icon6.addFile(u"pictures/seven_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(20, 20))
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(90, 180, 75, 23))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon7 = QIcon()
        icon7.addFile(u"pictures/eight_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(20, 20))
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(170, 180, 75, 23))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon8 = QIcon()
        icon8.addFile(u"pictures/nine_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(90, 210, 75, 23))
        self.pushButton_0.setFont(font1)
        self.pushButton_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet(u"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 55, 55);")
        icon9 = QIcon()
        icon9.addFile(u"pictures/zero_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_0.setIcon(icon9)
        self.pushButton_0.setIconSize(QSize(20, 20))
        self.pushButton_C = QPushButton(Form)
        self.pushButton_C.setObjectName(u"pushButton_C")
        self.pushButton_C.setGeometry(QRect(10, 210, 75, 23))
        self.pushButton_C.setFont(font1)
        self.pushButton_C.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_C.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon10 = QIcon()
        icon10.addFile(u"pictures/C_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_C.setIcon(icon10)
        self.pushButton_C.setIconSize(QSize(20, 20))
        self.pushButton_plus = QPushButton(Form)
        self.pushButton_plus.setObjectName(u"pushButton_plus")
        self.pushButton_plus.setGeometry(QRect(10, 240, 54, 41))
        self.pushButton_plus.setFont(font1)
        self.pushButton_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_plus.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon11 = QIcon()
        icon11.addFile(u"pictures/plus_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_plus.setIcon(icon11)
        self.pushButton_plus.setIconSize(QSize(22, 22))
        self.pushButton_minus = QPushButton(Form)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        self.pushButton_minus.setGeometry(QRect(70, 240, 54, 41))
        self.pushButton_minus.setFont(font1)
        self.pushButton_minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minus.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon12 = QIcon()
        icon12.addFile(u"pictures/minus_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minus.setIcon(icon12)
        self.pushButton_minus.setIconSize(QSize(22, 22))
        self.pushButton_multiplication = QPushButton(Form)
        self.pushButton_multiplication.setObjectName(u"pushButton_multiplication")
        self.pushButton_multiplication.setGeometry(QRect(130, 240, 54, 41))
        self.pushButton_multiplication.setFont(font1)
        self.pushButton_multiplication.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_multiplication.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"pictures/bold_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_multiplication.setIcon(icon13)
        self.pushButton_multiplication.setIconSize(QSize(22, 22))
        self.pushButton_division = QPushButton(Form)
        self.pushButton_division.setObjectName(u"pushButton_division")
        self.pushButton_division.setGeometry(QRect(190, 240, 54, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_division.sizePolicy().hasHeightForWidth())
        self.pushButton_division.setSizePolicy(sizePolicy)
        self.pushButton_division.setFont(font1)
        self.pushButton_division.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_division.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon14 = QIcon()
        icon14.addFile(u"pictures/div_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_division.setIcon(icon14)
        self.pushButton_division.setIconSize(QSize(20, 20))
        self.pushButton_division.setCheckable(False)
        self.pushButton_division.setAutoRepeat(False)
        self.pushButton_division.setAutoExclusive(False)
        self.pushButton_division.setAutoDefault(False)
        self.pushButton_division.setFlat(False)
        self.pushButton_result = QPushButton(Form)
        self.pushButton_result.setObjectName(u"pushButton_result")
        self.pushButton_result.setGeometry(QRect(10, 290, 234, 35))
        self.pushButton_result.setFont(font1)
        self.pushButton_result.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_result.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon15 = QIcon()
        icon15.addFile(u"pictures/result_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_result.setIcon(icon15)
        self.pushButton_result.setIconSize(QSize(24, 24))
        self.pushButton_comma = QPushButton(Form)
        self.pushButton_comma.setObjectName(u"pushButton_comma")
        self.pushButton_comma.setGeometry(QRect(170, 210, 75, 23))
        self.pushButton_comma.setFont(font1)
        self.pushButton_comma.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_comma.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon16 = QIcon()
        icon16.addFile(u"pictures/com_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_comma.setIcon(icon16)
        self.pushButton_comma.setIconSize(QSize(20, 20))
        self.calculator_label_result = QLabel(Form)
        self.calculator_label_result.setObjectName(u"calculator_label_result")
        self.calculator_label_result.setGeometry(QRect(10, 40, 235, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setKerning(True)
        self.calculator_label_result.setFont(font2)
        self.calculator_label_result.setLayoutDirection(Qt.RightToLeft)
        self.calculator_label_result.setStyleSheet(u"color: white;\n"
"background-color:rgb(45, 45, 45);\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.calculator_label_result.setTextFormat(Qt.AutoText)
        self.calculator_label_result.setScaledContents(False)
        self.calculator_label_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calculator_label_result.setWordWrap(False)
        self.calculator_label_result.setMargin(0)
        self.calculator_label_result.setIndent(6)
        self.pushButton_backspace = QPushButton(Form)
        self.pushButton_backspace.setObjectName(u"pushButton_backspace")
        self.pushButton_backspace.setGeometry(QRect(170, 90, 75, 23))
        self.pushButton_backspace.setFont(font1)
        self.pushButton_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backspace.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon17 = QIcon()
        icon17.addFile(u"pictures/backspace_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_backspace.setIcon(icon17)
        self.pushButton_backspace.setIconSize(QSize(20, 20))
        self.pushButton_plus_minus = QPushButton(Form)
        self.pushButton_plus_minus.setObjectName(u"pushButton_plus_minus")
        self.pushButton_plus_minus.setGeometry(QRect(10, 90, 75, 23))
        self.pushButton_plus_minus.setFont(font1)
        self.pushButton_plus_minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_plus_minus.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon18 = QIcon()
        icon18.addFile(u"pictures/plus_minus_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_plus_minus.setIcon(icon18)
        self.pushButton_plus_minus.setIconSize(QSize(20, 20))
        self.pushButton_percent = QPushButton(Form)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setGeometry(QRect(90, 90, 75, 23))
        self.pushButton_percent.setFont(font1)
        self.pushButton_percent.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_percent.setStyleSheet(u"color: white;\n"
"background-color: rgb(158, 158, 158);\n"
"border-radius: 10px;")
        icon19 = QIcon()
        icon19.addFile(u"pictures/percent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_percent.setIcon(icon19)
        self.pushButton_percent.setIconSize(QSize(13, 13))

        self.retranslateUi(Form)

        self.pushButton_division.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(accessibility)
        Form.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.calculator_label_input.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_0.setText("")
        self.pushButton_C.setText("")
        self.pushButton_plus.setText("")
        self.pushButton_minus.setText("")
        self.pushButton_multiplication.setText("")
        self.pushButton_division.setText("")
        self.pushButton_result.setText("")
        self.pushButton_comma.setText("")
        self.calculator_label_result.setText("")
        self.pushButton_backspace.setText("")
        self.pushButton_plus_minus.setText("")
        self.pushButton_percent.setText("")
    # retranslateUi

