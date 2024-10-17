import string
import algorithms
import random
import time
from colorama import Fore

if __name__ == "__main__":

    game_board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]
        


    amount = int(input("how many words u want to add? (from 1-5):  "))

    for i in range(amount):
        word = input("enter your word: (max length of a word: 8-9) ") 
        print(f"when you choose an algorithm {Fore.RED}MAKE SURE {Fore.WHITE}to do it like this: any cross > any column > any row")
        time.sleep(2)
        algo = input("choose an algorithm to mix up the letter: (row,r_row,column,r_column,cross,r_cross) ")
        time.sleep(0.5)
        if algo == "row":
            algorithms.Algorithms.row(word)
        elif algo == "column":
            algorithms.Algorithms.column(word)
        elif algo == "cross":
            algorithms.Algorithms.cross(word)
        elif algo == "r_row":
            algorithms.Algorithms.reverse_row(word)
        elif algo == "r_column":
            algorithms.Algorithms.reverse_column(word)
        elif algo == "r_cross":
            algorithms.Algorithms.reverse_cross(word)


    game_board = algorithms.game_board
    
    alphabet = string.ascii_lowercase

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                rnd = random.randint(0,25) # there are 26 letters but the index starts at 0 so the range is 25
                game_board[i][j] = alphabet[rnd]

    for line in game_board:
        print(line)

