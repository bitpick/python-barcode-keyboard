
from keyboard import VirtualKeyboard, KeyFilter

if __name__ == "__main__":
    kbd = VirtualKeyboard()
    kbd.find_devices()
    kbd.find_keyboard()

    allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    fltr = KeyFilter(allowed_chars)
    kbd.set_key_filter(fltr)

    kbd.type_key('0')
    kbd.type_key('1')
    kbd.type_key('2')
    kbd.type_key('3')
    kbd.type_key('4')
    kbd.type_key('5')
    kbd.type_key('A')
    kbd.type_key('9')
    kbd.emit_return()

