


def equilibrium_index(list):
    """
    """
    output = []
    for index, elem in enumerate(list):
        if index > 0 and sum(list[:index]) == sum(list[index+1:]):
            output.append(index)
    return output

def binary_gap(number):
    """
    """
    bin_number = "{0:b}".format(number)  # binary conversion
    count = 0
    output = 0  # or use set, add and return max(output)
    for d in bin_number:
        if d == '0':
            count += 1
        else:
            output = count if count > output else output  # output.add(count)
            count = 0
    output = count if count > output else output  # otherwise trail at the end will be missed.
    return output

def cyclic_rotation(num_list, k):
    """
    A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted
    right by one index, and the last element of the array is also moved to the first place.

    For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times;
    that is, each element of A will be shifted to the right by K indexes.

    """
    new_list = [0] * len(num_list)
    new_index = k
    for index, elem in enumerate(num_list):
        if new_index >= len(num_list):
            new_index = 0
            new_list[new_index] = elem
            new_index += 1
        else:
            new_list[new_index] = elem
            new_index += 1
    return new_list

def odd_occurency(odd_list):
    """
    A non-empty zero-indexed array A consisting of N integers is given.
    The array contains an odd number of elements, and each element of the array can be paired with another element
    that has the same value, except for one element that is left unpaired.

    """
    if len(odd_list) % 2:
        sorted_list = sorted(odd_list)
        index = 0
        while index < (len(odd_list) - 1):
            if sorted_list[index] == sorted_list[index+1]:
                index += 2
            else:
                return sorted_list[index]
        # return sorted_list[-1]
        return sorted_list[index]
    else:
        return "List has to have an odd number of elements!"

def tape_equilibrium(num_list):
    """

    """
    p = 1
    while p < (len(num_list) - 1):
        if abs(sum(num_list[:p]) - sum(num_list[p:])) == 1:  # tape equilibrium condition
            return p
        else:
            p += 1
    return p

def frog_jump(X, Y, D):
    """
    A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to
    get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

    :return - that, given three integers X, Y and D, returns the minimal number of jumps from position X to a
    position equal to or greater than Y.

    For example, given:
    X = 10 Y = 85 D = 30
    the function should return 3, because the frog will be positioned as follows:

        * after the first jump, at position 10 + 30 = 40
        * after the second jump, at position 10 + 30 + 30 = 70
        * after the third jump, at position 10 + 30 + 30 + 30 = 100

    Assume that:

        * X, Y and D are integers within the range [1,,1,000,000,000];
        * X <= Y.

    Complexity:

        * expected worst-case time complexity is O(1);
        * expected worst-case space complexity is O(1).
    """
    jumps = (Y - X)/D + 1 if ((Y - X) % D) else (Y - X)/D  # to handle the int division - +1 to round-up
    # import math
    # jumps = math.ceil(Y - X)//D
    return jumps

def permissingelem(num_list):
    """
    """
    sorted_list = sorted(num_list)
    if sorted_list[0] != 1:  # boundary case - 1, first element is missing
        return 1
    for index, elem in enumerate(sorted_list):
        if index < (len(sorted_list) - 1):
            if not sorted_list[index+1] - sorted_list[index] == 1:
                return sorted_list[index] + 1
        else:
            return sorted_list[index] + 1

def max_counter(A, N):
    """
    You are given N counters, initially set to 0, and you have two possible operations on them:

        * increase(X) - counter X is increased by 1,
        * max counter - all counters are set to the maximum value of any counter.

    A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

        * if A[K] = X, such that 1 <= X <= N, then operation K is increase(X),
        * if A[K] = N + 1 then operation K is max counter.

    For example, given integer N = 5 and array A such that:
    A[0] = 3 A[1] = 4 A[2] = 4 A[3] = 6 A[4] = 1 A[5] = 4 A[6] = 4
    the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0) (0, 0, 1, 1, 0) (0, 0, 1, 2, 0) (2, 2, 2, 2, 2) (3, 2, 2, 2, 2) (3, 2, 2, 3, 2) (3, 2, 2, 4, 2)
    The goal is to calculate the value of every counter after all operations.

    Write a function:
    def solution(N, A)
    that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of
    integers representing the values of the counters.
    The sequence should be returned as:

        * a structure Results (in C), or
        * a vector of integers (in C++), or
        * a record Results (in Pascal), or
        * an array of integers (in any other programming language).

    For example, given:
    A[0] = 3 A[1] = 4 A[2] = 4 A[3] = 6 A[4] = 1 A[5] = 4 A[6] = 4
    the function should return [3, 2, 2, 4, 2], as explained above.
    Assume that:

        * N and M are integers within the range [1..100,000];
        * each element of array A is an integer within the range [1..N + 1].

    Complexity:

        * expected worst-case time complexity is O(N+M);
        * expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

    Elements of input arrays can be modified.

    """
    counters = [0] * N
    for index, elem in enumerate(A):
        if 1 <= elem <= N:
            counters[elem-1] += 1
        else:
            counters = [max(counters)] * N

def perm_check(num_list):
    sorted_list = sorted(num_list)
    if sorted_list[0] != 1:
        return 0  # not a permutation
    for index, elem in enumerate(sorted_list[:-1]):  # exclude the last element
        if not sorted_list[index+1] - sorted_list[index] == 1:
            return 0  # not a permutation
    return 1


if __name__ == "__main__":
    list1 = [-1, 3, -4, 5, 1, -6, 2, 1]
    print equilibrium_index(list1)  # [1, 3, 7]

    print "BinGap --> ", binary_gap(10000)  # 4
    print "BinGap --> ", binary_gap(2147483646)  # 1
    print "BinGap --> ", binary_gap(2147483647)  # 0

    a = [3, 8, 9, 7, 6]
    k = 3
    print cyclic_rotation(a, k)  # [9, 7, 6, 3, 8]

    odd_num = [9, 3, 9, 3, 9, 6, 9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7]  # size 20
    print odd_occurency(odd_num)  # List has to have an odd number of elements!
    odd_num = [10, 9, 3, 9, 3, 9, 6, 9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7]  # size 21
    print odd_occurency(odd_num)  # 7
    odd_num = [10, 9, 3, 9, 3, 12, 9, 6, 9, 4, 4, 5, 6, 5, 10, 11, 11, 11, 10, 10, 11, 7, 7]  # size 23
    print odd_occurency(odd_num)  # 12 boundary case

    te_list = [3, 1, 2, 4, 3]
    print tape_equilibrium(te_list)  # 3

    print frog_jump(10, 85, 30)
    print frog_jump(10, 85, 20)
    print frog_jump(10, 85, 10)
    print frog_jump(10, 85, 1)

    # b = [2, 3, 1, 5, 6, 7, 8, 9, 10, 4, 12]  # 11 is missing
    # b = [2, 3, 1, 5, 6, 7, 8, 9, 10, 4, 11]  # 12 - last elem is missing
    b = [2, 3, 12, 5, 6, 7, 8, 9, 10, 4, 11]  # 1 - first elem is missing
    print "Missing element --> ", permissingelem(b)

    A = [3, 4, 4, 6, 1, 4, 4]  # consecutive operations array.
    N = 5  # counter size
    max_counter(A, N)  # output (3, 2, 2, 4, 2)

    perm = [1, 2, 3, 4, 5, 6, 8]  # 1 - not a perm 7 missing
    perm = [7, 2, 3, 4, 5, 6, 8]  # 1 - not a perm 1 missing
    perm = [1, 2, 3, 4, 5, 6, 7]  # 0 - a permutation
    print "is permutation --> ", perm_check(perm)









