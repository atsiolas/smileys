def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(100)
    basic.show_icon(IconNames.SAD)
    basic.pause(100)
basic.forever(on_forever)
