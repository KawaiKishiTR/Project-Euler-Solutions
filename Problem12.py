


def triangular_number_generator():
    result = 0
    number = 1
    while True:
        result += number
        number += 1
        yield result
    
def calc_divisor_count(number:int):
    divisor_count = 2
    limit = number
    num = 1

    while num < limit:
        num += 1
        if number % num == 0:
            limit = number // num
            divisor_count += 2
    
    return divisor_count

def main():
    num_gen = triangular_number_generator()

    for number in num_gen:
        divisor_count = calc_divisor_count(number)

        if divisor_count > 500:
            print(number)
            break

if __name__ == "__main__":
    main()