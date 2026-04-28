#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N, M, temp = 0;
	int temp_v, temp_t;
	cin >> N >> M;

	vector<int> a(1), b(1);

	for (int i = 0; i < N; i++) {
		cin >> temp_v >> temp_t;
		for (int j = 0; j < temp_t; j++) {
			a.push_back(a[temp] + temp_v);
			temp++;
		}
	}
	temp = 0;
	for (int i = 0; i < M; i++) {
		cin >> temp_v >> temp_t;
		for (int j = 0; j < temp_t; j++) {
			b.push_back(b[temp] + temp_v);
			temp++;
		}
	}

	int cnt = 0;
	for (int i = 0; i < a.size() - 1; i++) {
		if ((a[i] < b[i]) && (a[i + 1] >= b[i + 1])) {
			cnt += 1;
		}
		else if ((a[i] > b[i]) && (a[i + 1] <= b[i + 1])) {
			cnt += 1;
		}
		else if ((a[i] == b[i]) && (a[i+1] != b[i+1])) {
			cnt += 1;
		}
	}
	cout << cnt << endl;
}