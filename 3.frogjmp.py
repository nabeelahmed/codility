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
    # jumps = math.ceil(Y - X)/D
    return jumps

if __name__ == "__main__":
    print frog_jump(10, 85, 30)
    print frog_jump(10, 85, 20)
    print frog_jump(10, 85, 10)
    print frog_jump(10, 85, 1)
