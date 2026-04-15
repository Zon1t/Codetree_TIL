#include <iostream>
using namespace std;

int main() {
    int N, temp = 1;
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= i; j++) {
            cout << temp << " ";
            temp++;
        }
        cout << "\n";
    }

    return 0;
}