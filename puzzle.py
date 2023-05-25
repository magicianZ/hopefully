win = False
import random
import time
gamblingfr = True
from collections import Counter
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
            while slot < '100':
                print('Please enter a valid gambling amount.')
                slot = input('How much would you like to gamble? MUST BE 100 GOLD OR OVER.')
            if slot >= '100':
                print('Nice amount. YOU NOW SPIN THE SLOT MACHINE.')
                a_list = ['Gold', 'Junk','Diamond']
                slot1 = random.choice(a_list)
                slot2 = random.choice(a_list)
                slot3 = random.choice(a_list)
                slot_machine = [slot1,slot2,slot3]
                commence = Counter(slot_machine)
                if commence['Gold'] > 1:
                    if commence['Gold'] == 3:
                        print('You hit the 3 gold!')
                        print(commence)
                    print('You have won a little bit of gold.')
                    print(commence)
                if commence['Diamond'] > 1:
                    if commence['Diamond'] == 3:
                        print('YOU HIT THE JACKPOT')
                        print(commence)
                    print('You have won a little bit of gold.')
                    print(commence)
                if commence['Junk'] > 1:
                    if commence['Junk'] == 3:
                        print('You hit the junk jackpot nerd')
                        print(commence)
                    print('You lost a bit of gold...')
                    print(commence)
                else:
                    print(commence)




                


def typing():
    math = ["Pneumonoultramicroscopicsilicovolcanoconiosis","Hippopotomonstrosesquippedaliophobia","Floccinaucinihilipilification","Supercalifragilisticexpialidocious","Thyroparathyroidectomized","Honorificabilitudinitatibus"]
    #s
    print('Welcome to the typing puzzle, you are going to type a word for me. TYPE AS FAST AS YOU CAN. If you get spell the word wrong or run out of time, your gold will face some consequences.')
    input('Type when you are ready.')
    variable = random.choice(math)
    time.sleep(1)
    print(f'Type... {variable}')
    time1 = time.time()
    their_spelling = input('')
    time2 = time.time()
    t = time1 - time2
    positive_t = abs(t)
    print(positive_t)
    if their_spelling == variable:
        if positive_t <= 10:
            base = float( (2-(positive_t/10))*100)
            real_base = round(base)
            #self.gold = self.gold + real_base
            print(f'Good job, you typed this in {positive_t} seconds. You gained some gold.')
        elif positive_t >10:
            print('You were too slow. You do not get anything.')
    elif their_spelling != variable:
        self.gold = self.gold - 50
        print(f'you spelt it wrong nerd. You lost gold, you now have {self.gold}')
        
    


            
def trivia():
    trivia = {'question':"How much does the wand buff your magic damage by?", 'answer': '150'}
    trivia1 = {'question':"What is the ultimate's base damage.", 'answer':'500'}
    trivia2 = {'question':"How much does the stone cost?",'answer':'50'}
    trivia3 = {'question':"How many energy points do you start each battle with?",'answer': '3'}
    trivia4 = {'question':"What letter do you need to press to increase ultimate damage?",'answer':'f'}
    trivia5 = {'question':"Who was the 2nd US President",'answer':'john adams'}
    trivia6 = {'question':"Who is the 16th president?",'answer':'abraham lincoln'}
    trivia7 = {'question':"What is the 6th planet in our solar system",'answer':'saturn'}
    trivia8 = {'question':"When you get sick, your body produces what immune system protein is produced",'answer':'antibodies'}

    questions = [trivia,trivia1,trivia2,trivia3,trivia4,trivia5,trivia6,trivia7,trivia8]
    the_question = random.choice(questions)
    print(the_question['question'])
    yessir = input('Answer').lower()
    if yessir == the_question['answer']:
        #self.gold = self.gold + 100
        print(f'Correct, you now have') #{self.gold}
    else:
        #self.gold = self.gold - 50
        print(f'The correct answer was...')
        print(the_question['answer'])
        print(f'Incorrect, you have lost gold... ')#You now have {self.gold})

            
gamble()



def puzzle1():
    choices = ['Rock','Paper','Scissors']
    print('Lets play rock paper scissors!')

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
        self.gold = self.gold + 150
        print(f'Good job you won, you have gained $150 gold. Your gold is now {self.gold}')
    if match != True:
        self.gold = self.gold - 50
        print(f'You lost, and lost some gold. You now have {self.gold}')