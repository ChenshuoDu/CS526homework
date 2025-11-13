def solve(A, B, startA):
    n, m = len(A), len(B)
    d1 = [1] * n
    d2 = [1] * m

    for j in range(m):
        for i in range(n):
            if startA:
                if B[j] < A[i] and j < i:
                    d1[i] = max(d1[i], d2[j] + 1)
                if A[i] < B[j] and i < j:
                    d2[j] = max(d2[j], d1[i] + 1)
            else:
                if A[i] < B[j] and i < j:
                    d2[j] = max(d2[j], d1[i] + 1)
                if B[j] < A[i] and j < i:
                    d1[i] = max(d1[i], d2[j] + 1)

    return max(max(d1), max(d2))


def main():
    import sys, pathlib
    path = pathlib.Path(sys.argv[1])
    lines = [l.strip() for l in path.read_text().splitlines() if l.strip()]
    A = list(map(int, lines[2].split()))
    B = list(map(int, lines[3].split()))

    ans = max(solve(A, B, True), solve(A, B, False))

    print(f"File Input: {path.name}")
    print(f"Longest Sequence: {ans}")


if __name__ == "__main__":
    main()
