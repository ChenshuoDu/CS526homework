import sys
from collections import Counter

def read_input(filename):
    with open(filename, "r") as f:
        lines = [x.strip() for x in f.readlines() if x.strip()]
    n = int(lines[0])
    categories = [x.strip() for x in lines[1].replace(',', ' ').split()]
    return n, categories

def max_items(categories):
    left = 0
    counter = Counter()
    best = 0
    for right, cat in enumerate(categories):
        counter[cat] += 1
        while len(counter) > 2:
            left_cat = categories[left]
            counter[left_cat] -= 1
            if counter[left_cat] == 0:
                del counter[left_cat]
            left += 1
        best = max(best, right - left + 1)
    return best

def main():
    if len(sys.argv) < 2:
        print("Usage: python q3.py <input_file>")
        return
    n, categories = read_input(sys.argv[1])
    print(f"{max_items(categories)} items were selected")

if __name__ == "__main__":
    main()
