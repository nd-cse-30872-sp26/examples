// Exercise 13-C: Binary Tree Height

#include <iostream>
#include <memory>

using namespace std;

// Node structures

template <typename T>
struct Node {
    T value;
    struct Node *left;
    struct Node *right;
};

// Find height of tree

template <typename T>
size_t height_tree(Node<T> *root) {
    // Base Case: Invalid Node
    if (root == nullptr) {
    	return 0;
    }

    // Divide and Conquer: Recursively solve left and right sub-trees
    size_t left  = height_tree(root->left);
    size_t right = height_tree(root->right);

    // Combine: Take maximum of sub-trees and add 1
    return max(left, right) + 1;
}

// Main execution

int main(int argc, char *argv[]) {
    Node<int> *root = new Node<int>{7,
    	new Node<int>{5,
    	    new Node<int>{3,
		new Node<int>{2, nullptr, nullptr},
		nullptr},
    	    nullptr
	},
    	new Node<int>{4,
    	    nullptr,
    	    new Node<int>{2, nullptr, nullptr}
	}
    };

    cout << height_tree(root) << endl;
    return 0;
}
