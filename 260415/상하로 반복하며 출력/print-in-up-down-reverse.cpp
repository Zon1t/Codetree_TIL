#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        for (int j = 0; j < N; j++) {
            if (j%2 == 0) {
                cout << i;
            } else {
                cout << N-i+1;
            }
        }
        cout << "\n";
    }
    return 0;
}