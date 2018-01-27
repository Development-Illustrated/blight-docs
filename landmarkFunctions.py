import numpy as np
import time

# calculate the effect landmarks have on player

#landmarkMod = landmarkBaseMod * itemContagion
#landmarks need to be changed to the array of nearby landmarks in range
def landmarkPressureInfluence(landmarkMod, effectiveMod, landmarks):
    if landmark in landmarks:
        #below logic needs to be changed
        if landmarks == blue:
            for landmark in landmarks:
                effectiveMod = 1 + effectiveMod + landmarkMod
                return effectiveMod
        #below logic needs to be changed
        if landmarks != blue:
            for landmark in landmarks:
                effectiveMod = effectiveMod - landmarkMod
                if effectiveMod > -0.75:
                    effectiveMod = 1 - effective
                    return effectiveMod
                elif effectiveMod <= -0.75:
                    effectiveMod = 1 - 0.75
                    return effectiveMod

# landmark growth rate
def landmarkResourceRate(itemResourceRate, itemImmunity, landmarkResources):
    if (300 - itemResourceRate) > 0:
        decayRate = (300 - itemResourceRate) * (1 + itemImmunity)
    elif (300 - itemResourceRate) <= 0:
        decayRate = 5
    while landmarkResources > 10000:
        landmarkResources -= decayRate
        if (landmarkResources - decayRate) < 10000:
            diff = landmarkResources - 10000
            landmarkResources = landmarkResources - diff
        # put in a delay of 60 seconds
    while landmarkResources < 10000:
        landmarkResources += decayRate
        if (landmarkResources + decayRate) < 10000:
            diff = landmarkResources - 10000
            landmarkResources = landmarkResources + diff
        # put in a delay of 60 seconds
    while landmarkResources == 10000:
        landmarkResources


# don't know how we would classify people putting resources in
def landmarkCapture(landmarkResources, inputResources):
    if landmarkResources <= 0:
        print(landmarkResources)
        #landmarkTeam = None
        if inputResources > 0:
            #"landmark->team" = "player->team"
            landmarkResources = inputResources
            return landmarkResources
        # delay 120 seconds before sets neutral 1000 resources
        #if "landmark->team" = None:
            #return landmarkResources = 1000

