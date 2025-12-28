n = int(input("Введите число "))


def fizz_buzz(n):
    for v in range(1, n + 1):
        if v % 3 == 0 and v % 5 == 0:
            print("FizzBuzz")
        elif v % 3 == 0:
            print("Fizz")
        elif v % 5 == 0:
            print("Buzz")
        else:
            print(v)


fizz_buzz(n)
