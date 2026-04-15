#include <iostream>
using namespace std;

int div(int n) {
    int temp = (n * (n+1))/2;
    return temp/10;
}

int main() {
    int N;
    cin >> N;
    cout << div(N);
    // Please write your code here.
    return 0;
}