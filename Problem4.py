


def main():
    palindrome_numbers = []

    for i in range(999, 1, -1):
        for k in range(999, 1, -1):
            number = i*k
            if str(number) == str(number)[::-1]:
                palindrome_numbers.append(number)

    print(max(palindrome_numbers))            


if __name__ == "__main__":
    main()

