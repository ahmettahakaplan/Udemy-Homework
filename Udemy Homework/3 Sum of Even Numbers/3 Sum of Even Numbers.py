#Add Even Numbers Homework 3
from functools import reduce
check_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter = list(filter(lambda a : a % 2 == 0,check_liste))
result = reduce(lambda a,b : a+ b,filter)
print(result)