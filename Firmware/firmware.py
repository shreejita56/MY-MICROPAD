import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros , Press , Release , Tap, Delay
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.row_pins = (board.GP28, board.GP29)
keyboard.col_pins = (board.GP3 , board.GP4 , board.GP2 , board.GP1)

keyboard.diode_orientation = DiodeOrientation.COL2ROW
macros = Macros()
encoder = EncoderHandler()
keyboard.modules = [macros , encoder]
keyboard.extension.append(MediaKeys())

def open_url(url):
    return KC.MACRO( 
        Press(KC.LGUI),
        Tap(KC.R),
        Release(KC.LGUI),
        Delay(500),
        url,
        Delay(100),
        Tap(KC.ENTER),
    )

YOUTUBE = open_url("https://www.youtube.com")
GOOGLE = open_url("https://www.google.com")
CHATGPT = open_url("https://chatgpt.com")
GMAIL = open_url("https://mail.google.com")
GITHUB = open_url("https://github.com")
SPOTIFY = open_url("https://open.spotify.com")
REDDIT = open_url("https://www.reddit.com")
WIKI = open_url("https://www.wikipedia.org")

SHUTDOWN = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.X),
    Release(KC.LGUI),
    Delay(500),
    Tap(KC.U),
    Delay(300),
    Tap(KC.U),

)

encoder.pins = ((board.GP26 , board.GP27 ,board.GP5,False,4),)
encoder.map = [((KC.VOLD,KC.VOLU,SHUTDOWN),)]

keyboard.keymap = [[YOUTUBE, GOOGLE,CHATGPT,GMAIL,
                    GITHUB,SPOTIFY,REDDIT,WIKI,]]

if __name__ == "__main__":
    keyboard.go()
    