#include <iostream>
using namespace std;

int main() {
    int cnt = 0; char c;
    string s[5] = {"apple", "banana", "grape", "blueberry", "orange"};

    cin >> c;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < s[i].length(); j++) {
            if (s[i][j] == c && (j==2 || j==3)) {
                cout << s[i] << endl;
                cnt++;
                break;
            }
        }
    }
    cout << cnt << endl;
    
    return 0;
}