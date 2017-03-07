

def missinginterger(A):
    sorted_A = sorted(A)
    print sorted_A
    for index, elem in enumerate(sorted_A):
        if not (sorted_A[index+1] - sorted_A[index]) == 1 and not (sorted_A[index+1] - sorted_A[index]) == 0:
            return sorted_A[index] + 1
        else:
            pass



if __name__ == "__main__":
    A = [1, 3, 6, 4, 2, 1, 7, 8, 6, 10, 11]
    print missinginterger(A)