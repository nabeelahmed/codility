def cyclicrotation(A, K):
    """
    For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].
    """
    new_list = [0] * len(A)
    new_index = K
    for index, elem in enumerate(A):
        if new_index >= len(A):
            new_index = 0
            new_list[new_index] = elem
            new_index += 1
        else:
            new_list[new_index] = elem
            new_index += 1

    return new_list

if __name__ == "__main__":
    A = [3, 8, 9, 7, 6]
    K = 3
    answer = cyclicrotation(A, K)
    print answer
