morse_code_vowels = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-',
}

def count_vowel_sequences(code: str) -> int:
    patterns = list(morse_code_vowels.values())
    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for p in patterns:
            L = len(p)
            if i - L >= 0 and code[i-L:i] == p:
                total += dp[i - L]
        dp[i] = total
    return dp[n]

def main():
    import sys, pathlib
    if len(sys.argv) != 2:
        print("Usage: python vowels_morse.py <input_file>")
        sys.exit(1)
    path = pathlib.Path(sys.argv[1])
    code = path.read_text(encoding='utf-8').strip()
    result = count_vowel_sequences(code)
    print(f"File Input: {path.name}")
    print(f"The Number of Vowel combinations is: {result}")

if __name__ == '__main__':
    main()
