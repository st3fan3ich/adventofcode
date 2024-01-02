"""adventofcode 01"""

import re

solution = 0
# regex = re.compile(r"\d")

# with open("input_file01.txt", "r") as file:
#     for line in file:
#         matches = [m[0] for m in regex.finditer(line)]
#         number = matches[0] + matches[-1]
#         solution += int(number)


# print("the solution is:", solution)

"""adventofcode 01.5"""

# def convert_first():
#     if matches[0] == "one":
#             matches[0] = 1
#         elif matches[0] == "two":
#             matches[0] = 2
#         elif matches[0] == "three":
#             matches[0] = 3
#         elif matches[0] == "four":
#             matches[0] = 4
#         elif matches[0] == "five":
#             matches[0] = 5
#         elif matches[0] == "six":
#             matches[0] = 6
#         elif matches[0] == "seven":
#             matches[0] = 7
#         elif matches[0] == "eight":
#             matches[0] = 8
#         elif matches[0] == "9":
#             matches[0] = 9
#         break


regex = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d)")
with open("input_file01.txt", "r") as file:
    for line in file:
        matches = [m[0] for m in regex.finditer(line)]
        if matches[0] == "one":
            matches[0] = 1
        elif matches[0] == "two":
            matches[0] = 2
        elif matches[0] == "three":
            matches[0] = 3
        elif matches[0] == "four":
            matches[0] = 4
        elif matches[0] == "five":
            matches[0] = 5
        elif matches[0] == "six":
            matches[0] = 6
        elif matches[0] == "seven":
            matches[0] = 7
        elif matches[0] == "eight":
            matches[0] = 8
        elif matches[0] == "9":
            matches[0] = 9
        break
print(matches[0])
