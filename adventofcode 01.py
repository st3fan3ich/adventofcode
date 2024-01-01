"""adventofcode 01"""


import re

p = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'                  # define what you are looking for with re.search

s = '2127'                         # string you are filtering

filter = []                                             # empty array, to be filled with the filtered numbers
coord = []                                              # empty array, to be filled with the coordinates

if re.search(p, s) is not None:                         # filter funktion
    for catch in re.finditer(p, s):
            filter.append(catch[0])
#            print(catch[0])                             # catch is a match object, for testing


print(filter)                                           # print filtered array, for testing

a = filter[0]                                           # get first number from filtered array
b = filter[-1]                                          # get last number from filtered array
if int(a) > 999:                                        # check for exceptions first integer > 999
      a1 = int(a)//1000
elif int(a) > 99:                                       # check for exceptions first integer > 99
      a1 = int(a)//100                                  # take the first digit, discard the rest
elif int(a) > 9:                                        # check for exceptions first integer > 9
      a1 = int(a)//10                                   # take the first digit, discard the rest
else:
      a1 = int(a)

if int(b) > 99:                                         # check for exceptions last integer > 99
      b1 = int(b)%10                                    # take the last digit, discard the rest
elif int(b) > 9:                                          # check for exceptions last integer > 9
      b1 = int(b)%10                                    # take the last digit, discard the rest
else:
      b1 = int(b)
      
print(a1)
print(b1)
c = str(a1) + str(b1)                                   # form the number a + b = ab (1 + 1 = 11)
print(c)
coord.append(int(c))
print(coord)

print(27%10) 
#print(93//10)
#test = [2, 4, 3, 9, 1]
#print(test[-1], test[0])