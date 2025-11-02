import sys, math

def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    symbols = [s.strip() for s in lines[1].split(',')]
    board = [[c.strip() for c in line.split(',')] for line in lines[2:]]
    return n, symbols, board

def no_dups(seq):
    seen = set()
    for x in seq:
        if x == ".": continue
        if x in seen: return False
        seen.add(x)
    return True

def is_valid(n, board):
    k = int(math.isqrt(n))
    for row in board:
        if not no_dups(row): return False
    for c in range(n):
        if not no_dups([board[r][c] for r in range(n)]): return False
    for br in range(0, n, k):
        for bc in range(0, n, k):
            block = [board[r][c] for r in range(br, br+k) for c in range(bc, bc+k)]
            if not no_dups(block): return False
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python q4.py <input_file>")
        return
    n, symbols, board = read_input(sys.argv[1])
    print(f"The board is {'valid' if is_valid(n, board) else 'invalid'}")

if __name__ == "__main__":
    main()
