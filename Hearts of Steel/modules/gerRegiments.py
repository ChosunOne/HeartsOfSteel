from modules.regiment import Regiment

class gerArmReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Armor", 5000, 50, 2, 13, 16, 16, 18, 2, 16, 28, 7, .1, 1)

class gerMotInfReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Mot Inf", 6000, 50, 1, 15, 6, 10, 0, 2, 27, 16, 11, .6, 1)

class gerTDReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Med Art", 2000, 50, 1, 1, 2, 2, 0, 0, 15, 10, 6, 1, 1)

class gerHvAAReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Hv AA", 700, 50, 0, 1, 2, 22, 0, 12, 8, 3, 18, .85, 1)

class gerTruckReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Truck", 100, 15, 0, -1, -1, 0, 0, 0, -1, -1, 0, .75, 1)

class gerDivHQReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Div HQ", 250, 75, 0, 0, 0, 0, 0, 4, 2, 2, 12, .5, 1)

class gerMedArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Med Art", 2000, 50, 1, 1, 2, 2, 0, 0, 15, 10, 6, 1, 1)

class gerInfReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Inf. Reg", 9000, 50, 1, 12, 3, 7, 0, 2, 23, 12, 15, 1, 1)

class gerArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Art. Reg", 1800, 50, 0, 1, 2, 2, 0, 0, 12, 8, 7, .9, 1)

class gerATReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER AT Reg", 400, 50, 0, 3, 20, 26, 0, 0, 9, 2, 12, .6, 1)

class gerMotRecReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Mot. Rec.", 600, 51, 0, 5, 0, 0, 0, 2, 3, 4, 11, .5, 1)

class gerEngReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Eng.", 400, 50, 0, 4, 2, 2, 0, 2, 23, 26, 15, .9, 1)

class gerHorseReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Horse", 100, 33, 0, -1, -1, 0, 0, 0, -1, -1, 0, 1, 1)

class gerHvArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Hv. Art.", 1500, 40, 1, 1, 3, 4, 0, 0, 14, 2, 7, 1, 1)

class gerAAReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER AA", 400, 50, 0, 1, 2, 20, 0, 14, 8, 2, 22, .7, 1)

class gerSemiMotReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Semi Mot.", 9000, 50, 1, 12, 3, 7, 0, 2, 26, 14, 15, 1, 1)

class gerMotEngReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Mot. Eng.", 600, 50, 0, 5, 2, 4, 0, 2, 24, 27, 15, .7, 1)

class gerLtTruckReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Lt. Truck", 100, 6, 0, -1, -1, 0, 0, 0, -1, -1, 0, 1, 1)

class gerGarReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "GER Gar", 3000, 55, 1, 9, 2, 4, 4, 7, 27, 10, 15, 1, 1)