import sys
import heapq

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_map(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def build_huffman_tree(freq_map):
    heap = []
    for ch, f in freq_map.items():
        heapq.heappush(heap, Node(ch, f))

    if len(heap) == 1:
        single = heapq.heappop(heap)
        root = Node(None, single.freq, single, None)
        return root

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        parent = Node(None, n1.freq + n2.freq, n1, n2)
        heapq.heappush(heap, parent)

    return heapq.heappop(heap)


def print_tree(node, prefix=""):
    if node is None:
        return
    if node.char is not None:
        print(f"{prefix}Leaf(char={repr(node.char)}, freq={node.freq})")
    else:
        print(f"{prefix}Node(freq={node.freq})")
        print_tree(node.left, prefix + "  ")
        print_tree(node.right, prefix + "  ")


def build_code_map(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes
    if node.char is not None:
        codes[node.char] = current_code if current_code != "" else "0"
        return codes

    build_code_map(node.left, current_code + "0", codes)
    build_code_map(node.right, current_code + "1", codes)
    return codes


def encode_text(text, code_map):
    encoded_bits = []
    for ch in text:
        encoded_bits.append(code_map[ch])
    return "".join(encoded_bits)


def write_compressed_file(filename, freq_map, encoded_bits):
    with open(filename, "w", encoding="utf-8") as f:
        for ch, freq in freq_map.items():
            f.write(f"{repr(ch)}:{freq}\n")
        f.write("END_HEADER\n")
        f.write(encoded_bits)


def read_compressed_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    freq_map = {}
    i = 0
    while i < len(lines) and lines[i] != "END_HEADER":
        line = lines[i]

        char_part, freq_part = line.split(":", 1)
        ch = eval(char_part) 
        freq = int(freq_part)
        freq_map[ch] = freq
        i += 1

    i += 1


    encoded_bits = "".join(lines[i:])
    return freq_map, encoded_bits


def decode_bits(encoded_bits, root):
    result = []
    node = root
    for bit in encoded_bits:
        if bit == "0":
            node = node.left
        else:
            node = node.right


        if node.char is not None:
            result.append(node.char)
            node = root
    return "".join(result)


def encode_mode(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    print("=== ENCODING MODE ===")
    print("Input text:")
    print(text)
    print("=" * 40)

    freq_map = build_frequency_map(text)
    print("Frequency map:")
    for ch, freq in freq_map.items():
        print(f"{repr(ch)} : {freq}")
    print("=" * 40)

    root = build_huffman_tree(freq_map)
    print("Huffman Tree:")
    print_tree(root)
    print("=" * 40)

    code_map = build_code_map(root)
    print("Code map:")
    for ch, code in code_map.items():
        print(f"{repr(ch)} : {code}")
    print("=" * 40)

    encoded_bits = encode_text(text, code_map)
    print("Encoded bit string (preview, first 200 bits):")
    print(encoded_bits[:200] + ("..." if len(encoded_bits) > 200 else ""))
    print("=" * 40)

    write_compressed_file(output_file, freq_map, encoded_bits)
    print(f"Compressed file written to: {output_file}")


def decode_mode(input_file, output_file):
    print("=== DECODING MODE ===")
    print(f"Reading compressed file: {input_file}")
    freq_map, encoded_bits = read_compressed_file(input_file)

    print("Frequency map from file:")
    for ch, freq in freq_map.items():
        print(f"{repr(ch)} : {freq}")
    print("=" * 40)

    print("Encoded bit string (preview, first 200 bits):")
    print(encoded_bits[:200] + ("..." if len(encoded_bits) > 200 else ""))
    print("=" * 40)

    root = build_huffman_tree(freq_map)

    decoded_text = decode_bits(encoded_bits, root)

    print("Decoded text:")
    print(decoded_text)
    print("=" * 40)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decoded_text)
    print(f"Reconstructed text written to: {output_file}")


def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python huffman.py encode <input.txt> <compressed.huff>")
        print("  python huffman.py decode <compressed.huff> <reconstructed.txt>")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if mode == "encode":
        encode_mode(input_file, output_file)
    elif mode == "decode":
        decode_mode(input_file, output_file)
    else:
        print("Unknown mode. Use 'encode' or 'decode'.")


if __name__ == "__main__":
    main()
