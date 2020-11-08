import arcade

def bg_image():
    #adding image
    background = arcade.load_texture("stars.png")
    arcade.draw_lrwh_rectangle_textured(0 , 0 ,SCREEN_WIDTH ,SCREEN_HEIGHT ,background)

def matrix_10():
    
    for i in range(10):
        arcade.draw_line(0 , i*80 , 800 , i*80 , arcade.color.WHITE , 3)
        arcade.draw_line(i*80 , 0 , i*80 , 800 , arcade.color.WHITE , 3)



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800 
SCREEN_TITLE = "AI In Action Lab_01 Feat SNAILS Game"
i=0
arcade.open_window(SCREEN_WIDTH , SCREEN_HEIGHT ,SCREEN_TITLE)

arcade.start_render()

#addimg background
bg_image()


#sprite of red pac..

red_pac = arcade.load_texture("red_ghost.png")
arcade.draw_lrwh_rectangle_textured( 5 , 5 , 75 , 75 , red_pac)
##############
red_pac = arcade.load_texture("red_ghost.png")
arcade.draw_lrwh_rectangle_textured(85 , 5 , 75 , 75 , red_pac)
############
red_pac = arcade.load_texture("red_ghost.png")
arcade.draw_lrwh_rectangle_textured(165 , 5 , 75 , 75 , red_pac)
############
red_pac = arcade.load_texture("red_ghost.png")
arcade.draw_lrwh_rectangle_textured(165 , 85 , 75 , 75 , red_pac)
###########
red_pac = arcade.load_texture("red_ghost.png")
arcade.draw_lrwh_rectangle_textured(245 , 165 , 75 , 75 , red_pac)
###########
red_pac = arcade.load_texture("red_ghost.png")
arcade.draw_lrwh_rectangle_textured(245 , 245 , 75 , 75 , red_pac)
###########
red_pac = arcade.load_texture("red_pac.png")
arcade.draw_lrwh_rectangle_textured(245 , 325 , 75 , 75 , red_pac)



#sprite of yellow pac..
yellow_pac = arcade.load_texture("yellow_ghost.png")
arcade.draw_lrwh_rectangle_textured( 725 , 725 , 75 , 75 , yellow_pac)
##########
yellow_pac = arcade.load_texture("yellow_ghost.png")
arcade.draw_lrwh_rectangle_textured( 645 , 645 , 75 , 75 , yellow_pac)
##########
yellow_pac = arcade.load_texture("yellow_ghost.png")
arcade.draw_lrwh_rectangle_textured( 725 , 645 , 75 , 75 , yellow_pac)
##########
yellow_pac = arcade.load_texture("yellow_ghost.png")
arcade.draw_lrwh_rectangle_textured( 645 , 565 , 75 , 75 , yellow_pac)
##########
yellow_pac = arcade.load_texture("yellow_ghost.png")
arcade.draw_lrwh_rectangle_textured( 565 , 565 , 75 , 75 , yellow_pac)
##########
yellow_pac = arcade.load_texture("yellow_ghost.png")
arcade.draw_lrwh_rectangle_textured( 485 , 565 , 75 , 75 , yellow_pac)
###########
yellow_pac = arcade.load_texture("yellow_pac1.png")
arcade.draw_lrwh_rectangle_textured( 405 , 565 , 75 , 75 , yellow_pac)


#adding 10 x 10 matrix lines...
matrix_10()

arcade .finish_render()


arcade.run()