from timeit import timeit


def print_prime(n):
    prime = [True for _ in range(n + 1)]
    for divisor in range(2, int(n**0.5) + 1):  # divisor<=sqrt(n)
        if prime[divisor]:
            for i in range(2 * divisor, n + 1, divisor):
                prime[i] = False

    prime_num = list()
    for i in range(2, n + 1):
        if prime[i]:
            prime_num.append(i)

    return filter(lambda x: x, prime_num)


def isprime(n):
    for i in range(2, 1 + int(n**0.5)):
        if n % i == 0:
            return False

    return True


def prime(n):
    return [i for i in range(2, n) if isprime(i)]


# compare to general find_prime
print(timeit('print_prime(100000)', globals=globals(), number=100))
print(timeit('prime(100000)', globals=globals(), number=100))
