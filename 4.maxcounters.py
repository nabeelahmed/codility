
def max_counter(A, N):
    counters = [0] * N
    for index, elem in enumerate(A):
        if N >= elem >= 1:  # increase counter step
            counters[elem-1] += 1
        elif elem > N:  # the out of index elements - max counter step.
            tmp = [max(counters) for _ in counters]
            counters = tmp
        print counters

if __name__ == "__main__":
    A = [3, 4, 4, 6, 1, 4, 4]  # consecutive operations array.
    N = 5  # counter size
    max_counter(A, N)

