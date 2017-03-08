

def binary_gap(N):
    N_bin = str('{0:b}'.format(N))  # 0 in the format arg pos, and b is for formating.
    counter = set()
    tmp_count = 0
    ###### ---  with loop - O(N) complexity
    for d in N_bin:
        if d == '0':
            tmp_count += 1
        else:
            counter.add(tmp_count)
            tmp_count = 0
    counter.add(tmp_count)
    return max(counter)

if __name__ == "__main__":
    a = binary_gap(10000)
    print "BinGap --> ", a
    b = binary_gap(2147483646)
    print "BinGap --> ", b
    c = binary_gap(2147483647)
    print "BinGap --> ", c
