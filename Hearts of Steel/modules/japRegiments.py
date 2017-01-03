from modules.regiment import Regiment

class japInfReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Inf.", 9000, 38, 0, 11, 3, 7, 0, 2, 22, 20, 15, 1, 1)

class japRecCavReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Rec. Cav.", 3000, 34, 1, 6, 1, 2, 0, 0, 16, 15, 13, .9, 1)

class japATReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP AT", 200, 34, 0, 2, 14, 14, 0, 0, 8, 2, 12, .6, 1)

class japArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Art.", 1300, 34, 0, 1, 2, 2, 0, 0, 12, 8, 7, .9, 1)

class japEngReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Eng.", 200, 38, 0, 3, 1, 2, 0, 2, 22, 22, 15, .9, 1)

class japWagReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Wagon", 100, 33, 0, -1, -1, 0, 0, 0, -1, -1, 0, 1, 1)

class japDivHQReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Div. HQ", 250, 75, 0, 0, 0, 0, 0, 4, 2, 2, 12, .5, 1)

class japTropGarReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Trop. Gar.", 3000, 38, 1, 9, 2, 4, 4, 7, 27, 10, 15, 1, 1)

class japGarReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Gar.", 3000, 38, 1, 9, 2, 4, 4, 7, 27, 10, 15, 1, 1)

class japGarDetReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Gar. Det.", 800, 38, 1, 8, 2, 4, 4, 3, 22, 10, 9, 1, 1)

class japMixSupReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Mix. Sup.", 400, 31, 0, 5, 5, 11, 0, 6, 22, 5, 12, .7, 1)

class japHvArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Hv. Art.", 1000, 32, 1, 1, 2, 3, 0, 0, 10, 1, 7, 1, 1)

class japHvAAReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Hv. AA.", 500, 34, 0, 1, 2, 13, 0, 11, 8, 2, 16, .85, 1)

class japInfTnkReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Inf. Tnk.", 2500, 34, 0, 10, 4, 4, 14, 0, 7, 8, 5, .1, 1)

class japACReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Arm. Car", 1200, 34, 0, 2, 1, 5, 5, 2, 3, 6, 6, .5, 1)

class japSemiMotReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Semi Mot. Inf.", 3000, 38, 1, 11, 3, 7, 0, 2, 25, 22, 15, 1, 1)

class japMotSupReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Mot. Sup.", 700, 31, 0, 6, 4, 9, 0, 8, 11, 9, 14, .6, 1)

class japMotEngReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Mot. Eng.", 300, 38, 0, 4, 2, 4, 0, 2, 23, 23, 15, .7, 1)

class japTruckReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Truck", 100, 8, 0, -1, -1, 0, 0, 0, -1, -1, 0, .75, 1)

class japAAReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP AA", 200, 34, 0, 1, 2, 7, 0, 12, 8, 2, 19, .7, 1)

class japMarineReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Marine", 6000, 40, 1, 11, 3, 7, 0, 2, 26, 34, 16, .8, 1)

class japPackArtReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Pack Art.", 600, 34, 0, 1, 1, 2, 0, 0, 4, 5, 7, .9, 1)

class japMotRecReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Mot. Rec.", 600, 34, 0, 5, 0, 0, 0, 2, 4, 4, 11, .5, 1)

class japLtTruckReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Lt. Truck", 100, 8, 0, -1, -1, 0, 0, 0, -1, -1, 0, 1, 1)

class japLtArmorReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Lt. Arm", 3000, 34, 2, 5, 3, 4, 12, 0, 5, 5, 5, .2, 1)

class japMotInfReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Mot. Inf", 2000, 34, 1, 14, 6, 10, 0, 2, 26, 24, 11, .6, 1)

class japSpecInfReg(Regiment):
    def __init__(self):
        Regiment.__init__(self, "JAP Spec Inf", 6000, 40, 0, 17, 3, 7, 0, 2, 25, 30, 11, .7, 1)