from modules.usDivisions import *
from modules.gerDivisions import *
from modules.japDivisions import *
from modules.simulator import simulate

usDivs = [usArmDiv(), usGarDiv(), usMarineDiv()]
gerDivs = [gerArmDiv(), gerInfDiv(), gerGarDiv(), gerSemiMotDiv()]
japDivs = [japInfDiv(), japInf2Div(), japTropGarDiv(), japInfTnkDiv(), japSemiMotDiv(), japMarineDiv(), japMarine2Div(), japLtArmorDiv(), japSpecInfDiv()]


for adiv in usDivs:
    for ddiv in gerDivs:
        results = simulate(adiv, ddiv, 1000) 

        print("Attacker:", adiv.name)
        print("Defender:", ddiv.name)
        print("Attacker Win Pct:", results["attackerWinPct"])
        print("Defender Win Pct:", results["defenderWinPct"])
        print("Avg. Attacker Losses:", results["avgAttackerLosses"], "Avg. Attacker Org Loss:", results["avgAttackerOrgLoss"])
        print("Avg. Defender Losses:", results["avgDefenderLosses"], "Avg. Defender Org Loss:", results["avgDefenderOrgLoss"])
        print("Avg. Duration:", results["avgHours"], "hours")
        print()

for adiv in gerDivs:
    for ddiv in usDivs:
        results = simulate(adiv, ddiv, 1000) 

        print("Attacker:", adiv.name)
        print("Defender:", ddiv.name)
        print("Attacker Win Pct:", results["attackerWinPct"])
        print("Defender Win Pct:", results["defenderWinPct"])
        print("Avg. Attacker Losses:", results["avgAttackerLosses"], "Avg. Attacker Org Loss:", results["avgAttackerOrgLoss"])
        print("Avg. Defender Losses:", results["avgDefenderLosses"], "Avg. Defender Org Loss:", results["avgDefenderOrgLoss"])
        print("Avg. Duration:", results["avgHours"], "hours")
        print()
    
for adiv in usDivs:
    for ddiv in japDivs:
        results = simulate(adiv, ddiv, 1000) 

        print("Attacker:", adiv.name)
        print("Defender:", ddiv.name)
        print("Attacker Win Pct:", results["attackerWinPct"])
        print("Defender Win Pct:", results["defenderWinPct"])
        print("Avg. Attacker Losses:", results["avgAttackerLosses"], "Avg. Attacker Org Loss:", results["avgAttackerOrgLoss"])
        print("Avg. Defender Losses:", results["avgDefenderLosses"], "Avg. Defender Org Loss:", results["avgDefenderOrgLoss"])
        print("Avg. Duration:", results["avgHours"], "hours")
        print()

for adiv in japDivs:
    for ddiv in usDivs:
        results = simulate(adiv, ddiv, 1000) 

        print("Attacker:", adiv.name)
        print("Defender:", ddiv.name)
        print("Attacker Win Pct:", results["attackerWinPct"])
        print("Defender Win Pct:", results["defenderWinPct"])
        print("Avg. Attacker Losses:", results["avgAttackerLosses"], "Avg. Attacker Org Loss:", results["avgAttackerOrgLoss"])
        print("Avg. Defender Losses:", results["avgDefenderLosses"], "Avg. Defender Org Loss:", results["avgDefenderOrgLoss"])
        print("Avg. Duration:", results["avgHours"], "hours")
        print()