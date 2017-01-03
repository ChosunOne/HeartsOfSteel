import random

class Division:
    def __init__(self, name, regiments, effectiveness = 1):
        self.name = name
        self.manpower = sum([x.manpower for x in regiments])
        self.maxManpower = self.manpower
        self.organization = sum([x.organization for x in regiments]) / len(regiments)
        self.maxOrganization = self.organization
        self.width = sum([x.width for x in regiments])
        self.softAttack = sum([x.softAttack for x in regiments])
        self.hardAttack = sum([x.hardAttack for x in regiments])
        self.piercing = max([x.piercing for x in regiments])
        self.armor = max([x.armor for x in regiments])
        self.airAttack = sum([x.airAttack for x in regiments])
        self.defensiveness = sum([x.defensiveness for x in regiments])
        self.toughness = sum([x.toughness for x in regiments])
        self.airDefense = sum([x.airDefense for x in regiments])
        self.softness = sum([x.softness for x in regiments]) / len(regiments)
        self.regiments = regiments
        
        self.effectiveness = effectiveness
        self.receivedHits = 0
        self.effectiveness = 1

        # Terrain Modifiers
        # Attack
        numRegs = len(regiments)
        self.woodsAttack = sum([x.woodsAttack for x in regiments]) / numRegs
        self.forestAttack = sum([x.forestAttack for x in regiments]) / numRegs
        self.jungleAttack = sum([x.jungleAttack for x in regiments]) / numRegs
        self.hillsAttack = sum([x.hillsAttack for x in regiments]) / numRegs
        self.mountainAttack = sum([x.mountainAttack for x in regiments]) / numRegs
        self.marshAttack = sum([x.marshAttack for x in regiments]) / numRegs
        self.riverAttack = sum([x.riverAttack for x in regiments]) / numRegs
        self.amphibiousAttack = sum([x.amphibiousAttack for x in regiments]) / numRegs
        self.urbanAttack = sum([x.urbanAttack for x in regiments]) / numRegs
        self.fortAttack = sum([x.fortAttack for x in regiments]) / numRegs

        # Defense
        self.woodsDefense = sum([x.woodsDefense for x in regiments]) / numRegs
        self.forestDefense = sum([x.forestDefense for x in regiments]) / numRegs
        self.jungleDefense = sum([x.jungleDefense for x in regiments]) / numRegs
        self.hillsDefense = sum([x.hillsDefense for x in regiments]) / numRegs
        self.mountainDefense = sum([x.mountainDefense for x in regiments]) / numRegs
        self.marshDefense = sum([x.marshDefense for x in regiments]) / numRegs
        self.riverDefense = sum([x.riverDefense for x in regiments]) / numRegs
        self.amphibiousDefense = sum([x.amphibiousDefense for x in regiments]) / numRegs
        self.urbanDefense = sum([x.urbanDefense for x in regiments]) / numRegs
        self.forestDefense = sum([x.forestDefense for x in regiments]) / numRegs
        

    def attack(self, enemy):
        soft = False    

        #Determine to hit soft or hard part
        if (random.random() < enemy.softness):
            soft = True

        # Determine the number of hits to deliver, and how many hits to receive
        if soft:
            for x in range(0, int(self.softAttack * self.effectiveness - 1)):
                if x < enemy.defensiveness:
                    if (random.random() < .3):
                        enemy.receivedHits += 1
                else:
                    if (random.random() < .52):
                        enemy.receivedHits += 1

            # Determine if defender hits soft or hard part
            defSoft = False
            if (random.random() < self.softness):
                defSoft = True

            if defSoft:
                for x in range(0, int(enemy.softAttack * enemy.effectiveness - 1)):
                    if x < self.toughness:
                        if (random.random() < .3):
                            self.receivedHits += 1
                    else:
                        if (random.random() < .52):
                            self.receivedHits += 1

            else:
                for x in range(0, int(enemy.hardAttack * enemy.effectiveness - 1)):
                    if x < self.toughness:
                        if (random.random() < .3):
                            self.receivedHits += 1
                    else:
                        if (random.random() < .52):
                            self.receivedHits += 1

        else:
            for x in range(0, int(self.hardAttack * self.effectiveness - 1)):
                if x < enemy.defensiveness:
                    if (random.random() < .3):
                        enemy.receivedHits += 1
                else:
                    if (random.random() < .52):
                        enemy.receivedHits += 1

            # Determine if the enemy hits soft or hard part
            defSoft = False 
            if (random.random() < self.softness):
                defSoft = True

            if defSoft:
                for x in range(0, int(enemy.softAttack * enemy.effectiveness - 1)):
                    if x < self.toughness:
                        if (random.random() < .3):
                            self.receivedHits += 1
                    else:
                        if (random.random() < .52):
                            self.receivedHits += 1

            else:
                for x in range(0, int(enemy.hardAttack * enemy.effectiveness - 1)):
                    if x < self.toughness:
                        if (random.random() < .3):
                            self.receivedHits += 1
                    else:
                        if (random.random() < .52):
                            self.receivedHits += 1
        
        pierced = False
        defPierced = False

        piercedMod = .5
        defPiercedMod = .5

        if self.piercing >= enemy.armor:
            pierced = True
        if enemy.piercing >= self.armor:
            defPierced = True

        # Apply damage from received hits
        if defPierced:
            defPiercedMod = 1
        for x in range(0, self.receivedHits - 1):
            if (random.random() < .5):
                self.manpower -= 1.5 * defPiercedMod
            else:
                self.manpower -= 3 * defPiercedMod
            
            roll = random.random()
            if (roll < .33):
                self.organization -= .1 * defPiercedMod
            elif(roll < .66): 
                self.organization -= .2 * defPiercedMod
            else:
                self.organization -= .3 * defPiercedMod

        if pierced:
            piercedMod = 1
        for x in range(0, enemy.receivedHits - 1):
            if (random.random() < .5):
                enemy.manpower -= 1.5 * piercedMod
            else:
                enemy.manpower -= 3 * piercedMod

            roll = random.random()
            if (roll < .33):
                enemy.organization -= .1 * piercedMod
            elif (roll < .66):
                enemy.organization -= .2 * piercedMod
            else:
                enemy.organization -= .3 * piercedMod

        self.receivedHits = 0
        enemy.receivedHits = 0

    def regAttack(self, enemy):
        for regiment in self.regiments:
            index = int(random.random() * (len(enemy.regiments) - 1))
            regiment.attack(enemy.regiments[index])