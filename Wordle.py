########################################
# Name: Quinn Varnell
# Collaborators (if any): Abygale Brien, Google, ChatGPT, Quad
# GenAI Transcript (if any): N/A
# Estimated time spent (hr): ~ 9
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle(): # The main function to play the Wordle game.
    answer = ""
    while len(answer) != 5: # originally used if/else statement. While statement allows for continuous check until false. != 5 means does not equal 5.
        answer = random.choice(ENGLISH_WORDS) # answer equals a random word in the english alpabet. Does not only pull out 5 letter words, but will not print if it is not a 5 letter word.
    print(answer) # prints the answer to the wordle for visual clarification. Will print a 5 letter word in the elglish alphabet. 

    #answer = "glass"  
    
    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        row_number = gw.get_current_row()
        string = ""
        for i in range(N_COLS):
            w = gw.get_square_letter(row_number, i)
            string += w # permenately assignms string to w
        is_english_word(string)
        if is_english_word(string) and len(string) == 5: # singles out all words in ENGLISH_WORDS that are 5 characters long.
            gw.show_message("Is A Word") # If typed word is_english_word, show message "Is A Word"
            
            guess = "" # Defines guess as empty string
            for i in range(N_COLS):
                guess += gw.get_square_letter(gw.get_current_row(), i) # Pulls specific letters from each row and makes them permenately = to guess
                guess = guess.lower() # makes guess lower case
            print(guess)

            unmatched_letter = str(answer)
            # Turn_Letters_Green
            for i in range(N_COLS):
                if guess[i] == answer[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    unmatched_letter = unmatched_letter.replace(guess[i], "", 1)
                    gw.set_key_color(guess[i], CORRECT_COLOR) # Set_Key_Green
            # Turn_Letters_Yellow
            for i in range(N_COLS):
                if guess[i] in unmatched_letter and gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR: # if guess has letters that are in answer, but are unmatched, do not set to CORRECT_COLOR
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    unmatched_letter = unmatched_letter.replace(guess[i], "", 1)
                    gw.set_key_color(guess[i], PRESENT_COLOR) # Set_Key_Yellow
            # Turn_Letters_Grey
            for i in range(N_COLS):
                if guess[i] != answer[i] and gw.get_square_color(gw.get_current_row(), i) != PRESENT_COLOR:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                    unmatched_letter = unmatched_letter.replace(guess[i], "", 1)
                    gw.set_key_color(guess[i], MISSING_COLOR) # Set_Key_Grey

            gw.set_current_row(gw.get_current_row()+1)
            if guess == answer:
                gw.show_message("Great, I Guess...")
                gw.set_current_row(N_ROWS)
            elif gw.get_current_row() == (N_ROWS):
                gw.show_message("YOU LOST!!! GOOD FOR YOU!!!")

        else:
            gw.show_message("Not A Word Dingleberry") # If typed word is not in is_english_word, show message "Not A Word Dingleberry"

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    #word = "WAGER"
    #gw.set_square_letter(0, 0, word[0])
    #gw.set_square_letter(0, 1, word[1])
    #gw.set_square_letter(0, 2, word[2])
    #gw.set_square_letter(0, 3, word[3])
    #gw.set_square_letter(0, 4, word[4])





# Startup boilerplate
if __name__ == "__main__":
    wordle()
