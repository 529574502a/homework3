import random as r
import math
n = 10000000
count = 0
for i in range(n):
    x = r.uniform(-1,1)
    y = r.uniform(1,-1)
    if math.sqrt(x**2+y**2) <= 1:
        count +=1
    pi = 4 * count / n
print(pi)