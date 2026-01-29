
cache = {
    1:1
}

def CollatzSequence(number:int):
    if number in cache:
        return cache[number]
    
    if number % 2 == 0:
        lenght = 1 + CollatzSequence(number//2)
    else:
        lenght = 1 + CollatzSequence(number*3+1)

    cache[number] = lenght
    return lenght

def main():
    longest_lenght:int = 0
    longest_number:int = 0
    for i in range(1,1_000_000):
        lenght = CollatzSequence(i)

        if lenght > longest_lenght:
            longest_lenght = lenght
            longest_number = i
    
    print(longest_lenght, longest_number)





if __name__ == "__main__":
    main()



