win = False
import random
import time
gamblingfr = True
def gamble():
    while gamblingfr == True:
        print('You encounter, a GAMBLING MACHINE.')
        time.sleep(1)
        gamb = input('Would you like to GAMBLE? Y/N')
        if gamb == 'N':
            print('So be it.')
            break
        if gamb == 'Y':
            print('COMMENCE THE GAMBLING..')
            time.sleep(1)
            print('You encounter a slot machine.')
            slot = input('How much would you like to gamble? MUST BE 100 GOLD OR OVER.')
            while slot < 100:
                print('Please enter a valid gambling amount.')
                slot = input('How much would you like to gamble? MUST BE 100 GOLD OR OVER.')
            if slot >= 100:
                print('Nice amount. YOU NOW SPIN THE SLOT MACHINE.')
                slot_machine = [slot1,slot2,slot3]
                a_list = ['Gold', 'Junk','Diamond']
                slot1 = random.choice(a_list)
                slot2 = random.choice(a_list)
                slot3 = random.choice(a_list)
                



            

            




def puzzle1():
    choices = ['Rock','Paper','Scissors']

    player_choice = input("Rock paper scissors, what do you pick?").capitalize()
    computer_choice = random.choice(choices)

    while player_choice not in choices:
        player_choice = input('Rock paper scissors, what do you pick?').capitalize()

    if player_choice == computer_choice:
        print('It was a tie')
        print('You have won, you may continue..')
        match = True
    elif player_choice == 'Rock':
        if computer_choice == 'Paper':
            print ('You lose')
        elif computer_choice == 'Scissors':
            print ('You win')
            print('You have won, you may continue..')
            match = True
            

    elif player_choice == 'Paper':
        if computer_choice == 'Scissors':
            print ('You lose')
        elif computer_choice == 'Rock':
            print ('You win')
            print('You have won, you may continue..')
            match = True
        

    elif player_choice == 'Scissors':
        if computer_choice == 'Rock':
            print ('You lose')
    elif computer_choice == 'Paper':
        print ('You win')
        print('You have won, you may continue..')
        match = True
    if match == True:
        global win
        win = True