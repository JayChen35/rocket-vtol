import pygame
import serial
import time


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
speed = 0
ser = serial.Serial('COM15', baudrate=9600, timeout=0)
start = time.time()

# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()

# -------- Main Program Loop -----------
while not done:
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            print(joystick.get_button(0))
            print(time.time() - start)
            if time.time() - start > 5:
                ser.write("a".encode())
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        elif event.type == pygame.JOYAXISMOTION:
            x1 = joystick.get_axis(0)
            y1 = -joystick.get_axis(1)
            y2 = -joystick.get_axis(3)
            x2 = joystick.get_axis(4)
            print("Joystick axis moved")
            print(x1, y1, x2, y2)
            if y1 <= 0:
                y1 = 0
            # Max speed of 5
            sped = int(y1 * 7)
            if sped != speed:
                speed = sped
                val = "t" + str(speed)
                print(val)
                ser.write(val.encode())

    screen.fill(WHITE)
    textPrint.reset()

    i = 0
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

    textPrint.tprint(screen, "Joystick {}".format(i))
    textPrint.indent()

    name = joystick.get_name()
    textPrint.tprint(screen, "Joystick name: {}".format(name))

    axes = joystick.get_numaxes()
    textPrint.tprint(screen, "Number of axes: {}".format(axes))
    textPrint.indent()

    for i in range(axes):
        axis = joystick.get_axis(i)
        textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
    textPrint.unindent()

    buttons = joystick.get_numbuttons()
    textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
    textPrint.indent()

    for i in range(4):
        button = joystick.get_button(i)
        textPrint.tprint(screen,
                            "Button {:>2} value: {}".format(i, button))
    textPrint.unindent()

    hats = joystick.get_numhats()
    textPrint.tprint(screen, "Number of hats: {}".format(hats))
    textPrint.indent()


    pygame.display.flip()
    clock.tick(20)

pygame.quit()
