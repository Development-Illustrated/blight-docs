import numpy as np
import time

# calculate the effect landmarks have on player
class landmark(object):
    landmarkBaseMod = 0.5

    def __int__(self, name, landmarkResources, landmarkItems, landmarkTeam):
        self.name = name
        self.landmarkResources = landmarkResources
        self.landmarkItems = []
        self.landmarkTeam = landmarkTeam

    def addItem(self, item):
        self.landmarkItems.append(item)

    def captureLandmark(self, resources)
        self.landmarkResources = resources

landmarkMod = landmarkBaseMod * itemContagion
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
        landmarkTeam = None
        inputResources = "resources put in by player"
        if inputResources = True:
            return "landmark->team" = "player->team"
            return landmarkResources = inputResources
        time.sleep(120)
        if "landmark->team" = None:
            return landmarkResources = 1000
