// Exercise 12-A: Climbing Stairs

#include <iostream>
#include <unordered_map>

using namespace std;

// Functions

size_t count_steps(size_t n, unordered_map<size_t, size_t> &cache) {
    // TODO: Determine number of distinct ways to climb n steps using only
    // increments of 1 or 2 steps at a time.
    return 0;
}

// Main Execution

int main(int argc, char *argv[]) {
    // XXX: Because we are using size_t we will not be able to represent
    // really large numbers
    
    unordered_map<size_t, size_t> cache;
    size_t n;

    while (cin >> n) {
    	cout << count_steps(n, cache) << endl;
    }

    return 0;
}
