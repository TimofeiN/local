from itertools import islice

n = 15
gen = (num for num in range(1, n+1, 2))

# print(type(gen))
print(*islice(gen, None))
