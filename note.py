
import random


class Player:
    def __init__(self,HP,Weapon,Name,Damage):
        self.HP = HP
        self.Weapon = Weapon
        self.Name = Name
        self.Damage = Damage

    def parry(self):
        parry1 = [1,2]
        chance = random.choice(parry1)
        if chance == 2:
            print('You parried')
        else:
            print('You got hit...')
            self.HP = self.HP - self.Damage

        return chance
    def damage(self):
        chance = self.parry()
        if chance != 2:
            self.Damage = self.HP - self.Damage






Ly = Player(100,"Sword","Lie Lee",1)

Ly.parry()
Ly.damage()
print(Ly.HP)