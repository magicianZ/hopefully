import random
import time

class Player:
    Sharpening_Stone = 50
    Armor = 50
    Wand = 100
    Magic_Armor = 50
    items = ['Sharpening_Stone','Armor','Wand','Magic_Armor']
    inventory_items = ['Smoothie','Protein_Bar','Potion']
    Smoothie = 50
    Protein_Bar = 30
    Potion = 20
    noah_rozin = True
   
    def __init__(self,HP,Name,Damage,energy_point,magic_damage,gold,max_HP,max_magicdmg,max_attack,ultpoints,ultdmg,inventory):
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
            self.ultpoints = 0
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
                print(real_dmg)
                print (f'{target.Name} is now {target.HP} HP')
            elif t < -5:
                print('You have exceeded 5 seconds..')
                real_dmg = self.ultdmg
                nuke_taken = target.HP - real_dmg
                target.HP = nuke_taken
                print (f'{target.Name} is now {target.HP} HP')
                print('--------------------------------------------')
    def use_item(self):
        while self.noah_rozin == True:
            choicehm = input(f'You have chose to use an item, out of {self.inventory}, what item would you like to use? If you do not want to use an item, type N')
            if 'Smoothie' in self.inventory:
                if choicehm == 'Smoothie':
                    self.HP = self.HP + self.Smoothie
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Smoothie')
            if 'Protein_Bar' in self.inventory:
                if choicehm == 'Protein_Bar':
                    self.HP = self.HP + self.Protein_Bar
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Protein_Bar')
            if 'Potion' in self.inventory:
                if choicehm == 'Potion':
                    self.HP = self.HP + self.Protein_Bar
                    print(f'{self.Name} is now {self.HP} HP.')
                    self.inventory.remove('Potion')
            if choicehm == 'N':
                break
            else:
                print('You do not have that item.')


        




    



    def turn(self,target):
        print('---------------------------------------------------')
        user_input = input(f'{self.Name}s turn - Would you like to - Regular Attack | Magic Attack | Ultimate or Use an Item. To Regular Attack type "Attack" , to Magic Attack type "Magic" to Ultimate type "Ult" to Use an Item, type "Item').capitalize()
        
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
        print(f'Welcome to the shop, our items are {self.items}')
        print('Sharpening stone increases your damage by 10, Armor increases your HP by 50, Magic Armor increases your magic health by 50 and the wand increases your magic damage by 100')
        weapon_choice = input('Would you like to buy anything? Y/N').capitalize()
        if weapon_choice == 'Y':
            what_item = input('What item would you like to buy?').capitalize()
            if what_item == 'Sharpening_Stone':
                if self.gold >= 75:
                    self.max_attack = self.Damage + self.Sharpening_Stone
                    print(f'{self.Name} damage is now {self.Damage}')
                    self.Damage = self.max_attack
                    self.gold = self.gold - 75
              
            if what_item == 'Armor':
                if self.gold >= 50:
                    self.max_HP = self.max_HP + self.Armor
                    print(f'{self.Name} HP is now {self.max_HP}')
                    self.HP = self.max_HP
                    self.gold = self.gold - 50
                  
            if what_item == 'Wand':
                if self.gold >= 100:
                    self.max_magicdmg = self.magic_damage + self.Wand
                    print(f'{self.Name} magic damage is now {self.magic_damage}')
                    self.gold = self.gold - 100
                    self.magic_damage = self.max_magicdmg
            if self.gold <= 0:
                print('You have no gold, brokie...')
        if weapon_choice == 'N':
            print('Ok cheapskate...')
    def selling(self):
        print(f'It seems you have {self.inventory}')
        sell = input('Do you wish to sell?')
        if sell == 'Y':
            the_Sell = input('Would you like to sell, ALL YOUR ITEMS? Y or N')
            if the_Sell == 'Y':
                length = len(self.inventory)
                final_cost = 50 * length
                self.gold =  self.gold + final_cost
                self.inventory.clear()
                print(self.inventory)
                print(self.gold)
                print(f'Your gold is now {self.gold}')
            if the_Sell == 'N':
                print('Goodbye')
        

        if sell == 'N':
            print('Ok then, goodbye!')

    





      
        

Character = Player(150,"idk",50,3,100,100,150,100,50,10,500,[])
NPC1 = Player(400,"NPC",10,3,20,0,200,10,20,0,0,[])
NPC2 = Player(500,"NPC",10,3,20,0,200,10,20,0,0,[])
NPC3 = Player(550,"NPC",10,3,20,0,200,10,20,0,0,[])
#HP,Name,Damage,energy_point,magic_damage,gold,max_HP




