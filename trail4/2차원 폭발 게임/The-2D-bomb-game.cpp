#include <iostream>

using namespace std;

int N, M, K;
int pointer1, pointer2;
int grid[100][100];
int temp[100][100];

bool InRange(int row, int col) {
	return 0 <= row && row < N && 0 <= col && col < N;
}

bool find() {
	bool is_bomb = false;
	for (int col = 0; col < N; col++) {
		pointer1 = 0;
		pointer2 = 1;
		while (pointer2 < N) {
			if (grid[pointer2][col] != grid[pointer2 - 1][col]) {
				if (pointer2 - pointer1 >= M && grid[pointer1][col] != 0) {
					is_bomb = true;
					for (int j = pointer1; j < pointer2; j++) {
						grid[j][col] = 0;
					}
				}
				pointer1 = pointer2;
				pointer2 = pointer1 + 1;
			}
			else {
				pointer2 += 1;
			}
		}
		if (pointer2 - pointer1 >= M && grid[pointer1][col] != 0) {
			is_bomb = true;
			for (int j = pointer1; j < pointer2; j++) {
				grid[j][col] = 0;
			}
		}
	}
	return is_bomb;
}

void apply_gravity() {
	for (int col = 0; col < N; col++) {
		int pointer = N - 1;
		for (int row = N - 1; 0 <= row; row--) {
			if (grid[row][col] != 0) {
				if (row != pointer) {
					grid[pointer][col] = grid[row][col];
					grid[row][col] = 0;
				}
				pointer -= 1;
			}
		}
	}
}

void rotate() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			temp[i][j] = 0;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			temp[i][j] = grid[N - 1 - j][i];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			grid[i][j] = temp[i][j];
		}
	}
}

int main() {
	cin >> N >> M >> K;
	for (int row = 0; row < N; row++) {
		for (int col = 0; col < N; col++) {
			cin >> grid[row][col];
		}
	}

	for (int t = 0; t < K; t++) {
		while (find()) {
			apply_gravity();
		}
		rotate();
		apply_gravity();
	}
	while (find()) {
		apply_gravity();
	}
	
	int answer = 0;
	for (int row = 0; row < N; row++) {
		for (int col = 0; col < N; col++) {
			if (grid[row][col] != 0) {
				answer += 1;
			}
		}
	}
	cout << answer << endl;
}