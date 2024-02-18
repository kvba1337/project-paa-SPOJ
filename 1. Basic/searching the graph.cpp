// zrodla z ktorych czerpalem wiedze dotyczaca DFSa oraz BSA:
// https://www.youtube.com/watch?v=LzaSVPVluBU
// https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

#include <iostream>
#include <list>
#include <vector>
#include <queue>

using namespace std;

void dfs(int vertex, vector<bool>& visited, vector<list<int>>& adjacencyList) {
    visited[vertex] = true;
    cout << (vertex + 1) << " ";

    for (int neighborIndex : adjacencyList[vertex]) {
        if (!visited[neighborIndex]) {
            dfs(neighborIndex, visited, adjacencyList);
        }
    }
}

void bfs(int startVertex, int numberOfVertices, vector<list<int>>& adjacencyList) {
    vector<bool> visited(numberOfVertices, false);
    queue<int> q;

    visited[startVertex] = true;
    q.push(startVertex);

    while (!q.empty()) {
        int currentVertex = q.front();
        cout << (currentVertex + 1) << " ";
        q.pop();

        for (int neighborIndex : adjacencyList[currentVertex]) {
            if (!visited[neighborIndex]) {
                visited[neighborIndex] = true;
                q.push(neighborIndex);
            }
        }
    }
}

int main() {
    int t, numberOfVertices, vertexIndex, numberOfNeighbors, neighborIndex, startVertex, query;
    int graphNumber = 1;

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> numberOfVertices;

        vector<list<int>> adjacencyList(numberOfVertices);

        for (int j = 0; j < numberOfVertices; j++) {
            cin >> vertexIndex >> numberOfNeighbors;
            for (int k = 0; k < numberOfNeighbors; k++) {
                cin >> neighborIndex;
                adjacencyList[vertexIndex - 1].push_back(neighborIndex - 1);
            }
        }

        cout << "graph " << (graphNumber) << endl;
        graphNumber++;

        while (true) {
            cin >> startVertex >> query;
            if (startVertex == 0 && query == 0) break;
            else if (query == 0) {
                vector<bool> visited(numberOfVertices, false);
                dfs(startVertex - 1, visited, adjacencyList);
            }
            else bfs(startVertex - 1, numberOfVertices, adjacencyList);

            cout << endl;
        }
    }

    return 0;
}