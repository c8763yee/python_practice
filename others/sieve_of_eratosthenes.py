from timeit import timeit


def isprime(n):
    for i in range(2, 1 + int(n**0.5)):
        if n % i == 0:
            return False

    return True


def general(n):
    return [i for i in range(2, n) if isprime(i)]


def eratisthenes(n):
    prime = [True for _ in range(n + 1)]
    for divisor in range(2, int(n**0.5) + 1):  # divisor<=sqrt(n)
        if prime[divisor]:
            for i in range(2 * divisor, n + 1, divisor):
                prime[i] = False

    return filter(lambda x: x, [i for i in range(2, n + 1) if prime[i]])


print(list(eratisthenes(220)))
