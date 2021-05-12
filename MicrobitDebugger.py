from time import time
import sys

# TODO Consider switching raise statements on user input to infinite loops waiting for a valid input.

print("===== Python Debug Mode =====")
_prevPrint = "===== Python Debug Mode ====="
_logCount = 1


def _implement(name):
    print('{} method is not implemented yet.'.format(name))


def _qprint(text, prefix=""):
    global _prevPrint, _logCount
    if _prevPrint == text:
        _logCount += 1
    elif _logCount > 1:
        print("REPEAT: {}".format(_logCount))
        print()
        if prefix == "":
            print(text)
        else:
            print("{}: {}".format(prefix, text))
        _logCount = 1
    else:
        if prefix == "":
            print(text)
        else:
            print("{}: {}".format(prefix, text))
    _prevPrint = text


class _Button:

    def __init__(self, name):
        self.name = name

    def is_pressed(self):
        # TODO write is_pressed method.
        _implement("is_pressed")

    def was_pressed(self):
        print("Press " + self.name + "? (y/n)")
        value = input()
        if value in ["y", "Y"]:
            return True
        else:
            return False

    def get_presses(self):
        # TODO write get_presses method.
        _implement("is_pressed")


class _DigitalPin:

    def __init__(self, idx, function):
        self.id = idx
        self.type = "digital"
        self.function = function
        self.value = 0

    def read_digital(self):
        value = input("Enter desired value (1 for high, 0 for low or nothing to take current value): ")
        try:
            if int(value) == 1 or int(value) == 0:
                self.value = int(value)
                return value
            else:
                return self.value
        except ValueError:
            return self.value

    def write_digital(self, value):
        if value == 1 or value == 0:
            self.value = int(value)
        else:
            raise ValueError("Value must be either 1 or 0.")


class _AnalogPin:

    def __init__(self, idx, function):
        self.id = idx
        self.type = "analog"
        self.function = function
        self.value = 0
        self.periodMicroSeconds = 256

    def read_analog(self):
        value = input("Enter desired voltage (0 to 1023 or nothing for current value): ")
        try:
            if 0 <= int(value) <= 1023:
                return int(value)
            else:
                raise ValueError("Must be an integer between 0 and 1023.")
        except ValueError:
            return self.value

    def write_analog(self, value):
        if 0 <= value <= 1023:
            self.value = int(value)
        else:
            raise ValueError("Value must be an integer between 0 and 1023.")

    def set_analog_period(self, period):
        if isinstance(period, int) and period >= 1:
            self.periodMicroSeconds = 1000 * period
        else:
            raise ValueError("Period must be an integer >= 1.")

    def set_analog_period_microseconds(self, period):
        if isinstance(period, int) and period >= 256:
            self.periodMicroSeconds = period
        else:
            raise ValueError("Period must be an integer >= 256.")


class _TouchPin:

    def __init__(self, idx, function):
        self.id = idx
        self.type = "touch"
        self.function = function
        self.CAPACITIVE = "CAPACITIVE"
        self.RESISTIVE = "RESISTIVE"
        self.touch_mode = self.CAPACITIVE

    def is_touched(self):
        try:
            return bool(input("Enter pin touched status (True/False)"))
        except ValueError:
            raise ValueError("Input must be a boolean.")

    def set_touch_mode(self, value):
        # TODO write set_touch_mode method.
        _implement("set_touch_mode")


