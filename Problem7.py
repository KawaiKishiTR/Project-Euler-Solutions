prime_list = [2]

def is_prime(number:int):
    prime = True
    for prime_num in prime_list:
        if number % prime_num == 0:
            prime = False
            break
    
    if prime:
        prime_list.append(number)

    return prime



def prime_generator():
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2
    

def main():
    prime_gen = prime_generator()
    for i in range(10000):
        next(prime_gen)
    
    print(prime_list[-1])

if __name__ == "__main__":
    main()
