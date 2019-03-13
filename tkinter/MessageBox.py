from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Windows Title", "Did you Know That")
answer = tkinter.messagebox.askquestion("Question 1", "Are you Human?")

if answer == "yes":
    tkinter.messagebox.showinfo("Congrats", "You are human")

if answer == "no":
    tkinter.messagebox.showinfo("Alien", "You are confirmed alien")

root.mainloop()
