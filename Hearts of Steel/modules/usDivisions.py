from modules.usRegiments import *
from modules.division import Division

class usArmDiv(Division):
    def __init__(self):
        Division.__init__(self, "US Armor Division", [usArmorReg(), usArmSupReg(), usDivHQReg(), usHvArmReg(), usHvArmReg(), usArmCarReg(), usTruckReg()])

class usMarineDiv(Division):
    def __init__(self):
        Division.__init__(self, "US Marine Div", [usMarineReg(), usArmSupReg(), usTDReg(), usArmCarReg(), usMotEngReg(), usTruckReg(), usDivHQReg()])

class usGarDiv(Division):
    def __init__(self):
        Division.__init__(self, "US Gar Div", [usGarReg(), usHQDefReg(), usMixSupReg(), usArtReg(), usEngReg(), usTruckReg(), usDivHQReg()])