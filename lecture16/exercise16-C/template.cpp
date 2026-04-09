// Exercise 16-C: Passcode Cracking

#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// Structures

struct Graph {
    unordered_map<char, unordered_set<char>> edges;
    unordered_map<char, int>		     degrees;
};

// Functions

Graph read_graph() {
    // TODO
}

string topological_sort(Graph &graph) {
    // TODO
}

// Main Execution

int main(int argc, char *argv[]) {
    auto graph = read_graph();
    auto code  = topological_sort(graph);

    cout << code << endl;
    return EXIT_SUCCESS;
}
