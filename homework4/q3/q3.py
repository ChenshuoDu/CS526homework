import sys
from math import gcd
from collections import defaultdict

if len(sys.argv) < 2:
    print("Usage: python q3.py <input_file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

n = int(lines[0])
points = [tuple(map(int, line.split())) for line in lines[1:]]

count = 0

for i in range(n):
    x1, y1 = points[i]
    slopes = defaultdict(int)
    
    for j in range(n):
        if i == j:
            continue
        dx = points[j][0] - x1
        dy = points[j][1] - y1
        if dx == 0 and dy == 0:
            continue
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        slopes[(dx, dy)] += 1

    for (dx, dy), cnt in slopes.items():
        count += cnt * slopes.get((-dy, dx), 0)

print(count)



