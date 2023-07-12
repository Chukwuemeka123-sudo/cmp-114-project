import tkinter as tk
from tkinter import messagebox

class SavingsAccountGUI:
    def __init__(self):
        self.balance = 0

        self.root = tk.Tk()
        self.root.title("Savings Account")

        self.label_balance = tk.Label(self.root, text="Current Balance: #0")
        self.label_balance.pack()

        self.label_deposit = tk.Label(self.root, text="Deposit Amount:")
        self.label_deposit.pack()

        self.entry_deposit = tk.Entry(self.root)
        self.entry_deposit.pack()

        self.button_deposit = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.button_deposit.pack()

        self.label_withdraw = tk.Label(self.root, text="Withdraw Amount:")
        self.label_withdraw.pack()

        self.entry_withdraw = tk.Entry(self.root)
        self.entry_withdraw.pack()

        self.button_withdraw = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack()

    def deposit(self):
        try:
            amount = float(self.entry_deposit.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            self.label_balance.config(text="Current Balance: #{:.2f}".format(self.balance))
            self.entry_deposit.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid deposit amount!")

    def withdraw(self):
        try:
            amount = float(self.entry_withdraw.get())
            if amount <= 0:
                raise ValueError
            if amount > self.balance:
                raise ValueError("Insufficient funds!")
            self.balance -= amount
            self.label_balance.config(text="Current Balance: #{:.2f}".format(self.balance))
            self.entry_withdraw.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SavingsAccountGUI()
    app.run()
