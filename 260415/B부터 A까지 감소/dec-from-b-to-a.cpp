#include <iostream>
using namespace std;

int main() {
    int end, start;
    cin >> end >> start;

    int i = start;
    for (i; i >= end; i--){
        cout << i << ' ';
    }
    return 0;
}