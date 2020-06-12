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

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (148, 0, 211)
RED = (255, 0, 0)
BLUE = (105, 152, 255)

L = []
rect = []



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
            mergesort(0, n - 1, n)
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


# /*------------------------------- END OF INSERTION SORT FUNCTION----------------------------------------------------*/

# /*-------------------------------------- QUICK SORT FUNCTION-------------------------------------------------------*/

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


# /*------------------------------------END OF QUICKSORT FUNCTION----------------------------------------------------*/


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
                pygame.time.delay(0)
                pygame.display.update()
            pygame.display.update()


# /*---------------------------------------------END OF BUBBLESORT----------------------------------------------------*/
n = 100


def array(n_):
    global L
    L.clear()
    arr = [(3 * i) for i in range(1, n_ + 1)]
    for a in range(n_):
        random_no = random.choice(arr)
        L.append(random_no + 10)
        arr.remove(random_no)


def create_new_array(n):
    array(n)
    rect.clear()
    WidthOfEachBar = 800 // (n + 1)
    for i in range(n):
        x = (i + 1) * (1 + WidthOfEachBar)
        y = 680 - L[i]
        rect.append(Rect(x, y, WidthOfEachBar, L[i]))
    refresh(n)


create_new_array(n)
sorted_quick = True
sorted_merge = True
sorted_bubble = True
sorted_insertion = True

while True:
    # print("enter options")
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                bubble_sort(n)
            elif event.key == pygame.K_q:
                quicksort(0, n - 1, n)
            elif event.key == pygame.K_i:
                insertionsort(n)
            elif event.key == pygame.K_m:
                mergesort(0, n - 1, n)
            elif event.key == pygame.K_r:
                create_new_array(n)
                refresh(n)
            elif event.key == pygame.K_UP:
                if n <= 220:
                    n = n + 30
                    print("up pressed")
                    screen.fill(WHITE)
                    create_new_array(n)
                    refresh(n)
            elif event.key == pygame.K_DOWN:
                if n >= 40:
                    n = n - 30
                    print("down pressed")
                    screen.fill(WHITE)
                    create_new_array(n)
                    refresh(n)
    for i in range(n):
        rect[i].colour = PURPLE
        rect[i].show()
        pygame.time.delay(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
    pygame.display.update()
