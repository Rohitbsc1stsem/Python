def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))

if num >= 0:
    print("Factorial is: ", factorial(num))
else:
    print("Factorial not defined for negative number")
