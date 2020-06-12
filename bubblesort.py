import pygame
import random


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


pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("SORTING VISUALS")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (148, 0, 211)

L = []
rect = []


# n = 150  # n belongs till [50,220]


def array(n_):
    global L
    arr = [(3 * i) for i in range(1, n_ + 1)]
    for a in range(n_):
        random_no = random.choice(arr)
        L.append(random_no + 10)
        arr.remove(random_no)


# /*-------------------------------------- BUBBLE SORT FUNCTION-------------------------------------------------------*/
def swap(a, b):
    global rect
    rect[a], rect[b] = rect[b], rect[a]
    rect[a].X, rect[b].X = rect[b].X, rect[a].X


def bubble_sort(n):
    global rect
    for ii1 in range(n):
        for j in range(n - 1):
            rect[j].colour = GREEN
            rect[j + 1].colour = GREEN

            if rect[j].height > rect[j + 1].height:
                # print(r[j].X, r[j + 1].X)
                swap(j, j + 1)
                # print(r[j].X, r[j + 1].X)
                for amb in range(n):
                    print(rect[amb].height, end=" ")
                print()
            screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
            for no1 in range(n):
                rect[no1].show()
            pygame.time.delay(0)
            pygame.display.update()
            rect[j].colour = BLACK
            rect[j + 1].colour = BLACK
    print("DONE")


def BBSORRT_VISUAL(n):
    array(n)
    WidthOfEachBar = 800 // (n + 1)
    # initialise the rectangles...
    for i in range(n):
        x = (i + 1) * (1 + WidthOfEachBar)
        y = 680 - L[i]
        rect.append(Rect(x, y, WidthOfEachBar, L[i]))
    sorted_bubble = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        if not sorted_bubble:
            bubble_sort(n)
            sorted_bubble = True
            for no1 in range(n):
                rect[no1].colour = PURPLE
                rect[no1].show()
                pygame.time.delay(50)
                pygame.display.update()
            pygame.display.update()


# /*---------------------------------------------END OF BUBBLESORT----------------------------------------------------*/

# call the function
BBSORRT_VISUAL(50)
