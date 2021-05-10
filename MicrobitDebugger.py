from time import time

print("===== Python Debug Mode =====")


class Button:

    def __init__(self, name):
        self.name = name

    def was_pressed(self):
        print("Press " + self.name + "? (y/n)")
        value = input()
        if value in ["y", "Y"]:
            return True
        else:
            return False


class Pin:

    def __init__(self, idx, type, function):
        self.id = idx
        self.type = type
        self.function = function


class Image:
    EMPTY = "00000:" * 5
    HEART = "09090:" + "90909:" + "90009:" + "09090:" + "00900:"

    def __init__(self, image=EMPTY):
        self.image = list(image)

    def __str__(self):
        out = "\n"
        for i in range(5):
            out += "".join(self.image[i * 6:i * 6 + 5]) + "\n"
        return out

    def get_pixel(self, x, y):
        return self.image[x + 6 * y]

    def set_pixel(self, x, y, value):
        self.image[x + 6 * y] = value


class Display:

    def __init__(self, image=Image.EMPTY):
        self.image = Image()
        self.QUIET_MODE = True
        self.log = ["===== Python Debug Mode ====="]
        self.logCount = 0

    def qprint(self, text):
        if self.log[len(self.log) - 1] == text:
            self.logCount += 1
        elif self.logCount > 0:
            self.logCount = 0
            print(text)
        else:
            print(text)
        self.log.append(text)

    def scroll(self, text, wait=False):
        self.qprint(text)

    def show(self, image):
        self.qprint(image)
        self.image = image

    def clear(self):
        self.image = Image.EMPTY

    def set_pixel(self, x, y, value):
        self.image.set_pixel(x, y, value)
        print(self.image)

    def get_pixel(self, x, y):
        return self.image.get_pixel(x, y)


class MicroBit:

    @staticmethod
    def time_ms():
        return int(time()*1000)

    def __init__(self):
        self.isPanicMode = False
        self.startTime = self.time_ms()
        self.timeSlept = 0

        self.display = Display()

        self.button_a = Button('A')
        self.button_b = Button('B')
        self.pin0 = Pin(0, "touch", "Pad 0")
        self.pin1 = Pin(1, "touch", "Pad 1")
        self.pin2 = Pin(2, "touch", "Pad 2")
        self.pin3 = Pin(3, "analog", "Column 1")
        self.pin4 = Pin(4, "analog", "Column 2")
        self.pin5 = Pin(5, "digital", "Button A")
        self.pin6 = Pin(6, "digital", "Column 9")
        self.pin7 = Pin(7, "digital", "Column 8")
        self.pin8 = Pin(8, "digital", None)
        self.pin9 = Pin(9, "digital", "Column 7")
        self.pin10 = Pin(10, "analog", "Column 3")
        self.pin11 = Pin(11, "digital", "Button B")
        self.pin12 = Pin(12, "digital", None)
        self.pin13 = Pin(13, "digital", "SPI SCK")
        self.pin14 = Pin(14, "digital", "SPI MISO")
        self.pin15 = Pin(15, "digital", "SPI MOSI")
        self.pin16 = Pin(16, "digital", None)
        self.pin19 = Pin(19, "digital", "I2C SCL")
        self.pin20 = Pin(20, "digital", "I2C SDA")

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
