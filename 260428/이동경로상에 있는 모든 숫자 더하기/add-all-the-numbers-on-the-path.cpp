#include <iostream>
#include <vector>
using namespace std;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool in_range(int row, int col, int N) {
	return (0 <= row && row < N && 0 <= col && col < N);
}

int main()
{
	int N, T;
	cin >> N >> T;

	string commands;
	cin >> commands;

	int grid[N][N];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> grid[i][j];
		}
	}

	int curr_row = N / 2, curr_col = N / 2, curr_direction = 3;
	int next_row, next_col, answer = grid[curr_row][curr_col];

	for (int i = 0; i < T; i++) {
		if (commands[i] == 'R') {
			curr_direction = (curr_direction + 1) % 4;
		}
		else if (commands[i] == 'L') {
			curr_direction -= 1;
			if (curr_direction < 0) {
				curr_direction += 4;
			}
		}
		else {
			next_row = curr_row + dr[curr_direction];
			next_col = curr_col + dc[curr_direction];
			if (in_range(next_row, next_col, N)) {
				curr_row = next_row;
				curr_col = next_col;
				answer += grid[curr_row][curr_col];
			}
		}
	}
	cout << answer << endl;
}