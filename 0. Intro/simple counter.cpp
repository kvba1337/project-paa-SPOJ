#include <iostream>

using namespace std;

int main() {
	int lines=0, words=0, chars=0;
	char temp;
	bool inWord = false;

	while ((temp = getchar()) != EOF) {
		chars++;

		if (temp == '\n') lines++;

		if (isalpha(temp)) {
			if (!inWord) {
				inWord = true;
				words++;
			}
		} else inWord = false;
	}

	cout << lines << " " << words << " " << chars << endl;
}