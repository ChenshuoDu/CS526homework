import sys

def is_palindrome(s):
    s = s.strip()
    return s == s[::-1]

def main():
    if len(sys.argv) < 2:
        print("Usage: python palindrome.py <input_file>")
        return

    input_file = sys.argv[1]
    count = 0

    with open(input_file, "r") as f:
        for line in f:
            if is_palindrome(line):
                print("true")
                count += 1
            else:
                print("false")

    print(count)

if __name__ == "__main__":
    main()