class _Accelerometer:

    def __init__(self):
        self.log = []
        self.x = 0
        self.y = 0
        self.z = 0
        self.gestureList = ["up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake"]

    def _get_coord(self, l_bound, u_bound):
        try:
            value = int(input("Enter desired x acceleration ({} to {}): ".format(l_bound, u_bound)))
            if l_bound <= value <= u_bound:
                return value
            else:
                raise ValueError("Acceleration must be an integer between {} and {}.".format(l_bound, u_bound))
        except ValueError:
            raise TypeError("Acceleration must be an integer between {} and {}.".format(l_bound, u_bound))

    def get_x(self):
        self._get_coord(0, 1024)

    def get_y(self):
        self._get_coord(0, 1024)

    def get_z(self):
        self._get_coord(0, 1024)

    def get_values(self):
        try:
            value = input("Enter desired x, y, z acceleration (0 to 1024): ")
            value = tuple(map(int, value.split(', ')))
            for i in value:
                if not 0 <= i <= 1024:
                    raise ValueError("Acceleration must be a comma separated list of integers between 0 and 1024.")
            return value
        except ValueError:
            raise TypeError("Acceleration must be a comma separated list of integers between 0 and 1024.")

    def current_gesture(self):
        value = input("Enter desired gesture.")
        if value in self.gestureList:
            return value
        else:
            raise ValueError('Gesture must be "up", "down", "left", "right", "face up", "face down", "freefall", "3g", '
                             '"6g", "8g", or "shake".')

    def is_gesture(self, name):
        try:
            return bool(input("Is current gesture {}? ".format(name)))
        except ValueError:
            raise ValueError("input must be a boolean.")

    def was_gesture(self, name):
        try:
            return bool(input("Was gesture {} done since last call? ".format(name)))
        except ValueError:
            raise ValueError("input must be a boolean.")

    def get_gestures(self):
        try:
            value = input("Enter desired x, y, z acceleration (0 to 1024): ")
            value = tuple(value.split(', '))
            for i in value:
                if i not in self.gestureList:
                    raise ValueError('Gestures must be a comma separated list of "up", "down", "left", "right", '
                                     '"face up", "face down", "freefall", "3g", "6g", "8g", or "shake".')
            return value
        except ValueError:
            raise ValueError('Gestures must be a comma separated list of "up", "down", "left", "right", "face up", '
                             '"face down", "freefall", "3g", "6g", "8g", or "shake".')


class _AudioFrame:

    # TODO Check this works!!
    def __init__(self):
        self.data = [0]*32

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        return self.data


class _Audio:

    GIGGLE = "Giggle sound"
    HAPPY = "Happy sound"
    HELLO = "Hello sound"
    MYSTERIOUS = "Mysterious sound"
    SAD = "Sad sound"
    SLIDE = "Slide sound"
    SOARING = "Soaring sound"
    SPRING = "Spring sound"
    TWINKLE = "Twinkle sound"
    YAWN = "Yawn sound"

    def __init__(self, pin):
        self.isPlaying = False
        self.default_pin = pin

    def play(self, source, wait=True, pin=None, return_pin=None):
        if isinstance(pin, type(None)):
            pin = self.default_pin
        # TODO write play method.
        _implement('play')

    def is_playing(self):
        # TODO write is_playing method
        _implement('is_playing')

    def stop(self):
        # TODO write stop method
        _implement('stop')


class _Compass:

    def __init__(self):
        self.calibrated = False

    def calibrate(self):
        print("Calibrating compass...")
        self.calibrated = True
        print("Calibrated.")

    def is_calibrated(self):
        value = input("Is the compass calibrated? (True/False or \"c\" for current value)")
        try:
            self.calibrated = bool(value)
            return value
        except ValueError:
            if value == "c":
                return self.calibrated
            else:
                raise ValueError("Value must be either bool or \"c\".")

    def clear_calibration(self):
        self.calibrated = False

    def get_coord(self, axis):
        value = input("Enter desired {} value: ".format(axis))
        try:
            return int(value)
        except ValueError:
            raise TypeError("Value must be an integer.")

    def get_x(self):
        self.get_coord('x')

    def get_y(self):
        self.get_coord('y')

    def get_z(self):
        self.get_coord('z')

    def heading(self):
        value = input("Enter desired heading (0 to 360): ")
        try:
            value = int(value)
            if 0 <= value <= 360:
                return value
            else:
                raise ValueError("Heading must be an integer between 0 and 360.")
        except ValueError:
            raise TypeError("Heading must be an integer between 0 and 360.")

    def get_field_strength(self):
        self.get_coord('field strength')


