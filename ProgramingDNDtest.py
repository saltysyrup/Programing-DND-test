from random import *

# HELPER FUNCTION
def rolldice (sides):
    return randint(1,sides)

# ROOT OF HEIRARCHY
class LB: # Living Being
    def __init__(self,weapon,HP):
        players = []
        
        self.weapon = weapon
        self.HP = HP #Health Points

        Priority = 'ERROR - This shouldn't be printed'
        Target = 'ERROR - please dont print'
        Side='ERROR - Hope this doesnt print'
        
    def attack (weapon):
        damage = 'ERROR - who printed this?'
        return damage

# LEVEL 1 - Weapon Types
class Range(LB):
    def __init__(self):
        LB.Priority=1
        LB.Target='Melee'
class Melee(LB):
    def __init__(self):
        LB.Priority=2
        LB.Target='Magic'
class Magic(LB):
    def __init__(self):
        LB.Priority=3
        LB.Target='Range'
# LEVEL ???
class Good:
    def __init__(self):
        Gold = 'ERROR - this better not print'
    def declare:
        print ('I am good')
        
class Evil:
    def declare:
        print ('I am evil')
        
# LEVEL 2 - Players
class Dwarf(Melee,Good):
    def __init__(self):
        LB.players.append(Dwarf)
        Good.Gold = 10
        HP=100
    def attack:
        return rolldice(25)
    
class Wizard(Magic,Good):
    def __init__(self):
        LB.players.append(Wizard)
        Good.Gold = 10
        HP=100
    def attack:
        return rolldice(50)
    
# LEVEL 2 - Monsters
class Spidr(Range,Evil):
    def __init__(self):
        HP = 60
    def attack:
        return rolldice(15)
class Slime(Melee,Evil):
    def __init__(self):
        HP = 25
    def attack:
        return rolldice(30)
class Witch(Magic,Evil):
    def __init__(self):
        HP = 30
    def attack:
        return rolldice(40)

RoundNum = 0
ON = True
while ON:
    RoundNum += 1
    ec = rolldice(2) #EncounterChance
    if ec == 1:
        for i in LB.players:
            i.HP += 10
    if ec == 2:
        ec = rolldice(3)
        if ec == 1:
            Fight Monsters
            
        if ec == 2:
            fg = rolldice(0,100) #found gold
            Dwarf.Gold += (fg/2)
            Wizard.Gold +=
        if ec == 3:
            fp = rolldice(0,100) #found potion

    DisplayUpdates()







