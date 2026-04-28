#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	cin >> N;

	int arr[N];
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		if (i % 2 == 0) {
			sort(arr, arr + i + 1);
			cout << arr[i/2] << " ";
		}
	}
}