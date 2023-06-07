import random
import time
from collections import Counter
gamblingfr = True

class Player:
    Stone = 50
    Armor = 150
    Wand = 200
    Magic_Armor = 50
    items = ['Stone','Armor','Wand','Magic_Armor']
    inventory_items = ['Smoothie','Protein','Potion','Elixir']
    Smoothie = 75
    Protein = 50
    Potion = 100
    noah_rozin = True
    Elixir = 2
   
    def __init__(self,HP,Name,Damage,energy_point,magic_damage,gold,max_HP,max_magicdmg,max_attack,ultpoints,ultdmg,inventory,maxult):
        self.HP = HP
        
        self.Name = Name
        self.Damage = Damage
        self.energy_point = energy_point
        self.magic_damage = magic_damage
        self.max_attack = max_attack
        self.max_magicdmg = max_magicdmg
        self.gold = gold
        self.max_HP = max_HP
        self.ultpoints = ultpoints
        self.ultdmg = ultdmg
        self.inventory = inventory
        self.maxult = maxult
    def name(self):
        name1 = input('What shall you be called adventurer?')
        self.Name = name1


    def attack(self,target):
        damage_taken = target.HP - self.Damage
        target.HP = damage_taken
        self.energy_point = self.energy_point + 1
        print(f'{self.Name} has attacked {target.Name}')
        print('')
        print(f'{target.Name} is {target.HP} HP ')
        print(f'{self.Name} has {self.energy_point} energy points')
        
        
            
        

      



    def magic_dmg(self,target):
        if self.energy_point > 0:
            self.energy_point = self.energy_point - 1
            self.ultpoints = self.ultpoints + 1
            damage_taken = target.HP - self.magic_damage
            target.HP = damage_taken
            print('')
            print(f'{self.Name} has magic attacked {target.Name}')
            time.sleep(0.5)
            print(f'{target.Name} is now {target.HP} HP')
            print(f'{self.Name} has {self.energy_point} energy points and {self.ultpoints}  ultimate points')
            print('')
            

        else:
            print('Recover energy')
    def ult(self,target):
        if self.ultpoints >= 5:
            print('You charge up an ultimate, press F as much as you can to increase the damage of your ultimate!')
            time.sleep(1)
            print('Be careful! If you press F for more than 5 seconds, your damage bonus will not count!')
            time.sleep(3)
            print('Get ready!')
            time.sleep(2)
            t1 = time.time()
            thedmg = input('Go for it!')
            t2 = time.time()
            t = t1 - t2
            
            if t>= -5:
                real_dmg = self.ultdmg + len(thedmg)
                nuke_taken = target.HP - real_dmg
                target.HP = nuke_taken
                print(f'You have done {real_dmg} dmg')
                self.ultpoints = 0
                print (f'{target.Name} is now {target.HP} HP')
                print(f'{self.Name} has {self.ultpoints} ultimate points')
            elif t < -5:
                print('You have exceeded 5 seconds..')
                real_dmg = self.ultdmg
                nuke_taken = target.HP - real_dmg
                target.HP = nuke_taken
                self.ultpoints = 0
                print (f'{target.Name} is now {target.HP} HP ')
                print(f'{self.Name}  has {self.ultpoints} ultimate points.')
                print('--------------------------------------------')
    def use_item(self):
        while self.noah_rozin == True:
            choicehm = input(f'You have chose to use an item, out of {self.inventory}, what item would you like to use? If you do not want to use an item, type N').capitalize()
            print(choicehm)
            if 'Smoothie' in self.inventory:
                if choicehm == 'Smoothie':
                    self.HP = self.HP + self.Smoothie
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Smoothie')
            if 'Protein' in self.inventory:
                if choicehm == 'Protein':
                    self.HP = self.HP + self.Protein
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Protein')
            if 'Potion' in self.inventory:
                if choicehm == 'Potion':
                    self.HP = self.HP + self.Potion
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Potion')
            if 'Elixir' in self.inventory:
                if choicehm == 'Elixir':
                    self.energy_point = self.energy_point + self.Elixir
                    print(f'{self.Name} now has {self.energy_point} energy points.')
                    self.inventory.remove('Elixir') 
            if choicehm == 'N':
                break
            else:
                print('Use another item if you have!')


        




    



    def turn(self,target):
       print(f'{self.Name}s turn. Would you like to....')
       time.sleep(0.5)
       print(f'Regular Attack : Type "Attack" and deal {self.Damage} damage.')
       time.sleep(0.5)
       print(f'Magic Attack: Type "Magic" and deal {self.magic_damage} damage')
       time.sleep(0.5)
       print(f'Use an item: Type "Item" and choose an item out of {self.inventory}')
       time.sleep(0.5)
       print(f'Use an Ultimate: Type "Ult" and deal {self.ultdmg} damage plus your modifier!')
       time.sleep(0.3)
       print(f'You have {self.energy_point} energy points and {self.ultpoints} ult points.')
       user_input = input('What would you like to do?').capitalize()
       print('')

        
       if user_input == 'Attack':
            self.attack(target)
       elif user_input == 'Magic':
            self.magic_dmg(target)
       elif user_input == 'Ult':
            self.ult(target)
       elif user_input == 'Item':
            self.use_item()





    def AI(self,target):
        self.list = ['Attack','Attack','Attack']
        get_lucky = random.choice(self.list)
        if self.energy_point > 0:
                self.magic_dmg(Character)
        elif self.energy_point == 0:
                self.attack(Character)
             
       
          

    def add_gold(self,amount):
        self.gold = self.gold + amount
        print(f'{self.Name} now has {self.gold} gold')




    def preview_items(self):
        print('Welcome to the shop')
        print(f'I see you have, {self.gold} gold.')
        time.sleep(1)
        print('Our items are...')
        time.sleep(0.5)
        print('Stone: Cost: 50 gold. Buff: Increases Normal Attack by 50.')
        time.sleep(0.5)
        print('Wand: Cost: 150 Buff: Increases Magic Damage by 200 and Ultimate Damage by 200')
        time.sleep(0.5)
        print('Armor: Cost: 100. Buff: Increases HP by 150.')
        time.sleep(0.5)
        weapon_choice = input('Would you like to buy anything? Y/N').capitalize()
        if weapon_choice == 'Y':
            what_item = input('What item would you like to buy?').capitalize()
            if self.gold <= 0:
                print('You have no gold, brokie...')
            if what_item == 'Stone':
                if self.gold >= 50:
                    self.max_attack = self.Damage + self.Stone
                    self.Damage = self.max_attack
                    print(f'{self.Name} damage is now {self.Damage}')
                    self.gold = self.gold - 50
                    print(f'You now have {self.gold} gold')
              
            if what_item == 'Armor':
                if self.gold >= 100:
                    self.max_HP = self.max_HP + self.Armor
                    self.HP = self.max_HP
                    print(f'{self.Name} HP is now {self.max_HP}')
                    time.sleep(0.5)
                    print('Take an item for your troubles!')
                    time.sleep(0.3)
                    item()
                    self.gold = self.gold - 100
                    print(f'You now have {self.gold} gold')
                  
            if what_item == 'Wand':
                if self.gold >= 150:
                    self.max_magicdmg = self.magic_damage + self.Wand
                    self.magic_damage = self.max_magicdmg
                    self.maxult = self.ultdmg + 200
                    self.ultdmg = self.maxult
                    print(f'{self.Name} magic damage is now {self.magic_damage} and your ultimate damage is now {self.ultdmg}')
                    print('Take an elixir for your troubles!')
                    self.inventory.append('Elixir')
                    self.gold = self.gold - 150
                    print(f'You now have {self.gold} gold')
        if weapon_choice == 'N':
            print('Ok cheapskate...')

    




      
        

