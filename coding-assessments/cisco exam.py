"""
inputNum, represents the number of rows and columns of the chess board (N).
"""

def funcChessBoard(inputNum):
    # Write your code here
    for i in range(inputNum):
        row = []
        # Loop through each column in the row
        for j in range(inputNum):
            # If the sum of row and column indexes is even, it's "W", else "B"
            if (i + j) % 2 == 0:
                row.append("W")
            else:
                row.append("B")
        # Print the row as space-separated values
        print(" ".join(row))

    return


"""
inputArr, represents the given array of element of size inputArr_size.
"""

def funcTwins(inputArr):
    # Write your code here
    # marked = False
    a = 0
    for i in range(a, len(inputArr)):
        for j in range(a + 1, len(inputArr) - 1):
            if inputArr[i] == inputArr[j]:
                a = a + 2
                # inputArr.remove(inputArr[j])
                # i = i + 1
                # marked = True
                # break
        # if i == len(inputArr) - 1:
        #     print(inputArr[i])
            # else:
            #
            #     print(inputArr[i])

    return


"""
inputNum1, represents the number X.
inputNum2, represents the number Y.
"""

def funcCount(inputNum1, inputNum2):
    # Write your code here
    x = inputNum1
    y = inputNum2
    count = 0
    while x >= y:
        print("yes")
        if y + inputNum2 <= x:
            print("If yes")
            y = y + inputNum2
            print("y")
            print(y)
        count += 1
    print(count)
    if count == 0:
        print(-1)
    else:
        print(count)

    return


def main():
    # input for inputNum
    inputNum = int(input())
    result = funcChessBoard(inputNum)

    # input for inputArr
    inputArr = []
    inputArr_size = int(input())
    inputArr = list(map(int, input().split()))
    result = funcTwins(inputArr)

    # input for inputNum1
    inputNum1 = int(input())
    # input for inputNum2
    inputNum2 = int(input())
    result = funcCount(inputNum1, inputNum2)


if __name__ == "__main__":
    main()