from modules.division import Division
from modules.usRegiments import *


def simulate(attacker, defender, count):
    attackerWins = 0
    defenderWins = 0
    avgHours = []
    avgAttackerLosses = []
    avgAttackerOrgLoss = []
    avgDefenderLosses = []
    avgDefenderOrgLoss =[]
    
    for x in range(0, count):
        attacker.manpower = attacker.maxManpower
        attacker.organization = attacker.maxOrganization

        defender.manpower = defender.maxManpower
        defender.organization = defender.maxOrganization

        hours = 0
        time = 0

        while(attacker.organization > 1 and defender.organization > 1 and attacker.manpower > 0 and defender.manpower > 0):
            if time < 5 and time > 20:
                attacker.effectiveness -= .4
                defender.effectiveness -= .4
            else:
                attacker.effectiveness = 1
                attacker.effectiveness = 1
            attacker.attack(defender)
            hours += 1
            time += 1
            if time > 23:           
                time = 0

        avgAttackerLosses += [attacker.maxManpower - attacker.manpower]
        avgDefenderLosses += [defender.maxManpower - defender.manpower]
        avgAttackerOrgLoss += [attacker.maxOrganization - attacker.organization]
        avgDefenderOrgLoss += [defender.maxOrganization - defender.organization]
        avgHours += [hours]

        if attacker.organization <= 1 or attacker.manpower <= 0:
            defenderWins += 1
        else:
            attackerWins += 1

    attackerWinPct = attackerWins / count
    defenderWinPct = defenderWins / count
    avgHours = sum(avgHours) / len(avgHours)
    avgAttackerLosses = sum(avgAttackerLosses) / count
    avgDefenderLosses = sum(avgDefenderLosses) / count
    avgAttackerOrgLoss = sum(avgAttackerOrgLoss) / count
    avgDefenderOrgLoss = sum(avgDefenderOrgLoss) / count
    
    return {"attackerWinPct":attackerWinPct, "defenderWinPct":defenderWinPct, "avgHours":avgHours, 
            "avgAttackerLosses":avgAttackerLosses, "avgAttackerOrgLoss":avgAttackerOrgLoss, "avgDefenderLosses":avgDefenderLosses, "avgDefenderOrgLoss":avgDefenderOrgLoss}
    