#include <iostream>
using namespace std;

int main() {
    int start, end, temp, cnt = 0;
    cin >> start >> end;

    for (int i = start; i <= end; i++) {
        temp = 0;
        for (int j = 1; j <= i; j++) {
            if (i%j == 0) {
                temp++;
            }
        }
        if (temp == 3) {
            cnt++;
        }
    }

    cout << cnt;
    return 0;
}