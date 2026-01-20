
def main():
    for a in range(2,501):
        for b in range(2,501):
            c = (a**2 + b**2)**.5
            if a + b + c == 1000:
                print(int(a*b*c))
                return


if __name__ == "__main__":
    main()