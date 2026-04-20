#include <iostream>
using namespace std;

int can_divide_3(int n) {
    if (n%3 == 0) {
        return true;
    } else {
        return false;
    }
}

int is_in_369(int n) {
    while (n > 0) {
        int digit = n%10;
        if (digit == 3 || digit == 6 || digit == 9) {
            return true;
        }
        n /= 10;
    }
    return false;
}

int main() {
    int start, end, cnt = 0;
    cin >> start >> end;

    for (int i=start; i <= end; i++) {
        if (can_divide_3(i) || is_in_369(i)) {
            cnt += 1;
        }
    }
    cout << cnt << endl;
    return 0;
}