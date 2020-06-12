import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("SORTING VISUALS")


class Rect:
    def __init__(self, x, y, width, height):
        self.X = x
        self.Y = y
        self.width = width
        self.height = height
        self.colour = BLACK

    def show(self):
        pygame.draw.rect(screen, self.colour, (self.X, self.Y, self.width, self.height))

    def changeCol(self, colour):
        self.colour = colour


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (148, 0, 211)

L = []
rect = []
#n = 150  # n belongs till [50,220]


def array(n_):
    global L
    arr = [(3 * i) for i in range(1, n_ + 1)]
    for a in range(n_):
        random_no = random.choice(arr)
        L.append(random_no + 10)
        arr.remove(random_no)


# /*-------------------------------------- INSERTION SORT FUNCTION----------------------------------------------------*/
def equal(b):
    a = Rect(0, 0, 0, 0)
    a.X = b.X
    a.Y = b.Y
    a.width = b.width
    a.height = b.height
    a.colour = b.colour
    return a


def insertionsort(n):
    global rect
    for oo in range(n):
        print(rect[oo].height, end=" ")
    print()
    for i in range(1, n):
        print("outer loop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        rect[i].colour = GREEN
        key = rect[i]
        key.X = rect[i].X
        j = i - 1
        while j >= 0 and key.height < rect[j].height:
            for oo in range(n):
                print(rect[oo].height, end=" ")
            print()
            rect[j + 1], rect[j] = rect[j], rect[j + 1]
            rect[j + 1].X, rect[j].X = rect[j].X, rect[j + 1].X
            j = j - 1

        rect[j + 1], key = key, rect[j + 1]
        rect[j + 1].X, key.X = key.X, rect[j + 1].X

        screen.fill(WHITE)
        for a in range(n):
            rect[a].show()
        pygame.display.update()
        rect[j + 1].colour = BLACK


def INSERTION_SORT_VISUAL(n):
    array(n)
    WidthOfEachBar = 800 // (n + 1)
    for i in range(n):
        x = (i + 1) * (1 + WidthOfEachBar)
        y = 680 - L[i]
        rect.append(Rect(x, y, WidthOfEachBar, L[i]))

    sorted_insertion = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        if not sorted_insertion:
            insertionsort(n)
            for oo in range(n):
                print(rect[oo].height, end=" ")
            print()
            print("came once")
            sorted_insertion = True
            for a in range(n):
                rect[a].colour = PURPLE
                rect[a].show()
                pygame.display.update()
            pygame.display.update()


INSERTION_SORT_VISUAL(50)
