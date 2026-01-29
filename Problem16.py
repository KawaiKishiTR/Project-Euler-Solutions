


def main():
    digit_sum = 0
    number = 2**1000
    while number != 0:
        digit_sum += number % 10
        number //= 10
    
    print(digit_sum)


if __name__ == "__main__":
    main()