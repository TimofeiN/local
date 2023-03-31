numbers = []

for i in range(1, 1000, 2):
    number_one = i**3
    numbers.append(number_one)
#print(numbers)

total_amount_1 = 0
for number in numbers:
    units = number % 10
    tens = number % 100 // 10
    hundreds = number // 100 % 10
    thousands = number // 1000 % 10
    ten_thousands = number // 10000 % 10
    hundred_thousands = number // 100000 % 10
    millions = number // 1000000 % 10
    ten_millions = number // 10000000 % 10
    hundred_millions = number // 100000000 % 10
    amount = units+tens+hundreds+thousands+ten_thousands+hundred_thousands+millions+ten_millions+hundred_millions
    if amount % 7 == 0:
        total_amount_1 += number
print('total amount 1 = ', total_amount_1)

for idx in range(len(numbers)):
    numbers[idx] += 17
#print(numbers)

total_amount_2 = 0
for number in numbers:
    units = number % 10
    tens = number % 100 // 10
    hundreds = number // 100 % 10
    thousands = number // 1000 % 10
    ten_thousands = number // 10000 % 10
    hundred_thousands = number // 100000 % 10
    millions = number // 1000000 % 10
    ten_millions = number // 10000000 % 10
    hundred_millions = number // 100000000 % 10
    amount = units+tens+hundreds+thousands+ten_thousands+hundred_thousands+millions+ten_millions+hundred_millions
    if amount % 7 == 0:
        total_amount_2 += number
print('total amount 2 = ', total_amount_2)
