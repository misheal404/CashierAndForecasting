import pandas as pd
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to group and sum Subtotal by Item
def item_category(DataFrame):
    jumlah = DataFrame.groupby('Item')['Subtotal'].sum().reset_index()
    return jumlah

# Function to save DataFrame to a CSV file, appending without headers if file exists and there's new data
def csv_all(dataframe, file_name):
    file_path = os.path.join("C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data", f"{file_name}.csv")
    
    # Check if the file exists
    if os.path.exists(file_path):
        existing_df = pd.read_csv(file_path)
        if not existing_df.equals(dataframe):
            dataframe.to_csv(file_path, mode='a', index=False, header=False)
            print(f"DataFrame updated and saved to {file_path}")
        else:
            print(f"No update required for {file_path}")
    else:
        dataframe.to_csv(file_path, index=False)
        print(f"DataFrame saved to {file_path}")

# Function to group and sum Quantity by Item, then merge with Subtotal
def product_selling(DataFrame):
    jumlah = DataFrame.groupby('Item')['Quantity'].sum().reset_index()
    subtotal_df = item_category(DataFrame)
    result = pd.merge(jumlah, subtotal_df, on='Item', how='left')
    return result

# Function to find the maximum quantity sold for a product
def best_product(DataFrame):
    jumlah = DataFrame.groupby('Item')['Quantity'].sum().reset_index()
    max_quantity = jumlah.loc[jumlah['Quantity'].idxmax()]
    return max_quantity

# Function to find the top buyer based on Subtotal
def top_buyer(DataFrame):
    jumlah = DataFrame.groupby('Customer')['Subtotal'].sum().reset_index()
    max_subtotal = jumlah.loc[jumlah['Subtotal'].idxmax()]
    return max_subtotal

# Function to group and sum Subtotal by Customer
def selling_buyer(DataFrame):
    jumlah = DataFrame.groupby('Customer')['Subtotal'].sum().reset_index()
    return jumlah

# Load the sales data
file_path = 'C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data\\sales_data.csv'
selling_data = pd.read_csv(file_path)

# Generate DataFrames for each category
item = item_category(selling_data)
buyer_all = selling_buyer(selling_data)
top_buyeerr = top_buyer(selling_data)
product = product_selling(selling_data)
best_menu = best_product(selling_data)

# Save DataFrames to CSV files for each category
csv_all(item, 'item_category')
csv_all(buyer_all, 'buyer_all')
csv_all(product, 'Product_Selling_Detail')

# Testing output
print(buyer_all)
print(product)
print(item)


import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("CSV Viewer")
        self.geometry("300x200")
        
        self.label = tk.Label(self, text="Select a CSV file to view:")
        self.label.pack(pady=10)
        
        self.product_selling_detail_button = tk.Button(self, text="View Product_Selling_Detail.csv", command=self.open_product_selling_detail)
        self.product_selling_detail_button.pack(pady=10)
    
    def open_product_selling_detail(self):
        # Fixed file path
        file_path = 'C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data\\Product_Selling_Detail.csv'
        ProductSellingDetailWindow(self, file_path)

class ProductSellingDetailWindow(tk.Toplevel):
    def __init__(self, master, file_path):
        super().__init__(master)
        
        self.title("Product Selling Detail")
        self.geometry("800x600")
        
        self.df = pd.read_csv(file_path)
        self.create_widgets()
        self.display_table()
        self.display_graph()

    def create_widgets(self):
        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    def display_table(self):
        cols = list(self.df.columns)
        self.tree = ttk.Treeview(self.table_frame, columns=cols, show='headings')
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))
        
        self.tree.pack(fill="both", expand=True)

    def display_graph(self):
        fig, ax = plt.subplots()
        ax.bar(self.df['Item'], self.df['Subtotal'])
        ax.set_xlabel('Item')
        ax.set_ylabel('Subtotal')
        ax.set_title('Subtotal by Item')
        
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()



# Load the CSV data
sales_data = pd.read_csv('C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data\\sales_data.csv')

# Process the data
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['YearMonth'] = sales_data['Date'].dt.to_period('M')
monthly_sales = sales_data.groupby('YearMonth')['Subtotal'].sum().reset_index()
monthly_sales['YearMonth'] = monthly_sales['YearMonth'].dt.to_timestamp()

# Function to plot data using Tkinter
def plot_monthly_sales():
    root = tk.Tk()
    root.title("Monthly Sales Data")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_sales['YearMonth'], monthly_sales['Subtotal'], marker='o', linestyle='-', color='b')
    ax.set_title('Monthly Sales Data')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Sales')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    fig.autofmt_xdate()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    root.mainloop()

plot_monthly_sales()

