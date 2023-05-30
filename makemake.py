import random
import time
from collections import Counter
gamblingfr = True
match = False

class Player:
    Stone = 100
    Armor = 150
    Wand = 150
    Magic_Armor = 50
    items = ['Stone','Armor','Wand','Magic_Armor']
    inventory_items = ['Smoothie','Protein_Bar','Potion']
    Smoothie = 75
    Protein_Bar = 50
    Potion = 100
    noah_rozin = True
   
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
        print(f'{self.Name} has attacked {target.Name}. {target.Name} is {target.HP} HP and {self.Name} has {self.energy_point}energy points')
        print('')
        print('')
            
        

      



    def magic_dmg(self,target):
        if self.energy_point > 0:
            self.energy_point = self.energy_point - 1
            self.ultpoints = self.ultpoints + 1
            damage_taken = target.HP - self.magic_damage
            target.HP = damage_taken
            print(f'{self.Name} has magic attacked {target.Name}. {target.Name} is now {target.HP} HP and {self.Name} has {self.energy_point} energy points and {self.ultpoints} points')
            print('')
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
                print (f'{target.Name} is now {target.HP} HP and you have {self.ultpoints} ultimate points')
            elif t < -5:
                print('You have exceeded 5 seconds..')
                real_dmg = self.ultdmg
                nuke_taken = target.HP - real_dmg
                target.HP = nuke_taken
                self.ultpoints = 0
                print (f'{target.Name} is now {target.HP} HP and you have {self.ultpoints} ultimate points.')
                print('--------------------------------------------')
    def use_item(self):
        while self.noah_rozin == True:
            choicehm = input(f'You have chose to use an item, out of {self.inventory}, what item would you like to use? If you do not want to use an item, type N').capitalize()
            if 'Smoothie' in self.inventory:
                if choicehm == 'Smoothie':
                    self.HP = self.HP + self.Smoothie
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Smoothie')
            elif 'Protein_Bar' in self.inventory:
                if choicehm == 'Protein_Bar':
                    self.HP = self.HP + self.Protein_Bar
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Protein_Bar')
            elif 'Potion' in self.inventory:
                if choicehm == 'Potion':
                    self.HP = self.HP + self.Protein_Bar
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Potion')
            elif choicehm == 'N':
                break
            else:
                print('You do not have that item.')


        




    



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
        print('Stone: Cost: 50 gold. Buff: Increases Normal Attack by 100.')
        time.sleep(0.5)
        print('Wand: Cost: 200 Buff: Increases Magic Damage by 150 and Ultimate Damage by 200')
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
                if self.gold >= 200:
                    self.max_magicdmg = self.magic_damage + self.Wand
                    self.magic_damage = self.max_magicdmg
                    self.maxult = self.ultdmg + 200
                    self.ultdmg = self.maxult
                    print(f'{self.Name} magic damage is now {self.magic_damage} and your ultimate damage is now {self.ultdmg}')
                    self.gold = self.gold - 200
                    print(f'You now have {self.gold} gold')
        if weapon_choice == 'N':
            print('Ok cheapskate...')

    




      
        

Character = Player(300,"idk",50,3,100,int(100),150,100,50,10,500,[],500)





NPC1 = Player(1300,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC2 = Player(1500,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC3 = Player(1400,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC4 = Player(950,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC5 = Player(1000,"NPC",10,3,30,0,200,10,20,0,0,[],0)

Boss = Player(7000,"NPC",100,6,200,0,200,200,100,0,0,[],0)
#HP,Name,Damage,energy_point,magic_damage,gold,max_HP
from puzzle import typing, trivia, gamble, puzzle1



LysTurn = True
EnemiestURN = False
running = True
enemies = [NPC1,NPC2,NPC3,NPC4,NPC5]





def encounter():
    Character.energy_point = 3
    enemy = random.choice(enemies)
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
    print(Character.inventory)



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
ran = [4,4,4,4]
prs = [1,2]
puz = [1,2,3,4]
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
            which = random.choice(puz)
            if which == 1:
                gamble()
            elif which == 2:
                puzzle1()
            elif which == 3:
                typing()
            elif which == 4:
                trivia()
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
        elif numb == 2:
            print("You found another Monster.")
            tatakae()
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

