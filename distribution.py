# distribution
from random import randint

d = {}
for p in range (1, 100):
    d[p] = 0
for i in range(1, 365):
    customers = 0
    for p in range(1, 100):
        if randint(0, 99) < 30:
            customers += 1
    d[customers] += 1

for (index, value) in d.items():
    print("{},{}".format(index, value))
