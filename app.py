import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

from settings import *
from main import game_window
from game import *

app = tkinter.Tk()

canvas = Canvas(app, width=WIDTH, height=HEIGHT, highlightthickness=0)

def get_info():
    messagebox.showinfo('Справка', 'Для игры используйте стрелочки(вправо, влево).\n\nВнимание!: платформа продолжает движение в сторону последней нажатой клавиши.')

def get_about():
    messagebox.showinfo('О программе', 'Версия: 1.0\nИгру сделал: Sapphire')

#start game and refresh results
def game_app():
    global last_score, record

    game_window()
    score_list = Game.last_and_best_score()
    canvas.delete(last_score)
    canvas.delete(record)
    last_score = canvas.create_text(250, 160, text=f'Вас прошлый счёт: {score_list[0]}', font=(FONT_STYLE, FONT_SIZE), fill=MENU_TEXT_COLOR)
    record = canvas.create_text(250, 210, text=f'Рекорд: {score_list[1]}', font=(FONT_STYLE, FONT_SIZE), fill=MENU_TEXT_COLOR)

bg = ImageTk.PhotoImage(Image.open('menu_bg.jpg').resize((WIDTH, HEIGHT)))
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg)

start_button = Button(text = "Играть", command = game_app, anchor = W)
start_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
start_button_window = canvas.create_window(190, 100, anchor=NW, window=start_button)

score_list = Game.last_and_best_score()

last_score = canvas.create_text(250, 160, text=f'Вас прошлый счёт: {score_list[0]}', font=(FONT_STYLE, FONT_SIZE), fill=MENU_TEXT_COLOR)
record = canvas.create_text(250, 210, text=f'Рекорд: {score_list[1]}', font=(FONT_STYLE, FONT_SIZE), fill=MENU_TEXT_COLOR)

canvas.pack()
app.update()

###app = tkinter.Tk() # create a window of our app
app.title(GAME_NAME) # name of our app
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

menuBar = tkinter.Menu(app)# create main menu

reference_menu = tkinter.Menu(menuBar) # a reference drop-down menu
reference_menu.add_command(label="Посмотреть справку", command=get_info)
reference_menu.add_command(label="О программе", command=get_about)

app.config(menu = menuBar) #  publish a menu
menuBar.add_cascade(label="Новая игра", command=game_app)
menuBar.add_cascade(label="Справка", menu = reference_menu)
menuBar.add_cascade(label="Выход", command = app.quit)

app.mainloop() # infinite loop