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
#             matches[0] = "1"
#         elif matches[0] == "two":
#             matches[0] = "2"
#         elif matches[0] == "three":
#             matches[0] = "3"
#         elif matches[0] == "four":
#             matches[0] = "4"
#         elif matches[0] == "five":
#             matches[0] = "5"
#         elif matches[0] == "six":
#             matches[0] = "6"
#         elif matches[0] == "seven":
#             matches[0] = "7"
#         elif matches[0] == "eight":
#             matches[0] = "8"
#         elif matches[0] == "nine":
#             matches[0] = "9"

# def convert_last():
#     if matches[-1] == "one":
#             matches[-1] = "1"
#         elif matches[-1] == "two":
#             matches[-1] = "2"
#         elif matches[-1] == "three":
#             matches[-1] = "3"
#         elif matches[-1] == "four":
#             matches[-1] = "4"
#         elif matches[-1] == "five":
#             matches[-1] = "5"
#         elif matches[-1] == "six":
#             matches[-1] = "6"
#         elif matches[-1] == "seven":
#             matches[-1] = "7"
#         elif matches[-1] == "eight":
#             matches[-1] = "8"
#         elif matches[-1] == "nine":
#             matches[-1] = "9"


regex = re.compile(
    r"(one|two|three|four|five|six|seven|eight|nine|\d).*(one|two|three|four|five|six|seven|eight|nine|\d)|(one|two|three|four|five|six|seven|eight|nine|\d)"
)
with open("input_file01.txt", "r") as file:
    for line in file:
        matches = [m[0] for m in regex.finditer(line)]
        if matches[0] == "one":
            matches[0] = "1"
        elif matches[0] == "two":
            matches[0] = "2"
        elif matches[0] == "three":
            matches[0] = "3"
        elif matches[0] == "four":
            matches[0] = "4"
        elif matches[0] == "five":
            matches[0] = "5"
        elif matches[0] == "six":
            matches[0] = "6"
        elif matches[0] == "seven":
            matches[0] = "7"
        elif matches[0] == "eight":
            matches[0] = "8"
        elif matches[0] == "nine":
            matches[0] = "9"
        if matches[-1] == "one":
            matches[-1] = "1"
        elif matches[-1] == "two":
            matches[-1] = "2"
        elif matches[-1] == "three":
            matches[-1] = "3"
        elif matches[-1] == "four":
            matches[-1] = "4"
        elif matches[-1] == "five":
            matches[-1] = "5"
        elif matches[-1] == "six":
            matches[-1] = "6"
        elif matches[-1] == "seven":
            matches[-1] = "7"
        elif matches[-1] == "eight":
            matches[-1] = "8"
        elif matches[-1] == "nine":
            matches[-1] = "9"
        number = matches[0] + matches[-1]
        solution += int(number)
# print(matches[0])
print(solution)
