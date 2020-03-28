from functools import reduce

val = [10, 2, 3, 45, 78, 2]

rs = reduce(lambda x,y : x+y, val)
print(rs)