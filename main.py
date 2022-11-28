#from pickle import FALSE
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

class Calculator:

    def __init__(self):
        
        Form, Window = uic.loadUiType("interface.ui")
        
        self.form = Form

        self.app = QApplication([])
        self.window = Window()
        self.form = Form()
        self.data = ["0"]
        self.data_to_print = "0"            # used for display number
        self.math_symbol = 0                # used for decision which mathematical operation will be used
        self.data_first_num = ""            # used for storage of entered first number
        self.data_second_num = ""           # used for storage of entered second number
        self.length_first = 0               # used to aid in the calculation of second number
        self.result = False                 # used to aid display the result
        self.error = False                  # used if is error (for example for division by 0)
        self.max_one_comma = False          # we need to have only one comma in each number
        self.percent = False                # used to count the percentage

        self.math_symbols = [" + ", " - ", " x ", " ÷ "]

        self.error_message_zero = "Not divisible by 0"  # error message for division by 0
        self.error_message_zero_2 = "Cannot divide 0"   # error message when user divide 0


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
        self.form.pushButton_comma.clicked.connect(self.input_comma)
        self.form.pushButton_backspace.clicked.connect(self.input_backspace)
        self.form.pushButton_plus_minus.clicked.connect(self.input_plus_minus)
        self.form.pushButton_percent.clicked.connect(self.input_percent)


    """ output to the display """

    def __str__(self):
        if self.data and not self.result:
            if len(self.data) > 1 and self.data[0] == "0" and not self.math_symbol and self.data[1] != ".":
                del(self.data[0])
            if self.math_symbol and not self.max_one_comma and len(self.data) > 2:
                if self.data[-2] == "0" and self.data[-3] in self.math_symbols:
                    del(self.data[-2]) 
            self.data_to_print = ''.join(self.data)
            if self.data_to_print.find(".") > 0:
                self.data_to_print = self.data_to_print.replace(".",",")
            self.form.calculator_label_input.setText(self.data_to_print)
            if self.data_to_print.find(",") > 0:
                self.data_to_print = self.data_to_print.replace(",",".")
        elif self.error:
            self.form.calculator_label_input.setText(self.data_to_print)
        elif self.result:
            if self.data_to_print < 1 and self.data_to_print > 0:
                pass
            elif self.data_to_print == 0.0 or self.data_to_print % round(self.data_to_print) == 0:
                self.data_to_print = int(self.data_to_print)                                            # if the number is without a decimal, it will display it without a decimal (as int)               
            self.data_to_print = str(self.data_to_print)  
            self.data_to_print = self.data_to_print.replace(".",",")            
            self.form.calculator_label_result.setText(self.data_to_print)
        else:
            self.form.calculator_label_input.setText("0")


    """ Calculator inputs of number buttons """

    def input_zero(self):
        if not self.math_symbol:
            if (len(self.data) == 1):
                if self.data[0] != "0" and self.data[0] != "-":
                    self.data.append("0")
            else:
                self.data.append("0")         
        elif self.math_symbol:
            if self.data[-1] == "0" and self.data[-2] in self.math_symbols:
                pass
            else:            
                self.data.append("0")
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


    """ comma (dot) input for float numbers """

    def input_comma(self):
        if self.data[-1] == ".":
            pass
        else:
            if self.result == True:
                self.next_number()
            if self.data[-1] in self.math_symbols:
                self.data.append("0")
            if not self.max_one_comma:
                self.data.append(".")
                self.max_one_comma = True
            self.__str__()


    """ input for C button which will reset display and data """

    def input_c(self):
        self.data = ["0"]
        self.data_to_print = "0"
        self.math_symbol = 0
        self.data_first_num = ""
        self.data_second_num = ""
        self.length_first = 0
        self.result = False
        self.error = False
        self.max_one_comma = False
        self.math_symbol = False
        self.percent = False
        self.form.calculator_label_result.setText("")
        self.__str__()


    """ method for backspace button for remove last number or symbol """

    def input_backspace(self):
        if (len(self.data) == 1):
                if self.data[0] != "0":
                    self.data[0] = "0"
        elif self.result:
            self.form.calculator_label_result.setText("")
            self.result = False   
        else:
            if self.data[-1] in self.math_symbols:
                self.math_symbol = False
            if self.data[-1] == ".":
                self.max_one_comma = False
            del(self.data[-1])
        self.__str__()


    """ method to switch the number to a positive or negative """

    def input_plus_minus(self):
        if self.math_symbol == False:
            if (len(self.data) == 1):
                    if self.data[0] == "0":
                        self.data.append("-")
                    elif self.data[0] != "-":
                        self.data.reverse()
                        self.data.append("-")
                        self.data.reverse()
            elif "-" in self.data[0]:
                self.data.remove("-")
                self.data.insert(0,"0")
            elif self.data[0] != "-":
                self.data.reverse()
                self.data.append("-")
                self.data.reverse()
        if self.result:
            self.next_number()
            if not self.data_to_print.startswith("-"):
                self.data.reverse()
                self.data.append("-")
                self.data.reverse()              
            else:
                self.data_to_print = self.data_to_print.replace("-","0")
        self.__str__()

    """ method to count the percentage """
    
    def input_percent(self):
        if self.data[-1] != ".":
            if self.math_symbol:
                self.percent = True
            self.input_result()


    """ method for operations with multiple numbers  """

    def next_number(self):
        self.form.calculator_label_result.setText("")
        if self.result:
            self.data = []
            for x in self.data_to_print:
                self.data.append(x)
            self.math_symbol = False
            self.result = False
            self.max_one_comma = False
            self.percent = False
            try:
                self.data_to_print = self.data_to_print.replace(",",".")
            except:
                pass
        else:
            self.max_one_comma = False

    """ inputs for math symbols + - x :  """

    def input_plus(self):
        self.next_number()
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
        elif self.math_symbol and self.data[-1] not in self.math_symbols:
            self.input_result()
            self.data_first_num = self.data_to_print
            self.next_number()
        else:
            self.data.pop()
        self.data.append(self.math_symbols[0])
        self.math_symbol = 1
        self.__str__()

    def input_minus(self):
        self.next_number()
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
        elif self.math_symbol and self.data[-1] not in self.math_symbols:
            self.input_result()
            self.data_first_num = self.data_to_print
            self.next_number()
        else:
            self.data.pop()
        self.data.append(self.math_symbols[1])
        self.math_symbol = 2
        self.__str__()

    def input_multiplication(self):
        self.next_number()
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
        elif self.math_symbol and self.data[-1] not in self.math_symbols:
            self.input_result()
            self.data_first_num = self.data_to_print
            self.next_number()
        else:
            self.data.pop()
        self.data.append(self.math_symbols[2])
        self.math_symbol = 3
        self.__str__()

    def input_division(self):
        self.next_number()
        if not self.math_symbol:
            self.data_first_num = self.data_to_print
        elif self.math_symbol and self.data[-1] not in self.math_symbols:
            self.input_result()
            self.data_first_num = self.data_to_print
            self.next_number()
        else:
            self.data.pop()
        self.data.append(self.math_symbols[3])
        self.math_symbol = 4
        self.__str__()             

  
    """ if user click on equel sign, program will calculate result and send to dispaly """

    def input_result(self):
        if self.result == True:
            pass
        else:
            self.length_first = len(self.data_first_num) + 3
            self.data_second_num = self.data_to_print[self.length_first:len(self.data_to_print)]
            if self.data[-1] in self.math_symbols:
                pass
            elif self.math_symbol == 1:
                if self.percent:
                    self.data_to_print = float(self.data_first_num) + (float(self.data_first_num) / 100 * float(self.data_second_num))
                else:
                    self.data_to_print = float(self.data_first_num) + float(self.data_second_num)
                    self.data_to_print = round(self.data_to_print, 3)
                self.result = True
            elif self.math_symbol == 2:
                if self.percent:
                    self.data_to_print = float(self.data_first_num) - (float(self.data_first_num) / 100 * float(self.data_second_num))
                else:
                    self.data_to_print = float(self.data_first_num) - float(self.data_second_num)
                    self.data_to_print = round(self.data_to_print, 3)
                self.result = True
            elif self.math_symbol == 3:
                if self.percent:
                    self.data_to_print = float(self.data_first_num) / 100 * float(self.data_second_num)
                    self.data_to_print = round(self.data_to_print, 3)
                else:
                    self.data_to_print = float(self.data_first_num) * float(self.data_second_num)
                    self.data_to_print = round(self.data_to_print, 3)
                self.result = True
            elif self.math_symbol == 4:
                if self.data_second_num == "0" and not self.percent:
                    self.data_to_print = self.error_message_zero
                    self.error = True
                elif self.data_first_num == "0" and not self.percent:
                    self.data_to_print = self.error_message_zero_2
                    self.error = True
                elif self.percent:
                    if float(self.data_first_num) == 0 and float(self.data_second_num) != 0:
                        self.data_to_print = float(self.data_second_num) / 100
                    elif float(self.data_second_num) == 0:
                        self.data_to_print = 0
                    else:
                        self.data_to_print = 100 / float(self.data_second_num) * float(self.data_first_num)
                else:
                    self.data_to_print = float(self.data_first_num) / float(self.data_second_num)
                    self.data_to_print = round(self.data_to_print, 3)
                self.result = True
            self.__str__()
  
    
cal = Calculator()
cal.main()

