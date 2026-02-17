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

Table compute_table(Grid &grid) {
    // TODO: 1. Initialize table

    // TODO: 2. Build table

    // TODO: 3. Use table result
}

// Main Execution

int main(int argc, char *argv[]) {
    size_t n;

    while (cin >> n) {
    	auto grid  = read_grid(n);
    	auto table = compute_table(grid);

    	cout << table[n][n] << endl;
    }

    return 0;
}
