#include <iostream>
using namespace std;

int main() {
    int A[10];
    int num1, num2, temp;
    cin >> num1 >> num2;
    A[0] = num1;
    A[1] = num2;
    
    int i;
    for (i = 2; i < 10; i++) {
        temp = num1 + num2;
        if (temp >= 10) {
            temp = temp%10;
        }
        A[i] = temp;
        num1 = num2;
        num2 = temp;
    }

    for (i = 0; i < 10; i++) {
        cout << A[i] << ' ';
    }
    return 0;
}