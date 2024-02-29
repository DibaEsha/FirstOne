import tkinter as tk
from tkinter import messagebox

def reverse(num):
    # Reverses the digits of a number
    rev = 0
    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    return rev

def isPalindrome(num):
    # Checks if a number is a palindrome
    return num == reverse(num)

def findLychrel(number, max_iterations=240):
    for i in range(max_iterations):
        number = number + reverse(number)
        if isPalindrome(number):
            return i + 1, number
    return max_iterations, number

def run_program():
    try:
        input_number = int(entry.get())
        iterations, palindrome = findLychrel(input_number)
        
        result_text.set(f"Input number: {input_number}\n")
        result_text.set(result_text.get() + f"Is Lychrel: {iterations == 240}\n")
        result_text.set(result_text.get() + f"Iterations completed: {iterations}\n")
        if iterations == 240:
            result_text.set(result_text.get() + f"Last number reached: {palindrome}\n")
        else:
            result_text.set(result_text.get() + f"Palindrome number: {palindrome}\n")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid natural number.")

# Create GUI
root = tk.Tk()
root.title("Lychrel Number Checker")

label = tk.Label(root, text="Enter a natural number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

run_button = tk.Button(root, text="Check Lychrel", command=run_program)
run_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()