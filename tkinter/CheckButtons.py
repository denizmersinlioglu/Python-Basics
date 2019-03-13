from tkinter import *

root = Tk()

label1 = Label(root, text="Name: ")
label1.grid(row=0, column=0, sticky="E")

entrySpace = Entry(root)
entrySpace.grid(row=0, column=1)

label1 = Label(root, text="Password: ")
label1.grid(row=1, column=0, sticky="E")

entryPassword = Entry(root)
entryPassword.grid(row=1, column=1)

cbutton = Checkbutton(root, text="Remember password")
cbutton.grid(row=2, columnspan=2)

root.mainloop()
