import sys
from gale_shapley import parse_input_file, gale_shapley

def save_output(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_q3.py <input_file>")
        print("Example: python run_q3.py marraige_ten.txt")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace(".txt", "_output.txt")

    n, men_order, women_order, men_prefs, women_prefs = parse_input_file(input_file)

    lines = []
    lines.append(f"=== Input from {input_file} ===\n")
    lines.append(f"Number of men/women: {n}\n\n")

    lines.append("Men preferences:\n")
    for m in men_order:
        lines.append(f"  {m}: {', '.join(men_prefs[m])}\n")

    lines.append("\nWomen preferences:\n")
    for w in women_order:
        lines.append(f"  {w}: {', '.join(women_prefs[w])}\n")

    matches = gale_shapley(men_prefs, women_prefs)

    lines.append("\nFinal stable matching (man - woman):\n")
    for m in sorted(matches.keys()):
        lines.append(f"  {m} - {matches[m]}\n")

    save_output(output_file, "".join(lines))

    print(f"Done! Full output saved to: {output_file}")

if __name__ == "__main__":
    main()
