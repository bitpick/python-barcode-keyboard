
import evdev
import time


class KeyFilter(object):


    def __init__(self, allowed_chars):
        self._allowed_chars = allowed_chars


    def filter(self, char):
        if char in self._allowed_chars:
            return char
        else:
            raise ValueError('The character \'' + char + '\' has been dropped by filter')



class VirtualKeyboard(object):


    def __init__(self):
        self._devices = None
        self._fltr = None


    def find_devices(self):
        self._devices = [evdev.InputDevice(fd) for fd in evdev.list_devices()]


    def find_keyboard(self):
        self._keyboard_dev = None
        for device in self._devices:
            if 'keyboard' in device.name:
                self._keyboard_dev = device
                print("Found: \"" + device.name + "\"")
                break
        return self._keyboard_dev

    def set_key_filter(self, filter_obj):
        self._fltr = filter_obj


    def _emit_key(self, key):
        if self._keyboard_dev:
            self._keyboard_dev.write(evdev.ecodes.EV_KEY, key, 1)
            time.sleep(.1)
            self._keyboard_dev.write(evdev.ecodes.EV_KEY, key, 0)


    def _keycode_from_char(self, char):
        key_name = 'KEY_' + char
        return evdev.ecodes.ecodes[key_name]


    def type_key(self, char=''):
        if self._fltr:
            try:
                self._emit_key(self._keycode_from_char(self._fltr.filter(char)))
            except ValueError as e:
                print("Error while processing: ", e)
        else:
            self._emit_key(self._keycode_from_char(char))


    def emit_return(self):
        self._emit_key(evdev.ecodes.KEY_ENTER)
