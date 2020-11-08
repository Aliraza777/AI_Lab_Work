import arcade


def bg_image():
    #adding image
    background = arcade.load_texture("stars.png")
    arcade.draw_lrwh_rectangle_textured(0 , 0 ,SCREEN_WIDTH ,SCREEN_HEIGHT ,background)

def matrix_10():
    
    for i in range(10):
        arcade.draw_line(0 , i*60 , 600 , i*60 , arcade.color.WHITE , 3)
        arcade.draw_line(i*60 , 0 , i*60 , 600 , arcade.color.WHITE , 3)




SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "AI in Action feat TIC TAC TOE"


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

snailboard = []
def initialize_board(rows , cols):
    rows , cols = (rows , cols)
    
   #method 1...........
    for i in range(cols):
        cols=[]
        for j in range(rows):
            cols.append(0)
        snailboard.append(cols)
    

    snailboard[0][0] = 1
    snailboard[-1][-1]= 2
    return snailboard


def init_grid(board):
    arcade.start_render()
    bg_image()
    #.......abhi is me board k sath link r grid banni h uski smjh nai a rhi
    arcade.finish_render()

    arcade.run()




init_board = initialize_board(10 , 10)

init_grid(init_board)



# print(len(snailboard))
# print(init_board)




# arcade.start_render()


# arcade.finish_render()


# arcade.run()
