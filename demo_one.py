

def solution(A):
    """
    Task description
    This is a demo task.

    Write a function:



    that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    For another example, given A = [1, 2, 3], the function should return 4.

    Given A = [-1, -3], the function should return 1.

    """
    sorted_A = sorted(A)
    if sorted_A[0] != 1:
        return 1
    for index, num in enumerate(sorted_A[:-1]):
        if sorted_A[index + 1] - sorted_A[index] > 1 and sorted_A[index] > 0:
            return sorted_A[index] + 1
    if sorted_A[-1] >= 100000:  # max N
        return 1
    elif sorted_A[-1] > 0:
        return sorted_A[-1] + 1  # next to the last integer
    else:  # all negatives
        return 1



if __name__ == "__main__":
    A = [
        [1, 3, 6, 4, 1, 2],
        [1, 2, 3],
        [-1, -3],
        [100000],  # max N
        [2]
    ]
    for a in A:
        print "missing positive --> ", solution(a)