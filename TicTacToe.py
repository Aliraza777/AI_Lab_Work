import arcade
import random

cross = arcade.load_texture("cross_01.png")
circle = arcade.load_texture("circle_01.png")

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = [0,0,0,0,0,0,0,0,0]
        self.human = "x"
        self.bot = "o"
        self.win = "0"
        self.state = "GameMenu"

    def on_key_press(self, key, modifiers):
        if self.state == "GameMenu":
            if key == arcade.key.X:
                self.human = "X"
                self.bot = "O"
                self.state = "GameOn"
            elif key == arcade.key.O:
                self.human = "O"
                self.bot = "X"
                self.state = "GameOn"

        if self.state == "GameOn":
            if self.human == "O":
                self.BotMove()

    def evalBoard(self):
        if self.board[0] == 'x' and self.board[1] == 'x' and self.board[2] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x':
            if self.human == "X":
                self.win = "human"
            else:
                self.win = "bot"
        elif self.board[0] == 'o' and self.board[1] == 'o' and self.board[2] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[3] == 'o' and self.board[4] == 'o' and self.board[5] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[6] == 'o' and self.board[7] == 'o' and self.board[8] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[0] == 'o' and self.board[3] == 'o' and self.board[6] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[1] == 'o' and self.board[4] == 'o' and self.board[7] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[2] == 'o' and self.board[5] == 'o' and self.board[8] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[0] == 'o' and self.board[4] == 'o' and self.board[8] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif self.board[2] == 'o' and self.board[4] == 'o' and self.board[6] == 'o':
              if self.human == "O":
                  self.win = "human"
              else:
                  self.win = "bot"
        elif all(self.board):
            self.win = "draw"

        if self.win != "0":
            self.state = "GameOver"


    def BotMove(self):
        if self.state == "GameOn":
            self.temp = []
            try:
                if self.bot == "X":
                    for x in range(len(self.board)):
                        if self.board[x] == 0:
                            self.temp.append(x)
                    self.move = random.choice(self.temp)
                    self.board[self.move] = "x"

                elif self.bot == "O":
                    for o in range(len(self.board)):
                        if self.board[o] == 0:
                            self.temp.append(o)
                    self.move = random.choice(self.temp)
                    self.board[self.move] = "o"
            except IndexError:
                pass


    def on_show(self):
        arcade.set_background_color(arcade.color.INDIGO)


    def on_draw(self):
        arcade.start_render()
        if self.state == "GameMenu":
            arcade.draw_text("Tic Tac Toe", 300, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
            arcade.draw_text("Press X or O to choose a sign..", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")

        elif self.state == "GameOn":
            # self.shape_list = arcade.ShapeElementList()
            arcade.draw_line(0, 400, 600, 400, arcade.color.WHITE, 3)
            arcade.draw_line(0, 200, 600, 200, arcade.color.WHITE, 3)
            arcade.draw_line(400, 0, 400, 600, arcade.color.WHITE, 3)
            arcade.draw_line(200, 0, 200, 600, arcade.color.WHITE, 3)

            for sign in self.board:
                if sign == "o":
                    if self.board[0] == "o":
                        arcade.draw_lrwh_rectangle_textured(50, 450, 100, 100, circle)
                    if self.board[1] == "o":
                        arcade.draw_lrwh_rectangle_textured(250, 450, 100, 100, circle)
                    if self.board[2] == "o":
                        arcade.draw_lrwh_rectangle_textured(450, 450, 100, 100, circle)
                    if self.board[3] == "o":
                        arcade.draw_lrwh_rectangle_textured(50, 250, 100, 100, circle)
                    if self.board[4] == "o":
                        arcade.draw_lrwh_rectangle_textured(250, 250, 100, 100, circle)
                    if self.board[5] == "o":
                        arcade.draw_lrwh_rectangle_textured(450, 250, 100, 100, circle)
                    if self.board[6] == "o":
                        arcade.draw_lrwh_rectangle_textured(50, 50, 100, 100, circle)
                    if self.board[7] == "o":
                        arcade.draw_lrwh_rectangle_textured(250, 50, 100, 100, circle)
                    if self.board[8] == "o":
                        arcade.draw_lrwh_rectangle_textured(450, 50, 100, 100, circle)

                elif sign == "x":
                    if self.board[0] == "x":
                        arcade.draw_lrwh_rectangle_textured(50, 450, 100, 100, cross)
                    if self.board[1] == "x":
                        arcade.draw_lrwh_rectangle_textured(250, 450, 100, 100, cross)
                    if self.board[2] == "x":
                        arcade.draw_lrwh_rectangle_textured(450, 450, 100, 100, cross)
                    if self.board[3] == "x":
                        arcade.draw_lrwh_rectangle_textured(50, 250, 100, 100, cross)
                    if self.board[4] == "x":
                        arcade.draw_lrwh_rectangle_textured(250, 250, 100, 100, cross)
                    if self.board[5] == "x":
                        arcade.draw_lrwh_rectangle_textured(450, 250, 100, 100, cross)
                    if self.board[6] == "x":
                        arcade.draw_lrwh_rectangle_textured(50, 50, 100, 100, cross)
                    if self.board[7] == "x":
                        arcade.draw_lrwh_rectangle_textured(250, 50, 100, 100, cross)
                    if self.board[8] == "x":
                        arcade.draw_lrwh_rectangle_textured(450, 50, 100, 100, cross)
                # self.shape_list.draw()

        elif self.state == "GameOver":
            if self.win == "human":
                arcade.draw_text("Congratulations, you won !", 300, 300, arcade.color.WHITE, font_size=40, anchor_x="center")
                arcade.draw_text("Click to continue", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")

            elif self.win == "bot":
                arcade.draw_text("Computer wins :(", 300, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
                arcade.draw_text("Click to continue", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")

            elif self.win == "draw":
                arcade.draw_text("It's a draw..", 300, 300, arcade.color.WHITE, font_size=50, anchor_x="center")
                arcade.draw_text("Click to continue", 300, 250, arcade.color.WHITE, font_size=20, anchor_x="center")


    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOn":
            if self.human == "O":
                try:
                    if 0 <= x <= 200 and 400 <= y <= 600:
                        if self.board[0] == 0:
                            self.board[0] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 200 <= x <= 400 and 400 <= y <= 600:
                        if self.board[1] == 0:
                            self.board[1] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 400 <= x <= 600 and 400 <= y <= 600:
                        if self.board[2] == 0:
                            self.board[2] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 0 <= x <= 200 and 200 <= y <= 400:
                        if self.board[3] == 0:
                            self.board[3] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 200 <= x <= 400 and 200 <= y <= 400:
                        if self.board[4] == 0:
                            self.board[4] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 400 <= x <= 600 and 200 <= y <= 400:
                        if self.board[5] == 0:
                            self.board[5] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 0 <= x <= 200 and 0 <= y <= 200:
                        if self.board[6] == 0:
                            self.board[6] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 200 <= x <= 400 and 0 <= y <= 200:
                        if self.board[7] == 0:
                            self.board[7] = "o"
                        else:
                            raise Exception("Not allowed")
                    elif 400 <= x <= 600 and 0 <= y <= 200:
                        if self.board[8] == 0:
                            self.board[8] = "o"
                        else:
                            raise Exception("Not allowed")
                    self.evalBoard()
                    self.BotMove()
                    self.evalBoard()
                except Exception:
                    pass

            elif self.human == "X":
                    try:
                        if 0 <= x <= 200 and 400 <= y <= 600:
                            if self.board[0] == 0:
                                self.board[0] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 200 <= x <= 400 and 400 <= y <= 600:
                            if self.board[1] == 0:
                                self.board[1] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 400 <= x <= 600 and 400 <= y <= 600:
                            if self.board[2] == 0:
                                self.board[2] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 0 <= x <= 200 and 200 <= y <= 400:
                            if self.board[3] == 0:
                                self.board[3] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 200 <= x <= 400 and 200 <= y <= 400:
                            if self.board[4] == 0:
                                self.board[4] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 400 <= x <= 600 and 200 <= y <= 400:
                            if self.board[5] == 0:
                                self.board[5] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 0 <= x <= 200 and 0 <= y <= 200:
                            if self.board[6] == 0:
                                self.board[6] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 200 <= x <= 400 and 0 <= y <= 200:
                            if self.board[7] == 0:
                                self.board[7] = "x"
                            else:
                                raise Exception("Not allowed")
                        elif 400 <= x <= 600 and 0 <= y <= 200:
                            if self.board[8] == 0:
                                self.board[8] = "x"
                            else:
                                raise Exception("Not allowed")
                        self.evalBoard()
                        self.BotMove()
                        self.evalBoard()
                    except Exception:
                        pass

        elif self.state == "GameOver":
            self.board = [0,0,0,0,0,0,0,0,0]
            self.human = "x"
            self.bot = "o"
            self.win = "0"
            self.state = "GameMenu"


if __name__ == "__main__":
    window = arcade.Window(600, 600, "Tic Tac Toe")
    game_view = Game()
    window.show_view(game_view)
    arcade.run()