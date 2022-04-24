

from pygame.locals import *

##### COLOR DEFINITIONS #####

# color    R    G    B
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
LIGHTRED = (175,  20,  20)
GREEN = (0, 155,   0)
LIGHTGREEN = (20, 175,  20)
BLUE = (0,   0, 155)
LIGHTBLUE = (20,  20, 175)
YELLOW = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

# color initialization
BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS = (BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)


######### CLASS DEFINITIONS #########

# next queue


class NQueue:

    MAX_SIZE = 3

    def __init__(self, size):
        if size > self.MAX_SIZE:
            raise Exception(
                " NQUEUE Error : size cannot be greater than Max size (" + self.MAX_SIZE + ")")
        self.size = size


# game conf


class GameConf:
    def __init__(self):
        self.color = "color"
        self.music = False
        self.level = "hard"
        self.hold = False
        self.seed = 42
        self.fps = 25
        self.initColors()

    def initColors(self):
        if self.color == "color":
            self.border = BLUE
            self.bg = BLACK
            self.text = WHITE
            self.textShadow = GRAY
            self.colors = (BLUE, GREEN, RED, YELLOW)
            self.lcolors = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
        else:
            self.border = BLACK
            self.bg = WHITE
            self.text = BLACK
            self.textShadow = GRAY
            self.colors = (BLACK,)
            self.lcolors = (GRAY,)

    def getColors(self):
        return self.border, self.bg, self.text, self.textShadow, self.colors, self.lcolors

    def getFPS(self):
        return self.fps
# control conf


class CtrlConf:
    def __init__(self):
        # movement
        self.down = K_DOWN
        self.left = K_LEFT
        self.right = K_RIGHT
        self.rotateC = K_UP
        self.rotateAC = K_q
        self.hardDrop = K_SPACE
        # game action
        self.exit = K_ESCAPE
        self.pause = K_p

    # board/display conf


class Board:
    BOXSIZE = 20

    def __init__(self):
        self.windowWidth = 640
        self.windowHeight = 480
        self.boardWidth = 10
        self.boardHeight = 20

    def getWindowVals(self):
        return self.windowWidth, self.windowHeight

    def getBoardVals(self):
        return self.boardWidth, self.boardHeight

################## Default objects ##################
