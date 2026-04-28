#include <iostream>
using namespace std;

int get_lcm(int n, int m) {
	int temp, a, b;
	a = n;
	b = m;
	while (a%b != 0) {
		temp = a % b;
		a = b;
		b = temp;
	}
	return n * m / b;
}
int main()
{
	int N;
	cin >> N;

	int temp, answer = 1;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		answer = get_lcm(answer, temp);
	}
	cout << answer << endl;
}