import random

class Ball():
    def __init__(self, canvas, paddle, score, color, size):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.canvas.move(self.id, 250, 100)
        self.canvas_width = self.canvas.winfo_width()

        starts = [-2, -1, 1, 2]

        random.shuffle(starts)

        self.x = starts[0]
        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                self.score.add_point()
                return True
        
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        speed = self.score.difficulty_change() * 2

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.score.last_and_best_score()

        if pos[1] <= 0:
            self.y = speed

        if self.hit_paddle(pos) == True:
            self.y = self.score.difficulty_change() * -2
        
        if pos[0] <= 0:
            self.x = speed
        
        if pos[2] >= self.canvas_width:
            self.x = 0 - speed

class Paddle():

    def __init__(self, canvas, color, height, width, score):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, height, width, fill=color)
        self.score = score

        start_1 = [40, 60, 120, 150, 180, 200]
        random.shuffle(start_1)

        self.start_pos_x = start_1[0]
        self.canvas.move(self.id, self.start_pos_x, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.game_started = False

        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
    
    def turn_right(self, event):
        if self.canvas.coords(self.id)[2] < self.canvas_width:
            self.x = self.score.difficulty_change() * 2

    def turn_left(self, event):
        if self.canvas.coords(self.id)[0] > 0:
            self.x = self.score.difficulty_change() * -2
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        
        elif pos[2] >= self.canvas_width:
            self.x = 0

class Score():
    def __init__(self, canvas, color, font_style, font_size, parent=None):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(450, 25, text=self.score, font=(font_style, font_size), fill=color)
    
    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)
    
    def difficulty_change(self):
        if self.score < 2:
            return 1

        elif self.score < 8:
            return 2

        elif self.score < 12:
            return 3
        
        else:
            return 4
        
    def last_and_best_score(self):
        last_score = self.score

        f = open('best_score.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()

        if last_score > int(lines[1]):
            lines[1] = last_score
        
        last_score = f'{self.score}\n'

        f = open('best_score.txt', 'w', encoding='utf-8')
        for item in range(2):
            if item == 0:
                f.write(str(last_score))
            else:
                f.write(str(lines[1]))
        f.close()

        return