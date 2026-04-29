#include <iostream>

using namespace std;

int N;
int grid[20][20];

int dr[4] = { 1, 1, -1, -1 };
int dc[4] = { -1, 1, 1, -1 };

int max_sum = 0;

bool InRange(int row, int col) {
	return (0 <= row && row < N && 0 <= col && col < N);
}

void backtrack(int row, int col, int direction, int dist, int cum_sum, int start_row, int start_col) {
	if (direction == 3 && 0 < dist && row == start_row && col == start_col) {
		if (max_sum < cum_sum) {
			max_sum = cum_sum;
		}
		return;
	}
	if (0 < dist) {
		backtrack(row, col, direction + 1, 0, cum_sum, start_row, start_col);
	}
	int next_row = row + dr[direction];
	int next_col = col + dc[direction];
	if (InRange(next_row, next_col)) {
		backtrack(next_row, next_col, direction, dist + 1, cum_sum + grid[next_row][next_col], start_row, start_col);
	}
}

int main() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> grid[i][j];
		}
	}

	// Please write your code here.

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			backtrack(i, j, 0, 0, 0, i, j);
		}
	}
	cout << max_sum << endl;

	return 0;
}
