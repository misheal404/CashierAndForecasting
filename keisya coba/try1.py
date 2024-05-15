import tkinter as tk


class CafeMenuDisplay:
    def __init__(self, master):
        self.master = master
        self.master.title("Cafe Menu")
        
        self.menu_items = {
            "Coffee": 2.50,
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header label
        header_label = tk.Label(self.master, text="Welcome to Our Cafe", font=("Helvetica", 18, "bold"))
        header_label.pack(pady=10)
        
        # Menu items
        for item, price in self.menu_items.items():
            item_label = tk.Label(self.master, text=f"{item}: ${price:.2f}", font=("Helvetica", 12))
            item_label.pack(anchor="w", padx=20)
        
        # Exit button
        exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        exit_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = CafeMenuDisplay(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from PIL import Image, ImageTk

class CafeMenuDisplay:
    def __init__(self, master):
        self.master = master
        self.master.title("Cafe Menu")
        
        self.menu_items = {
            "Coffee": {"price": 2.50, "image": "1.png"},
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Header label
        header_label = tk.Label(self.master, text="Welcome to Our Cafe", font=("Helvetica", 18, "bold"))
        header_label.pack(pady=10)
        
        # Menu items
        for item, details in self.menu_items.items():
            frame = tk.Frame(self.master)
            frame.pack(anchor="w", padx=20, pady=5)
            
            # Load image
            image = Image.open(details["1.png"])
            image = image.resize((50, 50), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            
            label = tk.Label(frame, imagec=photo)
            label.image = photo
            label.pack(side="left", padx=10)
            
            item_label = tk.Label(frame, text=f"{item}: ${details['price']:.2f}", font=("Helvetica", 12))
            item_label.pack(side="left")
        
        # Exit button
        exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        exit_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = CafeMenuDisplay(root)
    root.mainloop()

if __name__ == "__main__":
    main()
