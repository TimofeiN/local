src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

result_set = set()
tmp = set()
for num in src:
    if num not in tmp:
        result_set.add(num)
    else:
        result_set.discard(num)
    tmp.add(num)
result = [num for num in src if num in result_set]
print(result)