class _Radio:

    def __init__(self):
        self.RATE_250KBIT = 256000
        self.RATE_1MBIT = 1000000
        self.RATE_2MBIT = 2000000
        self.on = False
        self.configDict = {'length': 32, 'queue': 3, 'channel': 7, 'power': 6, 'address': 0x75626974, 'group': 0,
                           'data_rate': self.RATE_1MBIT}
        self.lb = {'length': 1, 'queue': 1, 'channel': 0, 'power': 0, 'address': 0, 'group': 0}
        self.ub = {'length': 251, 'queue': sys.maxsize, 'channel': 83, 'power': 7, 'address': 2**32-1, 'group': 255}

    def on(self):
        _qprint("Radio on.")
        self.on = True

    def off(self):
        _qprint("Radio off.")
        self.on = False

    def config(self, **kwargs):
        keys = list(kwargs.keys())
        options = list(self.configDict.keys())
        for item in keys:
            if item == "data_rate":
                if kwargs[item] == self.RATE_250KBIT or kwargs[item] == self.RATE_1MBIT or kwargs[item] == self.RATE_2MBIT:
                    self.configDict[item] = kwargs[item]
                else:
                    raise ValueError("data_rate must be either radio.RATE_250KBIT, radio.RATE_1MBIT or"
                                     " radio.RATE_2MBIT.")
            elif item in options:
                if isinstance(kwargs[item], int) and self.lb[item] <= kwargs[item] <= self.ub:
                    self.configDict[item] = kwargs[item]
                    _qprint("radio.{} set to {}".format(item, kwargs[item]))
                else:
                    raise ValueError("{} must be an integer between {} and {}.".format(item, self.lb[item], self.ub[item]))

    def reset(self):
        self.__init__()

    def send_bytes(self, message):
        # TODO write send_bytes method.
        _implement("send_bytes")

    def receive_bytes(self):
        # TODO write receive_bytes method.
        _implement("receive_bytes")

    def receive_bytes_into(self, buffer):
        # TODO write receive_bytes_into method.
        _implement("receive_bytes_into")

    def send(self, message):
        # TODO write send method.
        _implement("send")

    def receive(self):
        # TODO write receive method.
        _implement("receive")

    def receive_full(self):
        # TODO write receive_full method.
        _implement("receive_full")


