class Regiment:
    def __init__(self, name, manpower, organization, width, softAttack, hardAttack, piercing, armor, airAttack, defensiveness, toughness, airDefense, softness, efficiency, 
        woodsAttack, forestAttack, jungleAttack, hillsAttack, mountainAttack, marshAttack, riverAttack, amphibiousAttack, urbanAttack, fortAttack, 
        woodsDefense, forestDefense, jungleDefense, hillsDefense, mountainDefense, marshDefense, riverDefense, amphibiousDefense, urbanDefense, fortDefense):
        
        # Unit attributes
        self.name = name
        self.manpower = manpower
        self.organization = organization
        self.width = width
        self.softAttack = softAttack
        self.hardAttack = hardAttack
        self.piercing = piercing
        self.armor = armor
        self.airAttack = airAttack
        self.defensiveness = defensiveness
        self.toughness = toughness
        self.airDefense = airDefense
        self.softness = softness

        self.efficiency = 1

        # Terrain Modifiers
        # Attack
        self.woodsAttack = woodsAttack
        self.forestAttack = forestAttack
        self.jungleAttack = jungleAttack
        self.hillsAttack = hillsAttack
        self.mountainAttack = mountainAttack
        self.marshAttack = marshAttack
        self.riverAttack = riverAttack
        self.amphibiousAttack = amphibiousAttack
        self.urbanAttack = urbanAttack
        self.fortAttack = fortAttack

        # Defense
        self.woodsDefense = woodsDefense
        self.forestDefense = forestDefense
        self.jungleDefense = jungleDefense
        self.hillsDefense = hillsDefense
        self.mountainDefense = mountainDefense
        self.marshDefense = marshDefense
        self.riverDefense = riverDefense
        self.amphibiousDefense = amphibiousDefense
        self.urbanDefense = urbanDefense
        self.forestDefense = forestDefense