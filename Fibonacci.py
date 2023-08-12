def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Set the upper limit for the Fibonacci series
upper_limit = 50

# Get the Fibonacci series
series = list(fibonacci_series(upper_limit))

# Print the Fibonacci series
print(' '.join(map(str, series)))
