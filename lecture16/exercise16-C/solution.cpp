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
    Graph  graph;
    string digits;
    
    while (cin >> digits) {
    	graph.edges[digits[0]].insert(digits[1]);
    	graph.edges[digits[1]].insert(digits[2]);
    }

    for (auto e : graph.edges) {
    	auto s  = e.first;
    	auto ts = e.second;

    	graph.degrees[s];
    	for (auto t : ts) {
    	    graph.degrees[t] += 1;
	}
    }

    return graph;
}

string topological_sort(Graph &graph) {
    queue<int>	frontier;
    string	visited;

    for (auto d : graph.degrees) {
    	if (d.second == 0) {
    	    frontier.push(d.first);
	}
    }

    while (!frontier.empty()) {
    	auto vertex = frontier.front(); frontier.pop();

    	visited += vertex;

    	for (auto neighbor : graph.edges[vertex]) {
    	    graph.degrees[neighbor] -= 1;
    	    if (graph.degrees[neighbor] == 0) {
    	    	frontier.push(neighbor);
	    }
	}
    }

    return visited;
}

// Main Execution

int main(int argc, char *argv[]) {
    auto graph = read_graph();
    auto code  = topological_sort(graph);

    cout << code << endl;
    return EXIT_SUCCESS;
}
