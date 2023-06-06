#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        j = a % 5 == 0
        n = a % 3 == 0
        h = j and n
        mes = f"FizzBuzz" if h else f"Buzz" if j \
            else f"Fizz" if n else f"{a:d}"
        print(mes, end=" ")
