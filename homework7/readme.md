Name: Chenshuo Du
Course: CS526

1. Overview

This project is my implementation of Huffman encoding and decoding. The encode mode reads a text file, builds the Huffman tree from character frequencies, converts the text into a bit string, and writes it to a compressed file. The decode mode reads that file and reconstructs the original text.

2. Heart of the Algorithm (Encoding)

My approach is straightforward:
I scan the input once to count how many times each character shows up. Then I build a min-heap where each entry is a node containing a character and its frequency. I repeatedly take out the two smallest nodes and merge them into a new parent node. Doing this until one node is left gives me the Huffman tree.

To get the codes, I walk the tree and record 0 for left and 1 for right. Every leaf ends up with a unique code. Then I just replace each character in the original text with its code and write that data (plus the frequency map) to the compressed file.

3. Heart of the Algorithm (Decoding)

Decoding basically reverses that process. I load the frequency map from the compressed file and rebuild the same Huffman tree. Then I take the bit string and walk the tree bit by bit: 0 means go left, 1 means go right. Whenever I reach a leaf, I output the character and jump back to the root. Doing that for all bits reconstructs the original text.

4. How to Run

Inside the homework7 folder:

Encoding:

python huffman.py encode input.txt compressed.huff


Decoding:

python huffman.py decode compressed.huff reconstructed.txt

5. Output and Screenshots

The program prints the input text, the frequency map, the Huffman tree, and a preview of the bit string in encode mode; and the reconstructed text in decode mode. I included screenshots of both runs.
