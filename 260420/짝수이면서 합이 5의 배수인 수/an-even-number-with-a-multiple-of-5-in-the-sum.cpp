#include <iostream>
using namespace std;

int is_valid(int n) {
    if (n%2 == 0) {
        if ((n/100 + n/10 + n%10)%5 == 0) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

int main() {
    int n;
    cin >> n;

    if (is_valid(n)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}