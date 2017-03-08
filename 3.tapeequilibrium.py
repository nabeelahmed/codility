def tapeequilibrium(A):
    diff = set()
    for index, elem in enumerate(A):
        diff.add(abs(sum(A[:index]) - sum(A[index:])))
    return min(diff)

if __name__ == "__main__":
    A = [3, 1, 2, 4, 3]
    answer = tapeequilibrium(A)
    print answer
