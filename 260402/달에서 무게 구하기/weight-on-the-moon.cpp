#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int weight = 13;
    double gravity = 0.165;
    cout << weight << " * ";
    cout.setf(ios::fixed);
    cout.precision(6);
    cout << gravity << " = " << weight*gravity;
    return 0;
}