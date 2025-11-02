import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python q1.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r") as f:
        data = f.read().strip().replace(",", " ").split()

    n = int(data[0])
    nums = list(map(int, data[1:]))

    daily = [nums[0]] + [nums[i] - nums[i-1] for i in range(1, len(nums))]
    total = sum(daily)
    half = total / 2

    found = False
    for i in range(len(daily) - 2):
        if sum(daily[i:i+3]) > half:
            found = True
            break

    print(f"{' '.join(map(str, nums))} solution: {'YES' if found else 'NO'}")

if __name__ == "__main__":
    main()
