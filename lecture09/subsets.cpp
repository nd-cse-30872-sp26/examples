// subsets.cpp

#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

// Functions

size_t subsets(vector<int> &s, vector<int> &c, size_t k) {
    if (k == c.size()) { // Base: have complete subset
    	// for (auto e : s) { cout << " " << e; }; cout << endl;
    	return (accumulate(s.begin(), s.end(), 0) % 3 == 0) ? 1 : 0;
    }

    // Recurse: skip current
    size_t count1 = subsets(s, c, k + 1);

    // Recurse: with current
    s.push_back(c[k]);
    size_t count2 = subsets(s, c, k + 1);
    s.pop_back(); // Reset subset
    
    return count1 + count2;
}

// Main execution

int main(int argc, char *argv[]) {
    vector<int> subset;
    vector<int> numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    size_t      count   = subsets(subset, numbers, 0);

    cout << count << endl;
    return 0;
}
