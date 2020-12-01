import arcade
import os
import random
import math

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

SPRITE_SCALING = 0.10
board=[]

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Khan Alone"

MOVEMENT_SPEED = 60



       
            
   
class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        background = arcade.load_texture("menu4.jpg")
        arcade.start_render()
        
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        arcade.draw_text("Khan Alone", SCREEN_WIDTH/2, SCREEN_HEIGHT-270,
                         arcade.color.BLUEBERRY, font_size=90, anchor_x="center")
        arcade.draw_text("Click to Enter The Game", SCREEN_WIDTH/2, SCREEN_HEIGHT-320,
                         arcade.color.RED, font_size=40, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)



"""Instructions View"""

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        background = arcade.load_texture("start.jpg")
        snail = arcade.load_texture("1.png")
        snail2 = arcade.load_texture("2.png",flipped_horizontally=True)
        arcade.start_render()
        
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
        arcade.draw_text("S N A I L S", SCREEN_WIDTH/2, SCREEN_HEIGHT-180,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
        
       
        arcade.draw_text("Click To Begin The Challenge", SCREEN_WIDTH/2, SCREEN_HEIGHT-400,
                         arcade.color.GRAY_ASPARAGUS, font_size=25,bold=True,font_name='calibri', anchor_x="center")
        arcade.draw_lrwh_rectangle_textured(50, 600,100,100,snail)
        arcade.draw_lrwh_rectangle_textured(SCREEN_WIDTH-150, 600,100,100,snail2)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

"""End Instructions View"""
"""                                         Game Start"""



class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.score=0
        self.count=0
        self.count2=0
        self.pre_score=0
        self.pre_score2=0
        self.score2=0
        self.turn=0
        self.temp_board=[]
        self.state="Game On"
        rows, cols = (10, 10)
        self.initialize_board(rows,cols)
        # Sprite lists
      
        # Set up the player
        
       
      

    def initialize_board(self,rows,cols):
        for i in range(cols): 
            col = [] 
            for j in range(rows): 
                col.append(0) 
            board.append(col) 
        board[9][0],board[0][9]=1,2
       
    def on_show(self):
        # Don't show the mouse cursor
        self.window.set_mouse_visible(True)

    def on_draw(self):
        background = arcade.load_texture("menu4.jpg")
        s1=arcade.load_texture('s1.png')
        s2=arcade.load_texture('s2.png')
        p1=arcade.load_texture('1.png')
        p2=arcade.load_texture('2.png',flipped_horizontally=True)

        if(self.state=="Game On"):
         
            arcade.start_render()
        # Draw all the sprites.
            arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
            
            arcade.draw_lrwh_rectangle_textured(30,700,50,50,p1)
            arcade.draw_lrwh_rectangle_textured(720,700,50,50,p2)

        # Put the text on the screen.
            output = f"Score \nP1: {self.score}"
            output2 = f"Score \nP2: {self.score2}"
            arcade.draw_text(output,15,650, arcade.color.WHITE, 20)
            arcade.draw_text(output2,720,650, arcade.color.WHITE, 20)
            output_total = f"Total Score: {self.window.total_score}"
            arcade.draw_text(output_total, 350, 700, arcade.color.WHITE, 20)
            turn=f"Turn Of Player: {self.turn+1}"
            # time_taken=f"Time Taken:{self.time_taken}"
            arcade.draw_text(turn, 350, 750, arcade.color.WHITE,20,italic=True)
            # arcade.draw_text(time_taken, 450, 700, arcade.color.WHITE,20,italic=True)
        
            """ Making Grid"""
            box=int(600/10)
        
# Started making grid  
            for y in range (100,701,box):
    # for horizontal line 
   
                arcade.draw_line(100,y,700,y,arcade.color.GRAY_BLUE,5)
    # for verticle line
                arcade.draw_line(y,100,y,700,arcade.color.GRAY_BLUE,5)
            for y in range(0,10):
                for x in range(0,10):
                    if(board[y][x]==11):
                        
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,s1)
                    elif(board[y][x]==22):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,s2)
                    elif(board[y][x]==1):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,p1)
                    elif(board[y][x]==2):
                        arcade.draw_lrwh_rectangle_textured(100+(x*60),630-(60*y)+10,50,50,p2)
        elif(self.state=="Game Over"):
            background = arcade.load_texture("menu4.jpg")
            if(self.score>self.score2):
                arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
                arcade.draw_text("Player 1 Win \nNice Played",SCREEN_WIDTH/2, SCREEN_HEIGHT-180,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
                arcade.draw_text("Press Esc To Exit \n Enter To Reset",400, 500,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
            elif(self.score2>self.score):
                arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
                arcade.draw_text("Player 2 Win \nNice Played",SCREEN_WIDTH/2, SCREEN_HEIGHT-180,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
                arcade.draw_text("Press Esc To Exit \n Enter To Reset",400, 500,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
            else:
                arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
                arcade.draw_text("Draw \nNice Played",SCREEN_WIDTH/2, SCREEN_HEIGHT-180,
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
                arcade.draw_text("Press Esc To Exit \n Enter To Reset",400, 500,    
                         arcade.color.SKY_BLUE, font_size=50, bold=True,anchor_x="center")
        # Draw all the sprites.
            """ Ending Grid"""

    def on_update(self, delta_time):
        self.time_taken += delta_time
     
       
    def get_human_pos(self):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 1:
                    return row , col
    def get_bot_pos(self):
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 2:
                    return row,col

    def slip_up(self , x , y , i , j):
        for x in range(x , 0 , -1):
            if(x - 1 == 0):
                return x-1 , y
            if board[x-1][y] == 0 or board[x-1][y]==i or board[x-1][y]==j:
                return x , y
    def slip_down(self , x , y , i ,j):
        for x in range(x , 9 , 1):
            if(x + 1 == 9):
                return x+1 , y
            if board[x+1][y] == 0 or board[x+1][y]==i or board[x+1][y]==j:
                return x , y
    
    def slip_left(self , x , y , i ,j):
        for y in range(y , 0 , -1):
            if(y - 1 == 0):
                return x , y-1
            if board[x][y-1] == 0 or board[x][y-1]==i or board[x][y-1]==j:
                return x , y
    def slip_right(self , x , y , i ,j):
        for y in range(y , 9 , 1):
            if(y + 1 == 9):
                return x , y+1
            if board[x][y+1] == 0 or board[x][y+1]==i or board[x][y+1]==j:
                return x , y
    
    def score_count(self):
        self.pre_score=self.score
        self.pre_score2=self.score2
        self.score=0
        self.score2=0
        for x in range(0,10):
            for y in range(0,10):
                if board[x][y]==11:
                    self.score+=1
                elif board[x][y]==22:
                    self.score2+=1
    def eval(self):
        # if(self.pre_score>0 and self.pre_score==self.score):
        #     self.count+=1
        #     if(self.count>=15):
        #         if(self.score>self.score2):
        #             self.state='Game Over'
        # if(self.pre_score2>0 and self.pre_score2==self.score2):
        #     self.count2+=1
        #     if(self.count2>=15):
        #         if(self.score2>self.score):
        #             self.state='Game Over'
        
        if(self.score>49 or self.score2>49):
            self.state='Game Over'
        elif(self.score==49 and self.score2==49):
            self.state='Game Over'
   
    def possible_move(self,x,y,i,j):
        
        if(((i-1==x and x>=0) or (i+1==x and x<=9)) and j==y):
            return True
        elif(((j-1==y and y>=0)or (j+1==y and y<=9)) and i==x):
            return True
        return False
    def heuristic(self,x,y):
        move=[]
        temp=100
        best_x=None
        best_y=None
        temp_x=None
        temp_y=None
        previous_x=None
        previous_y=None
        #best serach to reach oppenet using empty spaces
        for i in range(0,10):
            for j in range(0,10):
                #Chek empty spaces
                if(board[i][j]==0):
                    #check valid move
                    valid=self.possible_move(x,y,i,j)
                    if(valid==True):
                        #store them in temporarily
                        #because if it is not minimizing the distance the bot will not 
                        #take that move due to temp>h condition
                        temp_x=i
                        temp_y=j
                        hx,hy=self.get_human_pos()
                        #check the distance
                        h=abs(i-hx)+abs(j-hy)
                        #suppose there were two valid move having same distance
                        #bot will only take the first one
                        #now check the movemnet towards center 
                        #get the best one
                        if(previous_x!=None):
                            h2=abs(previous_x-5)+abs(previous_y-5)
                            h1=abs(i-5)+abs(j-5)
                            if(h1<h2):
                                h=h-2
                        if(temp>h):
                            temp=h
                            best_x=i
                            best_y=j
                            previous_x=i
                            previous_y=j
                        #when all sides have spashes or sprite even temp_x can b none
        if(best_x==None and temp_x!=None):
            best_x=temp_x
            best_y=temp_y
        elif(temp_x==None):
            #here we will implement strategy about splash movements
            i,j=self.get_bot_pos()
            for k in range(0,10):
                #if(board[i+k][j]==22)
                if(i+k<10 and  board[i+k][j]==0 and board[i+k-1][j]==22):
                    return (i+k-1),j
                elif(i-k>0 and board[i-k][j]==0 and board[i-k+1][j]==22):
                    return (i-k+1),j
                elif(j+k<10 and board[i][j+k]==0 and board[i][j+k-1]==22):
                    return i,(j+k-1)
                elif(j-k>0 and board[i][j-k]==0 and board[i][j-k+1]==22):
                    return i,(j-k+1)
         #now design a strategy to if there is no 0
         #this is test case but still not completed
            for k in range(0,10):
                if(i+k<10 and  (board[i+k][j]==11 or i+k==10) ):
                    return (i+k-1),j
                elif(i-k>0 and (board[i-k][j]==11 or i-k==0)):
                    return (i-k+1),j
                elif(j+k<10 and (board[i][j+k]==11 or j+k==10)):
                    return i,(j+k-1)
                elif(j-k>0 and (board[i][j-k]==11 or j-k==0)):
                    return i,(j-k+1)
        return (best_x,best_y)
        
    def on_key_press(self , key , modifiers):
        
        if self.state == "Game On":
            if key == arcade.key.ESCAPE:
                exit(0)
            if self.turn == 0:
                self.turn = 1
                self.i = 22
                self.j = 2
                x , y = self.get_human_pos()
                        
                if key == arcade.key.UP:
                    if(x==0 and board[x][y]==1):
                            board[x][y] = 1

                    elif board[x-1][y] == 11:
                            board[x][y] = 11
                            x , y = self.slip_up(x , y , self.i , self.j)
                            board[x][y] = 1
                    
                    elif board[x-1][y] == 0:
                        
                        board[x][y] = 11
                        board[x-1][y] = 1
                        

                    
                elif key == arcade.key.DOWN:
                    if(x==9 and board[x][y]==1):
                            board[x][y] = 1
 
                    # x , y = self.get_human_pos()
                    elif(board[x+1][y] == 11):
                        board[x][y] = 11
                        x , y = self.slip_down(x , y , self.i , self.j)
                        board[x][y] = 1
                        # raise Exception("Invalid Move")
                        
                    elif board[x+1][y] == 0:
                            
                        board[x][y] = 11
                        board[x+1][y] = 1
                            
                elif key == arcade.key.LEFT:
                    if(y==0 and board[x][y]==1):
                            board[x][y] = 1

                    elif(board[x][y-1] == 11):
                        board[x][y] = 11
                        x , y = self.slip_left(x , y , self.i , self.j)
                        board[x][y] = 1
                   
                    elif board[x][y-1] == 0:
                        board[x][y] = 11
                        board[x][y-1] = 1

                elif key == arcade.key.RIGHT:
                    if(y==9 and board[x][y]==1):
                            board[x][y] = 1

                    elif(board[x][y+1] == 11):
                        board[x][y] = 11
                        x , y = self.slip_right(x , y , self.i , self.j)
                        board[x][y] = 1
                    elif board[x][y+1] == 0:
                        board[x][y] = 11
                        board[x][y+1] = 1
                self.score_count()    
                self.eval()
            elif self.turn == 1:
                self.turn=0
                self.i = 11
                self.j = 1
                bot_x,bot_y = self.get_bot_pos()
                sp_x,sp_y=self.heuristic(bot_x,bot_y)
                # print(sp_x,sp_y)
                if(sp_x!=None):
                    board[bot_x][bot_y]=22
                    board[sp_x][sp_y]=2
                self.score_count()    
                self.eval()
        elif(self.state=='Game Over'):
            if key == arcade.key.ESCAPE:   # resume game
                exit(0)
            elif key == arcade.key.ENTER:  # reset game
                board.clear()
                game = GameView()
                self.window.show_view(game)
        
   


def main():
    
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,resizable=True)
    window.total_score = 0
    menu_view = MenuView()
    window.center_window()
    window.show_view(menu_view)
  
    arcade.run()


if __name__ == "__main__":
    main()