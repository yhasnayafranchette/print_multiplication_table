#Exercise 13: Print multiplication table from 1 to 10

#Print multiplication table from 1 to 10 in matrix format
for multiplicand in range(1, 11):
    for multiplier in range(1, 11):
        result = multiplicand * multiplier
        print(f"{result:4}", end=" ") 
    print()  
