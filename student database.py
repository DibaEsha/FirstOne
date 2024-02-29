import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog

class StudentDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database App")
        self.root.geometry("400x300")

        # Create database (initially empty)
        self.database = pd.DataFrame(columns=["Name", "Number", "Birthday", "Major", "Minor", "Blood Group"])

        # GUI elements
        self.label = tk.Label(root, text="Student Database", font=("Helvetica", 16))
        self.label.pack()

        self.add_button = tk.Button(root, text="Add Record", command=self.add_record)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View All Records", command=self.view_records)
        self.view_button.pack()

        self.search_button = tk.Button(root, text="Search Records", command=self.search_records)
        self.search_button.pack()

        self.export_button = tk.Button(root, text="Export to Excel", command=self.export_to_excel)
        self.export_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

    def add_record(self):
        # Implement logic to add a new record (e.g., using entry widgets)
        # Update self.database with the new record

        # Example: Ask user for input (you can create entry widgets for each field)
        name = "John Doe"
        number = "1234567890"
        birthday = "2000-01-01"
        major = "Computer Science"
        minor = "Mathematics"
        blood_group = "A+"

        self.database = self.database.append({
            "Name": name,
            "Number": number,
            "Birthday": birthday,
            "Major": major,
            "Minor": minor,
            "Blood Group": blood_group
        }, ignore_index=True)

        messagebox.showinfo("Success", "Record added successfully!")

    def view_records(self):
        # Display all records in a new window (e.g., using a listbox)
        # You can use self.database to populate the listbox

        # Example: Show records in a messagebox
        records_text = "\n".join(self.database["Name"])
        messagebox.showinfo("All Records", records_text)

    def search_records(self):
        # Implement logic to search records based on partial name match, number match, or birthday
        # Display the matching records in a new window

        # Example: Search by partial name match
        search_name = "John"
        matching_records = self.database[self.database["Name"].str.contains(search_name, case=False)]
        records_text = "\n".join(matching_records["Name"])
        messagebox.showinfo("Matching Records", records_text)

    def export_to_excel(self):
        # Export self.database to an Excel file
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            self.database.to_excel(file_path, index=False)
            messagebox.showinfo("Export Successful", f"Data exported to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDatabaseApp(root)
    root.mainloop()