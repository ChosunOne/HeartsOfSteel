from modules.gerRegiments import *
from modules.division import Division

class gerArmDiv(Division):
    def __init__(self):
        Division.__init__(self, "GER Armor Division", [gerArmReg(), gerDivHQReg(), gerHvAAReg(), gerMotInfReg(), gerTDReg(), gerTruckReg(), gerMedArtReg()])

class gerInfDiv(Division):
    def __init__(self):
        Division.__init__(self, "GER Inf. Division", [gerInfReg(), gerArtReg(), gerATReg(), gerMotRecReg(), gerEngReg(), gerHorseReg(), gerDivHQReg()])

class gerGarDiv(Division):
    def __init__(self):
        Division.__init__(self, "GER Gar. Division", [gerGarReg(), gerHvArtReg(), gerHvArtReg(), gerATReg(), gerHvAAReg(), gerAAReg()])

class gerSemiMotDiv(Division):
    def __init__(self):
        Division.__init__(self, "GER Semi Mot. Division", [gerSemiMotReg(), gerArtReg(), gerHvAAReg(), gerATReg(), gerMotEngReg(), gerLtTruckReg(), gerDivHQReg()])