def on_button_pressed_a():
    turtle.forward(1)
    turtle.turn_left()
    turtle.forward(1)
    turtle.pen(TurtlePenMode.DOWN)
    # I'M A FAST TURTLE
    turtle.forward(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    basic.show_icon(IconNames.CHESSBOARD)
    basic.show_icon(IconNames.DIAMOND)
basic.forever(on_forever)
