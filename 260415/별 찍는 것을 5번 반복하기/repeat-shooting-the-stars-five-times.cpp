#include <iostream>
using namespace std;

void print_star() {
    cout << "**********" << endl;
}

int main() {
    for (int i = 0; i < 5; i++) {
        print_star();
    }
    return 0;
}