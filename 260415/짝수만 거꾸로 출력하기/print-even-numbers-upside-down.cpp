#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int A[N], temp, i;
    for (i = 0; i < N; i++) {
        cin >> temp;
        A[i] = temp;
    }
    for (i = N-1; i >= 0; i--) {
        if (A[i]%2 == 0) {
            cout << A[i] << ' ';
        }
    }
    return 0;
}