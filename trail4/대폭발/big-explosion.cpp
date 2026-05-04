#include <iostream>
#include <vector>

using namespace std;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };
int N, M, r, c;

bool InRange(int row, int col) {
	return 0 <= row && row < N && 0 <= col && col < N;
}

int main() {
	cin >> N >> M >> r >> c;

	vector<pair<int, int>> bombs = {};
	bombs.push_back({ r - 1, c - 1 });
	for (int k = 0; k < M; k++) {
		vector<pair<int, int>> temp = {};
		for (int i = 0; i < bombs.size(); i++) {
			int curr_row = bombs[i].first;
			int curr_col = bombs[i].second;
			for (int d = 0; d < 4; d++) {
				int next_row = curr_row + dr[d] * (1 << k);
				int next_col = curr_col + dc[d] * (1 << k);

				if (InRange(next_row, next_col)) {
					temp.push_back({ next_row, next_col });
				}
			}
		}
		for (int i = 0; i < temp.size(); i++) {
			bool can_put = true;
			for (int j = 0; j < bombs.size(); j++) {
				if (temp[i] == bombs[j]) {
					can_put = false;
					break;
				}
			}
			if (can_put) {
				bombs.push_back(temp[i]);
			}
		}
	}
	cout << bombs.size() << endl;
}