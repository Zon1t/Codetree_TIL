#include <iostream>
using namespace std;

int main() {
    int total = 0;
    int temp;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cin >> temp;
            if (j <= i) {
                total += temp;
            }
        }
    }
    cout << total;
    return 0;
}