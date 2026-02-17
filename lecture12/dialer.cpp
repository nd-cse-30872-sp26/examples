// Example: Knight's Dialer (Dynamic Programming)

#include <iostream>
#include <map>
#include <tuple>
#include <vector>

using namespace std;

// Globals

map<int, vector<int>> NEIGHBORS = {
    {1, {6, 8}},
    {2, {7, 9}},
    {3, {4, 8}},
    {4, {0, 3, 9}},
    {5, {}},
    {6, {0, 1, 7}},
    {7, {2, 6}},
    {8, {1, 3}},
    {9, {2, 4}},
    {0, {4, 6}},
};

map<tuple<int, int>, int> CACHE;

// Functions

int dial_numbers_count(int start, int length) {
    // Version 1: Recursive
    if (length == 1) {	// Base case
    	return 1;
    } else {		// Recursive step
    	int count = 0;
    	for (auto neighbor : NEIGHBORS[start]) {
    	    count += dial_numbers_count(neighbor, length - 1);
	}
	return count;
    }
}

int dial_numbers_count_cached(int start, int length) {
    // Version 1: Recursive (with Memoization)
    if (length == 1) {	// Base case
    	return 1;
    } else {		// Recursive step
    	auto pair = make_tuple(start, length);
    	if (!CACHE.count(pair)) {
	    int count = 0;
	    for (auto neighbor : NEIGHBORS[start]) {
		count += dial_numbers_count(neighbor, length - 1);
	    }
	    CACHE[pair] = count;

	}
	return CACHE[pair];
    }
}

int dial_numbers_count_table(int start, int length) {
    // Version 3: Table Building in O(n^2) space
    // Initialize Table
    vector<vector<int>> table(NEIGHBORS.size(), vector<int>(length + 1, 0));

    // Initialize Base Case: 1 Permutation to Length 1
    for (size_t number = 0; number < NEIGHBORS.size(); number++) {
    	table[number][1] = 1;
    }

    // Compute Permutations(Number, Hops):
    //
    //	Permutations(Number, Hops) = Sum(
    //	    Permutations(Neighbor, Hops - 1) for Neighbor in Neighbors
    //	)
    for (int hops = 2; hops <= length; hops++) {
	for (size_t number = 0; number < NEIGHBORS.size(); number++) {
	    int sum = 0;
	    for (auto neighbor : NEIGHBORS[number]) {
	    	sum += table[neighbor][hops - 1];
	    }
	    table[number][hops] += sum;
	}
    }

    return table[start][length];
}

// Main Execution

int main(int argc, char *argv[]) {
    int start, length;
    while (cin >> start >> length) {
    	// cout << dial_numbers_count(start, length) << endl;
    	// cout << dial_numbers_count_cached(start, length) << endl;
    	cout << dial_numbers_count_table(start, length) << endl;
    }
    return 0;
}