class Image:
    EMPTY = "00000:" * 4 + "00000"
    FULL = "99999:" * 5
    HEART = "09090:" + "90909:" + "90009:" + "09090:" + "00900:"
    SMALL_HEART = "00000:" + "09090:" + "09990:" + "00900:" + "00000:"
    YES = "00000:" + "00009:" + "00090:" + "90900:" + "09000:"
    NO = "90009:" + "09090:" + "00900:" + "09090:" + "90009:"
    HAPPY = "00000:" + "09090:" + "00000:" + "90009:" + "09990:"
    SAD = "00000:" + "09090:" + "00000:" + "09990:" + "90009:"
    CONFUSED = "00000:" + "09090:" + "00000:" + "09090:" + "90909:"
    ANGRY = "90009:" + "09090:" + "00000:" + "99999:" + "90909:"
    ASLEEP = "00000:" + "99099:" + "00000:" + "09990:" + "00000:"
    SURPRISED = "09090:" + "00000:" + "00900:" + "09090:" + "00900:"
    SILLY = "90009:" + "00000:" + "99999:" + "00099:" + "00099:"
    FABULOUS = "99999:" + "99099:" + "00000:" + "09090:" + "09990:"
    MEH = "99099:" + "00000:" + "00090:" + "00900:" + "09000:"
    TSHIRT = "99099:" + "99999:" + "09990:" * 3
    ROLLER_SKATE = "00099:" * 2 + "99999:" * 2 + "09090:"
    DUCK = "09900:" + "99900:" + "09999:" + "09990:" + "00000:"
    HOUSE = "00900:" + "09990:" + "99999:" + "09990:" + "09090:"
    TORTOISE = "00000:" + "09990:" + "99999:" + "09090:" + "00000:"
    BUTTERFLY = "99099:" + "99999:" + "00900:" + "99999:" + "99099:"
    STICK_FIGURE = "00900:" + "99999:" + "00900:" + "09090:" + "90009:"
    GHOST = "09990:" + "09090:" + "99999:" * 2 + "09090:"
    SWORD = "00900:" * 3 + "09990:" + "00900:"
    GIRAFFE = "99000:" + "09000:" * 2 + "09990:" + "09090:"
    SKULL = "09990:" + "90909:" + "99999:" + "09990:" * 2
    UMBRELLA = "09990:" + "99999:" + "00900:" + "90900:" + "99900:"
    SNAKE = "99000:" + "99099:" + "09090:" + "09990:" + "00000:"
    RABBIT = "90900:" * 2 + "99990:" + "99090:" + "99990:"
    COW = "90009:" * 2 + "99999:" + "09990:" + "00900:"
    QUARTER_NOTE = "00900:" * 3 + "99900:" * 2
    EIGTH_NOTE = "00900:" + "00990:" + "00909:" + "99900:" * 2
    PITCHFORK = "90909:" * 2 + "99999:" + "00900" * 2
    TARGET = "00900:" + "09990:" + "99099:" + "09990:" + "00900:"
    TRIANGLE = "00000:" + "00900:" + "09090:" + "99999:" + "00000:"
    LEFT_TRIANGLE = "90000:" + "99000:" + "90900:" + "90090:" + "99999:"
    CHESS_BOARD = "09090:" + "90909:" + "09090:" + "90909:" + "09090:"
    DIAMOND = "00900:" + "09090:" + "90009:" + "09090:" + "00900:"
    SMALL_DIAMOND = "00000:" + "00900:" + "09090:" + "00900:" + "00000:"
    SQUARE = "99999:" + "90009:" * 3 + "99999:"
    SMALL_SQUARE = "00000:" + "09990:" + "09090:" + "09990:" + "00000:"
    SCISSORS = "99009:" + "99090:" + "00900:" + "99090:" + "99009:"

    def __init__(self, image=EMPTY):
        # TODO implement init methods for each type of input.
        if type(image) == str:
            self._image = list(image)
            if self._image[len(self._image)-1] == ':':  # Check end character is not :
                raise ValueError("Image string should not end with ':'")
            lineBreakList = []
            for i in range(len(self._image)):  # Add index of ':' chars to list, raise error if non-int or ':'
                if self._image[i] == ':':
                    lineBreakList.append(i)
                else:
                    try:
                        int(self._image[i])
                    except ValueError:
                        raise TypeError("Image string must contain only integers from 0 to 9 and ':'.")
            if len(lineBreakList) == 0:  # If no ':' assume height is 1
                self._height = 1
                self._width = len(self._image)
                return
            lineBreakList = [-1] + lineBreakList + [len(self._image)]  # Added line break dummy line breaks at
            lineBreakDiff = lineBreakList[1]+1                         # beginning and end
            self._height = 0
            for i in range(0, len(lineBreakList)-1):  # Check gap between line breaks in consistent
                if lineBreakDiff == lineBreakList[i+1]-lineBreakList[i]:
                    lineBreakDiff = lineBreakList[i+1]-lineBreakList[i]
                else:
                    raise ValueError("Inconsistent row width.")  # raise error if not
                self._height += 1
            self._width = lineBreakDiff-1

    # TODO implement image adding and scale multiplication.
    def __repr__(self):
        return "".join(self._image)

    def __str__(self):
        out = "\n"
        for i in range(self._height):
            out += "".join(self._image[i * (self._width + 1):i * (self._width + 1) + self._width]) + "\n"
        return out

    def width(self):
        return self._width

    def height(self):
        return self._height

    def get_pixel(self, x, y):
        return self._image[x + (self._width + 1) * y]

    def set_pixel(self, x, y, value):
        self._image[x + (self._width + 1) * y] = value

    def shift_left(self, n):
        # TODO write shift_left method.
        _implement("shift_left")

    def shift_right(self, n):
        # TODO write shift_right method.
        _implement("shift_right")

    def shift_up(self, n):
        # TODO write shift_up method.
        _implement("shift_up")

    def shift_down(self, n: int):
        if n > self._height:
            n = self._height
        if n >= 0:
            self._image = (['0'] * self._width + [':']) * n + self._image[0:(self._width + 1) * (self._height - n)]
        else:
            self.shift_up(-n)
        if self._image[len(self._image)-1] == ':':
            self._image.pop()

    def crop(self, x, y, w, h):
        # TODO write crop method.
        _implement("crop")

    def copy(self):
        return self._image

    def invert(self):
        # TODO write invert method.
        _implement("invert")

    def fill(self, value):
        # TODO write fill method.
        _implement("fill")

    def blit(self, src, x, y, w, h, xdest=0, ydest=0):
        # TODO write blit method.
        _implement("blit")


