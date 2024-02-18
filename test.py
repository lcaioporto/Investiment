import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("User Input")

    # Define the input fields
    name_label = tk.Label(root, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=10, pady=5)

    age_label = tk.Label(root, text="Age:")
    age_label.grid(row=1, column=0, padx=10, pady=5)
    age_entry = tk.Entry(root)
    age_entry.grid(row=1, column=1, padx=10, pady=5)

    # Function to retrieve user input
    def submit():
        name = name_entry.get()
        age = age_entry.get()
        if name and age:
            print("Name:", name)
            print("Age:", age)
        else:
            print("Please fill in all fields.")
        root.destroy()

    # Button to submit the input
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=2, columnspan=2, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    get_user_input()
