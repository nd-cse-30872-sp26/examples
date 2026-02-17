// Exercise 12-B: Squirrel Hunting

#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

// Type Definitions

typedef vector<int> Row;
typedef vector<Row> Grid;
typedef vector<Row> Table;
typedef deque<int>  Path;

// Functions

Grid read_grid(size_t n) {
    Grid grid(n + 1, Row(n + 1, 0));	// Pad Grid

    for (size_t r = 1; r <= n; r++) {
	for (size_t c = 1; c <= n; c++) {
	    cin >> grid[r][c];
	}
    }

    return grid;
}

Table hunt_squirrels(Grid &grid) {
    // 1. Initialize table
    Table table(grid.size(), Row(grid[0].size()));

    // 2. Table[row][col] = Grid[row][col] + max(from_left, from_above)
    //
    //	S(r, c) = Max(S(r, c - 1), S(r - 1, c)) + G(r, c)
    for (size_t row = 1; row < grid.size(); row++) {
    	for (size_t col = 1; col < grid[0].size(); col++) {
    	    table[row][col] = grid[row][col] + max(
    	    	table[row][col - 1],
    	    	table[row - 1][col]
    	    );
	}
    }

    // 3. Use table result
    return table;
}

Path find_path(Grid &grid, size_t n, Table &table) {
    // Reconstruct the path by going from end to beginning
    Path   path;
    size_t r = n;
    size_t c = n;

    while (r > 0 && c > 0) {
    	// Add current position to path
    	path.push_front(grid[r][c]);

    	// Consider which path we took based on the values in the table
    	if (table[r][c] - grid[r][c] == table[r][c - 1]) {
    	    c -= 1;
	} else {
	    r -= 1;
	}
    }

    return path;
}


// Main Execution

int main(int argc, char *argv[]) {
    size_t n;

    while (cin >> n) {
    	auto grid  = read_grid(n);
    	auto table = hunt_squirrels(grid);

    	cout << table[n][n] << endl;

    	/*
    	auto path  = find_path(grid, n, table);
    	cout << "[" << path[0];
    	for (size_t i = 1; i < path.size(); i++) {
    	    cout << ", " << path[i];
	}
	cout << "]" << endl;
	*/
    }

    return 0;
}
