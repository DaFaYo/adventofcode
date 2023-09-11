import math
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True




def prime_factors(n):
    primes = set()

    while n % 2 == 0:
        primes.add(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            primes.add(int(i))
            n = n / i

    if n > 2:
        primes.add(n)

    return primes

print(prime_factors(100))