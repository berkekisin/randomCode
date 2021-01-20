import pygame as p
import random
import pygame as p

counter = 0
rows = 8
cols = 12
pieces = []
valid_pieces = list(range(rows * cols))
puzzle = []
pos = 0

# colors
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
orange = (255, 165, 0)
blue = (0, 0, 255)

# pygame
p.init()
screen = p.display.set_mode((480, 600))
screen.fill(black)

x = [37, 22, 33, 8, 25, 91, 95, 32, 54, 15, 62, 68, 61, 38, 67, 2, 56, 49, 19, 73, 93, 21, 65, 16, 94, 6, 92, 27, 47,
     36, 30, 66, 59, 3, 18, 48, 82, 58, 85, 75, 74, 24, 46, 72, 44, 77, 34, 86, 70, 57, 88, 83, 13, 9, 39, 63, 64, 87,
     35, 29, 53, 80, 79, 20, 76, 40, 43, 71, 55, 28, 26, 23, 60, 1, 41, 10, 31, 45, 14, 11, 52, 17, 12, 5, 81, 69, 42,
     89, 7, 78, 90, 51, 0, 50, 4, 84]
x2 = [62, 43, 30, 14, 16, 35, 4, 42, 87, 22, 63, 12, 71, 59, 68, 52, 45, 15, 70, 26, 60, 92, 17, 57, 88, 95, 19, 38, 40,
      50, 13, 9, 55, 86, 27, 31, 53, 93, 44, 34, 54, 49, 91, 58, 28, 47, 85, 29, 8, 18, 46, 77, 32, 0, 23, 37, 90, 33,
      69, 84, 21, 94, 51, 10, 64, 66, 79, 61, 48, 81, 7, 5, 11, 20, 3, 36, 72, 82, 56, 65, 78, 67, 73, 39, 1, 83, 75,
      89, 41, 76, 74, 6, 24, 2, 80, 25]


def getColorArray(colors):
    array = []

    for i in range(len(colors)):
        if colors[i] == 'Orange':
            array.append(orange)
        if colors[i] == 'Blue':
            array.append(blue)
        if colors[i] == 'Green':
            array.append(green)
        if colors[i] == 'Yellow':
            array.append(yellow)
    return array


def drawSol():
    screen.fill(black)
    offset = 20

    for i in range(rows):
        start_y = 400 - i * 2 * offset
        for j in range(cols):

            index = i + rows * j
            if index < len(puzzle):
                colors = getColorArray(getColors(puzzle[index]))
                start_x = 2 * j * offset

                p.draw.polygon(screen, colors[0],
                               ((start_x, start_y), (start_x + offset, start_y + offset),
                                (start_x + 2 * offset, start_y)))
                p.draw.polygon(screen, colors[1],
                               ((start_x + offset, start_y + offset), (start_x + 2 * offset, start_y),
                                (start_x + 2 * offset, start_y + 2 * offset)))
                p.draw.polygon(screen, colors[2],
                               ((start_x + offset, start_y + offset), (start_x + 2 * offset, start_y + 2 * offset),
                                (start_x, start_y + 2 * offset)))
                p.draw.polygon(screen, colors[3],
                               ((start_x, start_y), (start_x + offset, start_y + offset),
                                (start_x, start_y + 2 * offset)))


    p.display.update()


def printBoard():
    for i in range(len(puzzle)):
        print(getColors(i))


def getColors(index):
    return pieces[2 + index * 6:2 + index * 6 + 4]


def createPieces():
    global pieces

    text = open(r".\input", "r").read()
    pieces = text.split()


def solvePuzzle(curr_pieces):
    global puzzle, counter, pos

    index = 0
    while 1:
        events = p.event.get()
        for event in events:
            if event.type == p.QUIT:
                exit()

        counter += 1
        valid = True

        # check reset
        if counter > 1000000:
            #print("-----------------------reset----------------")
            # exit()
            return

        # ---------------------------------get new piece-----------------------------------------
        if len(curr_pieces) == 0:
            # print("-----------------------go back----------------")
            valid_pieces.append(puzzle.pop())
            pos -= 1
            return

        elif len(curr_pieces) == 1:
            index = 0
        else:
            index = random.randint(0, len(curr_pieces) - 1)

        piece = curr_pieces[index]
        curr_pieces.remove(piece)
        piece_colors = getColors(piece)

        # ----------------------------------check piece----------------------------------------------
        if (pos + 1) // rows > 0:
            left_piece = puzzle[pos - rows]
            left_colors = getColors(left_piece)
            if not (left_colors[1] == piece_colors[3]):
                valid = False

        if valid and pos % rows > 0:
            down_piece = puzzle[pos - 1]
            down_colors = getColors(down_piece)
            if not (down_colors[0] == piece_colors[2]):
                valid = False

        # -----------------------------if piece valid put it ----------------------------------------
        if valid:
            pos += 1
            puzzle.append(piece)
            valid_pieces.remove(piece)
            drawSol()
            #if pos > 94:
            # counter = 0
            #print("pos: ", pos)
            # print(puzzle)
            # print(valid_pieces)
            # drawSol()
            if pos == rows * cols:
                print("---------------------------Solution found------------- !!!!!!!!!!!!!!!!!!!!!!!")
                print(puzzle)
                drawSol()
                while 1:
                    events = p.event.get()
                    for event in events:
                        if event.type == p.QUIT:
                            exit()

            solvePuzzle(valid_pieces.copy())


def main():
    global pos, counter, puzzle, valid_pieces
    createPieces()
    start = list(range(rows * cols))
    while 1:
        solvePuzzle(start.copy())
        counter = 0
        pos = 0
        puzzle.clear()
        valid_pieces = list(range(rows * cols))


main()

# createPieces()
# drawSol()
# while 1:
#    events = p.event.get()
#    for event in events:
#        if event.type == p.QUIT:
#            exit()
