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

    def attack(self):
        self.HP = self.HP - self.Damage
        self.energy_point = self.energy_point - 1
    def block(self):
        self.Damage = self.Damage/2
        self.energy_point + 1
    def magic_attack(self):
        self.Damage = self.Damage + 50
        self.magic_points - 1
        
    def revert_Damage(self):
        self.Damage = self.Damage
    def turn(self):
        user_input = input('Would you like to, Attack , Block,or use a magic attack')
        while user_input == 'Attack':
            #something.damage()
            break
        while user_input == 'Block':
            #something.block()
            break
        while user_input == 'Magic Attack':
            #something.magic_attack()
            break
    
        
    
    
    






Ly = Player(100,"Sword","Lie Lee",1,3,1)
Ly.attack()
print(Ly.HP)
print(Ly.energy_point)



