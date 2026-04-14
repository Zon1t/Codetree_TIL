#include <iostream>
using namespace std;

int main() {
    int start, delta;

    cin >> start >> delta;

    int i;
    for (i = 0; i < delta; i++) {
        start += delta;
        cout << start << endl;
    }
    return 0;
}