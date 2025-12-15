import sys

def ints_from_stdin():
    data = sys.stdin.buffer.read()
    n = len(data)
    i = 0
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        if i >= n:
            break
        sign = 1
        if data[i] == 45:
            sign = -1
            i += 1
        x = 0
        while i < n and 48 <= data[i] <= 57:
            x = x * 10 + (data[i] - 48)
            i += 1
        yield sign * x

def main():
    it = ints_from_stdin()
    try:
        m = next(it)
    except StopIteration:
        return
    n = next(it)

    grid = [[0] * n for _ in range(m)]
    for r in range(m):
        row = grid[r]
        for c in range(n):
            row[c] = next(it)

    dp = [[0] * n for _ in range(m)]

    cells = []
    append = cells.append
    for r in range(m):
        gr = grid[r]
        for c in range(n):
            append((gr[c], r, c))
    cells.sort()  

    dirs = [(-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)]

    best_nodes = 1

    for h, r, c in cells:
        cur = 1 
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] < h:
                cand = 1 + dp[rr][cc]
                if cand > cur:
                    cur = cand
        dp[r][c] = cur
        if cur > best_nodes:
            best_nodes = cur

    best_moves = best_nodes - 1
    sys.stdout.write(str(best_moves) + "\n")

if __name__ == "__main__":
    main()
