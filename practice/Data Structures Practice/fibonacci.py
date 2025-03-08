def myster(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(2, n+1):
        fib = a + b
        a, b = b, fib
    return fib

print(myster(5))  # 8

# Memoization, works for large values of n by storing the results of expensive function calls
def fib(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]