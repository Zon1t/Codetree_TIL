#include <iostream>
using namespace std;

int main() {
    int A[5] = {3, 1, 4, 5, 9};

    int total = 0;
    int i;
    for (i = 0; i < 5; i++) {
        if (i == 1 || i == 3 || i == 4) {
            total += A[i];
        }
    }
    cout << total;
    return 0;
}