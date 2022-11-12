# RockPaperScissor
RockPaperScissor Game without random import

Write a program that simulates the game Rock-Paper-Scissor between a user and the computer.

A. For the computer options, an arbitrary string of 15 – 20 characters should be created, containing only the uppercase characters of the options. Each time it is the computer's turn, the program should select the next character in the string. Also, if the characters in the string run out, then the string will be accessed from the beginning.

B. For user selections, the program should prompt for input of the character corresponding to the first of the selection (“R”, “S”, “P” or lowercase equivalents) from the keyboard. The program, after comparing the player's choice with the computer's (as obtained by accessing the string), will display a message about the result according to the game rules below. Implement defensive programming so that the user's choice is valid ("R", "S", "P" or the corresponding lower case) and the user is asked if he wishes to start a new game or terminate the application by entering an empty string.

Rules: Rock beats scissors.
       Scissor beats paper.
       Paper beats rock.
       Same option is Draw.