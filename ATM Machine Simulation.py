import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, balance=5000):
        self.balance = balance

    def check_balance(self):
        return f"Current Balance: ₹{self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount."
        self.balance += amount
        return f"₹{amount} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        elif amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"₹{amount} withdrawn successfully."

class ATMGUI:
    def __init__(self, root, atm):
        self.root = root
        self.atm = atm
        self.root.title("ATM Machine")
        self.root.geometry("320x420")
        self.root.configure(bg="#f0f8ff")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="ATM Simulation", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#2f4f4f")
        self.label.pack(pady=20)

        self.balance_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#00008b")
        self.balance_label.pack(pady=10)

        self.amount_entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.amount_entry.pack(pady=10)
        self.amount_entry.insert(0, "Enter amount")

        # Create colorful buttons
        self.deposit_btn = tk.Button(root, text="Deposit", width=18, bg="#4CAF50", fg="white", font=("Arial", 12), command=self.deposit)
        self.deposit_btn.pack(pady=5)

        self.withdraw_btn = tk.Button(root, text="Withdraw", width=18, bg="#f44336", fg="white", font=("Arial", 12), command=self.withdraw)
        self.withdraw_btn.pack(pady=5)

        self.check_btn = tk.Button(root, text="Check Balance", width=18, bg="#2196F3", fg="white", font=("Arial", 12), command=self.check_balance)
        self.check_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", width=18, bg="#808080", fg="white", font=("Arial", 12), command=root.quit)
        self.exit_btn.pack(pady=20)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            msg = self.atm.deposit(amount)
            messagebox.showinfo("Deposit", msg)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            msg = self.atm.withdraw(amount)
            messagebox.showinfo("Withdraw", msg)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")

    def check_balance(self):
        msg = self.atm.check_balance()
        self.balance_label.config(text=msg)

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM()
    gui = ATMGUI(root, atm)
    root.mainloop()
