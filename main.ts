input.onButtonPressed(Button.A, function on_button_pressed_a() {
    turtle.forward(1)
    turtle.turnLeft()
    turtle.forward(1)
    turtle.pen(TurtlePenMode.Down)
    //  I'M A FAST TURTLE
    turtle.forward(1)
})
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Chessboard)
    basic.showIcon(IconNames.Diamond)
})
