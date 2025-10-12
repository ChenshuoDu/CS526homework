CS526 Homework 3

Name: Chenshuo Du
Course: CS526 — Data Structures and Algorithms

Overview

This folder includes my solutions for Homework 3.
There are four problems (q1–q4).
Each problem folder has the Python code, input files, and a screenshot showing the program running.

Problem 1 — Palindrome Check

Goal: Check if each string in the input file is a palindrome.
Run:

python q1/q1.py q1/palendrome_0.txt


Idea:
Read each line, remove spaces, compare it with its reverse, print true/false for each, and count the total number of palindromes.

Problem 2 — Unique Substrings (Recursion)

Goal: Use recursion to find and count all unique substrings of a string.
Run:

python q2/q2.py q2/q2.txt


Idea:
Recursively expand start and end positions to get all substrings, store them in a set to avoid duplicates, and print the count.

Problem 3 — Reverse Stack (Recursion)

Goal: Reverse a stack using recursion (array, singly linked list, and doubly linked list).
Run:

python q3/q3.py q3/q3.txt


Idea:
Pop all elements recursively and insert each one back at the bottom to reverse the stack.

Problem 4 — Ghostbusters

Goal: Check if all Ghostbusters can shoot their ghosts without the streams crossing.
Run:

python q4/q4.py q4/ghostbusters_input_0.txt


Idea:
Treat each Ghostbuster–Ghost pair as a line segment and check if any two lines intersect.
If none cross, all ghosts are eliminated.

Screenshots

Each folder includes a screenshot of the program running:
q1.png, q2.png, q3.png, q4.png.

Submission

All files are in this Homework3 folder.
