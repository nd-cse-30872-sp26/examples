// Exercise 06-A: Perfect Valid Square

#include <iostream>

using namespace std;

// Functions

bool is_perfect_square(long n) {
    // TODO: Use binary search to determine if n is a perfect valid square.
    return false;
}

// Main Execution

int main(int argc, char *argv[]) {
    long n;

    while (cin >> n) {
        cout << (is_perfect_square(n) ? "Yes" : "No") << endl;
    }

    return 0;
}
