# example.py
from line_profiler import LineProfiler

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def fibonaci_rec(n):
    if n <= 1:
        return n
    return fibonaci_rec(n-1) + fibonaci_rec(n-2)


profiler = LineProfiler()
profiler.add_function(fibonacci)
profiler.add_function(fibonaci_rec)
profiler.enable()

n=17

r1 = fibonacci(n)
r2 = fibonaci_rec(n)


profiler.print_stats()

print(f"fibonaci result: {r1}")
print(f"fibonaci_rec result: {r2}")
