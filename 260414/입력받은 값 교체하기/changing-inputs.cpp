#include <iostream>
using namespace std;

int main() {
    int a, b;
    int temp = 0;

    cin >> a >> b;
    temp = a;
    a = b;
    b = temp;

    cout << a << ' ' << b;
    return 0;
}