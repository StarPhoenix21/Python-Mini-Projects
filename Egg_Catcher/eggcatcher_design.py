from tkinter import Tk, Canvas
from eggcatcher import EggCatchGame

class EggCatchApp:
    def __init__(self, win):
        self.win = win
        self.canvas = Canvas(win, width=800, height=400, background='deep sky blue')
        self.canvas.create_rectangle(-5, 300, 805, 405, fill='sea green', width=0)
        self.canvas.create_oval(-80, -80, 120, 120, fill='orange', width=0)
        self.canvas.pack()

        self.game = EggCatchGame(self.win, self.canvas)

        self.win.after(1000, self.game.create_eggs)
        self.win.after(1000, self.game.move_eggs)
        self.win.after(1000, self.game.catch_check)

        self.canvas.focus_set()  # Set focus to canvas to capture key events
        self.canvas.bind('<Left>', lambda event: self.game.move_left())
        self.canvas.bind('<Right>', lambda event: self.game.move_right())

        self.win.mainloop()

win = Tk()
app = EggCatchApp(win)

