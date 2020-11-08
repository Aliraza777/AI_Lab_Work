import arcade

human2 = arcade.load_texture("red_pac.png")
human1 = arcade.load_texture("yellow_pac1.png")
human2splash = arcade.load_texture("red_ghost.png")
human1splash = arcade.load_texture("yellow_ghost.png")
background = arcade.load_texture("stars1.jpg")

class Snail(arcade.View):
    def __init__(self):
        super().__init__()
        self.board = []
        for i in range(10):
            cols =[]
            for j in range(10):
                cols.append(0)
            self.board.append(cols)
        self.board[0][-1] = 1
        self.board[-1][0] = 2
        
        # print(self.board)
        self.human1 = 1
        self.human2 = 2
        self.human1splash = 11
        self.human2splash = 22
        self.turn = 1
        # self.human2sprite = arcade.sprite("red_pac.png" , 0.5)
        # self.human1sprite = arcade.sprite("yellow_pac.png" , 0.5)

        self.Movemment = 80
        self.state = "GameMenu"
    def on_key_press(self , key , modifiers):
        if self.state == "GameMenu":
            if key:
                self.state = "GameOn"
        if self.state == "GameOn":
            if key == arcade.key.ESCAPE:
                exit(0)
            if self.turn == 1:
                x , y = self.get_human_pos()
                if key == arcade.key.UP:
                    if x == 0 or self.board[x-1] == 2 or self.board[x-1] == 11 or self.board[x-1] == 22:
                        pass
                        print("invalid move")
                    
                    elif self.board[x-1][y] == 0:
                        
                        self.board[x][y] = 11
                        self.board[x-1][y] = 1
                        

                    
                elif key == arcade.key.DOWN:
                    
                    # x , y = self.get_human_pos()
                    if x == 9 or self.board[x+1] == 2 or self.board[x+1] == 11 or self.board[x+1] == 22:

                        pass
                        # raise Exception("Invalid Move")
                        
                    elif self.board[x+1][y] == 0:
                            
                        self.board[x][y] = 11
                        self.board[x+1][y] = 1
                            
                elif key == arcade.key.LEFT:
                    # x , y = self.get_human_pos()
                    if y == 0 or self.board[y-1] == 2 or self.board[y-1] == 11 or self.board[y-1] == 22:
                        pass

                            
                    elif self.board[x][y-1] == 0:

                        self.board[x][y] = 11
                        self.board[x][y-1] = 1

                elif key == arcade.key.RIGHT:
                    # x , y = self.get_human_pos()
                    if y== 9 or self.board[y+1] == 2 or self.board[y+1] == 11 or self.board[y+1] == 22:        
                        pass

                    elif self.board[x][y+1] == 0:
                        self.board[x][y] = 11
                        self.board[x][y+1] = 1
                self.turn = 2
            elif self.turn == 2:
                x , y = self.get_bot_pos()
                if key == arcade.key.UP:
                    if x == 0 or self.board[x-1] == 1 or self.board[x-1] == 11 or self.board[x-1] == 22:
                        pass
                        print("invalid move")

                    elif self.board[x-1][y] == 0:
                        
                        self.board[x][y] = 22
                        self.board[x-1][y] = 2
                        

                    
                elif key == arcade.key.DOWN:
                    
                    # x , y = self.get_human_pos()
                    if x == 9 or self.board[x+1] == 1 or self.board[x+1] == 11 or self.board[x+1] == 22:

                        pass
                    elif self.board[x+1][y] == 0:
                            
                        self.board[x][y] = 22
                        self.board[x+1][y] = 2
                            
                elif key == arcade.key.LEFT:
                    # x , y = self.get_human_pos()
                    if y == 0 or self.board[y-1] == 1 or self.board[y-1] == 11 or self.board[y-1] == 22:
                        pass

                    elif self.board[x][y-1] == 0:

                        self.board[x][y] = 22
                        self.board[x][y-1] = 2

                elif key == arcade.key.RIGHT:
                    # x , y = self.get_human_pos()
                    if y== 9 or self.board[y+1] == 1 or self.board[y+1] == 11 or self.board[y+1] == 22:        
                        pass
                
                            
                    elif self.board[x][y+1] == 0:

                        self.board[x][y] = 22
                        self.board[x][y+1] = 2
                self.turn = 1
            # else:
            #     raise Exception("Invalid Move")

    def get_human_pos(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 1:
                    print (row, col)
                    return row , col
    def get_bot_pos(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 2:
                    print(row , col)
                    return row , col
 

    def on_show(self):
        # arcade.set_background_color(arcade.color.APPLE_GREEN)
        pass
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 , 0 , 1100 , 800 , background)
        if self.state == "GameMenu":
            arcade.draw_text("Snails Game" , 550 , 400 , arcade.color.WHITE , font_size=50 , anchor_x="center")
            arcade.draw_text("Press key to start the Game" , 550 , 500 , arcade.color.WHITE , font_size=30 , anchor_x="center")
        
        elif self.state == "GameOn":
            turn=f"Turn : Player {self.turn}"
            arcade.draw_text(turn , 830 , 100 ,arcade.color.WHITE,font_size=30,anchor_y='center')
            for i in range(11):
                arcade.draw_line(0 , i*80 , 800 , i*80 , arcade.color.WHITE , 3)
                arcade.draw_line(i*80 , 0 , i*80 , 800 , arcade.color.WHITE , 3)
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.board[row][col] == 1:
                        arcade.draw_lrwh_rectangle_textured( (col*80)+10 , 720-(80*row)+10 , 65 , 65 ,human1)
                        
                    elif self.board[row][col] == 2:
                        arcade.draw_lrwh_rectangle_textured( (col*80)+10 , 720-(80*row)+10 , 65 , 65 ,human2)
                        
                    elif self.board[row][col] == 11:
                        arcade.draw_lrwh_rectangle_textured( (col*80)+10 , 720-(80*row)+10 , 65 , 65 ,human1splash)

                    elif self.board[row][col] == 22:
                        arcade.draw_lrwh_rectangle_textured( (col*80)+10 , 720-(80*row)+10 , 65 , 65 ,human2splash)
                    

                     



if __name__ == "__main__":
    window = arcade.Window(1100 , 800 , "Snails Game")
    game_view = Snail()
    window.show_view(game_view)
    arcade.run()
