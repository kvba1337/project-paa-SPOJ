// zrodla z ktorych czerpalem wiedze dotyczaca konwersji roznych systemow liczbowych:
// https://blog.devgenius.io/number-systems-and-their-conversions-using-c-5b1ea99f200b
// https://4programmers.net/C/Konwersje_int_na_string_i_string_na_int

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

const int MAX_MULTIPLIERS = 10;

vector <int> convertStringToInt(const string& number) {
    vector <int> convertedNumber(number.size());
    int index = 0;
    int invertedIndex = number.size() - 1;

    while (index < number.size()) {
        if (number[invertedIndex] >= 'A') convertedNumber[index] = number[invertedIndex] - 'A' + 10;
        else convertedNumber[index] = number[invertedIndex] - '0';

        index++;
        invertedIndex--;
    }
    return convertedNumber;
}

vector <int> changeBase(vector <int>& number, int givenBase, int finalBase) {
    vector <int> convertedNumber;
    int numberSize = number.size();

    if (numberSize <= 0) return convertedNumber;

    if (givenBase == finalBase) {
        for (int i = 0; i < numberSize; i++) {
            convertedNumber.push_back(number[i]);
        }
        return convertedNumber;
    }

    if (givenBase < finalBase) {
        int multiplier[MAX_MULTIPLIERS] = { 1 };
        int currentPowerIndex = 1;
        int currentPowerValue = givenBase;
        int resultIndex = 0;
        int outerLoopIndex, innerLoopIndex, resultNumber;

        while (currentPowerIndex < MAX_MULTIPLIERS && currentPowerValue < finalBase) {
            multiplier[currentPowerIndex] = currentPowerValue;
            currentPowerValue *= givenBase;
            currentPowerIndex++;
        }

        for (outerLoopIndex = 0; outerLoopIndex < numberSize - currentPowerIndex; outerLoopIndex += currentPowerIndex) {
            resultNumber = 0;
            for (innerLoopIndex = 0; innerLoopIndex < currentPowerIndex; innerLoopIndex++) {
                resultNumber += number[outerLoopIndex + innerLoopIndex] * multiplier[innerLoopIndex];
            }
            number[resultIndex++] = resultNumber;
        }

        resultNumber = 0;
        for (innerLoopIndex = 0; outerLoopIndex < numberSize; outerLoopIndex++, innerLoopIndex++) {
            resultNumber += number[outerLoopIndex] * multiplier[innerLoopIndex];
        }

        number[resultIndex++] = resultNumber;
        numberSize = resultIndex;
        givenBase = currentPowerValue;
    }

    int lastPosition = numberSize - 1;

    while (lastPosition >= 0) {
        int remainder = 0;

        for (int i = lastPosition; i >= 0; i--) {
            number[i] += remainder * givenBase;
            remainder = number[i] % finalBase;
            number[i] /= finalBase;
        }

        convertedNumber.push_back(remainder);

        while (lastPosition >= 0 && number[lastPosition] == 0) {
            lastPosition--;
        }
    }
    return convertedNumber;
}

void convertIntToString(vector<int>& number, string& convertedNumber) {
    char digit;
    convertedNumber.clear();
    convertedNumber.reserve(number.size());

    for (int i = number.size() - 1; i >= 0; i--) {
        if (number[i] >= 10) digit = number[i] + 'A' - 10;
        else digit = number[i] + '0';

        convertedNumber.push_back(digit);
    }
}

int main() {
    int N;
    string n, result;
    int r, s;

    scanf("%i", &N);

    for (int i = 0; i < N; i++) {
        cin >> n;
        scanf("%i %i", &r, &s);

        vector<int> givenNumber = convertStringToInt(n);

        vector<int> convertedNumber = changeBase(givenNumber, r, s);
        
        convertIntToString(convertedNumber, result);

        printf("%s\n", result.c_str());
    }
    return 0;
}