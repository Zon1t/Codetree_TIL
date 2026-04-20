#include <iostream>
using namespace std;

int bound[12] = {31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30};

bool is_valid(int month, int day) {
    if ((1 <= day) && (day <= bound[month])) {
        return true;
    } else {
        return false;
    }
}

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
    int year, month, day;
    cin >> year >> month >> day;
    month %= 12;

    if (month == 2 && is_yoon(year)) {
        bound[2] = 29;
    }

    if (is_valid(month, day)) {
        if (month <= 2) {
            cout << "Winter" << endl;
        } else if (month <= 5) {
            cout << "Spring" << endl;
        } else if (month <= 8) {
            cout << "Summer" << endl;
        } else {
            cout << "Fall" << endl;
        } 
    } else {
        cout << -1 << endl;
    }
    // Please write your code here.
    return 0;
}