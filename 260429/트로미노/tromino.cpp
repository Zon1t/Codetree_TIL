#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

vector<vector<tuple<int, int>>> block_delta = {
	{
		{0, 0}, {0, 1}, {1, 0}
	}, {
		{0, 0}, {1, 0}, {1, 1}
	}, {
		{0, 1}, {1, 0}, {1, 1}
	}, {
		{0, 0}, {0, 1}, {1, 1}
	}, {
		{0, 0}, {0, 1}, {0, 2}
	}, {
		{0, 0}, {1, 0}, {2, 0}
	}
};

bool InRange(int row, int col, int N, int M) {
	return (0 <= row && row < N && 0 <= col && col < M);
}

int calc_score(int* grid, int curr_row, int curr_col, vector<tuple<int, int>> delta, int N, int M) {
	int score = 0;
	for (int c = 0; c < 3; c++) {
		int row = curr_row + get<0>(delta[c]);
		int col = curr_col + get<1>(delta[c]);
		if (InRange(row, col, N, M)) {
			score += grid[row * M + col];
		}
		else {
			return 0;
		}
	}
	return score;
}


int main()
{
	int N, M;
	cin >> N >> M;

	int grid[N][M];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> grid[i][j];
		}
	}

	int max_score = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			for (int k = 0; k < 6; k++) {
				int temp_score = calc_score((int*)grid, i, j, block_delta[k], N, M);
				if (max_score < temp_score) {
					max_score = temp_score;
				}
			}
		}
	}
	cout << max_score << endl;
}