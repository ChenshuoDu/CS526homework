import sys

def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    infected = set()
    for line in lines[1:]:
        parts = line.split()
        if len(parts) == 2:
            r, c = map(int, parts)
            infected.add((r, c))
    return n, infected

def spread_once(n, infected):
    new_inf = set(infected)
    for r in range(n):
        for c in range(n):
            if (r, c) in infected:
                continue
            neighbors = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            count = sum(
                (nr, nc) in infected
                for nr, nc in neighbors
                if 0 <= nr < n and 0 <= nc < n
            )
            if count >= 2:
                new_inf.add((r, c))
    return new_inf

def simulate(n, infected):
    while True:
        new_inf = spread_once(n, infected)
        if new_inf == infected:
            break
        infected = new_inf
    total = n * n
    return "There are no healthy counties left" if len(infected) == total else "There are healthy counties left"

def main():
    if len(sys.argv) < 2:
        print("Usage: python q2.py <input_file>")
        return
    n, infected = read_input(sys.argv[1])
    print(simulate(n, infected))

if __name__ == "__main__":
    main()
