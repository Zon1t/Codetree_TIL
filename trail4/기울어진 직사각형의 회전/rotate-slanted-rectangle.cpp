#include <iostream>

using namespace std;

int N, temp, start_row, start_col, now_dir, target_dir, dd, now_dist, next_row, next_col;
int r, c, dir;
int grid[100][100];
int dist[4];

int dr[4] = { -1, -1, 1, 1 };
int dc[4] = { 1, -1, -1, 1 };

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> grid[i][j];
		}
	}
	cin >> r >> c >> dist[0] >> dist[1] >> dist[2] >> dist[3] >> dir;
	
	r -= 1;
	c -= 1;
	start_row = r;
	start_col = c;

	if (dir == 0) {
		now_dir = 3;
		target_dir = 0;
		dd = -1;
	}
	else {
		now_dir = 0;
		target_dir = 3;
		dd = 1;
	}

	temp = grid[start_row][start_col];
	now_dist = 0;
	while (r != start_row || c != start_col || now_dir != target_dir) {
		if (now_dist != dist[now_dir]) {
			next_row = r + dr[now_dir] * dd;
			next_col = c + dc[now_dir] * dd;
			grid[r][c] = grid[next_row][next_col];
			r = next_row;
			c = next_col;
			now_dist += 1;
		}
		else {
			now_dir += dd;
			now_dist = 0;
		}
	}

	grid[start_row - dr[target_dir] * dd][start_col - dc[target_dir] * dd] = temp;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << grid[i][j] << " ";
		}
		cout << endl;
	}
}