from tkinter import *
import random


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hitBottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[3] >= self.canvas_height:
            self.hitBottom = True
            self.canvas.create_text(250, 250, text="Game Over")
        if pos[1] <= 0 or pos[3] >= self.canvas_height or self.hit_paddle(pos):
            self.y = -self.y
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x
