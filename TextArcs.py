from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
canvas.create_arc(10, 80, 200, 160, extent=167, style=ARC)

canvas.create_text(150, 150, text="First GUI text", font=("Times,30"))

root.mainloop()
