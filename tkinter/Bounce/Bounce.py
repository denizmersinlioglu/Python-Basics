from tkinter import *
import random
import time
from Ball import Ball
from Paddle import Paddle

tk = Tk()
tk.title("Bounce")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

while 1:
    if not ball.hitBottom:
        ball.draw()
        paddle.draw()

    tk.update()
    tk.update_idletasks()
    time.sleep(0.01)
