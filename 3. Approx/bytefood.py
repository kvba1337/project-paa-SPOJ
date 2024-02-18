# zrodla z ktorych czerpalem wiedze:
# https://www.digitalocean.com/community/tutorials/read-stdin-python
# https://www.simplilearn.com/tutorials/python-tutorial/strip-in-python
# https://www.toppr.com/guides/python-guide/references/methods-and-functions/global-local-nonlocal-variables/python-global-local-and-nonlocal-variables-with-examples/
 
import sys
 
def calculateDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
 
def calculatePotentialProfit(shop, currentPosX, currentPosY, totalTime, testDeadline, house):
    shopPosX, shopPosY, a, b, deadlineInShop = shop
    housePosX, housePosY = house
    distanceToShop = calculateDistance(currentPosX, currentPosY, shopPosX, shopPosY)
    distanceToHouse = calculateDistance(housePosX, housePosY, shopPosX, shopPosY)
 
    if (totalTime + distanceToShop + deadlineInShop + distanceToHouse) <= testDeadline:
        return a - b * (totalTime + distanceToShop + deadlineInShop)
    else:
        return -1
 
def updateVariables(shop, currentPosX, currentPosY, totalTime, visited, bestShopIndex, visitedCount, travelTime):
    currentPosX = shop[0]
    currentPosY = shop[1]
    totalTime += travelTime
    visited[bestShopIndex] = True
    visitedCount += 1
    return currentPosX, currentPosY, totalTime, visited, visitedCount
 
def findBestShop(shops, visited, currentPosX, currentPosY, totalTime):
    maxProfit = 0
    maxIndex = -1
    travelTime = 0
 
    for idx in range(len(shops)):
        shopPosX, shopPosY, a, b, deadlineInShop = shops[idx]
        if not visited[idx]:
            potentialProfit = calculatePotentialProfit(shops[idx], currentPosX, currentPosY, totalTime, testDeadline, house)
 
            if potentialProfit >= 0:
                profitRatio = deadlineInShop * b / (calculateDistance(currentPosX, currentPosY, shopPosX, shopPosY) + deadlineInShop)
 
                if profitRatio > maxProfit:
                    maxProfit = profitRatio
                    maxIndex = idx
                    travelTime = calculateDistance(currentPosX, currentPosY, shopPosX, shopPosY) + deadlineInShop
 
    return maxIndex, travelTime
 
def processTest(numberOfShops, testDeadline, shops, house):
    currentPosX = house[0]
    currentPosY = house[1]
    visited = [False] * numberOfShops
    totalTime = 0
    visitedCount = 0
    bestShopIndex = -1
 
    while totalTime < testDeadline and visitedCount < numberOfShops:
        bestShopIndex, travelTime = findBestShop(shops, visited, currentPosX, currentPosY, totalTime)
 
        if bestShopIndex != -1:
            print(f"{bestShopIndex + 1} {shops[bestShopIndex][4]}")
            currentPosX, currentPosY, totalTime, visited, visitedCount = updateVariables(shops[bestShopIndex], currentPosX, currentPosY, totalTime, visited, bestShopIndex, visitedCount, travelTime)
        else:
            break
 
    print(f"0 0")
 
if __name__ == "__main__":
    try:
        stringInput = input().strip()
        t = int(stringInput)
 
        for numberOfTest in range(1, t + 1):
            stringInput = input().strip()
            blank = stringInput.index(" ")
            numberOfShops = int(stringInput[:blank])
            testDeadline = int(stringInput[blank + 1:])
 
            shops = [tuple(map(int, input().strip().split())) for _ in range(numberOfShops)]
            house = tuple(map(int, input().strip().split()))
 
            print(numberOfTest)
            processTest(numberOfShops, testDeadline, shops, house)
            
    except EOFError:
        pass 