LysTurn = True
EnemiestURN = False
running = True
enemies = [NPC1,NPC2,NPC3]





def encounter():
    Character.energy_point = 3
    enemy = random.choice(enemies)
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
            Character.add_gold(12)
            Character.HP = Character.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            enemy.AI(Character)
        else:
            LysTurn == True 
        if Character.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Character.add_gold(12)
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

print("You are strolling around town, you can go to the shop or venture into the wilderness.")
start = "nogo"
first = input("(Shop/Explore)").capitalize()
Character.HP = Character.max_HP
Character.energy_point == 3
if first == "Shop":
    xy = "Continue"
    while xy[0] == "C":
        xy = input("(Enter 'Continue' to enter shop)").capitalize()
        shop()
        xy = input("(Enter 'Again' to shop again, enter 'No' to continue exploring)").capitalize()
        if xy == "Again":
            xy  == "Continue"
        elif xy  == "No":
            break
elif first == "Explore":
    start = "go"
if start == "go":    
    print("You're exploring a forest near the village you started at. While exploring you encounter a monster, you can choose fight it or run away...")
ran = [1,2,3]
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
        x = "Continue"
        while x[0] == "C":
            x = input("(Enter 'Continue' to enter shop)").capitalize()
            shop()
            x = input("(Enter 'Again' to shop again, enter 'No' to continue exploring)").capitalize()
            if x == "Again":
                x == "Continue"
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
            print("And return to the town...")
            town()
        elif numb == 2:
            print("You found another Monster.")
            tatakae()
        elif numb == 3:
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
    elif np == "Right" :
        numb = random.choice(ran)
        if numb == 1:
            cooi = random.choice(coi)
            print("--------------------------------")
            print("You found a treasure chest!")
            Character.add_gold(cooi)
            print("And return to the town...")
            town()
        elif numb == 2:
            print("You found another Monster.")
            tatakae()
        elif numb == 3:
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
    elif np == "Die":
        print("""||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||                      ||||||      ||||||||||      ||||||                      ||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||                      ||||||      ||||||||      ||||||||                      ||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||     |||||||||||||||||||||||      ||||||      ||||||||||||||||||      ||||||||||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||     |||||||||||||||||||||||      ||||      ||||||||||||||||||||      ||||||||||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||                      ||||||              ||||||||||||||||||||||      ||||||||||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||                      ||||||              ||||||||||||||||||||||      ||||||||||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||||||||||||||||||      ||||||      ||||      ||||||||||||||||||||      ||||||||||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||||||||||||||||||      ||||||      ||||||      ||||||||||||||||||      ||||||||||||||      ||||||||||||||||||||||      ||||||||||||||||||||||
||||||                      ||||||      ||||||||      ||||||||                      ||||||                      ||||||                      ||||||
||||||                      ||||||      ||||||||||      ||||||                      ||||||                      ||||||                      ||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||                      ||||||                      ||||||                      ||||||      ||||||||||      ||||||                      ||||||
||||||                      ||||||                      ||||||                      ||||||      ||||||||||      ||||||                      ||||||
||||||||||||||      ||||||||||||||     |||||||||||||||||||||||     |||||||||||||||||||||||      ||||||||||      ||||||      ||||||||||||||||||||||
||||||||||||||      ||||||||||||||     |||||||||||||||||||||||     |||||||||||||||||||||||      ||||||||||      ||||||      ||||||||||||||||||||||
||||||||||||||      ||||||||||||||                      ||||||                      ||||||      ||||||||||      ||||||                  ||||||||||
||||||||||||||      ||||||||||||||                      ||||||                      ||||||      ||||||||||      ||||||                  ||||||||||
||||||||||||||      ||||||||||||||||||||||||||||||      ||||||||||||||||||||||      ||||||      ||||||||||      ||||||      ||||||||||||||||||||||
||||||||||||||      ||||||||||||||||||||||||||||||      ||||||||||||||||||||||      ||||||      ||||||||||      ||||||      ||||||||||||||||||||||
||||||                      ||||||                      ||||||                      ||||||                      ||||||                      ||||||
||||||                      ||||||                      ||||||                      ||||||                      ||||||                      ||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||""")
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
            x = "Continue"
            while x == "Continue":
                x = input("(Enter 'Continue' to enter shop)").capitalize()
                shop()
                x = input("(Enter 'Again' to shop again, enter 'No' to continue exploring)").capitalize()
                if x == "Again":
                    x == "Continue"
                elif x == "No":
                    break
            print("You go into the portal...")
            print("N/A")
    elif input_ == "Enter":
        print("you entered the portal")
        break

