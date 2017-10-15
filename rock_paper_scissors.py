# Created by: David Wang
# Created on: 12-Oct-2017
# Created for: ICS3U
# Daily Assignment - Unit3-03
# This program displays the rock, paper, scissors game

import ui
import random

#constants
computer = ['rock_button', 'paper_button', 'scissors_button']
choice = ['rock.', 'paper.', 'scissors.']

def rock_paper_scissors_touch_up_inside(sender):
    # choose random number
    
    computer_choice = random.randint(0, 2)
    print(computer_choice)
    
    # output
    if sender.name == 'rock_button' and computer[computer_choice] == 'scissors_button' :
        view['outcome_label'].text = 'You Won!'
        view['computer_choice_label'].text = 'The computer chose: ' + choice[computer_choice]
    
    elif sender.name == 'paper_button' and computer[computer_choice] == 'rock_button' :
        view['outcome_label'].text = 'You Won!'
        view['computer_choice_label'].text = 'The computer chose: ' + choice[computer_choice]
    
    elif sender.name == 'scissors_button' and computer[computer_choice] == 'paper_button':
        view['outcome_label'].text = 'You Won!'
        view['computer_choice_label'].text = 'The computer chose: ' + choice[computer_choice]
    
    elif sender.name == computer[computer_choice] :
        view['outcome_label'].text = 'Its a Tie!'
        view['computer_choice_label'].text = 'The computer also chose: ' + choice[computer_choice]
    
    else:
        view['outcome_label'].text = 'You lose, Better Luck Next Time!'
        view['computer_choice_label'].text = 'The computer chose: ' + choice[computer_choice]
    

view = ui.load_view()
view.present('full_screen')
