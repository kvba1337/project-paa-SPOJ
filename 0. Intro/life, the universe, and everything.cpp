#include <iostream>

using namespace std;

int main() {
	int x;

	while (cin >> x) {
		if (x == 42)
			break;
		else cout << x << endl;
	}

	while (cin >> x) {
		continue;
	}
}