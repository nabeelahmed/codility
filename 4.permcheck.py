

def permcheck(A):
    sorted_A = sorted(A)
    for index, elem in enumerate(sorted_A[:-1]):
        # if index+1 < len(sorted_A):
            if not sorted_A[index+1] - sorted_A[index] == 1:
                return 0
            else:
                pass
        # else:  # last element
        #     if not sorted_A[index] - sorted_A[index-1] == 1:
        #         print sorted_A[index]
        #         return 0
    return 1


if __name__ == "__main__":
    # A = [1, 2, 3, 4, 5]
    A = [1, 2, 3, 4, 5, 6, 8]
    print permcheck(A)