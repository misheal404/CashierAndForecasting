import pandas as pd
import os
def add_csv(login_usn, pass_usn):
    # Get the file name from the user
    
    usn = []
    pw = []
    usn.append(login_usn)
    usn.append(pass_usn)
    df_login = pd.DataFrame({'Username' : [usn], 'Password' : [pw]})
    df_login.to_csv('login.csv', index=False, header=True)
    def to_csv():
        folder_path = r"C:\Users\USER\git rep\CashierAndForecasting\mishel\data"
        file_name = usn
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        return df
    def csv_all(dataframe, file_name):
        file_path = os.path.join("C:\Users\USER\git rep\CashierAndForecasting\mishel\data", f"{file_name}.csv")
        # Check if the file already exists
        if os.path.exists(file_path):
            dataframe.to_csv(file_path, mode='a', index=False)
        else:
            dataframe.to_csv(file_path, index=False)
        print(f"DataFrame saved to {file_path}")