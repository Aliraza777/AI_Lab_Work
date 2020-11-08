import arcade 

def v_lines():
    arcade.draw_line( 0 , 0 , 0 , 498 ,arcade.color.WHITE)
    arcade.draw_line( 166.667 , 0 , 166.667 , 500 ,arcade.color.WHITE ,3)
    arcade.draw_line( 333.32 , 0 , 333.32 , 500 , arcade.color.WHITE ,3)
    arcade.draw_line( 498 , 0 , 498 , 498 ,arcade.color.WHITE)

def h_lines():
    arcade.draw_line( 0 , 498 , 498 , 498 , arcade.color.WHITE)
    arcade.draw_line( 0 , 0 , 498 , 0 , arcade.color.WHITE)
    arcade.draw_line( 0 , 166.667 , 500 , 166.667 ,arcade.color.WHITE ,3)
    arcade.draw_line( 0 , 333.32 , 500 , 333.32 ,arcade.color.WHITE,3)

def bg_image():
    #import image 

    background = arcade.load_texture("stars.png")

    arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)




SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "AI in Action Lab_01 feat TIC TAC TOE"


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# arcade.set_background_color(arcade.color.BLACK)


arcade.start_render()

# adding background
bg_image()


#adding a sprite



#draw a lines
v_lines()
h_lines()


#left bottom corner sprite
tick_sprite = arcade.load_texture("cross_01.png")

arcade.draw_lrwh_rectangle_textured(0, 0, 163 , 163 , tick_sprite)
#middle left sprite
tick_sprite = arcade.load_texture("cross_01.png")

arcade.draw_lrwh_rectangle_textured(0, 168, 163 , 163 , tick_sprite)

#right top corner 
circle_sprite = arcade.load_texture("circle_01.png")

arcade.draw_lrwh_rectangle_textured(335, 335, 163 ,163 , circle_sprite)


#middle block sprite
circle_sprite = arcade.load_texture("circle_01.png")

arcade.draw_lrwh_rectangle_textured(168, 168, 163 , 163 , circle_sprite)


arcade.finish_render()

arcade.run()

