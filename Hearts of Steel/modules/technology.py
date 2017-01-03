class Technology:
    def __init__(self, name='', manpower=0, organization=0, width=0, softAttack=0, hardAttack=0, piercing=0, armor=0, airAttack=0, defensiveness=0, toughness=0, airDefense=0, softness=0, efficiency=0,
        woodsAttack=0, forestAttack=0, jungleAttack=0, hillsAttack=0, mountainAttack=0, marshAttack=0, riverAttack=0, amphibiousAttack=0, urbanAttack=0, fortAttack=0, bocageAttack=0,
        woodsDefense=0, forestDefense=0, jungleDefense=0, hillsDefense=0, mountainDefense=0, marshDefense=0, riverDefense=0, amphibiousDefense=0, urbanDefense=0, fortDefense=0, bocageDefense=0, units=None):
        
        # Technology Attributes
        self.name = name
        if units:
            self.units = units
        else:
            self.units = []
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

        self.efficiency = efficiency

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
        self.bocageAttack = bocageAttack

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
        self.fortDefense = fortDefense
        self.bocageDefense = bocageDefense