from modules.regiment import Regiment

class usArmorReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Armor Regiment", 5000, 50, 2, 18, 20, 18, 19, 0, 12, 24, 5, .1, 1)

class usArmSupReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US_Armored_Support", 2000, 37, 0, 10, 13, 23, 9, 10, 13, 19, 16, .2, 1)

class usHvArmReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Heavy Armor", 1000, 50, 0, 19, 27, 24, 25, 0, 18, 27, 5, .05, 1)

class usArmCarReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Armored Car", 1000, 50, 0, 7, 3, 13, 7, 2, 4, 16, 6, .44, 1)

class usTruckReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Truck Transport", 100, 8, 0, -1, -1, 0, 0, 0, -1, -1, 0, .75, 1)

class usDivHQReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US_Div_HQ", 250, 75, 0, 0, 0, 0, 0, 4, 2, 2, 12, .5, 1)

class usMarineReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Marines", 9000, 41, 1, 12, 3, 7, 0, 2, 24, 33, 16, .8, 1)

class usMotEngReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Mot. Eng.", 600, 50, 0, 4, 1, 4, 0, 2, 23, 25, 15, .7, 1)

class usGarReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Garrison", 3000, 53, 1, 9, 2, 4, 4, 7, 26, 9, 15, 1, 1)

class usHQDefReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US HQ Def.", 2000, 57, 1, 8, 2, 2, 0, 7, 26, 13, 15, 1, 1)

class usTDReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US TD", 2000, 54, 0, 11, 32, 31, 9, 0, 4, 4, 5, .2, 1)

class usMixSupReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Mix. Sup.", 1400, 36, 0, 6, 8, 23, 0, 6, 27, 5, 12, .7, 1)

class usArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Art.", 1800, 54, 0, 1, 2, 2, 0, 0, 15, 10, 7, .9, 1)

class usEngReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "US Eng", 400, 54, 0, 3, 1, 2, 0, 2, 24, 24, 15, .9, 1)