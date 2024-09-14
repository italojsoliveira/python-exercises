# Create a dictionary with four keys, each having a pseudo-random integer as its value
# Sort the dictionary by value

import random

points = {
    "Mary": random.randint(0, 100000), "John": random.randint(0, 100000),
    "Teresa": random.randint(0, 100000), "Peter": random.randint(0, 100000)
    }

sorted_dict = {
    k: v for k, v in sorted(points.items(), key=lambda item: item[1])
}

print(sorted_dict)