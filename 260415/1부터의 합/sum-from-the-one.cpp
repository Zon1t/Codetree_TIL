#include <iostream>
using namespace std;

int main() {
    int N, i = 1, temp = 0;
    cin >> N;

    while (temp < N) {
        temp += i;
        i++;
    }
    cout << i-1;
    return 0;
}