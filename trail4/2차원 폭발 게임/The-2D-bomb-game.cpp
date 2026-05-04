#include <iostream>
#include <vector>
using namespace std;

bool need_more_bomb(vector<vector<int>>& grid, int N, int M) {
	for (int col = 0; col < N; col++) {
		int cnt = 1, val = grid[0][col];
		if (grid[0][col] == 0) {
			val = -1;
		}
		for (int row = 1; row < N; row++) {
			if (grid[row][col] == val) {
				cnt++;
			}
			else {
				if (cnt >= M && val != -1) {
					int x = row - 1;
					for (int t = 0; t < cnt; t++) {
						return true;
					}
				}
				cnt = 1;
				val = grid[row][col];
				if (grid[row][col] == 0) {
					val = -1;
				}
			}
		}
		if (cnt >= M && val != -1) {
			int x = N - 1;
			for (int t = 0; t < cnt; t++) {
				return true;
			}
		}
	}
	return false;
}

void bomb(vector<vector<int>>& grid, int N, int M) {
	for (int col = 0; col < N; col++) {
		int cnt = 1, val = grid[0][col];
		if (grid[0][col] == 0) {
			val = -1;
		}
		for (int row = 1; row < N; row++) {
			if (grid[row][col] == val) {
				cnt++;
			}
			else {
				if (cnt >= M) {
					int x = row - 1;
					for (int t = 0; t < cnt; t++) {
						grid[x][col] = 0;
						x--;
					}
				}
				cnt = 1;
				val = grid[row][col];
				if (grid[row][col] == 0) {
					val = -1;
				}
			}
		}
		if (cnt >= M) {
			int x = N - 1;
			for (int t = 0; t < cnt; t++) {
				grid[x][col] = 0;
				x--;
			}
		}
	}

	// 중력 받아 내려오기
	for (int i = N - 1; i >= 0; i--) {
		for (int j = 0; j < N; j++) {
			if (grid[i][j] > 0) {
				for (int x = N - 1; x > i; x--) {
					if (grid[x][j] == 0) {
						grid[x][j] = grid[i][j];
						grid[i][j] = 0;
						break;
					}
				}
			}
		}
	}
}

void turn(int N, vector<vector<int>>& grid) {
	vector<vector<int>> temp(N, vector<int>(N, 0));
	for (int row = N - 1; row >= 0; row--) {
		for (int col = 0; col < N; col++) {
			temp[col][N - 1 - row] = grid[row][col];
		}
	}

	// 중력 받아 내려오기
	for (int i = N - 1; i >= 0; i--) {
		for (int j = 0; j < N; j++) {
			if (temp[i][j] > 0) {
				for (int x = N - 1; x > i; x--) {
					if (temp[x][j] == 0) {
						temp[x][j] = temp[i][j];
						temp[i][j] = 0;
						break;
					}
				}
			}
		}
	}
	// temp를 다시 grid에 넣기
	for (int x = 0; x < N; x++) {
		for (int y = 0; y < N; y++) {
			grid[x][y] = temp[x][y];
		}
	}
}

int main() {
	int N, M, K;
	cin >> N >> M >> K;
	vector<vector<int>> grid(N, vector<int>(N, 0));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> grid[i][j];
		}
	}

	for (int k = 0; k < K; k++) {
		while (need_more_bomb(grid, N, M)) {
			bomb(grid, N, M);
		}
		turn(N, grid);
	}
	while (need_more_bomb(grid, N, M)) {
		bomb(grid, N, M);
	}

	// 남은 폭탄 개수 세기
	int answer = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (grid[i][j] > 0) {
				answer++;
			}
		}
	}
	cout << answer;
	return 0;
}
