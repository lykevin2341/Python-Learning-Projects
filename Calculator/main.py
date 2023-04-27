import tkinter as tk
from tkinter import *

expression = ""

def press(num):
  global expression
  expression = expression + str(num)
  equation.set(expression)

def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""

def clear():
  global expression
  expression = ""
  equation.set("")

if __name__ == "__main__":
  calculatorWindow = tk.Tk(className="Calculator")
  calculatorWindow.geometry("360x480")
  equation = tk.StringVar()
  box = tk.Entry(calculatorWindow, text=equation)
  box.grid(columnspan=4, ipadx=97)
  one = tk.Button(
    text="1",
    command=lambda: press(1),
    width=2,
    height=2,
    bg="grey"
  )
  two = tk.Button(
    calculatorWindow,
    text="2",
    command=lambda: press(2),
    width=2,
    height=2,
    bg="grey",
  )
  three = tk.Button(
    calculatorWindow,
    text="3",
    command=lambda: press(3),
    width=2,
    height=2,
    bg="grey",
  )
  four = tk.Button(
    calculatorWindow,
    text="4",
    command=lambda: press(4),
    width=2,
    height=2,
    bg="grey",
  )
  five = tk.Button(
    calculatorWindow,
    text="5",
    command=lambda: press(5),
    width=2,
    height=2,
    bg="grey",
  )
  six = tk.Button(
    calculatorWindow,
    text="6",
    command=lambda: press(6),
    width=2,
    height=2,
    bg="grey",
  )
  clear = tk.Button(
    calculatorWindow,
    text="CL",
    command=clear,
    width=4,
    height=2,
    bg="grey"
  )
  plus = tk.Button(
    calculatorWindow,
    text="+",
    command=lambda: press("+"), 
    height=4, 
    width=2,
    bg="grey"
  )
  one.place(x=10, y=80)
  two.place(x=70, y=80)
  three.place(x=130, y=80)
  four.place(x=190, y=80)
  five.place(x=250, y=80)
  six.place(x=310, y=80)
  clear.place(x=310, y=140)
  plus.place(x=310, y=200)
  calculatorWindow.mainloop()
  