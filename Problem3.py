

def factor_finder(number:int):
    for i in range(1, number):
        if number % i == 0:
            yield i
    
def is_prime(number:int) -> bool:
    if number & 1 == 0:
        return False
    
    prime = True
    for i in range(3, int(number**.5)+1):
        if number % i == 0:
            prime = False
            break

    return prime
 


def main():
    number = 600851475143
    
    factor_gen = factor_finder(number)

    while True:
        factor = next(factor_gen)
        opposite_factor = number // factor

        if is_prime(opposite_factor):
            print(opposite_factor)
            break


if __name__ == "__main__":
    main()