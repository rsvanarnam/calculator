import tkinter as tk

expression = ''

# Functions
class Calculator():
    def input_number(number, equation):
        global expression
        expression = expression + str(number)
        equation.set(expression)

    def clear_input(equation):
        global expression
        expression = ''
        equation.set('0')

    def evaluate(equation):
        global expression
        try:
            result = str(eval(expression))
            equation.set(result)
            expression = ''
        except:
            expression = 'Error'

# GUI
root = tk.Tk()
root.title('Calculator')
root.geometry('390x375')
equation = tk.StringVar()
display = tk.Entry(root, textvariable=equation)
display.grid(columnspan=5, ipadx=125)
equation.set('0')

class Button():
    def standard_button(set_text, set_input, set_row, set_column):
        button = tk.Button(root, text = set_text, command=lambda: Calculator.input_number(set_input, equation), height = 4, width = 14)
        button.grid(row = set_row, column = set_column)

    def small_button(set_text, set_input, set_row, set_column):
        button = tk.Button(root, text = set_text, command=lambda: Calculator.input_number(set_input, equation), height = 4, width = 8)
        button.grid(row = set_row, column = set_column)

    def long_button(set_text, set_input, set_row, set_column):
        button = tk.Button(root, text = set_text, command=lambda: Calculator.input_number(set_input, equation), height = 4, width = 30)
        button.grid(row = set_row, column = set_column, columnspan = 2)

    def clear_button(set_text, set_row, set_column):
        button = tk.Button(root, text = set_text, command=lambda: Calculator.clear_input(equation), height = 4, width = 14)
        button.grid(row = set_row, column = set_column)

    def evaluate_button(set_text, set_row, set_column):
        button = tk.Button(root, text = set_text, command=lambda: Calculator.evaluate(equation), height = 4, width = 8)
        button.grid(row = set_row, column = set_column)

# Calculator buttons. Parameters are: Text, Column, Row
Button.clear_button('C', 2, 1)
Button.standard_button('(-)', '-', 2, 2)
Button.standard_button('^', '**', 2, 3)
Button.small_button('/', '/', 2, 4)

Button.standard_button('7', 7, 3, 1)
Button.standard_button('8', 8, 3, 2)
Button.standard_button('9', 9, 3, 3)
Button.small_button('x', '*', 3, 4)

Button.standard_button('4', 4, 4, 1)
Button.standard_button('5', 5,  4, 2)
Button.standard_button('6', 6, 4, 3)
Button.small_button('-', '-', 4, 4)

Button.standard_button('1', 1, 5, 1)
Button.standard_button('2', 2, 5, 2)
Button.standard_button('3', 3, 5, 3)
Button.small_button('+', '+', 5, 4)

Button.long_button('0', 0, 6, 1)
Button.standard_button('.', '.', 6, 3)
Button.evaluate_button('=', 6, 4)

root.mainloop()

"""
To do:
1. Refactor buttons.
"""