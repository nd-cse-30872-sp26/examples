// coins.cpp

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// Functions

// Rather than looking backwards, we can generate the table by looking
// forwards.
vector<int> compute_table(size_t n, vector<int> &coins) {
    // Initialize table to n
    vector<int> table(n + 1, n);

    // Initialize base cases (ie. coins)
    for (auto coin : coins) {
    	table[coin] = 1;
    }

    // For each entry i in table, generate successive values:
    //
    //	table[i + coin] = min(table[i] + 1, table[i + coin])
    for (size_t i = 1; i < n; i++) {
    	for (auto coin : coins) {
	    try {
		table.at(i + coin) = min(table[i] + 1, table.at(i + coin));
	    } catch (out_of_range &e) {
	    	continue;
	    }
	}
    }

    return table;
}

// Main Execution

int main(int argc, char *argv[]) {
    vector<int> coins = {1, 3, 4};
    vector<int> table = compute_table(100, coins);
    size_t n;

    while (cin >> n) {
    	cout << n << " = " << table[n] << endl;
    }
    
    return 0;
}
