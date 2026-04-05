🔐 PRODIGY_CS_01 – Caesar Cipher
Prodigy Infotech Cybersecurity Internship – Task 01
📌 Overview
A Python GUI application that encrypts and decrypts text using the Caesar Cipher algorithm. The user can input any message and choose a shift value to perform encryption or decryption instantly.
🖥️ Features
🔒 Encrypt any text message using a shift value (1–25)
🔓 Decrypt Caesar-encrypted messages
Handles uppercase, lowercase, and non-alphabetic characters correctly
Clean dark-themed GUI built with Tkinter
Clear button to reset inputs
🧠 How Caesar Cipher Works
Each letter in the message is shifted forward (encrypt) or backward (decrypt) by the chosen number of positions in the alphabet.
Example with shift = 3:
Plain:    H E L L O
Encrypted: K H O O R
Non-alphabetic characters (spaces, numbers, symbols) remain unchanged.
🚀 How to Run
Prerequisites
Python 3.8+
No extra libraries needed (uses built-in tkinter)
Run the Program
python PRODIGY_CS_01.py
🖼️ Usage
Type your message in the Input Message box
Set the Shift Value (1–25) using the spinner
Click ENCRYPT to encrypt or DECRYPT to decrypt
Output appears in the Output box
Click CLEAR to reset
📁 File Structure
PRODIGY_CS_01/
├── PRODIGY_CS_01.py   # Main program
└── README.md          # Documentation
🛠️ Tech Stack
Tool
Purpose
Python 3
Core language
tkinter
GUI framework
⚠️ Limitations
Caesar Cipher is a basic substitution cipher and is not secure for real-world use
Only alphabetic characters are shifted; all other characters pass through unchanged
