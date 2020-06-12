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
# n = 220  # n belongs till [50,220]



def array(n_):
    global L
    arr = [(3 * i) for i in range(1, n_ + 1)]
    for a in range(n_):
        random_no = random.choice(arr)
        L.append(random_no + 10)
        arr.remove(random_no)


# /*-------------------------------------- MERGE SORT FUNCTION----------------------------------------------------*/

def refresh(n):
    global rect
    screen.fill(WHITE)
    for i in range(n):
        rect[i].show()
        pygame.time.delay(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
    pygame.display.update()


def merge(l, m, r, n):
    global rect
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = []
    R = []
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L.append(Rect(rect[l + i].X, rect[l + i].Y, rect[l + i].width, rect[l + i].height))
        # L1[i] = Rect(rect[l + 1].X, rect[l + 1].Y, rect[l + 1].width, rect[l + 1].height)
        # L1[i] = Rect(0,0,0,0)
        # L1[i], rect[l + 1] = rect[l + i], L1[i]
        # L1[i].X, rect[l + 1].X = rect[l + i].X, L1[i].X
    refresh(n)
    # pygame.time.delay(1000)
    print("L1 working")
    for j in range(n2):
        R.append(Rect(rect[m + 1 + j].X, rect[m + 1 + j].Y, rect[m + 1 + j].width, rect[m + 1 + j].height))
        # R[j] = Rect(rect[m + 1 + j].X, rect[m + 1 + j].Y, rect[m + 1 + j].width, rect[m + 1 + j].height)
        # R[j] = Rect(0,0,0,0)
        # R[j], rect[m + 1 + j] = rect[m + 1 + j], R[j]
        # R[j].X, rect[m + 1 + j].X = rect[m + 1 + j].X, R[j].X
    refresh(n)
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        print("checking merge...")
        if L[i].height <= R[j].height:
            # rect[k] = Rect(L[i].X, L[i].Y, L[i].width, L[i].height)
            rect[k], L[i] = L[i], rect[k]
            rect[k].X, L[i].X = L[i].X, rect[k].X
            i += 1
            rect[k].colour = GREEN
            refresh(n)
            rect[k].colour = BLACK
        else:
            # rect[k] = Rect(R[j].X, R[j].Y, R[j].width, R[j].height)
            rect[k], R[j] = R[j], rect[k]
            rect[k].X, R[j].X = R[j].X, rect[k].X
            j += 1
            rect[k].colour = GREEN
            refresh(n)
            rect[k].colour = BLACK
        k += 1

    refresh(n)
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        rect[k], L[i] = L[i], rect[k]
        rect[k].X, L[i].X = L[i].X, rect[k].X
        i += 1
        k += 1
    refresh(n)
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        rect[k], R[j] = R[j], rect[k]
        rect[k].X, R[j].X = R[j].X, rect[k].X
        j += 1
        k += 1
    refresh(n)


def mergesort(l, r, n):
    if l < r:
        print("came here")
        m = (l + r - 1) // 2  # (rect[l].height + rect[r].height - 1) // 2
        mergesort(l, m, n)
        refresh(n)
        mergesort(m + 1, r, n)
        refresh(n)
        merge(l, m, r, n)
        refresh(n)


def MERGESORT_VISUAL(n):
    array(n)
    WidthOfEachBar = 800 // (n + 1)
    for i in range(n):
        x = (i + 1) * (1 + WidthOfEachBar)
        y = 680 - L[i]
        rect.append(Rect(x, y, WidthOfEachBar, L[i]))

    sorted_merge = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        if not sorted_merge:
            print("entered")
            mergesort(0, n - 1,n)
            sorted_merge = True
            for no1 in range(n):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit(0)
                rect[no1].colour = PURPLE
                rect[no1].show()
                pygame.time.delay(0)
                pygame.display.update()
        for no1 in range(n):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
            rect[no1].colour = PURPLE
            rect[no1].show()
        pygame.display.update()


# /*-------------------------------------- END OF MERGE SORT FUNCTION------------------------------------------------*/


MERGESORT_VISUAL(100)
