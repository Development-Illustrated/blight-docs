import numpy as np
import time
# plenty of things will not work but I will try to fix them
# playerLocation = [x1, y1], x1 and y1 being their coordinates, 100 being metres away
# boolean result
def calcDist(x2, y2):
    if (float(x2) <= 100) or (float(y2) <= 100):
        dist = np.sqrt( (x2 - 0)**2 + (y2 - 0)**2) < 100
        print(dist)
        return dist
    
# resource counter per second
def playerResourceIncrease(resources, itemResourceRate):
    resources += itemResourceRate
    # figure out the second delay
    return resources

# The effect they'll have on other players
def calcPlayerResourcePressure(resources, itemContagion):
    if resources < 100000:
        pressure = 0.0000005 * resources * (1 + itemContagion)
        return pressure
    else:
        pressure = 0.05 * (1 + itemContagion)
        return pressure

# for players with in dist, calculate the effect they have on the player
def calcPlayerResourceEfficiency(itemImmunity):
    # both effects should sum the array of all nearby players respective pressures
    allyEffect = sum(["nearby allies"])
    enemyEffect = sum(["nearby enemies"])

    effectiveMod = (1 + allyEffect - enemyEffect) * (1 + itemImmunity)

    if -0.75 < effectiveMod < 1.75:
        return effectiveMod
    elif effectiveMod <= -0.75:
        effectiveMod = 1 - 0.75
        return effectiveMod
    elif effectiveMod >= 1.75:
        effectiveMod = 1.75
        return effectiveMod


echo = calcPlayerResourceEfficiency(0)
print (echo)

