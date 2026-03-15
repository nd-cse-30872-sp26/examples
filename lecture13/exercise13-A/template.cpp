// Exercise 13-A: Traversal

#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

// Node structure

template <typename T>
struct Node {
    T	  value;
    Node *left;
    Node *right;
};

// Pre-defined Trees

Node<char> *AlgorithmTree() {
    return new Node<char>{'A',
    	new Node<char>{'L',
	    new Node<char>{'O',
		new Node<char>{'H', nullptr, nullptr},
		new Node<char>{'M', nullptr, nullptr}
	    },
	    new Node<char>{'R', nullptr, nullptr}
	},
	new Node<char>{'G',
	    new Node<char>{'I', nullptr, nullptr},
	    new Node<char>{'T', nullptr, nullptr}
	}
    };
}

// Traversal: BFS (Iterative)

template <typename T>
void bfs(Node<T> *root) {
}

// Traversal: DFS (Iterative)

template <typename T>
void dfs(Node<T> *root) {
}

// Traversal: DFS (Recursive)

template <typename T>
void dfs_recursive(Node<T> *root) {
}

// Main execution

int main(int argc, char *argv[]) {
    auto tree = AlgorithmTree();

    cout << "BFS:"; bfs(tree); cout << endl;
    cout << "DFS:"; dfs(tree); cout << endl;
    cout << "DFS:"; dfs_recursive(tree); cout << endl;

    return EXIT_SUCCESS;
}
