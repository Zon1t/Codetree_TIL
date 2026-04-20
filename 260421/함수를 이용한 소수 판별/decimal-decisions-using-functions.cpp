#include <iostream>
using namespace std;

int primes[4] = {2, 3, 5, 7};

bool is_prime(int n) {
    
    for (int i = 0; i < 4; i++) {
        if (n != primes[i] && n%primes[i] == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int start, end, total = 0;
    cin >> start >> end;

    for (int j = start; j <= end; j++) {
        if (is_prime(j)) {
            total += j;
        }
    }
    cout << total << endl;
    return 0;
}