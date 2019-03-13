from tkinter import *
import random


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turnLeft)
        self.canvas.bind_all("<KeyPress-Right>", self.turnRight)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0

    def turnLeft(self, event):
        self.x = -2

    def turnRight(self, event):
        self.x = 2
