"""adventofcode 01"""

import re

solution = 0
regex = re.compile(r"\d")

with open("input_file01.txt", "r") as file:
    for line in file:
        matches = [m[0] for m in regex.finditer(line)]
        number = matches[0] + matches[-1]
        solution += int(number)


print("the solution is:", solution)
