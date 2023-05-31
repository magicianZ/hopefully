import random
import time

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
        Character.gold = gold
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
                self.magic_dmg(Tutorial)
        elif self.energy_point == 0:
                self.attack(Tutorial)
             
       
          

    def add_gold(self,amount):
        Character.gold = Character.gold + amount
        print(f'{self.Name} now has {Character.gold} gold')




    def preview_items(self):
        print('Welcome to the shop')
        print(f'I see you have, {Character.gold} gold.')
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
            if Character.gold <= 0:
                print('You have no gold, brokie...')
            if what_item == 'Stone':
                if Character.gold >= 50:
                    self.max_attack = self.Damage + self.Stone
                    self.Damage = self.max_attack
                    print(f'{self.Name} damage is now {self.Damage}')
                    Character.gold = Character.gold - 50
                    print(f'You now have {Character.gold} gold')
              
            if what_item == 'Armor':
                if Character.gold >= 100:
                    self.max_HP = self.max_HP + self.Armor
                    self.HP = self.max_HP
                    print(f'{self.Name} HP is now {self.max_HP}')
                    time.sleep(0.5)
                    print('Take an item for your troubles!')
                    time.sleep(0.3)
                    item()
                    Character.gold = Character.gold - 100
                    print(f'You now have {Character.gold} gold')
                  
            if what_item == 'Wand':
                if Character.gold >= 200:
                    self.max_magicdmg = self.magic_damage + self.Wand
                    self.magic_damage = self.max_magicdmg
                    self.maxult = self.ultdmg + 200
                    self.ultdmg = self.maxult
                    print(f'{self.Name} magic damage is now {self.magic_damage} and your ultimate damage is now {self.ultdmg}')
                    Character.gold = Character.gold - 200
                    print(f'You now have {Character.gold} gold')
        if weapon_choice == 'N':
            print('Ok cheapskate...')

    





      
        

Tutorial = Player(150,"You",50,3,100,100,150,100,50,10,500,[],500)
NPC1 = Player(50,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC2 = Player(100,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC3 = Player(500,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC4 = Player(50,"NPC",10,3,30,0,200,10,20,0,0,[],0)
NPC5 = Player(1000,"NPC",10,3,30,0,200,10,20,0,0,[],0)

Boss = Player(7000,"NPC",100,6,200,0,200,200,100,0,0,[],0)
#HP,Name,Damage,energy_point,magic_damage,gold,max_HP




LysTurn = True
EnemiestURN = False
running = True
enemies = [NPC1,NPC2,NPC3,NPC4,NPC5]





def encounter():
    Tutorial.energy_point = 3
    enemy = NPC1
    enemy.energy_point = 3
    while running:
        if LysTurn:
            print(f'{Tutorial.Name}s Turn')
            Tutorial.turn(enemy)
            print('-----------------------------------------')
            EnemiestURN = True
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            print(f'{enemy.Name}s Turn')
            enemy.AI(Tutorial)
            print('-----------------------------------------')
        else:
            LysTurn == True 
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break

def encounter2():
    Tutorial.energy_point = 3
    enemy = NPC2
    enemy.energy_point = 3
    while running:
        if LysTurn:
            print(f'{Tutorial.Name}s Turn')
            Tutorial.turn(enemy)
            print('-----------------------------------------')
            EnemiestURN = True
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            print(f'{enemy.Name}s Turn')
            enemy.AI(Tutorial)
            print('-----------------------------------------')
        else:
            LysTurn == True 
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break

def encounter3():
    Tutorial.energy_point = 3
    enemy = NPC3
    enemy.energy_point = 3
    while running:
        if LysTurn:
            print(f'{Tutorial.Name}s Turn')
            Tutorial.turn(enemy)
            print('-----------------------------------------')
            EnemiestURN = True
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            print(f'{enemy.Name}s Turn')
            enemy.AI(Tutorial)
            print('-----------------------------------------')
        else:
            LysTurn == True 
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break

def encounter4():
    Tutorial.energy_point = 3
    enemy = NPC4
    enemy.energy_point = 3
    while running:
        if LysTurn:
            print(f'{Tutorial.Name}s Turn')
            Tutorial.turn(enemy)
            print('-----------------------------------------')
            EnemiestURN = True
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <=0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break
        if EnemiestURN:
            print(f'{enemy.Name}s Turn')
            enemy.AI(Tutorial)
            print('-----------------------------------------')
        else:
            LysTurn == True 
        if Tutorial.HP <= 0:
            print('You died')
            break
        if enemy.HP <= 0:
            print('You won, the Mob died')
            Tutorial.add_gold(100)
            Tutorial.HP = Tutorial.max_HP
            enemies.remove(enemy)
            break

def shop():

    Tutorial.preview_items()

def item():
    ok = random.choice(Tutorial.inventory_items)
    print(f'You have found an {ok}')
    Tutorial.inventory.append(ok)
    print(Tutorial.inventory)


print('Welcome to the tutorial nerd')
time.sleep(1)
print('I will teach you how to play the game.')
time.sleep(1)
print('You have multiple mechanics, but I will teach you how to basic attack first.')
time.sleep(1)
print('You are going to be in an encounter, type "Attack"')
input('Type when you are ready.')
encounter()
time.sleep(2)
print('A basic attack does 50 damage and regenerates 1 ENERGY POINT')
time.sleep(3)
print('You will now learn Magic Attacks, a magic attack will take up 1 energy point, (you start off with 3). You regenerate energy points by attacking. If you use a Magic Attack with no energy points, your turn will be skipped. Now type "Magic"')
input('Type when you are ready.')
encounter2()
time.sleep(3)
print('Magic attacks make you lose 1 energy point and deal 100 damage.')
time.sleep(3)
print('You will now learn how to ultimate, you start off with 5 ultimate points (5 ultimate points are required to use an ultimate)\n If you use the Ultimate with no ultimate points, your turn will be skipped.To generate ultimate points, you get 1 ultimate point everytime you magic attack')
time.sleep(2)
print('To use the ultimate, type "Ult". When you use an ultimate, you will have a timer where you have to type f as much as you can in 5 seconds.')
time.sleep(4)
print('The amount of times you press f is added to your ultimate damage.')
time.sleep(2)
print('If you exceed 5 seconds of pressing F, the damage addition will not count. Use your own judgement.')
input('Type when you are ready.')
encounter3()
time.sleep(4)
print('Throughout your journeies, you will find items, I will show you how to use items, but first let me give you one.')
item()
time.sleep(2)
print('To use an item, type "Item" in the encounter and then type the name of the item you will be using.')
time.sleep(1)
print('After you use the item, kill off the enemy with the attacks you have learned.')
input('Type when you are ready.')
encounter4()
time.sleep(2)
print('You might have noticed that you gain gold upon killing enemies. You can use this gold in the shop.')
time.sleep(1)
print('Buy stuff from the shop!')
time.sleep(2)
shop()
print('This is all you need to know, now use this experience in your adventure.')
