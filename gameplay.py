import numpy as np
import time

class Player(object):
    """docstring for Player"""
    def __init__(self, name, team, location, items, resources):
        self.name = name
        self.team = team
        self.location = []
        self.items = items
        self.resources = resources

class Items(Player):
    """docstring for Items"""
    def __init__(self):
        super(Items, self).__init__(self)
        self.itemResourceRate = itemResourceRate
        self.itemContagion = itemContagion
        self.itemImmunity = itemImmunity

# plenty of things will not work but I will try to fix them
# playerLocation = [x1, y1], x1 and y1 being their coordinates, 100 being metres away
def calcDist:
    if (float(x2) < 100) or (float(y2) < 100):
        return dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2)
    else:
        return None
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




