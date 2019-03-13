from tkinter import *

root = Tk()

theButton = Button(None, text="1 Click Me!", fg="Blue", bg="Yellow")
theButton.pack()

theSecondButton = Button(None, text="2 Click Me!", fg="Red")
theSecondButton.pack(fill=X)

theThirdButton = Button(None, text="3 Click Me!", fg="Purple")
theThirdButton.pack(side=RIGHT, fill=Y)

theFourthButton = Button(None, text="4 Click Me!", fg="Yellow")
theFourthButton.pack()

root.mainloop()
