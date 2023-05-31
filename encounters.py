import random


class Player:
    Sharpening_Stone = 50
    Armor = 50
    Wand = 100
    Magic_Armor = 50
    items = ['Sharpening_Stone','Armor','Wand','Magic_Armor']
   
    def __init__(self,HP,Weapon,Name,Damage,energy_point,magic_point,magic_damage,magic_health,gold):
        self.HP = HP
        self.Weapon = Weapon
        self.Name = Name
        self.Damage = Damage
        self.magic_point = magic_point
        self.energy_point = energy_point
        self.magic_damage = magic_damage
        self.magic_health = magic_health
        Character.gold = gold


    def attack(self,target):
        if self.energy_point > 0:
            damage_taken = target.HP - self.Damage
            target.HP = damage_taken
            self.energy_point = self.energy_point - 1
            print(f'{target.Name} is {target.HP} HP and you have {self.energy_point}energy points')
            print('-----------------------------')
            
        else:
            print('You got no energy points, you need to heal homie')

      
    def heal(self,target):
        real_HP = self.HP + 25
        self.HP = real_HP
        self.energy_point = self.energy_point + 1
        self.magic_point = self.magic_point = 0.5
        print(f'{self.Name} HP is now {real_HP} and {self.Name} have {self.energy_point}energy points')
        print('----------------------------')
    
        
    def magic_dmg(self,target):
        if self.magic_point > 0:
            damage_taken = target.HP - self.magic_damage
            target.HP = damage_taken
            self.magic_point = self.magic_point - 1
            print(f'{target.Name} is {target.HP} HP and you have {self.magic_point}magic points')
            print('-----------------------------')
        else:
            print('You got no magic points homie')

    
            
    def turn(self,target):
        user_input = input(f'{self.Name}s turn - Would you like to - Attack , Heal or Magic').capitalize()
        if user_input == 'Attack':
            self.attack(target)
        elif user_input == 'Heal':
            self.heal(target)
        elif user_input == 'Magic':
            self.magic_dmg(target)



    def AI(self,target):
        self.list = ['Attack','Attack','Attack']
        get_lucky = random.choice(self.list)
        if self.energy_point > 0:
             if get_lucky == 'Attack':
                self.attack(target)
                print('The NPC attacked you...')
        elif self.energy_point == 0:
            if get_lucky == 'Attack':
                self.heal(Ly)
             
            if get_lucky == 'Heal':
                self.heal(Ly)
                print('The NPC Healed...')
            else:
                print('Ai sucks')

    def add_gold(self,amount):
        Character.gold = Character.gold + amount
        print(f'{self.Name} now has {Character.gold} gold')

    def preview_items(self):
        print(f'Welcome to the shop, our items are {self.items}')
        print('Sharpening stone increases your damage by 10, Armor increases your HP by 50, Magic Armor increases your magic health by 50 and the wand increases your magic damage by 100')
        weapon_choice = input('Would you like to buy anything? Y/N').capitalize()
        if weapon_choice == 'Y':
            what_item = input('What item would you like to buy?')
            if what_item == 'Sharpening_Stone':
                if Character.gold >= 10:
                    self.Damage = self.Damage + self.Sharpening_Stone
                    print(self.Damage)
              
            if what_item == 'Armor':
                if Character.gold >= 10:
                    self.HP = self.HP + self.Armor
                    print(self.HP)
                  
            if what_item == 'Wand':
                if Character.gold >= 10:
                    self.magic_damage = self.magic_damage + self.Wand
                    print(self.magic_damage)
                  
            if what_item == 'Magic_Armor':
                if Character.gold >= 10:
                    self.magic_health = self.magic_health + self.Magic_Armor
                    print(self.magic_health)
            


        if weapon_choice == 'N':
            print('Ok cheapskate...')





      
        

Ly = Player(100,"Sword","Lie Lee",50,3,1,100,50,100)
NPC = Player(200,"Sword","NPC",10,3,1,20,100,0)


LysTurn = True
EnemiestURN = False
running = True



def encounter():
    while running:
        if LysTurn:
            Ly.turn(NPC)
        
            EnemiestURN = True
        if Ly.HP <= 0:
            print('You died')
            break
        if NPC.HP <=0:
            print('You won, the Mob died')
            Ly.add_gold(12)
            break


        if EnemiestURN:
            NPC.AI(Ly)
        
        else:
            LysTurn == True 
        if Ly.HP <= 0:
            print('You died')
            break
        if NPC.HP <=0:
            print('You won, the Mob died')
            Ly.add_gold(12)
            break
def shop():

    Ly.preview_items()


print("You're exploring a forest near the village you started at. While exploring you encounter a monster, you can choose fight it or run away...")
ran = [1,2,3]
prs = [1,2]
coi = [10,11,12,13,14,15,16,17,18]


def tatakae():
    if user_input == "Fight":
        print("You chose to fight the monster.")
        encounter()
    elif user_input == "Run":
        print("Nah you ain't running, go fight that thing.")
        encounter()
    else:
        print("Don't matter if you can't spell you still gotta fight.")
        encounter()
user_input = input("Do you choose to fight it or run way? (Fight/Run)").capitalize()
tatakae()
def paths():
    np = input("(Left/Right/Return)").capitalize()
    if np == "Left" :
        numb = random.choice(ran)
        if numb == 1:
            cooi = random.choice(coi)
            print("--------------------------------")
            print("You found a treasure chest!")
            Ly.add_gold(cooi)
            print("") 
        elif numb == 2:
            print("You found another Monster. (Fight/Run)")
            tatakae()     
    elif np == "Right" :
        numb = random.choice(ran)
        while numb == 1:
            cooi = random.choice(coi)
            print("--------------------------------")
            print("You found a treasure chest!")
            Ly.add_gold(cooi)
            if numb != 1:
                break
        while numb == 2:
            print("You found another Monster. (Fight/Run)")
            tatakae()
            if numb != 2:
                break
    elif np == "Return":
        Ly.HP == 100
        print(Ly.HP)
        
if NPC.HP <= 0:
    paths()
    NPC.HP == 200






