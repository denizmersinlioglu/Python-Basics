from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

theLabel = Label(root, text="This is our tkinter window")
theLabel.pack()

theLabel = Label(root, text="This is our second tkinter window")
theLabel.pack()

theButton = Button(topFrame, text="1 Click Me!", fg="Blue")
theButton.pack(side=LEFT)

theSecondButton = Button(topFrame, text="2 Click Me!", fg="Red")
theSecondButton.pack(side=LEFT)

theThirdButton = Button(bottomFrame, text="3 Click Me!", fg="Purple")
theThirdButton.pack(side=LEFT)

theFourthButton = Button(bottomFrame, text="4 Click Me!", fg="Yellow")
theFourthButton.pack(side=LEFT)

root.mainloop()
