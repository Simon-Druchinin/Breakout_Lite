from tkinter import *
from PIL import Image, ImageTk
import time

from settings import *
from objects import *
from game import *

def game_window():

    tk = Toplevel()

    tk.title(GAME_NAME)
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)

    canvas = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0)

    bg = ImageTk.PhotoImage(Image.open('bg.jpg').resize((WIDTH, HEIGHT)))
    canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg)

    canvas.pack()
    tk.update()

    score = Score(canvas, COLOR_SCORE, FONT_STYLE, FONT_SIZE)
    paddle = Paddle(canvas, COLOR_PADDLE, PADDLE_HEIGHT, PADDLE_WIDTH, score)
    ball = Ball(canvas, paddle, score, COLOR_BALL, BALL_SIZE)
    game = Game(canvas)

    game.beggining(COLOR_END_TEXT, FONT_STYLE, FONT_SIZE)

    while game.loop:

        if game.game_started == True:
            ball.draw()
            paddle.draw()
        
        if ball.hit_bottom == True:
            game.game_over(COLOR_END_TEXT, FONT_STYLE, FONT_SIZE)

        tk.update_idletasks()
        tk.update()

        time.sleep(0.01)

    time.sleep(2)
    tk.destroy()
    
    return game.last_and_best_score