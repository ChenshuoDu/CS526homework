CS526 Week 1 Assignment
Author: Chenshuo Du
Course: CS526

----------------------------------------
Description
----------------------------------------
This assignment ensures that the Python environment is correctly set up.
The program "helloworld.py" reads input (from a file or console) and prints it back to the output.

----------------------------------------
Files
----------------------------------------
- helloworld.py  -> Main Python program
- myfile         -> Sample text file containing test input
- readme.txt     -> Documentation file (this file)

----------------------------------------
Requirements
----------------------------------------
- Python 3.x installed
- Command Prompt (CMD) on Windows
  (Note: PowerShell redirection may cause issues)

----------------------------------------
How to Run (CMD Only)
----------------------------------------

1. Run with a file as input
   Make sure "myfile" exists in the same folder as "helloworld.py".
   Example content of "myfile":
   Hello from Chenshuo Du

   Command:
   python helloworld.py < myfile

   Output:
   Hello from Chenshuo Du

2. Run with direct input from console
   Command:
   echo HelloTest | python helloworld.py

   Output:
   HelloTest

3. Run manually and type input
   Command:
   python helloworld.py

   Then type your input, for example:
   This is a test

   To finish input:
   - On Windows CMD: Press Ctrl+Z then Enter
   - On Mac/Linux: Press Ctrl+D

   Output:
   This is a test

----------------------------------------
Submission Instructions
----------------------------------------
1. Create a new repository on GitHub (example name: CS526-Week1).
2. Upload these files:
   - helloworld.py
   - myfile
   - readme.txt
3. Commit and push your changes.
4. Email your GitHub repository link to the professor.

----------------------------------------
Notes
----------------------------------------
- Please use CMD instead of PowerShell.
  PowerShell treats "<" and "|" differently and may cause errors.
  CMD runs the commands correctly with file redirection and piping.
