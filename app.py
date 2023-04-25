from PIL import Image
import random


class Player:
   
    def __init__(self,HP,Weapon,Name,Damage,energy_point,magic_point):
        self.HP = HP
        self.Weapon = Weapon
        self.Name = Name
        self.Damage = Damage
        self.magic_point = magic_point
        self.energy_point = energy_point
        


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
        print(f'{self.Name} HP is now {real_HP}')
        print('----------------------------')
        self.energy_point = self.energy_point + 1
    def magic_attack(self):
        self.Damage = self.Damage + 50
        self.magic_points - 1
        
    def revert_Damage(self):
        self.Damage = self.Damage
    def turn(self,target):
        user_input = input(f'{self.Name}s turn - Would you like to, Attack , Heal,or use a magic attack').capitalize()
        if user_input == 'Attack':
            self.attack(target)
        elif user_input == 'Heal':
            NPC.heal(Ly)
        elif user_input == 'Magic Attack':
            print('magic')
    def AI(self,target):
        self.list = ['Attack','Attack','Attack','Heal']
        get_lucky = random.choice(self.list)
        if get_lucky == 'Attack':
            self.attack(target)
            print('The NPC attacked you...')
        elif get_lucky == 'Heal':
            self.heal(Ly)
            print('The NPC Healed...')
        else:
            print('Ai sucks')




      
            
    
        
    
    
    






Ly = Player(100,"Sword","Lie Lee",50,3,1)

NPC = Player(500,"Sword","NPC",10,3,1)
LysTurn = True
EnemiestURN = False
""" Ly.turn(NPC)
print(NPC.HP)

NPC.turn(Ly)
print(Ly.HP) """


running = True
while running:
    if LysTurn:
        Ly.turn(NPC)
        
        EnemiestURN = True
    if Ly.HP <= 0 or NPC.HP <= 0:
        break

    if EnemiestURN:
        NPC.AI(Ly)
        
    else:
        LysTurn == True 
    if Ly.HP <= 0 or NPC.HP <= 0:
        break

       






  





