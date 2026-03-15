// Exercise 13-B: Binary Tree Min

#include <climits>
#include <iostream>
#include <memory>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T     value;
    Node *left;
    Node *right;
};

// Find minimum of tree

template <typename T>
T minimum_tree(Node<T> *root) {
    // Base case: Invalid Node
    if (!root) {
    	return INT_MAX;
    }

    // Divide and Conquer: Recursively solve left and right sub-trees
    T left_minimum  = minimum_tree(root->left);
    T right_minimum = minimum_tree(root->right);

    // Combine: Take minimum of current node and left and right minimums
    return min(root->value, min(left_minimum, right_minimum));
}

// Main execution

int main(int argc, char *argv[]) {
    Node<int> *root = new Node<int>{7,
    	new Node<int>{5,
    	    new Node<int>{3, nullptr, nullptr},
    	    nullptr
	},
    	new Node<int>{4,
    	    nullptr,
    	    new Node<int>{2, nullptr, nullptr}
	}
    };

    cout << minimum_tree(root) << endl;
    return 0;
}