Character = Player(150,"idk",50,3,100,int(100),150,100,50,10,500,[],500)



NPC1 = Player(950,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC2 = Player(1000,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC3 = Player(1300,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC4 = Player(1400,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC5 = Player(1500,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC6 = Player(1700,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC7 = Player(2000,"NPC",10,3,30,0,200,10,20,0,0,[],0)


Boss = Player(7000,"Mr_Whalen",40,6,80,0,200,200,100,0,0,[],0)
#HP,Name,Damage,energy_point,magic_damage,gold,max_HP

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
        Character.gold = Character.gold + 150
        print(f'Good job you won, you have gained $150 gold. Your gold is now {Character.gold}')
     
    elif player_choice == 'Rock':
        if computer_choice == 'Paper':
            print ('You lose')
        elif computer_choice == 'Scissors':
            print ('You win')
            print('You have won, you may continue..')
            Character.gold = Character.gold + 150
            print(f'Good job you won, you have gained $150 gold. Your gold is now {Character.gold}')
           
            

    elif player_choice == 'Paper':
        if computer_choice == 'Scissors':
            print ('You lose')
        elif computer_choice == 'Rock':
            print ('You win')
            print('You have won, you may continue..')
            Character.gold = Character.gold + 150
            print(f'Good job you won, you have gained $150 gold. Your gold is now {Character.gold}')
            
        

    elif player_choice == 'Scissors':
        if computer_choice == 'Rock':
            print ('You lose')
    elif computer_choice == 'Paper':
        print ('You win')
        Character.gold = Character.gold + 150
        print(f'Good job you won, you have gained $150 gold. Your gold is now {Character.gold}')
    

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
            Character.gold = Character.gold + real_base
            print(f'Good job, you typed this in {positive_t} seconds. You gained some gold. You now have {Character.gold}')
        elif positive_t >10:
            print('You were too slow. You do not get anything.')
    elif their_spelling != variable:
        Character.gold = Character.gold - 50
        print(f'you spelt it wrong nerd. You lost gold, you now have {Character.gold}')
                   
def gamble():
    while gamblingfr == True:
        print(f'You encounter, a GAMBLING MACHINE. You have {Character.gold} gold.')
        time.sleep(1)
        gamb = input('Would you like to GAMBLE? Y/N')
        if gamb == 'N':
            print('So be it.')
            break
        if gamb == 'Y':
            print('COMMENCE THE GAMBLING..')
            time.sleep(1)
            print('You encounter a slot machine.')
            slot = int(input('How much would you like to gamble?'))
            
            while slot > Character.gold:
                slot = int(input('Enter a gambling amount that you have.'))
                if slot <= Character.gold:
                    break

           
     
            print('Nice amount. YOU NOW SPIN THE SLOT MACHINE.')
            a_list = ['Gold', 'Junk','Diamond']
            slot1 = random.choice(a_list)
            slot2 = random.choice(a_list)
            slot3 = random.choice(a_list)
            slot_machine = [slot1,slot2,slot3]
            commence = Counter(slot_machine)
            if commence['Gold'] > 1:
                if commence['Gold'] == 3:
                    Character.gold = Character.gold + 3 * slot
                    print(f'You hit the 3 gold!, you now have {Character.gold}')
                    print(commence)
                    break
                else:
                    Character.gold = Character.gold + 50
                    print(f'You have won a little bit of gold. You now have {Character.gold}')
                    print(commence)
                    break
            if commence['Diamond'] > 1:
                if commence['Diamond'] == 3:
                    Character.gold = Character.gold + slot * 5
                    print(f'YOU HIT THE JACKPOT. YOU NOW HAVE {Character.gold}')
                    print(commence)
                    break
                else:
                    Character.gold = Character.gold + 75
                    print(f'You have won a little bit of gold. You now have {Character.gold}')
                    print(commence)
                    break
            if commence['Junk'] > 1:
                if commence['Junk'] == 3:
                    Character.gold = Character.gold - 150
                    print(f'You hit the junk jackpot nerd, you now have {Character.gold}')
                    print(commence)
                    break
                else:
                    Character.gold = Character.gold - 50
                    print(f'You lost a bit of gold... You now have {Character.gold}')
                    print(commence)
                    break
            else:
                print(commence)
                break
                    

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
        Character.gold = Character.gold + 100
        print(f'Correct, you now have {Character.gold}')
    else:
        Character.gold = Character.gold - 50
        print(f'The correct answer was...')
        print(the_question['answer'])
        print(f'Incorrect, you have lost gold... You now have {Character.gold}')

LysTurn = True
EnemiestURN = False
running = True
enemies = [NPC1,NPC2,NPC3,NPC4,NPC5,NPC6,NPC7]

puzzl = ["puzzle1","gamble","trivia","typing"]



def encounter():
    Character.energy_point = 3
    enemy = enemies[0]
    enemy.energy_point = 3
    while running:
        if LysTurn:
            print(f'{Character.Name}s Turn')
            Character.turn(enemy)
            print('-----------------------------------------')
            EnemiestURN = True
        if Character.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Character.add_gold(100)
            Character.HP = Character.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            print(f'{enemy.Name}s Turn')
            enemy.AI(Character)
            print('-----------------------------------------')
        else:
            LysTurn == True 
        if Character.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Character.add_gold(100)
            Character.HP = Character.max_HP
            enemies.remove(enemy)
            break

def shop():

    Character.preview_items()

def item():
    ok = random.choice(Character.inventory_items)
    print(f'You have found an {ok}')
    Character.inventory.append(ok)
    print(f'Your inventory is now {Character.inventory}')



def boss():
    print('You encounter a large foe, good luck.')
    Character.energy_point = 3
    enemy = Boss
    enemy.energy_point = 3
    while running:
        if LysTurn:
            Character.turn(enemy)
            EnemiestURN = True
        if Character.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Character.add_gold(1000)
            Character.HP = Character.max_HP
            enemies.remove(Boss)
            break
        if EnemiestURN:
            enemy.AI(Character)
        if Character.HP <= 0:
            print('You died')
            break
Character.name()
print("You are strolling around town, you can go to the shop or venture into the wilderness.")
start = "nogo"
first = input("(Shop/Explore)").capitalize()
Character.HP = Character.max_HP
Character.energy_point == 3
if first == "Shop":
    xy = input("(Enter 'Continue' to enter shop)").capitalize()
    while xy == "Continue" or xy == "Again":
        shop()
        xy = input("(Enter 'Again' to shop again, enter 'No' to continue exploring)").capitalize()
        if xy == "Again":
            xy == "Again"
        elif xy == "No":
            start = "go"
            break
elif first == "Explore":
    start = "go"
if start == "go":    
    print("You're exploring a forest near the village you started at. While exploring you encounter a monster, you can choose fight it or run away...")
ran = [1,2,3,4,4]
prs = [1,2]

coi = list(range(100,300))


def tatakae():
    if len(enemies) > 0:
        user_input = input("Do you choose to fight it or run way? (Fight/Run)").capitalize()
        if user_input == "Fight":
            print("You chose to fight the monster.")
            encounter()
        elif user_input == "Run":
            print("You thought I was feeling you, you aint running bi-")
            encounter()
        else:
            print("Don't matter if you can't spell you still gotta fight.")
            encounter()
def town():
    print("You're back in town what do you want to do?")
    buy = input("(Shop/Explore)").capitalize()
    Character.HP = Character.max_HP
    Character.energy_point == 3
    if buy == "Shop":
        x = input("(Enter 'Continue' to enter shop)").capitalize()
        while x == "Continue" or x == "Again":
            shop()
            x = input("(Enter 'Again' to shop again, enter 'No' to continue exploring)").capitalize()
            if x == "Again":
                x == "Again"
            elif x == "No":
                break
        print("You found another Monster.")
        tatakae()
        
    elif buy == "Explore":
        print("You found another Monster.")
        tatakae()
def paths():
    np = input("(Left/Right/Return)").capitalize()
    if np == "Left" :
        numb = random.choice(ran)
        if numb == 1:
            cooi = random.choice(coi)
            print("--------------------------------")
            print("You found a treasure chest!")
            Character.add_gold(cooi)
            item()
            item()
            print("And return to the town...")
            town()
        elif numb == 2:
            print("You found another Monster.")
            tatakae()
        elif numb == 3:
            item()
            item()
            item()
            item()
            print("Go deeper or retreat?")
            new_input = input("(Deeper/Return)").capitalize()
            if new_input == "Deeper":
                deep = random.choice(prs)
                if deep == 1:
                    cooi = random.choice(coi)
                    print("--------------------------------")
                    print("You found a treasure chest!")
                    Character.add_gold(cooi)
                    print("And return to the town...")
                    town()
                elif deep == 2:
                    print("You found another Monster.")
                    tatakae()
        elif numb == 4:
            puz = random.choice(puzzl)
            if puz == "puzzle1":
                puzzle1()
                puzzl.remove("puzzle1")
            elif puz == "typing":
                typing()
                puzzl.remove("typing")
            elif puz == "trivia":
                trivia()
                puzzl.remove("trivia")
            elif puz == "gamble":
                gamble()
                puzzl.remove("gamble")
            town()
    elif np == "Right" :
        numb = random.choice(ran)
        if numb == 1:
            cooi = random.choice(coi)
            print("--------------------------------")
            print("You found a treasure chest!")
            Character.add_gold(cooi)
            item()
            item()
            print("And return to the town...")
            town()
        elif numb == 2:
            print("You found another Monster.")
            tatakae()
        elif numb == 3:
            item()
            item()
            item()
            print("Go deeper or retreat?")
            new_input = input("(Deeper/Return)").capitalize()
            if new_input == "Deeper":
                deep = random.choice(prs)
                if deep == 1:
                    cooi = random.choice(coi)
                    print("--------------------------------")
                    print("You found a treasure chest!")
                    Character.add_gold(cooi)
                    print("And return to the town...")
                    town()
                elif deep == 2:
                    print("You found another Monster.")
                    tatakae()      
        elif numb == 4:
            puz = random.choice(puzzl)
            if puz == "puzzle1":
                puzzle1()
                puzzl.remove("puzzle1")
            elif puz == "typing":
                typing()
                puzzl.remove("typing")
            elif puz == "trivia":
                trivia()
                puzzl.remove("trivia")
            elif puz == "gamble":
                gamble()
                puzzl.remove("gamble")
            town()
            

        
    elif np == "Return":
        town()
tatakae()
while enemies != 0:
    if len(enemies) == 0:
        break
    if Character.HP >0:    
        while Character.HP >0:
            paths()
            if len(enemies) == 0:
                break
while len(enemies) == 0:
    print("You have cleared the forest and it summons a portal , do you with to return to the town one last time or go straight into the portal?")
    input_ = input("(Return/Enter)").capitalize()
    if input_ == "Return":
        print("You're back in town what do you want to do?")
        buy = input("(Shop/Explore)").capitalize()
        Character.HP = Character.max_HP
        if buy == "Shop":
            x = input("(Enter 'Continue' to enter shop)").capitalize()
            while x == "Continue" or x == "Again":
                shop()
                x = input("(Enter 'Again' to shop again, enter 'No' to continue exploring)").capitalize()
                if x == "Again":
                    x == "Again"
                elif x == "No":
                    break
                elif x[1:] == "A":
                    x == "Again"
                elif x[1:] == "N":
                    break  
            print("You go into the portal...")
            print("N/A")
    elif input_ == "Enter":
        print("you entered the portal")
        boss()
        break

