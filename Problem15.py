



def main():
    grid = [[1]*21,
            *[([1]+[None]*20) for i in range(20)]]
    
    for row in range(21):
        for column in range(21):
            if grid[row][column] is not None:
                continue

            grid[row][column] = grid[row][column-1] + grid[row-1][column]
    
    print(grid[20][20])


if __name__ == "__main__":
    main()