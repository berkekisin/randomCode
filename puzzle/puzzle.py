import numpy as np
import pygame as p

rows = 8
cols = 12
puzzle = []


def main():
    createBoard()


def createBoard():
    text = open(r"C:\Users\kisin\Desktop\input", "r").read()
    board = text.split()

    # -------format input text-----------------
    index = 0
    for i in range(rows * cols):
        del board[index]
        del board[index]

        for j in range(4):
            board[index + j] = (board[index])[0]

        index += 4

    print(len(board)/(rows*cols))


main()
