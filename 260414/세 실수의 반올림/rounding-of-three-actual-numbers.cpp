#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a, b, c;

    cin >> a >> b >> c;
    cout << fixed;
    cout << setprecision(3);
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << c << std::endl;
    return 0;
}