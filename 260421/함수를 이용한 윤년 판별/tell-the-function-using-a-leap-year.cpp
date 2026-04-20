#include <iostream>
using namespace std;

bool is_yoon(int year) {
    if (year % 4 == 0) {
        if (year % 100 == 0 && year % 400 != 0) {
            return false;
        } else {
            return true;
        }
    } else {
        return false;
    }
}

int main() {
    int year;
    cin >> year;

    if (is_yoon(year)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    return 0;
}