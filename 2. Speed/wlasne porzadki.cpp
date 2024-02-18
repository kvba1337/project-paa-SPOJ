// zrodla z ktorych czerpalem wiedze:
// https://cpp0x.pl/dokumentacja/standard-C++/deque/1002
// https://www.youtube.com/watch?v=oGqjEx6hrI8
// https://codereview.stackexchange.com/questions/209055/most-efficient-way-to-find-an-entry-in-a-c-vector
// https://hackernoon.com/c-performance-optimization-best-practices

#include <iostream>
#include <algorithm>
#include <deque>
#include <unordered_map>

using namespace std;

void readInput(int& n, deque<int>& shelf, deque<int>& kValues, deque<int>& steps, unordered_map<int, int>& shelfMap) {
    scanf("%d", &n);
    int value;

    for (int i = 0; i < n; i++) {
        scanf("%d", &value);
        shelf.push_back(value);
        shelfMap[value] = i;
    }

    for (int i = 0; i < n; i++) {
        scanf("%d", &value);
        kValues.push_front(value);
    }

    while (scanf("%d", &value) != EOF) {
        steps.push_front(value);
    }
}

void printShelf(const deque<int>& shelf) {
    for (int value : shelf) {
        printf("%d ", value);
    }
    putchar('\n');
}

void updateShelfState(deque<int>& shelf, deque<int>& kValues, deque<int>& steps, unordered_map<int, int>& shelfMap, deque<int>& sortedShelf) {
    int counter = 1, kValue, foundValue, foundIndex, endIndex;

    while (!kValues.empty()) {
        kValue = kValues.back();
        kValues.pop_back();

        endIndex = shelf.size() - counter;
        foundValue = sortedShelf[sortedShelf.size() - kValue];

        if (kValue == 1) sortedShelf.pop_back();
        else sortedShelf.erase(sortedShelf.end() - kValue);

        foundIndex = shelfMap[foundValue];
        shelfMap[shelf[foundIndex]] = endIndex;
        shelfMap[shelf[endIndex]] = foundIndex;

        swap(shelf[foundIndex], shelf[endIndex]);

        if (steps.back() == counter) {
            printShelf(shelf);
            steps.pop_back();
        }
        counter++;
    }
}

int main() {
    int n;
    deque<int> shelf;
    deque<int> kValues;
    deque<int> steps;
    unordered_map<int, int> shelfMap;

    readInput(n, shelf, kValues, steps, shelfMap);

    deque<int> sortedShelf = shelf;
    sort(sortedShelf.begin(), sortedShelf.end());

    updateShelfState(shelf, kValues, steps, shelfMap, sortedShelf);

    return 0;
}