import arcade;

def main():
    # Width of the window: 800, height of the window: 500
    window = arcade.open_window(800, 500)

    # Set the background color 
    arcade.set_background_color(arcade.color.ALLOY_ORANGE)

    # Get ready to draw!
    arcade.start_render()

    # ----------- Drawing code goes here

    # We're done drawing
    arcade.finish_render()

    arcade.run()

main()
