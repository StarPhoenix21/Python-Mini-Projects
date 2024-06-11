from itertools import cycle
from random import randrange
from tkinter import messagebox, Tk, Canvas


class EggCatchGame:
    def __init__(self, win, canvas):
        self.win = win
        self.canvas = canvas

        self.canvas_width = 800
        self.canvas_height = 400

        self.color_cycle = cycle(
            ['light blue', 'light pink', 'light yellow', 'light green', 'red', 'blue', 'green', 'black'])
        self.egg_width = 45
        self.egg_height = 55
        self.egg_score = 10
        self.egg_speed = 500
        self.egg_interval = 4000
        self.difficulty_factor = 0.95

        self.catcher_color = 'blue'
        self.catcher_width = 100
        self.catcher_height = 100
        self.catcher_start_x = self.canvas_width / 2 - self.catcher_width / 2
        self.catcher_start_y = self.canvas_height - self.catcher_height - 20
        self.catcher_start_x2 = self.catcher_start_x + self.catcher_width
        self.catcher_start_y2 = self.catcher_start_y + self.catcher_height

        self.catcher = self.canvas.create_arc(self.catcher_start_x, self.catcher_start_y, self.catcher_start_x2,
                                              self.catcher_start_y2, start=200, extent=140, style='arc',
                                              outline=self.catcher_color, width=3)

        self.score = 0
        self.score_text = self.canvas.create_text(10, 10, anchor='nw', font=('Arial', 18, 'bold'), fill='darkblue',
                                                  text='Score : ' + str(self.score))

        self.lives_remaining = 3
        self.lives_text = self.canvas.create_text(self.canvas_width - 10, 10, anchor='ne', font=('Arial', 18, 'bold'),
                                                  fill='darkblue', text='Lives : ' + str(self.lives_remaining))

        self.eggs = []

    def create_eggs(self):
        x = randrange(10, 740)
        y = 40
        new_egg = self.canvas.create_oval(x, y, x + self.egg_width, y + self.egg_height, fill=next(self.color_cycle),
                                          width=0)
        self.eggs.append(new_egg)
        self.win.after(self.egg_interval, self.create_eggs)

    def move_eggs(self):
        for egg in self.eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = self.canvas.coords(egg)
            self.canvas.move(egg, 0, 10)
            if egg_y2 > self.canvas_height:
                self.egg_dropped(egg)

        self.win.after(self.egg_speed, self.move_eggs)

    def move_left(self):
        (x1, y1, x2, y2) = self.canvas.coords(self.catcher)
        if x1 > 0:
            self.canvas.move(self.catcher, -20, 0)

    def move_right(self):
        (x1, y1, x2, y2) = self.canvas.coords(self.catcher)
        if x2 < self.canvas_width:
            self.canvas.move(self.catcher, 20, 0)

    def egg_dropped(self, egg):
        self.eggs.remove(egg)
        self.canvas.delete(egg)
        self.lose_a_life()
        if self.lives_remaining == 0:
            messagebox.showinfo('GAME OVER!', 'Final Score : ' + str(self.score))
            self.win.destroy()

    def lose_a_life(self):
        self.lives_remaining -= 1
        self.canvas.itemconfigure(self.lives_text, text='Lives : ' + str(self.lives_remaining))

    def catch_check(self):
        (catcher_x, catcher_y, catcher_x2, catcher_y2) = self.canvas.coords(self.catcher)
        for egg in self.eggs:
            (egg_x, egg_y, egg_x2, egg_y2) = self.canvas.coords(egg)
            if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
                self.eggs.remove(egg)
                self.canvas.delete(egg)
                self.increase_score(self.egg_score)
        self.win.after(100, self.catch_check)

    def increase_score(self, points):
        self.score += points
        self.egg_speed = int(self.egg_speed * self.difficulty_factor)
        self.egg_interval = int(self.egg_interval * self.difficulty_factor)
        self.canvas.itemconfigure(self.score_text, text='Score : ' + str(self.score))

