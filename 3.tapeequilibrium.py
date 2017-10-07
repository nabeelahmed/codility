def tapeequilibrium(A):
    diff = set()
    for index, elem in enumerate(A):
        diff.add(abs(sum(A[:index]) - sum(A[index:])))
    return min(diff)

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

if __name__ == "__main__":
    A = [3, 1, 2, 4, 3]
    print tapeequilibrium(A)
    print tape_equilibrium(A)
