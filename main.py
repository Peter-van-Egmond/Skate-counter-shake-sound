Rondes = 0

def on_button_pressed_a():
    global Rondes
    Rondes = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("" + str(Rondes))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Rondes
    Rondes += 1
    basic.show_string("" + str(Rondes))
input.on_button_pressed(Button.B, on_button_pressed_b)
