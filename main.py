from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

class Calculator:

    def __init__(self):
        Form, Window = uic.loadUiType("interface.ui")
        
        self.form = Form

        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.data = []
        self.data_to_print = ""     # used for display number
        self.math_symbol = 0        # used for decision which mathematical operation will be used
        self.data_first_num = ""    # used for storage of entered first number
        self.data_second_num = ""   # used for storage of entered second number
        self.length_first = 0       # used to aid in the calculation of second number
        self.result = False         # used to aid display the result


    """ main method """

    def main(self):
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Calculator JV")
        self.window.show()
        self.user_input()
        self.app.exec()


    """ assigning buttons to methods """

    def user_input(self):
        self.form.pushButton_0.clicked.connect(self.input_zero)
        self.form.pushButton_1.clicked.connect(self.input_first)
        self.form.pushButton_2.clicked.connect(self.input_second)
        self.form.pushButton_3.clicked.connect(self.input_third)
        self.form.pushButton_4.clicked.connect(self.input_fourth)
        self.form.pushButton_5.clicked.connect(self.input_fifth)
        self.form.pushButton_6.clicked.connect(self.input_sixth)
        self.form.pushButton_7.clicked.connect(self.input_seventh)
        self.form.pushButton_8.clicked.connect(self.input_eigth)
        self.form.pushButton_9.clicked.connect(self.input_ninth)
        self.form.pushButton_C.clicked.connect(self.input_c)
        self.form.pushButton_plus.clicked.connect(self.input_plus)
        self.form.pushButton_minus.clicked.connect(self.input_minus)
        self.form.pushButton_multiplication.clicked.connect(self.input_multiplication)
        self.form.pushButton_division.clicked.connect(self.input_division)
        self.form.pushButton_result.clicked.connect(self.input_result)


    """ output to the display """

    def __str__(self):
        if self.data and not self.result:
            self.data_to_print = ''.join(self.data)
            self.form.calculator_label.setText(self.data_to_print)
        elif self.result:
            self.form.calculator_label.setText(str(self.data_to_print))
        else:
            self.form.calculator_label.setText("0")



    """ Calculator inputs of number buttons """

    def input_zero(self):
        if not self.math_symbol:
            if self.data_to_print != "":
                self.data.append("0")
            else:    
                pass            
        elif self.math_symbol:
            if self.data_to_print != "":
                self.data.append("0")
            else:            
                pass
        self.__str__()

    def input_first(self):
        if not self.math_symbol:
            self.data.append("1")
        elif self.math_symbol:
            self.data.append("1") 
        self.__str__()

    def input_second(self):
        if not self.math_symbol:
            self.data.append("2")
        elif self.math_symbol:
            self.data.append("2") 
        self.__str__()

    def input_third(self):
        if not self.math_symbol:
            self.data.append("3")
        elif self.math_symbol:
            self.data.append("3")
        self.__str__()

    def input_fourth(self):
        if not self.math_symbol:
            self.data.append("4")
        elif self.math_symbol:
            self.data.append("4")
        self.__str__()

    def input_fifth(self):
        if not self.math_symbol:
            self.data.append("5")
        elif self.math_symbol:
            self.data.append("5")
        self.__str__()

    def input_sixth(self):
        if not self.math_symbol:
            self.data.append("6")
        elif self.math_symbol:
            self.data.append("6")
        self.__str__()

    def input_seventh(self):
        if not self.math_symbol:
            self.data.append("7")
        elif self.math_symbol:
            self.data.append("7") 
        self.__str__()

    def input_eigth(self):
        if not self.math_symbol:
            self.data.append("8")
        elif self.math_symbol:
            self.data.append("8")
        self.__str__()

    def input_ninth(self):
        if not self.math_symbol:
            self.data.append("9")
        elif self.math_symbol:
            self.data.append("9") 
        self.__str__()


    """ input for C button which will reset display and data """

    def input_c(self):
        self.data = []
        self.data_to_print = ""
        self.math_symbol = 0
        self.data_first_num = ""
        self.data_second_num = ""
        self.length_first = 0
        self.result = False
        self.__str__()


    """ inputs for math symbols + - * /  """

    def input_plus(self):
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
            self.data.append(" + ")
        else:
            self.data.pop()
            self.data.append(" + ")
        self.math_symbol = 1
        self.__str__()

    def input_minus(self):
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
            self.data.append(" - ")
        else:
            self.data.pop()
            self.data.append(" - ")
        self.math_symbol = 2
        self.__str__()

    def input_multiplication(self):
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
            self.data.append(" * ")
        else:
            self.data.pop()
            self.data.append(" * ")
        self.math_symbol = 3
        self.__str__()

    def input_division(self):
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
            self.data.append(" / ")
        else:
            self.data.pop()
            self.data.append(" / ")
        self.math_symbol = 4
        self.__str__()             

  
    """ if user click on equel sign, program will calculate result and send to dispaly """

    def input_result(self):
        self.length_first = (len(self.data_first_num) + 3)
        self.data_second_num = self.data_to_print[self.length_first:(len(self.data_to_print))]
        self.data_to_print = 0
        if self.math_symbol == 1:
            self.data_to_print = int(self.data_first_num) + int(self.data_second_num)
            self.result = True
        elif self.math_symbol == 2:
            self.data_to_print = int(self.data_first_num) - int(self.data_second_num)
            self.result = True
        elif self.math_symbol == 3:
            self.data_to_print = int(self.data_first_num) * int(self.data_second_num)
            self.result = True
        elif self.math_symbol == 4:
            self.data_to_print = int(self.data_first_num) // int(self.data_second_num)
            self.result = True
        self.__str__()
  
    
cal = Calculator()
cal.main()
