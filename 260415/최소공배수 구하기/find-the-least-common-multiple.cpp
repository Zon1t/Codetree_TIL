#include <iostream>
using namespace std;

int get_gcd(int n, int m) {
    int temp;
    while (m != 0) {
        temp = m;
        m = n%m;
        n = temp;
    }
    return n;
}

int main() {
    int N, M;
    cin >> N >> M;

    cout << N*M/get_gcd(M, N) << endl;
    return 0;
}