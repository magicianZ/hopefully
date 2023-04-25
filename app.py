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
        target.incoming_damage = self.Damage

      
    def block(self,target):
        target.Damage = target.incoming_damage
        target.incoming_damage = target.incoming_damage/2
        self.energy_point + 1
    def magic_attack(self):
        self.Damage = self.Damage + 50
        self.magic_points - 1
        
    def revert_Damage(self):
        self.Damage = self.Damage
    def turn(self):
        user_input = input('Would you like to, Attack , Block,or use a magic attack')
        if user_input == 'Attack':
            Ly.attack(NPC)
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

NPC = Player(1000,"Sword","Lie Lee",1,3,1)
LysTurn = True
EnemiestURN = False

def Lygoturn():
    if LysTurn:
        Ly.turn()
        print('Ly Turn')
        EnemiestURN = True
    elif EnemiestURN:
        NPC.turn()
        print('Npc turn')
    else:
        LysTurn == True
def NPCgoturn():
    global LysTurn
    if EnemiestURN:
        NPC.turn()
        print('Npc Turn')
        LysTurn = True
    elif LysTurn:
        Ly.turn()
        print('Ly Turn')
    else:
        EnemiestURN == True



running = True
while running == True:
    
    Lygoturn()



       






  





