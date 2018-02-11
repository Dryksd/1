from random import randint


as_a = []
while len(as_a) < 21:
    as_a.append((randint(0,100)))

print([x**3 for x in as_a if x % 3 == 0 and x % 4 == 0]) # это написал в тесте.


