def fibonacci(n):
    if n == 0:
        return 0

    def fast_doubling(n):
        if n == 0:
            return (0, 1)

        a, b = fast_doubling(n // 2)

        c = a * (2 * b - a)
        d = a * a + b * b

        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return fast_doubling(n)[0]


# Main program
n = int(input("Enter the value of n: "))

print("The", n, "th Fibonacci number is:", fibonacci(n))
