#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
	return a.first < b.first;
}

int main()
{
	int N, temp;
	cin >> N;

	vector<pair<int, int>> v(N);
	for (int i = 0; i < N; i++) {
		cin >> v[i].first;
		v[i].second = i + 1;
	}

	stable_sort(v.begin(), v.end(), cmp);
	
	vector<int> answer(N + 1);
	for (int i = 0; i < N; i++) {
		answer[v[i].second] = i + 1;
	}

	for (int i = 1; i <= N; i++) {
		cout << answer[i] << " ";
	}
}