# zrodla z ktorych czerpalem wiedze:
# https://www.analyticsvidhya.com/blog/2021/06/working-with-lists-dictionaries-in-python/
# https://docs.python.org/3/library/fractions.html
# https://www.codingninjas.com/studio/library/handling-eoferror-exception-in-python
# https://docs.python.org/3/library/re.html
# https://realpython.com/python-fractions/#multiplication

from fractions import Fraction
import re

def multiply(fractionA, fractionB):
    return Fraction(fractionA.numerator * fractionB.numerator, fractionA.denominator * fractionB.denominator)

def divide(fractionA, fractionB):
    return Fraction(fractionA.numerator * fractionB.denominator, fractionA.denominator * fractionB.numerator)

def add(fractionA, fractionB):
    return Fraction((fractionA.numerator * fractionB.denominator) + (fractionB.numerator * fractionA.denominator), 
                    (fractionA.denominator * fractionB.denominator))

def recognizeOperation(fractionA, fractionB, operation):
    result = Fraction()

    if operation == "+":
        result = add(fractionA, fractionB)
    elif operation == "*":
        result = multiply(fractionA, fractionB)
    elif operation == "/":
        result = divide(fractionA, fractionB)

    return result

def handleExpression(expression, fractionsDict):
    stack = []
    componentsList = [t for t in re.split(r'(_|[*\/+])', expression) if t]

    for component in componentsList:
        if component == "_":
            continue
        elif component in ("+", "*", "/"):
            fractionB = stack.pop()
            fractionA = stack.pop()
            result = recognizeOperation(fractionA, fractionB, component)
            stack.append(result)
        else:
            stack.append(fractionsDict[component])

    return stack.pop()

def processCase(expressionsDict, variablesList):
    fractionsDict = {}

    if not variablesList:
        return fractionsDict
    
    givenCalculatedVariable = variablesList.pop()
    fractionsDict[givenCalculatedVariable] = Fraction(expressionsDict[givenCalculatedVariable])

    while variablesList:
        variable = variablesList.pop()
        fractionsDict[variable] = handleExpression(expressionsDict[variable], fractionsDict)

    sortedFractionsDict = dict(sorted(fractionsDict.items()))

    return sortedFractionsDict

def readCase(testsAmount, lastCase):
    for i in range(testsAmount):
        expressionsDict = {}
        variablesList = []

        while True:
            try:
                line = input()
            except EOFError:
                lastCase = True
            
            if "case" in line or lastCase:
                fractionsDict = processCase(expressionsDict, variablesList)
                print(f"case {i + 1} Y")
                for variable, value in fractionsDict.items():
                    print(f"{variable} {value.numerator} {value.denominator}")
                break
            else:
                variable, expression = map(str.strip, line.split("="))
                variablesList.append(variable)
                expressionsDict[variable] = expression

if __name__ == "__main__":
    testsAmount = 1000
    lastCase = False
    
    line = input()
    readCase(testsAmount, lastCase)