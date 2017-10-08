def solution(A):
    """
    Assume that:

    N is an integer within the range [1..1,000,000];
    each element of array A is an integer within the range [0..2147483647].
    Complexity:

    expected worst-case time complexity is O(N*log(N));
    expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

    Elements of input arrays can be modified.
    """
    from collections import Counter
    threshold = len(A)/2
    counts = Counter(A)  # returns value:count pairs
    probable_leader = counts.most_common(1)[0][0]
    count = counts.most_common(1)[0][1]
    if count > threshold:
        return probable_leader
    else:
        return -1


if __name__ == "__main__":
    A = [
        [1, 1, 50, 1],
        [4, 2, 2, 3, 2, 4, 2, 2, 6, 4]
    ]

    for a in A:
        print "Leader -->", solution(a)

