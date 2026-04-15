#include <iostream>
using namespace std;

int get_min(int n, int m) {
    if (n < m) {
        return n;
    } else {
        return m;
    }
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << get_min(get_min(a, b), c);
    return 0;
}