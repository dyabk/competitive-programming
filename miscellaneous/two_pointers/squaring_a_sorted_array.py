def make_squares(arr):
    n = len(arr) - 1
    squares = [-1 for _ in range(n + 1)]

    l, r = 0, len(arr) - 1

    while l <= r:
        lSq, rSq = arr[l] * arr[l], arr[r] * arr[r]
        if lSq > rSq:
            squares[n] = lSq
            l += 1
        else:
            squares[n] = rSq
            r -= 1
        n -= 1

    return squares
