"""adventofcode 01"""


import re

file=open("input_file01.txt","r")
#print(file.readline())


filter = []                                             # empty array, to be filled with the filtered numbers
coord = []                                              # empty array, to be filled with the coordinates
solution = 0

regex = '[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+'                  # define what you are looking for with re.search






for i in range(1000):
    s = file.readline()
    #print(s)                         # string you are filtering
    filter = []

    if re.search(regex, s) is not None:                         # filter funktion
        for catch in re.finditer(regex, s):
            filter.append(catch[0])
            #print(catch[0])                                         # catch is a match object, for testing
            #print(filter)                                           # print filtered array, for testing

        a = filter[0]                                           # get first number from filtered array
        b = filter[-1]                                          # get last number from filtered array
        #print(filter)
        if int(a) > 99999:                                        # check for exceptions first integer > 99999
            a1 = int(a)//100000
        elif int(a) > 9999:                                        # check for exceptions first integer > 9999
            a1 = int(a)//10000
        elif int(a) > 999:                                        # check for exceptions first integer > 999
            a1 = int(a)//1000
            #print("a>999", a1)
        elif int(a) > 99:                                       # check for exceptions first integer > 99
            a1 = int(a)//100 
            #print("a>99", a1)                                 # take the first digit, discard the rest
        elif int(a) > 9:                                        # check for exceptions first integer > 9
            a1 = int(a)//10
            #print("a>9", a1)                                   # take the first digit, discard the rest
        else:
            a1 = int(a)
            #print("a<9", a1)
                                    
        if int(b) > 9:                                          # check for exceptions last integer > 9
            b1 = int(b)%10                                    # take the last digit, discard the rest
            #print("b>9", b1)
        else:
            b1 = int(b)
            #print("b<9", b1)
      
#print(a1)
#print(b1)
    c = str(a1) + str(b1)                                   # form the number a + b = ab (1 + 1 = 11)
#print(c)
    coord.append(int(c))
            #print(coord, i)
print(coord)

for i in range(len(coord)):
    print([coord[i]], i)
    solution = solution + coord[i]

print("the solution is:", solution)


"""
with open("input_file01.txt", "r") as file:
    for line in file:
        if re.search(regex, s) is not None:                         # filter funktion
        for catch in re.finditer(p, s):
            filter.append(catch[0])
"""
#print(27%10) 
#print(93//10)
#test = [2, 4, 3, 9, 1]
#print(test[-1], test[0])