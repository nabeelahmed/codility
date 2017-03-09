


def frogriverone(A, dest):
    frogs_path = range(1, dest+1)
    for pos, leave in enumerate(A):
        if leave in frogs_path:
            print 'leave: ', leave, 'position: ', pos
            frogs_path.remove(leave)
            print "Remaining path: ", frogs_path
            if not frogs_path:
                return pos
    return -1


if __name__ == "__main__":
    # A = [1, 3, 1, 4, 2, 3, 5, 4]
    A = [1, 3, 1, 4, 2, 3, 5, 4, 6, 7, 8, 1, 3, 4, 5, 7, 8, 3, 4, 6, 3, 5, 6, 9, 10, 11]
    # dest = 5
    dest = 10
    print frogriverone(A, dest)
    # import profile
    # prfile.run('frogriverone(%s, %s)' % (A, X))
