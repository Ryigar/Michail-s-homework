lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
numbers = [n for n in lst if n < 30 and n % 3 == 0]

print(numbers)
