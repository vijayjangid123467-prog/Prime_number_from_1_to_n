Prime Number Generator in Python
📌 Project Description
This Python program generates and prints all prime numbers from 2 up to a user-entered number.

A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

🚀 Features
Takes a number as input from the user.
Checks each number to determine whether it is prime.
Uses nested for loops to check divisibility.
Uses the break statement to stop checking when a divisor is found.
Uses Python's for-else statement to print prime numbers.
💻 Code

python
n = int(input("Enter number for prime number:"))

for i in range(2, n + 1):
    for t in range(2, i):
        if i % t == 0:
            break
    else:
        print(i)
▶️ How to Run
Install Python 3 on your system.
Save the code in a file named prime.py.
Open the terminal.
Run the following command:

bash
python prime.py
📤 Example Output

text
Enter number for prime number: 20
2
3
5
7
11
13
17
19
🧠 Concepts Used
Python input() function
Type conversion using int()
Nested for loops
if condition
Modulus operator (%)
break statement
for-else statement
⏱️ Time Complexity
The approximate time complexity is O(n²) because the program checks divisibility for each number up to n.

📄 License
This project is open-source and free to use for learning and educational purposes.
