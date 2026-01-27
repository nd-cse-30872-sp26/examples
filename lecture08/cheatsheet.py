#!/usr/bin/env python3

# Create map

table = {
    'a': 0,
    'b': 1,
    'c': 2,
}

# Add pair to map

table['d'] = 3

# Access value

print(table['b'])

# Display number of pairs

print(len(table))

# Traverse pairs (keys)

for key in table:
    print(key, table[key])

# Traverse pairs (items)
for key, value in table.items():
    print(key, value)

# Searching
print('a' in table)
