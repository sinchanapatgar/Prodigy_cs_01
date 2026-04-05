"""
PRODIGY_CS_01 - Caesar Cipher
Prodigy Infotech Cybersecurity Internship - Task 01
Encrypt and decrypt text using the Caesar Cipher algorithm.
"""

import tkinter as tk
from tkinter import ttk, messagebox


def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher - PRODIGY_CS_01")
        self.root.geometry("680x520")
        self.root.configure(bg="#0f0f1a")
        self.root.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#0f0f1a")
        title_frame.pack(pady=(24, 0))

        tk.Label(title_frame, text="🔐 Caesar Cipher", font=("Courier New", 22, "bold"),
                 fg="#00ffcc", bg="#0f0f1a").pack()
        tk.Label(title_frame, text="PRODIGY INFOTECH  |  CS Task 01",
                 font=("Courier New", 9), fg="#555577", bg="#0f0f1a").pack(pady=(2, 0))

        # Divider
        tk.Frame(self.root, height=1, bg="#1e1e3a").pack(fill='x', padx=30, pady=14)

        # Input
        self._label("Input Message")
        self.input_text = self._textbox()

        # Shift row
        shift_frame = tk.Frame(self.root, bg="#0f0f1a")
        shift_frame.pack(padx=40, fill='x', pady=(10, 0))

        tk.Label(shift_frame, text="Shift Value (1–25):", font=("Courier New", 10),
                 fg="#aaaacc", bg="#0f0f1a").pack(side='left')

        self.shift_var = tk.IntVar(value=3)
        shift_spin = tk.Spinbox(shift_frame, from_=1, to=25, textvariable=self.shift_var,
                                width=5, font=("Courier New", 12, "bold"),
                                bg="#1a1a2e", fg="#00ffcc", insertbackground="#00ffcc",
                                buttonbackground="#1a1a2e", relief='flat',
                                highlightthickness=1, highlightbackground="#2e2e5e")
        shift_spin.pack(side='left', padx=12)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#0f0f1a")
        btn_frame.pack(pady=16)

        self._btn(btn_frame, "  ENCRYPT  ", "#00ffcc", "#003333", self.encrypt).pack(side='left', padx=10)
        self._btn(btn_frame, "  DECRYPT  ", "#ff6b9d", "#330022", self.decrypt).pack(side='left', padx=10)
        self._btn(btn_frame, "   CLEAR   ", "#555577", "#111122", self.clear).pack(side='left', padx=10)

        # Output
        self._label("Output")
        self.output_text = self._textbox(state='disabled')

        # Status bar
        self.status_var = tk.StringVar(value="Ready — Enter a message and choose a shift value.")
        tk.Label(self.root, textvariable=self.status_var, font=("Courier New", 8),
                 fg="#555577", bg="#0f0f1a").pack(pady=(8, 0))

    def _label(self, text):
        tk.Label(self.root, text=text, font=("Courier New", 10, "bold"),
                 fg="#7777aa", bg="#0f0f1a", anchor='w').pack(padx=40, fill='x', pady=(10, 2))

    def _textbox(self, state='normal'):
        frame = tk.Frame(self.root, bg="#1a1a2e", bd=0,
                         highlightthickness=1, highlightbackground="#2e2e5e")
        frame.pack(padx=40, fill='x')
        tb = tk.Text(frame, height=4, font=("Courier New", 11),
                     bg="#1a1a2e", fg="#e0e0ff", insertbackground="#00ffcc",
                     relief='flat', padx=10, pady=8, state=state,
                     wrap='word', selectbackground="#2e2e6e")
        tb.pack(fill='x')
        return tb

    def _btn(self, parent, text, fg, bg, cmd):
        return tk.Button(parent, text=text, font=("Courier New", 10, "bold"),
                         fg=fg, bg=bg, activeforeground=fg, activebackground="#1a1a2e",
                         relief='flat', cursor='hand2', bd=0,
                         highlightthickness=1, highlightbackground=fg,
                         command=cmd, pady=8)

    def encrypt(self):
        msg = self.input_text.get("1.0", "end-1c").strip()
        if not msg:
            messagebox.showwarning("Empty Input", "Please enter a message to encrypt.")
            return
        shift = self.shift_var.get()
        result = caesar_encrypt(msg, shift)
        self._set_output(result)
        self.status_var.set(f"✅ Encrypted with shift={shift}")

    def decrypt(self):
        msg = self.input_text.get("1.0", "end-1c").strip()
        if not msg:
            messagebox.showwarning("Empty Input", "Please enter a message to decrypt.")
            return
        shift = self.shift_var.get()
        result = caesar_decrypt(msg, shift)
        self._set_output(result)
        self.status_var.set(f"🔓 Decrypted with shift={shift}")

    def clear(self):
        self.input_text.delete("1.0", "end")
        self._set_output("")
        self.status_var.set("Cleared — Ready for new input.")

    def _set_output(self, text):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)
        self.output_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()
