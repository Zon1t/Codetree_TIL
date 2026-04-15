#include <iostream>
using namespace std;

int main() {
    string S;
    cin >> S;

    S[1] = 'a';
    S[S.length()-2] = 'a';
    cout << S;
    return 0;
}