class _Display:

    def __init__(self, image=Image.EMPTY):
        self.image = Image()
        self.isOn = True

    def get_pixel(self, x, y):
        return self.image.get_pixel(x, y)

    def set_pixel(self, x, y, value):
        self.image.set_pixel(x, y, value)
        print(self.image)

    def clear(self):
        self.image = Image.EMPTY
        _qprint("===== Display Cleared =====")

    def show_image(self, image, delay=400, wait=True, loop=False, clear=False):
        _qprint(image, prefix="SHOW")
        self.image = image
    
    def show_string(self, value, delay=400, wait=True, loop=False, clear=False):
        _qprint(value, prefix="SHOW")
        # self.image = image

    def show(self, value, delay=400, *args, wait=True, loop=False, clear=False):
        # TODO implement string value image show.
        if type(value) == Image:
            self.show_image(value, delay, wait, loop, clear)
        elif type(value) == str:
            self.show_string(value, delay, wait, loop, clear)

    def scroll(self, value, delay=150, *, wait=True, loop=False, monospace=False):
        # TODO implement other arguments.
        _qprint(value, prefix="SCROLL")

    def on(self):
        print("Display on.")
        self.isOn = True

    def off(self):
        print("Display off.")
        self.isOn = False

    def is_on(self):
        return self.isOn

    def read_light_level(self):
        try:
            value = int(input("Enter desired light level (0 to 255): "))
            if 0 <= value <= 255:
                return value
            else:
                raise ValueError("Level must be an integer between 0 and 255.")
        except ValueError:
            raise TypeError("Level must be an integer between 0 and 255.")


class _MicroBit:

    @staticmethod
    def time_ms():
        return int(time() * 1000)

    def __init__(self):
        self.isPanicMode = False
        self.startTime = self.time_ms()
        self.timeSlept = 0

        self.button_a = _Button('A')
        self.button_b = _Button('B')
        self.pin0 = _TouchPin(0, "Pad 0")
        self.pin1 = _TouchPin(1, "Pad 1")
        self.pin2 = _TouchPin(2, "Pad 2")
        self.pin3 = _AnalogPin(3, "Column 1")
        self.pin4 = _AnalogPin(4, "Column 2")
        self.pin5 = _DigitalPin(5, "Button A")
        self.pin6 = _DigitalPin(6, "Column 9")
        self.pin7 = _DigitalPin(7, "Column 8")
        self.pin8 = _DigitalPin(8, None)
        self.pin9 = _DigitalPin(9, "Column 7")
        self.pin10 = _AnalogPin(10, "Column 3")
        self.pin11 = _DigitalPin(11, "Button B")
        self.pin12 = _DigitalPin(12, None)
        self.pin13 = _DigitalPin(13, "SPI SCK")
        self.pin14 = _DigitalPin(14, "SPI MISO")
        self.pin15 = _DigitalPin(15, "SPI MOSI")
        self.pin16 = _DigitalPin(16, None)
        self.pin19 = _DigitalPin(19, "I2C SCL")
        self.pin20 = _DigitalPin(20, "I2C SDA")

        self.display = _Display()
        self.accelerometer = _Accelerometer()
        self.audio = _Audio(self.pin0)
        self.compass = _Compass()
        self.radio = _Radio()

    def panic(self, n):
        self.isPanicMode = True
        print("Panic Mode: ENABLED")

    def reset(self):
        self.__init__()
        print("Board Reset.")

    def sleep(self, n):
        self.timeSlept += n
        _qprint("Sleeping for {}ms".format(n))

    def running_time(self):
        userTime = int(input("Enter desired running time, in ms (-1 for automatic): "))
        if userTime == -1:
            return self.time_ms() - self.startTime
        else:
            return userTime

    def temperature(self):
        return float(input("Enter desired temperate: "))


_microbit = _MicroBit()
display = _microbit.display
accelerometer = _microbit.accelerometer
audio = _microbit.audio
compass = _microbit.compass
radio = _microbit.radio
button_a = _microbit.button_a
button_b = _microbit.button_b
pin0 = _microbit.pin0
pin1 = _microbit.pin1
pin2 = _microbit.pin2
pin3 = _microbit.pin3
pin4 = _microbit.pin4
pin5 = _microbit.pin5
pin6 = _microbit.pin6
pin7 = _microbit.pin7
pin8 = _microbit.pin8
pin9 = _microbit.pin9
pin10 = _microbit.pin10
pin11 = _microbit.pin11
pin12 = _microbit.pin12
pin13 = _microbit.pin13
pin14 = _microbit.pin14
pin15 = _microbit.pin15
pin16 = _microbit.pin16
pin19 = _microbit.pin19
pin20 = _microbit.pin20
panic = _microbit.panic
reset = _microbit.reset
sleep = _microbit.sleep
running_time = _microbit.running_time
temperature = _microbit.running_time
