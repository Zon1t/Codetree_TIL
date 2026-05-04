#include <iostream>

using namespace std;

int N, M;
int grid[200][200];
int columns[10];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool InRange(int row, int col) {
	return 0 <= row && row < N && 0 <= col && col < N;
}

void explore(int col) {
	int row = -1, k, next_row, next_col;
	for (int y = 0; y < N; y++) {
		if (grid[y][col] != 0) {
			row = y;
			k = grid[row][col];
			break;
		}
	}

	if (row != -1) {
		grid[row][col] = 0;
		for (int j = 1; j < k; j++) {
			for (int d = 0; d < 4; d++) {
				next_row = row + dr[d] * j;
				next_col = col + dc[d] * j;
				if (InRange(next_row, next_col)) {
					grid[next_row][next_col] = 0;
				}
			}
		}
	}
}

void apply_gravity() {
	for (int c = 0; c < N; c++) {
		int pointer = N-1;
		for (int r = N - 1; 0 <= r; r--) {
			if (grid[r][c] != 0) {
				if (r != pointer) {
					grid[pointer][c] = grid[r][c];
					grid[r][c] = 0;
				}
				pointer -= 1;
			}
		}
	}
}


int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> grid[i][j];
		}
	}
	for (int i = 0; i < M; i++) {
		cin >> columns[i];
	}

	for (int i = 0; i < M; i++) {
		explore(columns[i] - 1);
		apply_gravity();
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << grid[i][j] << ' ';
		}
		cout << endl;
	}
}