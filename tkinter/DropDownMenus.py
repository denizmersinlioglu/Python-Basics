from tkinter import *

root = Tk()


def random():
    print("This is random")


def random2():
    print("This is random2")


mainMenu = Menu(root)
root.configure(menu=mainMenu)

fileMenu = Menu(mainMenu)
fileMenu.add_command(label="Random Function", command=random)
fileMenu.add_command(label="New File", command=random)
fileMenu.add_command(label="Open File", command=random)
fileMenu.add_separator()
fileMenu.add_command(label="Super File", command=random)

editMenu = Menu(mainMenu)
editMenu.add_command(label="Random Function Two", command=random2)

mainMenu.add_cascade(label="File", menu=fileMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)

root.mainloop()
