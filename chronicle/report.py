import pandas as pd
import os

def item_category(DataFrame):
    jumlah = DataFrame.groupby('Item')['Subtotal'].sum().reset_index()
    #print(jumlah)
    return jumlah
def csv_all(dataframe, file_name):
    file_path = os.path.join("C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data", f"{file_name}.csv")
    # Check if the file already exists
    if os.path.exists(file_path):
        dataframe.to_csv(file_path, mode='a', index=False)
    else:
        dataframe.to_csv(file_path, index=False)
    print(f"DataFrame saved to {file_path}")

def product_selling(DataFrame):
    jumlah = DataFrame.groupby('Item')['Quantity'].sum().reset_index()
    
    subtotal_df = item_category(DataFrame)

    result = pd.merge(jumlah, subtotal_df, on='Item', how='left')
    return result

def best_product(DataFrame):
    jumlah = DataFrame.groupby('Item')['Quantity'].sum().reset_index()
    max = jumlah.max()
    return max
# top buyer
def top_buyer(DataFrame):
    jumlah = DataFrame.groupby('Customer')['Subtotal'].sum().reset_index()
    max = jumlah.max()
    return max
def selling_buyer(DataFrame):
    jumlah = DataFrame.groupby('Customer')['Subtotal'].sum().reset_index()
    max = jumlah.max()
    return jumlah

file_path = 'C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data\\sales_data.csv'
selling_data = pd.read_csv(file_path)

#DataFrsme each categoryy
item = item_category(selling_data)
buyer_all = selling_buyer(selling_data)
top_buyeerr = top_buyer(selling_data)
product = product_selling(selling_data)
best_menu = best_product(selling_data)

#DataFrame to csv for each category
csv_all(item, 'item_category')
csv_all(buyer_all, 'buyer_all')
csv_all(product, 'Product_Selling_Detail')

#testing
print(buyer_all)
print(product)
