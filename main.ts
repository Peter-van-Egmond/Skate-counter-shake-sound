let Rondes = 0
input.onGesture(Gesture.ScreenDown, function () {
    Rondes += 1
    basic.showString("" + Rondes)
    music.play(music.stringPlayable("- - - C5 - - - - ", 120), music.PlaybackMode.InBackground)
    basic.pause(100)
})
input.onButtonPressed(Button.A, function () {
    basic.showString("" + Rondes)
})
input.onButtonPressed(Button.AB, function () {
    Rondes = 0
})
input.onButtonPressed(Button.B, function () {
    Rondes += 1
    music.play(music.stringPlayable("- - - C5 - - - - ", 120), music.PlaybackMode.InBackground)
    basic.showString("" + Rondes)
    basic.pause(100)
})
