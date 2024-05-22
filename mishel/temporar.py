import tkinter as tk

# Create a list to store the entries
entry_list = []

def add_entry():
    # Retrieve text from the entry widget
    entry_text = entry.get()
    
    # Append the text to the list
    entry_list.append(entry_text)
    
    # Optionally, print the updated list
    print(entry_list)

# Create a Tkinter window
root = tk.Tk()

# Create an Entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button to add the entry to the list
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.pack()

# Run the Tkinter event loop
root.mainloop()
