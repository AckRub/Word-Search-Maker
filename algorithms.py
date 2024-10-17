import random

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




class Algorithms():
    def row(word: str): #completed

        valid_line = [0,0,0,0,0,0,0,0,0,0]
        valid = False
        while not valid:
            random_column = game_board[random.randint(0,9)]
            random_num = random.randint(0,10-len(word)) # sets the possible range to fit the word in a row
            if random_column[random_num:random_num+len(word)] == valid_line[random_num:random_num+len(word)]:
                valid = True
        

        random_column[random_num:random_num+len(word)] = word[0:len(word)] # replaces random places in a row with the word
    
        return game_board

    
    def reverse_row(word: str): #completed

        reverse = ""
        count = -1

        for j in word:
            reverse += word[count]
            count -= 1

        valid_line = [0,0,0,0,0,0,0,0,0,0]
        valid = False
        while not valid:
            random_column = game_board[random.randint(0,9)]
            random_num = random.randint(0,10-len(word)) # sets the possible range to fit the word in a row
            if random_column[random_num:random_num+len(word)] == valid_line[random_num:random_num+len(word)]:
                valid = True
        

        random_column[random_num:random_num+len(word)] = reverse[0:len(word)] # replaces random places in a row with the word


        return game_board
        




    def column(word: str): #completed

        random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
        row_index = random.randint(0,9) # random index of the row  
        temp_rnd_column = random_column

        valid_count = 0
        unvalid = True

        while unvalid:

            if game_board[random_column][row_index] == 0:

                random_column += 1
                valid_count += 1
                if valid_count == len(word):
                    unvalid = False

            else:
                random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
                row_index = random.randint(0,9) # random index of the row  
                valid_count = 0


        for i in range(len(word)):
            game_board[temp_rnd_column][row_index] = word[i]
            temp_rnd_column += 1

        return game_board


    def reverse_column(word: str): #completed
        
        reverse = ""
        count = -1

        for j in word:
            reverse += word[count]
            count -= 1

        random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
        row_index = random.randint(0,9) # random index of the row  
        temp_rnd_column = random_column

        valid_count = 0
        unvalid = True

        while unvalid:

            if game_board[random_column][row_index] == 0:

                random_column += 1
                valid_count += 1
                if valid_count == len(word):
                    unvalid = False

            else:
                random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
                row_index = random.randint(0,9) # random index of the row  
                valid_count = 0


        for i in range(len(word)):
            game_board[temp_rnd_column][row_index] = word[i]
            temp_rnd_column += 1
    
        return game_board



    def cross(word: str): #completed

        random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
        row_index = random.randint(0,10-len(word)) # random index of the row 

        valid_count = 0
        unvalid = True

        while unvalid:

            if game_board[random_column][row_index] == 0:

                random_column += 1
                row_index += 1
                valid_count += 1

                if valid_count == len(word):
                    unvalid = False

            else:
                random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
                row_index = random.randint(0,10-len(word)) # random index of the row  
                valid_count = 0


        for i in range(len(word)):
            game_board[random_column-len(word)][row_index-len(word)] = word[i]
            random_column += 1
            row_index += 1

        return game_board
    


    def reverse_cross(word: str): #completed

        reverse = ""
        count = -1

        for j in word:
            reverse += word[count]
            count -= 1

        random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
        row_index = random.randint(0,10-len(word)) # random index of the row 

        valid_count = 0
        unvalid = True

        while unvalid:

            if game_board[random_column][row_index] == 0:

                random_column += 1
                row_index += 1
                valid_count += 1

                if valid_count == len(word):
                    unvalid = False

            else:
                random_column = random.randint(0,10-len(word)) # generates a number for the start of the column index
                row_index = random.randint(0,10-len(word)) # random index of the row  
                valid_count = 0


        for i in range(len(word)):
            game_board[random_column-len(word)][row_index-len(word)] = reverse[i]
            random_column += 1
            row_index += 1

        return game_board