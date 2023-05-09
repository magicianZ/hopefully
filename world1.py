from PIL import Image
import random

class Player:
    Sharpening_Stone = 50
    Armor = 50
    Wand = 100
    Magic_Armor = 50
    items = ['Sharpening_Stone','Armor','Wand','Magic_Armor']
   
    def __init__(self,HP,Name,Damage,energy_point,magic_damage,gold,max_HP,max_magicdmg,max_attack):
        self.HP = HP
        
        self.Name = Name
        self.Damage = Damage
        self.energy_point = energy_point
        self.magic_damage = magic_damage
        self.max_attack = max_attack
        self.max_magicdmg = max_magicdmg
        self.gold = gold
        self.max_HP = max_HP


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
            damage_taken = target.HP - self.magic_damage
            target.HP = damage_taken
            print(f'{self.Name} has magic attacked {target.Name}. {target.Name} is now {target.HP} HP and {self.Name} has {self.energy_point} energy points ')
            print('')
            print('')
        else:
            print('Recover energy')
      
    



    def turn(self,target):
        print('---------------------------------------------------')
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
    





      
        

Ly = Player(100,"Lie Lee",50,3,100,100,100,100,50)
NPC1 = Player(200,"NPC",10,3,20,0,200,10,20)
NPC2 = Player(500,"NPC",10,3,20,0,200,10,20)
NPC3 = Player(1000,"NPC",10,3,20,0,200,10,20)
#HP,Name,Damage,energy_point,magic_damage,gold,max_HP




LysTurn = True
EnemiestURN = False
running = True
enemies = [NPC1,NPC2,NPC3]





def encounter():
    Ly.energy_point = 3
    enemy = random.choice(enemies)
    enemy.energy_point = 3
    while running:
        if LysTurn:
            Ly.turn(enemy)
            EnemiestURN = True
        if Ly.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Ly.add_gold(12)
            Ly.HP = Ly.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            enemy.AI(Ly)
        else:
            LysTurn == True 
        if Ly.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Ly.add_gold(12)
            Ly.HP = Ly.max_HP
            enemies.remove(enemy)
            break