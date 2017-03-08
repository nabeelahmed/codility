def frogjmp(X, Y, D):
    jumps = (Y - X)/D + 1 if ((Y - X) % D) else (Y - X)/D
    return jumps

if __name__ == "__main__":
    print frogjmp(10, 85, 30)
    print frogjmp(10, 85, 20)
    print frogjmp(10, 85, 10)
    print frogjmp(10, 85, 1)
