src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

res = [src[i+1] for i in range(len(src[:-1])) if src[i+1] > src[i]]
print(res)