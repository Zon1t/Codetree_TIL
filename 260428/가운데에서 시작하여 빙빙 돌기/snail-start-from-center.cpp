#include <iostream>
#include <vector>
using namespace std;

bool in_range(int row, int col, int N) {
	return (0 <= row && row < N && 0 <= col && col < N);
}

int main()
{
	int dr[4] = { 0, -1, 0, 1 };
	int dc[4] = { -1, 0, 1, 0 };

	int N;
	cin >> N;

	int grid[N][N];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			grid[i][j] = 0;
		}
	}

	int curr_row = N - 1, curr_col = N - 1, now_direction = 0;
	int next_row, next_col;

	for (int i = N * N; 0 < i; i--) {
		grid[curr_row][curr_col] = i;
		next_row = curr_row + dr[now_direction];
		next_col = curr_col + dc[now_direction];

		if (in_range(next_row, next_col, N) && grid[next_row][next_col] == 0) {
			curr_row = next_row;
			curr_col = next_col;
		}
		else {
			now_direction = (now_direction + 1) % 4;
			curr_row += dr[now_direction];
			curr_col += dc[now_direction];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << grid[i][j] << " ";
		}
		cout << endl;
	}
}