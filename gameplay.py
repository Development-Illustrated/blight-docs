import numpy as np
import time
# plenty of things will not work but I will try to fix them
# playerLocation = [x1, y1], x1 and y1 being their coordinates, 100 being metres away
def calcDist:
    if (float(x2) < 100) or (float(y2) < 100):
        return dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2)
    else:
        return None

itemContagion = []
itemImmunity = []
itemResourceRate = []
# resource counter per second
def playerResourceIncrease(resources, itemResourceRate):
    resources += itemResourceRate
    time.sleep(1)

# The effect they'll have on other players
def calcPlayerResourcePressure(resources, itemContagion):
    if resources < 100000:
        return pressure = 0.0000005 * resources * itemContagion
    else:
        return pressure = 0.05 * itemContagion

# for players with in dist, calculate the effect they have on the player
players = []
def calcPlayerResourceEfficiency(players, itemImmunity):
    if players in dist:
        if players == team:
            return allyEffect = sum("players->pressure")
        if players != team:
            return enemyEffect = sum("players->pressure")

    effectiveMod = (1 + allyEffect - enemyEffect) * itemImmunity

    if effectiveMod > -0.75:
        return effectiveMod
    else:
        return effectiveMod = -0.75

    if effectiveMod < 1.75:
        return effectiveMod
    else:
        return effectiveMod = 1.75

# calculate the effect landmarks have on player
landmarkMod = 0.5 * itemContagion
landmarks = []
def landmarkPressureInfluence(landmarkMod, effectiveMod, landmarks):
    if landmarks in dist:
        if "landmarks->team" == "players->team":
            for landmark in landmarks:
                return effectiveMod = effectiveMod + landmarkMod
        if "landmarks->team" != "players->team"
            for landmark in landmarks:
                effectiveMod = effectiveMod - landmarkMod
                if effectiveMod > -0.75:
                    return effectiveMod
                else:
                    return effectiveMod = -0.75

# landmark growth rate
def landmarkResourceRate(itemResourceRate, itemImmuity):
    landmarkResources = 10000
    decayRate = (300 + itemResourceRate) * itemImmunity

    while landmarkResources > 10000:
        return landmarkResources -= decayRate
        if (landmarkResources - decayRate) < 10000:
            diff = landmarkResources - 10000
            landmarkResources = landmarkResources - diff
        time.sleep(60)
    while landmarkResources < 10000:
        return landmarkResources += decayRate
        if (landmarkResources + decayRate) < 10000:
            diff = landmarkResources - 10000
            landmarkResources = landmarkResources + diff
        time.sleep(60)

# don't know how we would classify people putting resources in
def landmarkCapture(landmarkResources):
    if landmarkResources <= 0:
        "landmark->team" = None
        if "player puts in resources":
            return "landmark->team" = "player->team"
            return landmarkResources = "reasources player put in"
        time.sleep(120)
        if "landmark->team" = None:
            return landmarkResources = 1000
    

