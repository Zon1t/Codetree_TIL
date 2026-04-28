#include <iostream>
#include <vector>
using namespace std;

bool in_range(int row, int col, int N, int M) {
	return (0 <= row && row < N && 0 <= col && col < M);
}

int main()
{
	int dr[4] = { 0, 1, 0, -1 };
	int dc[4] = { 1, 0, -1, 0 };

	int N, M;
	cin >> N >> M;

	int now_direction = 0, curr_row = 0, curr_col = 0;
	int next_row, next_col;

	int grid[N][M];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			grid[i][j] = 0;
		}
	}

	for (int i = 1; i <= N * M; i++) {
		grid[curr_row][curr_col] = i;
		next_row = curr_row + dr[now_direction];
		next_col = curr_col + dc[now_direction];
		if (in_range(next_row, next_col, N, M) && (grid[next_row][next_col] == 0)) {
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
		for (int j = 0; j < M; j++) {
			cout << grid[i][j] << " ";
		}
		cout << endl;
	}
}