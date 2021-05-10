from time import time

# TODO Consider switching raise statements on user input to infinite loops waiting for a valid input.

print("===== Python Debug Mode =====")


class _Button:

    def __init__(self, name):
        self.name = name

    def was_pressed(self):
        print("Press " + self.name + "? (y/n)")
        value = input()
        if value in ["y", "Y"]:
            return True
        else:
            return False


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

    def is_touched(self):
        try:
            return bool(input("Enter pin touched status (True/False)"))
        except ValueError:
            raise ValueError("Input must be a boolean.")


class _Accelerometer:

    def __init__(self):
        self.log = []
        self.x = 0
        self.y = 0
        self.z = 0
        self.gestureList = ["up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake"]

    def get_x(self):
        try:
            value = int(input("Enter desired x acceleration (0 to 1024): "))
            if 0 <= value <= 1024:
                return value
            else:
                raise ValueError("Acceleration must be an integer between 0 and 1024.")
        except ValueError:
            raise TypeError("Acceleration must be an integer between 0 and 1024.")

    def get_y(self):
        try:
            value = int(input("Enter desired x acceleration (0 to 1024): "))
            if 0 <= value <= 1024:
                return value
            else:
                raise ValueError("Acceleration must be an integer between 0 and 1024.")
        except ValueError:
            raise TypeError("Acceleration must be an integer between 0 and 1024.")

    def get_z(self):
        try:
            value = int(input("Enter desired x acceleration (0 to 1024): "))
            if 0 <= value <= 1024:
                return value
            else:
                raise ValueError("Acceleration must be an integer between 0 and 1024.")
        except ValueError:
            raise TypeError("Acceleration must be an integer between 0 and 1024.")

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


class Image:
    EMPTY = "00000:" * 5
    HEART = "09090:" + "90909:" + "90009:" + "09090:" + "00900:"

    def __init__(self, image=EMPTY):
        self._image = list(image)
        self._width = 5
        self._height = 5

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
        return

    def shift_right(self, n):
        # TODO write shift_right method.
        return

    def shift_up(self, n):
        # TODO write shift_up method.
        return

    def shift_down(self, n):
        # TODO write shift_down method.
        return

    def crop(self, x, y, w, h):
        # TODO write crop method.
        return

    def copy(self):
        return self.Image

    def invert(self):
        # TODO write invert method.
        return

    def fill(self, value):
        # TODO write fill method.
        return

    def blit(self, src, x, y, w, h, xdest=0, ydest=0):
        # TODO write blit method.
        return


class _Display:

    def __init__(self, image=Image.EMPTY):
        self.image = Image()
        self.QUIET_MODE = True
        self.log = ["===== Python Debug Mode ====="]
        self.logCount = 0
        self.isOn = True

    def get_pixel(self, x, y):
        return self.image.get_pixel(x, y)

    def set_pixel(self, x, y, value):
        self.image.set_pixel(x, y, value)
        print(self.image)

    def clear(self):
        self.image = Image.EMPTY

    def show(self, image: Image):
        self.qprint(image)
        self.image = image

    def show(self, value, delay=400, *, wait=True, loop=False, clear=False):
        # TODO implement string value image show.
        self.qprint(value)
        # self.image = image

    def scroll(self, value, delay=150, *, wait=True, loop=False, monospace=False):
        # TODO implement other arguments.
        self.qprint(value)

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

    def qprint(self, text):
        if self.log[len(self.log) - 1] == text:
            self.logCount += 1
        elif self.logCount > 0:
            self.logCount = 0
            print(text)
        else:
            print(text)
        self.log.append(text)


class _MicroBit:

    @staticmethod
    def time_ms():
        return int(time() * 1000)

    def __init__(self):
        self.isPanicMode = False
        self.startTime = self.time_ms()
        self.timeSlept = 0

        self.display = _Display()
        self.accelerometer = _Accelerometer()

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

    def panic(self, n):
        self.isPanicMode = True
        print("Panic Mode: ENABLED")

    def reset(self):
        self.__init__()
        print("Board Reset.")

    def sleep(self, n):
        self.timeSlept += n
        print("Sleeping for {}ms".format(n))

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
