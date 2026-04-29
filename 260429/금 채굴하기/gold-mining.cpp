#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int n, m;
int grid[20][20];

bool InRange(int row, int col, int N) {
	return (0 <= row && row < N && 0 <= col && col < N);
}

int abs(int n) {
	return n >= 0 ? n : -n;
}

vector<tuple<int, int>> make_rh(int k) {
	vector<tuple<int, int>> deltas;
	for (int a = -k; a <= k; a++) {
		for (int b = -k; b <= k; b++) {
			if (abs(a) + abs(b) <= k) {
				deltas.push_back({ a, b });
			}
		}
	}
	return deltas;
}

int main() {
	cin >> n >> m;
	
	vector<vector<tuple<int, int>>> deltas;
	for (int k = 0; k <= n; k++) {
		deltas.push_back(make_rh(k));
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
		}
	}

	// Please write your code here.
	int max_gold = 0, curr_gold, cost, curr_row, curr_col;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k <= n; k++) {
				curr_gold = 0;
				cost = 2 * k*k + 2 * k + 1;
				vector<tuple<int, int>> delta = deltas[k];
				for (int l = 0; l < delta.size(); l++) {
					curr_row = i + get<0>(delta[l]);
					curr_col = j + get<1>(delta[l]);
					if (InRange(curr_row, curr_col, n) && grid[curr_row][curr_col] == 1) {
						curr_gold += 1;
					}
				}
				if (cost <= curr_gold * m && max_gold < curr_gold) {
					max_gold = curr_gold;
				}
			}
		}
	}
	cout << max_gold << endl;

	return 0;
}
