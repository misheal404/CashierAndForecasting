import pandas as pd
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
file_path = 'C:\\Users\\USER\\git rep\\CashierAndForecasting\\chronicle\\data\\sales_data.csv'
selling_data = pd.read_csv(file_path)

jumlah_ietem = selling_data.groupby('Item')['Subtotal'].sum().reset_index()
jumlah = selling_data.groupby('Item')['Quantity'].sum().reset_index()
subtotal_df = jumlah_ietem
result = pd.merge(jumlah, subtotal_df, on='Item', how='left')

jumlah_buyer = selling_data.groupby('Customer')['Subtotal'].sum().reset_index()


csv_all(jumlah_buyer, 'buyer_all')
csv_all(result, 'Product_Selling_Detail')



