import sys

def substrings_recursive(s, start, end, result):
    if start == len(s):
        return
    if end == len(s) + 1:
        substrings_recursive(s, start + 1, start + 2, result)
        return
    substring = s[start:end]
    result.add(substring)
    substrings_recursive(s, start, end + 1, result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python substrings.py <input_file>")
        return

    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        for line in f:
            s = line.strip()
            result = set()
            substrings_recursive(s, 0, 1, result)
            print(", ".join(result), "->", len(result))

if __name__ == "__main__":
    main()
