"""
To do:
1. Refactor buttons. For loops and lists?
2. Figure out displaying data.
3. Make buttons what they are supposed to. =)
"""

import tkinter as tk

root = tk.Tk()
root.title("Calculator")
canvas = tk.Canvas(master = root, width = 56, height = 100)
canvas.grid(row = 1, column = 1)

class Button:
    def __init__(self, setText, setRow, setColumn):
        self.setText = setText
        self.setRow
        self.setColumn

    def standardButton(setText, setRow, setColumn):
        button = tk.Button(root, text = setText, height = 4, width = 14)
        button.grid(row = setRow, column = setColumn)

    def smallButton(setText, setRow, setColumn):
        """A half size button, used for the xxx buttons on the right side"""
        button = tk.Button(root, text = setText, height = 4, width = 8)
        button.grid(row = setRow, column = setColumn)

    def longButton(setText, setRow, setColumn):
        """A button that spans two rows. Used for the '0' Button"""
        button = tk.Button(root, text = setText, height = 4, width = 30)
        button.grid(row = setRow, column = setColumn, columnspan = 2)



# Calculator buttons. Parameters are: Text, Column, Row
Button.standardButton('C', 2, 1)
Button.standardButton('+/-', 2, 2)
Button.standardButton('%', 2, 3)
Button.smallButton('/', 2, 4)

Button.standardButton('7', 3, 1)
Button.standardButton('8', 3, 2)
Button.standardButton('9', 3, 3)
Button.smallButton('x', 3, 4)

Button.standardButton('4', 4, 1)
Button.standardButton('5', 4, 2)
Button.standardButton('6', 4, 3)
Button.smallButton('-', 4, 4)

Button.standardButton('1', 5, 1)
Button.standardButton('2', 5, 2)
Button.standardButton('3', 5, 3)
Button.smallButton('+', 5, 4)

Button.longButton('0', 6, 1)
#Button.standardButton('', 6, 2)
Button.standardButton('.', 6, 3)
Button.smallButton('=', 6, 4)

root.mainloop()