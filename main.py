print("Hello curcit python")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.pressrelease import PressRelease

keyboard = KMKKeyboard()
keyboard.modules.append(PressRelease())

keyboard.debug_enabled = True
keyboard.col_pins = (board.GP0,)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [[KC.PR(KC.LGUI(KC.LCTRL(KC.RIGHT)),KC.LGUI(KC.LCTRL(KC.LEFT)))]]

if __name__ == "__main__":
    keyboard.go()
