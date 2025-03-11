Rondes = 0

def on_gesture_screen_down():
    global Rondes
    Rondes += 1
    basic.show_string("" + str(Rondes))
    music.play(music.string_playable("- - - C5 - - - - ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    basic.pause(100)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_a():
    basic.show_string("" + str(Rondes))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Rondes
    Rondes = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Rondes
    Rondes += 1
    music.play(music.string_playable("- - - C5 - - - - ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("" + str(Rondes))
    basic.pause(100)
input.on_button_pressed(Button.B, on_button_pressed_b)
