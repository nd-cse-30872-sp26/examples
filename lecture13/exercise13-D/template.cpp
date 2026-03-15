// Exercise 13-D: Invert Binary Tree

#include <iostream>
#include <memory>
#include <queue>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T value;
    struct Node *left;
    struct Node *right;
};

typedef Node<int> IntNode;

// Functions

bool read_values(vector<int> &values) {
    values.clear();

    string line;
    if (getline(cin, line)) {
    	stringstream ss(line);
    	int i;

    	while (ss >> i) {
    	    values.push_back(i);
	}
    }

    return !values.empty();
}

IntNode*  read_tree(vector<int> &values, size_t index=0) {
    return nullptr;
}

void	dump_tree(IntNode *root) {
}

IntNode*    invert_tree(IntNode *root) {
    // Base Case: Invalid Node

    // Divide and Conquer: Swap left and right and recurse
    return nullptr;
}

// Main execution

int main(int argc, char *argv[]) {
    vector<int> values;

    while (read_values(values)) {
    	auto root = read_tree(values);
    	invert_tree(root);
    	dump_tree(root);
    }

    return 0;
}
