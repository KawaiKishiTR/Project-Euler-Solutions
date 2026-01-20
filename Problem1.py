




def main():
    sum_ = 0
    for num in range(1,1000):
        if (num % 3 == 0) or (num % 5 == 0):
            sum_ += num
    print(sum_)

if __name__ == "__main__":
    main() 