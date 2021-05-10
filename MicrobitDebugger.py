print("===== Python Debug Mode =====")

class Button():

    def __init__(self, name):
        self.name = name
    
    def was_pressed(self):
        print("Press "+self.name+"? (y/n)")
        value = input()
        if value in ["y","Y"]:
            return True
        else:
            return False

class Image():

    EMPTY = "00000:"*5
    HEART = "09090:"+"90909:"+"90009:"+"09090:"+"00900:"

    def __init__(self, image=EMPTY):
        self.image = list(image)

    def __str__(self):
        out = "\n"
        for i in range(5):
            out += "".join(self.image[i*6:i*6+5])+"\n"
        return out

    def get_pixel(self,x,y):
        return self.image[x+6*y]

    def set_pixel(self,x,y,value):
        self.image[x+6*y] = value

class Display():

    def __init__(self, image=Image.EMPTY):
        self.image = Image()
        self.QUIET_MODE = True
        self.log = ["===== Python Debug Mode ====="]
        self.logCount = 0

    def qprint(self, text):
        if self.log[len(self.log)-1] == text:
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

    def set_pixel(self,x,y,value):
        self.image.set_pixel(x,y,value)
        print(self.image)

    def get_pixel(self,x,y):
        return self.image.get_pixel(x,y)

display = Display()

button_a = Button('A')
button_b = Button('B')

def sleep(time):
    if display.QUIET_MODE == False:
        print("Sleep for "+str(time)+"ms.")

def quiet_mode(switch):
    if isinstance(switch, bool):
        display.QUIET_MODE = switch
    else:
        raise TypeError("Quiet mode takes a single boolean value. Recieved "+type(switch))
