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
RED = (255, 0, 0)

L = []
rect = []


# n = 220  # n belongs till [50,220]


def array(n_):
    global L
    arr = [(3 * i) for i in range(1, n_ + 1)]
    for a in range(n_):
        random_no = random.choice(arr)
        L.append(random_no + 10)
        arr.remove(random_no)


def refresh(n):
    global rect
    screen.fill(WHITE)
    for i in range(n):
        # rect[i].colour = colour
        rect[i].show()
        pygame.time.delay(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
    pygame.display.update()


# /*-------------------------------------- QUICK SORT FUNCTION-------------------------------------------------------*/

def swap(a, b):
    global rect
    rect[a], rect[b] = rect[b], rect[a]
    rect[a].X, rect[b].X = rect[b].X, rect[a].X


def partition(low, high, n):
    global rect
    pivot = rect[high]
    pivot, rect[high] = rect[high], pivot
    pivot.X, rect[high].X = rect[high].X, pivot.X
    pivot.colour = RED
    i = low - 1
    for j in range(low, high):
        if rect[j].height < pivot.height:
            i += 1
            rect[i].colour = GREEN
            rect[j].colour = GREEN
            swap(i, j)
            refresh(n)
            rect[i].colour = BLACK
            rect[j].colour = BLACK
    rect[high].colour = RED
    rect[i + 1].colour = RED
    swap(high, i + 1)
    refresh(n)
    rect[high].colour = BLACK
    rect[i + 1].colour = BLACK
    return i + 1


def quicksort(low, high, n):
    global rect
    if low < high:
        pi = partition(low, high, n)  # pi is pivot element
        quicksort(low, pi - 1, n)
        refresh(n)
        quicksort(pi + 1, high, n)
        refresh(n)


# /*------------------------------------END OF QUICKSORT FUNCTION----------------------------------------------------*/
def QSORT_VISUAL(n):
    array(n)
    WidthOfEachBar = 800 // (n + 1)
    for i in range(n):
        x = (i + 1) * (1 + WidthOfEachBar)
        y = 680 - L[i]
        rect.append(Rect(x, y, WidthOfEachBar, L[i]))
    sorted_quick = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        # print("calling q sort")
        if not sorted_quick:
            quicksort(0, n - 1, n)
            refresh(n)
            sorted_quick = True
        for i in range(n):
            rect[i].colour = PURPLE
            rect[i].show()
            pygame.time.delay(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
        pygame.display.update()


QSORT_VISUAL(50)
