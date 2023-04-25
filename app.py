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
        damage_taken = target.HP - self.Damage
        target.HP = damage_taken

      
    def block(self,target):
        incoming_damage = target.Damage
        target.Damage = incoming_damage/2
        self.HP = self.HP - incoming_damage
    
        self.energy_point + 1
    def magic_attack(self):
        self.Damage = self.Damage + 50
        self.magic_points - 1
        
    def revert_Damage(self):
        self.Damage = self.Damage
    def turn(self,target):
        user_input = input(f'{self.Name}s turn - Would you like to, Attack , Block,or use a magic attack')
        if user_input == 'Attack':
            self.attack(target)
            #something.damage()
            print('attack')
            
        elif user_input == 'Block':
            NPC.block(Ly)
            print('block')
            #something.block()
            
        elif user_input == 'Magic Attack':
            print('magic')
            #something.magic_attack()
            
    
        
    
    
    






Ly = Player(100,"Sword","Lie Lee",50,3,1)

NPC = Player(1000,"Sword","NPC",1,3,1)
LysTurn = True
EnemiestURN = False
""" Ly.turn(NPC)
print(NPC.HP)

NPC.turn(Ly)
print(Ly.HP) """


running = True
while running == True:
    if LysTurn:
        Ly.turn(NPC)
        print(NPC.HP)
        EnemiestURN = True
    if EnemiestURN:
        NPC.turn(Ly)
        print(Ly.HP)
    else:
        LysTurn == True 

       






  





