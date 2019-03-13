from tkinter import *

root = Tk()

equa = ""

equation = StringVar()  # when its updated, update the label text
calculation = Label(root, textvariable=equation)
equation.set("Enter your Equation")

calculation.grid(columnspan=4)


def button_press(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


Button1 = Button(root, text="1", command=lambda: button_press(1))
Button1.grid(row=1, column=0)
Button2 = Button(root, text="2", command=lambda: button_press(2))
Button2.grid(row=1, column=1)
Button3 = Button(root, text="3", command=lambda: button_press(3))
Button3.grid(row=1, column=2)
ButtonPlus = Button(root, text="+", command=lambda: button_press("+"))
ButtonPlus.grid(row=1, column=3)

Button4 = Button(root, text="4", command=lambda: button_press(4))
Button4.grid(row=2, column=0)
Button5 = Button(root, text="5", command=lambda: button_press(5))
Button5.grid(row=2, column=1)
Button6 = Button(root, text="6", command=lambda: button_press(6))
Button6.grid(row=2, column=2)
ButtonMinus = Button(root, text="-", command=lambda: button_press("-"))
ButtonMinus.grid(row=2, column=3)

Button7 = Button(root, text="7", command=lambda: button_press(7))
Button7.grid(row=3, column=0)
Button8 = Button(root, text="8", command=lambda: button_press(8))
Button8.grid(row=3, column=1)
Button9 = Button(root, text="9", command=lambda: button_press(9))
Button9.grid(row=3, column=2)
ButtonProduct = Button(root, text="*", command=lambda: button_press("*"))
ButtonProduct.grid(row=3, column=3)

Button0 = Button(root, text="0", command=lambda: button_press(0))
Button0.grid(row=4, column=1)

ButtonDivide = Button(root, text="/", command=lambda: button_press("/"))
ButtonDivide.grid(row=4, column=3)


def equal_pressed():
    global equa
    equation.set(str(eval(equa)))
    equa = ""


def clear_pressed():
    global equa
    equa = ""
    equation.set("")


Equal = Button(root, text="=", command=equal_pressed)
Equal.grid(row=4, column=2)
Clear = Button(root, text="C", command=clear_pressed)
Clear.grid(row=4, column=0)

root.mainloop()
