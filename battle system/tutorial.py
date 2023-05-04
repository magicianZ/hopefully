
import random
win = False
def puzzle1():
    choices = ['Rock','Paper','Scissors']

    player_choice = input("Rock paper scissors, what do you pick?").capitalize()
    computer_choice = "Scissors"

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
      




class Player:
    Sharpening_Stone = 50
    Armor = 50
    Wand = 100
    Magic_Armor = 50
    items = ['Sharpening_Stone','Armor','Wand','Magic_Armor']
   
    def __init__(self,HP,Name,Damage,energy_point,magic_damage,gold,max_HP):
        self.HP = HP
        
        self.Name = Name
        self.Damage = Damage
        self.energy_point = energy_point
        self.magic_damage = magic_damage

        self.gold = gold
        self.max_HP = max_HP


    def attack(self,target):
        damage_taken = target.HP - self.Damage
        target.HP = damage_taken
        self.energy_point = self.energy_point + 1
        print(f'{target.Name} is {target.HP} HP and you have {self.energy_point}energy points')
        print('-----------------------------')
            
        

      



    def magic_dmg(self,target):
        if self.energy_point > 0:
            damage_taken = target.HP - self.magic_damage
            target.HP = damage_taken
            print(f'{target.Name} is now {target.HP} HP and you have {self.energy_point} energy points ')
            print('-----------------------------')
            self.energy_point = self.energy_point - 1
        else:
            print('Recover energy')
      
    



    def turn(self,target):
        user_input = input(f'{self.Name}s turn - Would you like to - Attack or Magic').capitalize()
        if user_input == 'Attack':
            self.attack(target)
        elif user_input == 'Magic':
            self.magic_dmg(target)





    def AI(self,target):
        self.list = ['Attack','Attack','Attack']
        get_lucky = random.choice(self.list)
        if self.energy_point > 0:
                self.magic_dmg(Ly)
                print('The NPC attacked you...')
        elif self.energy_point == 0:
                self.attack(Ly)
             
       
          

    def add_gold(self,amount):
        self.gold = self.gold + amount
        print(f'{self.Name} now has {self.gold} gold')




    def preview_items(self):
        print(f'Welcome to the shop, our items are {self.items}')
        print('Sharpening stone increases your damage by 10, Armor increases your HP by 50, Magic Armor increases your magic health by 50 and the wand increases your magic damage by 100')
        weapon_choice = input('Would you like to buy anything? Y/N').capitalize()
        if weapon_choice == 'Y':
            what_item = input('What item would you like to buy?').capitalize()
            if what_item == 'Sharpening_Stone':
                if self.gold >= 10:
                    self.Damage = self.Damage + self.Sharpening_Stone
                    print(f'{self.Name} damage is now {self.Damage}')
              
            if what_item == 'Armor':
                if self.gold >= 10:
                    self.max_HP = self.max_HP + self.Armor
                    print(f'{self.Name} HP is now {self.max_HP}')
                    self.HP = self.max_HP
                  
            if what_item == 'Wand':
                if self.gold >= 10:
                    self.magic_damage = self.magic_damage + self.Wand
                    print(f'{self.Name} magic damage is now {self.magic_damage}')
                  

            


        if weapon_choice == 'N':
            print('Ok cheapskate...')
    
    
    def puzzle(self):
        print('Welcome to my lair fool, you must complete 1 game against me to get past.')





      
        

Ly = Player(100,"Lie Lee",50,3,100,100,100)
NPC1 = Player(200,"NPC",10,3,20,0,200)
NPC2 = Player(500,"NPC",10,3,20,0,200)
NPC3 = Player(1000,"NPC",10,3,20,0,200)
#HP,Name,Damage,energy_point,magic_damage,gold,max_HP




LysTurn = True
EnemiestURN = False
running = True
enemies = [NPC1,NPC2,NPC3]





def encounter():
    enemy = random.choice(enemies)
    while running:
        if LysTurn:
            Ly.turn(NPC1)
            EnemiestURN = True
        if Ly.HP <= 0:
            print('You died')
            break
        if NPC1.HP <=0:
            print('You won, the Mob died')
            Ly.add_gold(12)
            Ly.HP = Ly.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            NPC1.AI(Ly)
        else:
            LysTurn == True 
        if Ly.HP <= 0:
            print('You died')
            break
        if NPC1.HP <= 0:
            print('You won, the Mob died')
            Ly.add_gold(12)
            Ly.HP = Ly.max_HP
            enemies.remove(enemy)
            break
        
def shop():

    Ly.preview_items()


print('Welcome to the tutorial, I will show you how to play the game.')
print('---------------------------------')
print('The attack system, you have basic attacks and magic attacks. Magic attacks require energy to pull off, if you do not have an energy point use an attack to gain one. If you use a magic attack with no energy points you will flail in exhaustation and your turn will be skipped. You will fight against monsters and they will fight you back, the HP of your character will be displayed. Now try against an monster.')
encounter()
print('Great job in your first battle, but it gets harder from here...')
question = input('Would you look to go Left or Right')
if question == 'Left' or 'Right':
    puzzle1()
else:
    print('You encounter a puzzle')
    puzzle1()
if win == True:
    print('You beat me... I guess you can continue.')






