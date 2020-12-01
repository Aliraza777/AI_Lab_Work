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
        self.tempboard = []
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
        self.count1 = 0
        self.count2 = 0
        self.pre_count1 = 0
        self.pre_count2 = 0
        self.temp1 = 0
        self.temp2 = 0
        # self.human2sprite = arcade.sprite("red_pac.png" , 0.5)
        # self.human1sprite = arcade.sprite("yellow_pac.png" , 0.5)
        self.win = "0"
        self.Movemment = 80
        self.state = "GameMenu"
    def slip_up(self , x , y , i , j):
        for x in range(x , 0 , -1):
            if(x - 1 == 0):
                return x-1 , y
            if self.board[x-1][y] == 0 or self.board[x-1][y]== i or self.board[x-1][y]==j:
                return x , y
    def slip_down(self , x , y , i ,j):
        for x in range(x , 9 , 1):
            if(x + 1 == 9):
                return x+1 , y
            if self.board[x+1][y] == 0 or self.board[x+1][y]==i or self.board[x+1][y]==j:
                return x , y
    
    def slip_left(self , x , y , i ,j):
        for y in range(y , 0 , -1):
            if(y - 1 == 0):
                return x , y-1
            if self.board[x][y-1] == 0 or self.board[x][y-1]==i or self.board[x][y-1]==j:
                return x , y
    def slip_right(self , x , y , i ,j):
        for y in range(y , 9 , 1):
            if(y + 1 == 9):
                return x , y+1
            if self.board[x][y+1] == 0 or self.board[x][y+1]==i or self.board[x][y+1]==j:
                return x , y
    def score(self):
        self.pre_count1=self.count1
        self.pre_count2=self.count2
        self.count1=0
        self.count2=0
        for i in range(0,10):
            for j in range(0,10):
                #  if self.board[i][j] != 0:
                #      self.state = "GameOver"
                if self.board[i][j] == 11:
                    self.count1 = self.count1 + 1
                    
                elif self.board[i][j] == 22:
                    self.count2 = self.count2 + 1
    def get_human_pos(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 1:
                    # print (row, col)
                    return row , col
    def get_bot_pos(self):
        self.c_position = ''
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 2:
                    return row ,col
                    
                # print(self.tempboard)
                # print(c_position)

    def possible_move(self , x , y , i , j):
           
        if(((i-1 == x and x >= 0) or (i+1 == x and x <= 9)) and j == y):
            return True
        elif(((j-1 == y and y >= 0 )or (j+1 == y and y <= 9)) and i == x):
            return True
        return False
    def heuristic(self , x , y):
        
        temp = 100
        best_x = None
        best_y = None
        temp_x = None
        temp_y = None
        previous_x = None
        previous_y = None
        #best serach to reach oppenet using empty spaces
        for i in range(0,10):
            for j in range(0,10):
                #Chek empty spaces
                if(self.board[i][j] == 0):
                    #check valid move
                    valid = self.possible_move(x , y , i , j)
                    if(valid == True):
                        #store them in temporarily
                        #because if it is not minimizing the distance the bot will not 
                        #take that move due to temp>h condition
                        temp_x = i
                        temp_y = j
                        hx , hy = self.get_human_pos()
                        #check the distance
                        h = abs(i-hx) + abs(j-hy)
                        #suppose there were two valid move having same distance
                        #bot will only take the first one
                        #now check the movemnet towards center 
                        #get the best one
                        if(previous_x != None):
                            h2 = abs(previous_x-5) + abs(previous_y-5)
                            h1 = abs(i-5) + abs(j-5)
                            if(h1 < h2):
                                h = h-2
                        if(temp > h):
                            temp = h
                            best_x = i
                            best_y = j
                            previous_x = i
                            previous_y = j
                        #when all sides have spashes or sprite even temp_x can b none
        if(best_x == None and temp_x != None):
            best_x = temp_x
            best_y = temp_y
        elif(temp_x == None):
            #here we will implement strategy about splash movements
            i , j = self.get_bot_pos()
            for k in range(0,10):
                #if(board[i+k][j]==22)
                if(i+k < 10 and  self.board[i+k][j] == 0 and self.board[i+k-1][j]==22):
                    return (i+k-1) , j
                elif(i-k > 0 and self.board[i-k][j]==0 and self.board[i-k+1][j]==22):
                    return (i-k+1) , j
                elif(j+k < 10 and self.board[i][j+k]==0 and self.board[i][j+k-1]==22):
                    return i , (j+k-1)
                elif(j-k > 0 and self.board[i][j-k]==0 and self.board[i][j-k+1]==22):
                    return i , (j-k+1)
         #now design a strategy to if there is no 0
         #this is test case but still not completed
            for k in range(0,10):
                if(i+k < 10 and  (self.board[i+k][j]==11 or i+k==10) ):
                    return (i+k-1) , j
                elif(i-k > 0 and (self.board[i-k][j]==11 or i-k==0)):
                    return (i-k+1) , j
                elif(j+k < 10 and (self.board[i][j+k]==11 or j+k==10)):
                    return i , (j+k-1)
                elif(j-k>0 and (self.board[i][j-k]==11 or j-k==0)):
                    return i , (j-k+1)
        return (best_x,best_y)
    def on_key_press(self , key , modifiers):
        if self.state == "GameMenu":
            if key:
                self.state = "GameOn"
        if self.state == "GameOn":
            if key == arcade.key.ESCAPE:
                exit(0)
            if self.turn == 1:
                self.turn = 2
                
                self.i = 22
                self.j = 2
                x , y = self.get_human_pos()
                        
                if key == arcade.key.UP:
                    if(x==0 and self.board[x][y] == 1):
                            self.board[x][y] = 1

                    elif self.board[x-1][y] == 11:
                            self.board[x][y] = 11
                            x , y = self.slip_up(x , y , self.i , self.j)
                            self.board[x][y] = 1
                    
                    elif self.board[x-1][y] == 0:
                        
                        self.board[x][y] = 11
                        self.board[x-1][y] = 1
                        

                    
                elif key == arcade.key.DOWN:
                    if(x==9 and self.board[x][y]==1):
                            self.board[x][y] = 1
 
                    # x , y = self.get_human_pos()
                    elif(self.board[x+1][y] == 11):
                        self.board[x][y] = 11
                        x , y = self.slip_down(x , y , self.i , self.j)
                        self.board[x][y] = 1
                        # raise Exception("Invalid Move")
                        
                    elif self.board[x+1][y] == 0:
                            
                        self.board[x][y] = 11
                        self.board[x+1][y] = 1
                            
                elif key == arcade.key.LEFT:
                    if(y==0 and self.board[x][y]==1):
                            self.board[x][y] = 1

                    elif(self.board[x][y-1] == 11):
                        self.board[x][y] = 11
                        x , y = self.slip_left(x , y , self.i , self.j)
                        self.board[x][y] = 1
                   
                    elif self.board[x][y-1] == 0:
                        self.board[x][y] = 11
                        self.board[x][y-1] = 1

                elif key == arcade.key.RIGHT:
                    if(y==9 and self.board[x][y]==1):
                            self.board[x][y] = 1

                    elif(self.board[x][y+1] == 11):
                        self.board[x][y] = 11
                        x , y = self.slip_right(x , y , self.i , self.j)
                        self.board[x][y] = 1
                    elif self.board[x][y+1] == 0:
                        self.board[x][y] = 11
                        self.board[x][y+1] = 1
                
                self.score()
                self.check_win()
            if self.turn == 2:
                self.turn = 1                
                self.i = 11
                self.j = 1
                x , y = self.get_bot_pos()
                qx , qy = self.heuristic(x , y) 
                if(qx != None):
                    self.board[x][y] = 22               
                    self.board[qx][qy] = 2
                self.score()
                        
                self.check_win()
                
              
    def check_win(self):
        # if(self.pre_count1 > 0 and self.pre_count1 == self.count1):
        #     self.temp1 += 1
        #     if(self.temp1 >= 15):
        #         if(self.count1 > self.count2):
        #             self.state = 'GameOver'
        #             self.win = "Player_1"
        # if(self.pre_count2 > 0 and self.pre_count2 == self.count2):
        #     self.temp2 += 1
        #     if(self.temp2 >= 15):
        #         if(self.count2 > self.count1):
        #             self.state = 'GameOver'
        #             self.win = "Player_2"
        
        if self.count1 > 49:
            self.state='GameOver'
            self.win = "Player_1"
        elif self.count2 > 49:
            self.state = "GameOver"
            self.win = "Player_2"
        elif self.count1 == 49 and self.count2 == 49:
            self.state = "GameOver"
            self.win = "draw"
        # else:
        #     for i in range(len(self.board)):
        #         for j in range(len(self.board)):
        #             if self.board[i][j] != 0:

        #                 self.win = "draw"

    def on_show(self):
        # arcade.set_background_color(arcade.color.APPLE_GREEN)
        pass
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 , 0 , 1100 , 800 , background)
        if self.state == "GameMenu":
            arcade.draw_text("Snails Game" , 550 , 400 , arcade.color.WHITE , font_size=50 , anchor_x="center")
            arcade.draw_text("Press any key to start the Game" , 550 , 300 , arcade.color.WHITE , font_size=30 , anchor_x="center")
        
        elif self.state == "GameOn":
            heading1 = f" Score of Player 1"
            heading2 = f" Score of Player 2"
            score1 = f"{self.count1}"
            score2 = f"{self.count2}"
            arcade.draw_text(heading1 , 820 , 700 , arcade.color.WHITE , font_size = 20 , anchor_y="center")
            arcade.draw_text(heading2 , 820 , 600 , arcade.color.WHITE , font_size = 20 , anchor_y="center")
            arcade.draw_text(score1 , 830 , 650 , arcade.color.WHITE , font_size = 40 , anchor_y="center")
            arcade.draw_text(score2 , 830 , 550 , arcade.color.WHITE , font_size = 40 , anchor_y="center")


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
        elif self.state == "GameOver":
            
            if self.win == "Player_1":

                arcade.draw_text("Player 1 Wins!" , 550, 400, arcade.color.WHITE, font_size=100, anchor_x="center")
                arcade.draw_text("Click to continue", 550, 250, arcade.color.WHITE, font_size=50, anchor_x="center")
                
                
            if self.win == "Player_2":
                arcade.draw_text("BOT Wins!", 550 , 400, arcade.color.WHITE, font_size=100, anchor_x="center")
                arcade.draw_text("Click to continue", 550, 250, arcade.color.WHITE, font_size=50, anchor_x="center")

            if self.win == "draw":
                arcade.draw_text("It's a draw..", 550, 400, arcade.color.WHITE, font_size=50, anchor_x="center")
                arcade.draw_text("Click to continue", 550, 250, arcade.color.WHITE, font_size=20, anchor_x="center")    
            # self.state = "GameMenu"
            # self.win = "0"

    def on_mouse_press(self, x, y, _button, _modifiers):
        if self.state == "GameOver":
            # self.win = "0"
            # self.state = "GameMenu"
            self.__init__()


if __name__ == "__main__":
    window = arcade.Window(1100 , 800 , "Snails Game")
    game_view = Snail()
    window.show_view(game_view)
    arcade.run()
