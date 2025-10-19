import sys

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()
else:
    lines = sys.stdin.read().splitlines()

n = int(lines[0])
T = int(lines[1])
arr = list(map(int, lines[2].split()))

arr.sort(reverse=True)

s = 0
count = 0
for x in arr:
    s += x
    count += 1
    if s > T:
        break

print(f"Answer: {count}")


