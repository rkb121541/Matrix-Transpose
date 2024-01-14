def transpose(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        subtranspose = []
        for j in range(len(matrix)):
            subtranspose += [matrix[j][i]]
        transpose += [subtranspose]
    return transpose

def main():
    # |a b|
    # |c d|
    a = 3
    b = 2
    c = 1
    d = 5
    print(transpose([[a,b],[c,d]]))

if __name__ == "__main__":
    main()