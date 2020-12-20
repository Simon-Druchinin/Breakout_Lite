import time
class Game():
    def __init__(self, canvas):

        self.canvas = canvas

        self.game_started = False
        self.loop = True

        self.canvas.bind_all("<KeyPress-Return>", self.start_game)

    def game_over(self, color_end_text, font_style, font_size):
        self.canvas.create_text(250, 120, text="Game over :(", font=(font_style, font_size), fill=color_end_text)
        self.loop = False
    
    def start_game(self, event):
        self.canvas.delete(self.text_id)
        self.game_started = True
    
    def beggining(self, color_end_text, font_style, font_size):
        self.text_id = self.canvas.create_text(250, 120, text="Press Enter to star :)", font=(font_style, font_size - 10), fill=color_end_text)
    
    @staticmethod
    def last_and_best_score():
        f = open('best_score.txt', 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        lines[0] = lines[0].rstrip('\n')

        return lines