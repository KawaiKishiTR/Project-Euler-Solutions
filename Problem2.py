




def main():
    fibo0 = 1
    fibo1 = 2

    sum_of_even_values = 2

    while True:
        new_fibo = fibo0 + fibo1

        if new_fibo > 4_000_000:
            break

        fibo0 = fibo1
        fibo1 = new_fibo

        if new_fibo % 2 == 0:
            sum_of_even_values += new_fibo
    
    print(sum_of_even_values)

if __name__ == "__main__":
    main()
    

