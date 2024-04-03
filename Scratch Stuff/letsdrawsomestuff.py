import arcade;

def main():
    # Width of the window: 800, height of the window: 500
    window = arcade.open_window(800, 500)

    # Set the background color 
    arcade.set_background_color(arcade.color.ALLOY_ORANGE)

    # Get ready to draw!
    arcade.start_render()

    # ----------- Drawing code goes here
    arcade.draw_circle_filled(400,250,200,arcade.color.YELLOW)
    arcade.draw_line(300,125,500,125,arcade.color.BLACK,10)
    arcade.draw_circle_filled(325,250,30,arcade.color.BLACK)
    arcade.draw_circle_filled(475,250,30,arcade.color.BLACK)
    arcade.draw_circle_outline(325,250,50,arcade.color.BALL_BLUE)
    arcade.draw_circle_outline(475,250,50,arcade.color.BALL_BLUE)
    arcade.draw_line(375,250,425,250,arcade.color.BALL_BLUE,3)
    
    # We're done drawing
    arcade.finish_render()

    arcade.run()

main()

'''
sudo code for basic clicker game:
x=0
window
write x but big
when space press x+=1
clear screen
rewrite x but big still
'''