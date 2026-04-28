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

	sort(v.begin(), v.end(), cmp);
	for (int i = 0; i < N; i++) {
		v[i].first = v[i].second;
		v[i].second = i + 1;
	}

	sort(v.begin(), v.end(), cmp);
	for (int i = 0; i < N; i++) {
		cout << v[i].second << " ";
	}
}