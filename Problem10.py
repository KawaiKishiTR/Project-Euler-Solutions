

prime_list = [2]

def is_prime(number):
    prime = True
    limit = int(number**.5)
    for prime_num in prime_list:
        if prime_num > limit:
            break
        if number % prime_num == 0:
            prime = False
            break
    
    if prime:
        prime_list.append(number)

    return prime

def number_generator():
    num = 3
    while True:
        yield num
        num += 2

def main():
    number_gen = number_generator()
    sum_of_all_primes = 2

    while True:
        number = next(number_gen)

        if number >= 2_000_000:
            break

        if is_prime(number):
            sum_of_all_primes += number
        
    print(sum_of_all_primes)

def main2():
    limit = 2_000_000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False

    print(sum(i for i, is_p in enumerate(sieve) if is_p))


if __name__ == "__main__":
    main()
    main2()
