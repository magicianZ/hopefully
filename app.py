from PIL import Image
import random


class Player:
   
    def __init__(self,HP,Weapon,Name,Damage,energy_point,magic_point,magic_damage):
        self.HP = HP
        self.Weapon = Weapon
        self.Name = Name
        self.Damage = Damage
        self.magic_point = magic_point
        self.energy_point = energy_point
        self.magic_damage = magic_damage


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




      
        

Ly = Player(100,"Sword","Lie Lee",50,3,1,100)
NPC = Player(200,"Sword","NPC",10,3,1,20)


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
            break
encounter()

       






  





