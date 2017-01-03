from modules.japRegiments import *
from modules.division import Division

class japInfDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Inf. Div.", [japInfReg(), japRecCavReg(), japATReg(), japArtReg(), japEngReg(), japWagReg(), japDivHQReg()])

class japTropGarDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Trop. Gar. Div", [japTropGarReg(), japGarReg(), japGarDetReg(), japMixSupReg(), japHvArtReg(), japATReg(), japHvAAReg()])

class japInfTnkDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Inf. Tnk. Div", [japInfReg(), japMixSupReg(), japInfTnkReg(), japACReg(), japEngReg(), japWagReg(), japDivHQReg()])

class japSemiMotDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Semi Mot. Div", [japSemiMotReg(), japMotSupReg(), japArtReg(), japRecCavReg(), japMotEngReg(), japTruckReg(), japDivHQReg()])

class japInf2Div(Division):
    def __init__(self):
        Division.__init__(self, "JAP Inf. Div. 2", [japInfReg(), japArtReg(), japATReg(), japAAReg(), japEngReg(), japWagReg(), japDivHQReg()])

class japMarineDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Marine Div.", [japDivHQReg(), japMarineReg(), japPackArtReg(), japAAReg(), japEngReg(), japWagReg()])

class japMarine2Div(Division):
    def __init__(self):
        Division.__init__(self, "JAP Marine 2 Div.", [japDivHQReg(), japPackArtReg(), japMarineReg(), japATReg(), japMotRecReg(), japEngReg(), japLtTruckReg()])

class japLtArmorDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Lt. Armor", [japLtArmorReg(), japMotInfReg(), japArtReg(), japACReg(), japTruckReg(), japDivHQReg()])

class japSpecInfDiv(Division):
    def __init__(self):
        Division.__init__(self, "JAP Spec. Inf. Div.", [japSpecInfReg(), japMixSupReg(), japPackArtReg(), japRecCavReg(), japEngReg(), japWagReg(), japDivHQReg()])