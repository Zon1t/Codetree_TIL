#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    string temp = "*";

    for (int i = 0; i < N; i++) {
        cout << temp << endl;
        temp += "**";
    }
    return 0;
}