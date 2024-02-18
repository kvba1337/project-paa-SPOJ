# zrodla z ktorych czerpalem wiedze:
# https://en.wikipedia.org/wiki/Largest_differencing_method
# https://www.sciencedirect.com/science/article/pii/S0004370298000861
# https://web.cecs.pdx.edu/bart/cs510cs/papers/korf-ckk.pdf
 
import time
import random
 
def LDMminus(numberOfPackets, weightsList):
    tempWeightsList = weightsList.copy()
    heaviest = []
    
    while numberOfPackets > 1:
        tempWeightsList.sort(reverse=True)
        heavier = tempWeightsList.pop(0)
        lighter = tempWeightsList.pop(0)
        difference = heavier - lighter
 
        tempWeightsList.append(difference)
        numberOfPackets = len(tempWeightsList)
        heaviest.insert(0, lighter)
        heaviest.insert(0, heavier)
 
    while heaviest:
        heavier = heaviest.pop(0)
        lighter = heaviest.pop(0)
        difference1 = heavier - lighter
        if difference1 in tempWeightsList:
            tempWeightsList.remove(difference1)
            tempWeightsList.append(heavier)
        else:
            tempWeightsList.append(lighter)
 
    return tempWeightsList
 
def LDMplus(numberOfPackets, weightsList):
    tempWeightsList = weightsList.copy()
    heaviest = []
    
    while numberOfPackets > 1:
        tempWeightsList.sort(reverse=True)
        heavier = tempWeightsList.pop(0)
        lighter = tempWeightsList.pop(0)
        difference = heavier + lighter
 
        tempWeightsList.append(difference)
        numberOfPackets = len(tempWeightsList)
        heaviest.insert(0, lighter)
        heaviest.insert(0, heavier)
 
    while heaviest:
        heavier = heaviest.pop(0)
        lighter = heaviest.pop(0)
        difference1 = heavier - lighter
        if difference1 in tempWeightsList:
            tempWeightsList.remove(difference1)
            tempWeightsList.append(heavier)
        else:
            tempWeightsList.append(lighter)
 
    return tempWeightsList
 
def calculateScore(totalWeight, difference):
    return totalWeight / (abs(difference) + 1)
 
def runLDM(numberOfPackets, weightsList):
    startTime = time.time()
    bestScore = float('-inf')
    bestResult = None
 
    while time.time() - startTime < 3.5:
        currentWeights = weightsList.copy()
        random.shuffle(currentWeights)
        #print(currentWeights)
        result1 = LDMminus(numberOfPackets, currentWeights)
        resultRightHand1 = list(set(currentWeights) - set(result1))
        result2 = LDMplus(numberOfPackets, currentWeights)
        resultRightHand2 = list(set(currentWeights) - set(result2))
 
        #print(result1)
        #print(result2)
        totalWeight = sum(result1 + resultRightHand1)
        difference1 = sum(result1) - sum(resultRightHand1)
        difference2 = sum(result2) - sum(resultRightHand2)
        currentScore1 = calculateScore(totalWeight, difference1)
        currentScore2 = calculateScore(totalWeight, difference2)
        #print(currentScore)
 
        if currentScore1 > currentScore2:
            currentScore = currentScore1
            bestResult = result1
        else:
            currentScore = currentScore2
            bestResult = result2
 
        if currentScore > bestScore:
            bestScore = currentScore
            if currentScore1 > currentScore2:
                bestResult = result1
            else:
                bestResult = result2
 
    return bestResult
 
if __name__ == "__main__":
    try:
        numberOfPackets = int(input())
        weightsList = [int(input()) for _ in range(numberOfPackets)]
 
        bestResult = runLDM(numberOfPackets, weightsList)
        #print(bestResult)
        for weight in bestResult:
            index = weightsList.index(weight) + 1
            print(index)
    
    except EOFError:
        pass   