// cheatsheet.cpp

#include <iostream>
#include <map>

using namespace std;

int main(int argc, char *argv[]) {
    // Create map
    map<char, int> table = {
	{'a', 0},
	{'b', 1},
	{'c', 2},
    };

    // Add pair to map
    table['d'] = 3;

    // Access value
    cout << table['b'] << endl;
    cout << table.at('b') << endl;

    // Display number of pairs
    cout << table.size() << endl;

    // Traverse pairs
    for (auto pair : table) {
    	cout << pair.first << " " << pair.second << endl;
    }

    // Search
    cout << table.count('a') << endl;
    cout << table.find('a')->first  << endl;

    return 0;
}
