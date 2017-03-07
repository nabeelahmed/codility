

def permissingelem(A):
    sorted_A = sorted(A)
    print sorted_A
    for index, elem in enumerate(sorted_A):
        print sorted_A[index+1]
        print sorted_A[index]
        if not sorted_A[index+1] - sorted_A[index] == 1:
            return sorted_A[index+1] - 1
            #return sorted_A[index] + 1
        else:
                pass

if __name__ == "__main__":
    # A = [2, 3, 1, 5]
    A = [2, 3, 1, 5, 6, 7, 8, 9, 10, 4, 12]
    # A = [2, 3, 1, 5]
    # A = [2, 3, 1, 5]
    print permissingelem(A)
