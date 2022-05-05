from timeit import timeit


def prime_factorization(n: int):
    return [i for i in range(1, n + 1) if n % i == 0]


runtime = timeit('prime_factorization(10000000)',
                 number=100, globals=globals())
print(f'average runtime in py(s):{runtime/100}')
