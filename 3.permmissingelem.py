

def permissingelem(A):
    sorted_A = sorted(A)
    if sorted_A[0] != 1:  # boundary case - 1, first element is missing
        return 1
    for index, elem in enumerate(sorted_A):
        if index < (len(sorted_A) - 1):
            if not sorted_A[index+1] - sorted_A[index] == 1:
                return sorted_A[index] + 1
        else:
            return sorted_A[index] + 1

if __name__ == "__main__":
    A = [
            [2, 3, 1, 5],
            [2, 3, 1, 5, 6, 7, 8, 9, 10, 4, 12],  # 11 is missing
            [2, 3, 1, 5, 6, 7, 8, 9, 10, 4, 11],  # 12 - last elem is missing
            [2, 3, 12, 5, 6, 7, 8, 9, 10, 4, 11]  # 1 - first elem is missing
    ]
    for example in A:
        print "missing element --> ", permissingelem(example)
