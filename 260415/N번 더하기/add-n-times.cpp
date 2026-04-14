#include <iostream>
using namespace std;

int main() {
    int start, delta;

    cin >> start >> delta;

    int i;
    int temp = start;
    for (i = 0; i < delta; i++) {
        temp += delta;
        cout << temp << endl;
    }
    return 0;
}