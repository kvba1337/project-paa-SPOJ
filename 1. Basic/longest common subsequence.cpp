// zrodla z ktorych czerpalem wiedze dotyczaca najdluzszego wspolnego podciagu:
// https://en.wikipedia.org/wiki/Longest_common_subsequence
// https://www.youtube.com/watch?v=sSno9rV8Rhg

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void printAnswer(const string& X, const string& Y, int n, int m, const vector<vector<int>>& table) {
    cout << "Y" << endl;
    cout << table[0][0] << endl;

    int i = 0, j = 0;

    while (i < n && j < m) {
        if (X[i] == Y[j]) {
            cout << X[i] << " " << i + 1 << " " << j + 1 << endl;
            i++;
            j++;
        }
        else {
            if (table[i + 1][j] > table[i][j + 1]) i++;
            else j++;
        }
    }
}

void lcs(const string& X, const string& Y, int n, int m) {
    vector<vector<int>> table(n + 1, vector<int>(m + 1, 0));

    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            if (X[i] == Y[j]) {
                table[i][j] = table[i + 1][j + 1] + 1;
            }
            else {
                table[i][j] = max(table[i + 1][j], table[i][j + 1]);
            }
        }
    }
    
    if (table[0][0] == 0) {
        cout << "N" << endl;
    }
    else {
        printAnswer(X, Y, n, m, table);
    }
}


int main() {
    int N, n, m;
    string x, y;
    int caseNumber = 1;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> n >> x;
        cin >> m >> y;

        cout << "case " << caseNumber << " ";
        caseNumber++;

        lcs(x, y, n, m);
    }

    return 0;
}