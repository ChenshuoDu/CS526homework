import sys

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def segments_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    return (o1 != o2) and (o3 != o4)

def all_ghosts_eliminated(pairs):
    n = len(pairs)
    for i in range(n):
        for j in range(i + 1, n):
            b1, g1 = pairs[i]
            b2, g2 = pairs[j]
            if segments_intersect(b1, g1, b2, g2):
                return "All Ghosts: were not eliminated"
    return "All Ghosts: were eliminated"

def main():
    if len(sys.argv) < 2:
        print("Usage: python ghostbusters.py <input_file>")
        return

    input_file = sys.argv[1]
    pairs = []

    with open(input_file, "r") as f:
        n = int(f.readline().strip())
        for _ in range(n):
            data = f.readline().split()
            bx, by = float(data[1]), float(data[2])
            gx, gy = float(data[4]), float(data[5])
            pairs.append(((bx, by), (gx, gy)))

    result = all_ghosts_eliminated(pairs)
    print(result)

if __name__ == "__main__":
    main()
