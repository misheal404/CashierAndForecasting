import tkinter as tk
import pandas as pd
import os
from tkinter import ttk
import datetime

def csv_all(dataframe, file_name):
    file_path = os.path.join("C:\\Users\\USER\\git rep\\CashierAndForecasting\\build new\\database", f"{file_name}.csv")
    if os.path.exists(file_path):
        dataframe.to_csv(file_path, mode='a', header=False, index=False)
    else:
        dataframe.to_csv(file_path, index=False)

usn = []
pw = []
menu = []
harga = []
total = []
amm = []

dfZ = pd.DataFrame({
    'Menu': ['Americano', 'Espresso', 'Latte', 'Cappucino', 'Cold Brew', 'Matcha Latte', 'Hazelnut Latte', 'Mocha Latte'],
    'Harga': [25000, 28000, 33000, 33000, 33000, 40000, 40000, 40000]
})

menuC = ['Americano', 'Espresso', 'Latte', 'Cappucino', 'Cold Brew', 'Matcha Latte', 'Hazelnut Latte', 'Mocha Latte']
def display_menu():
    print('1. Americano')
    print('2. Espresso')
    print('3. Latte')
    print('4. Cappucino')
    print('5. Cold Brew')
    print('6. Matcha Latte')
    print('7. Hazelnut Latte')
    print('8. Mocha Latte')


def add(menu_num, amm_entry):

    menu_pilihan = input('add menu or done : ')
    jumlah = int(input('add the amount of the product :'))
    if menu_pilihan in dfZ['Menu'].values:
        harga_pilihan = dfZ[dfZ['Menu'] == menu_pilihan]['Harga'].values[0]
        total_harga = harga_pilihan * jumlah
        menu.append(menu_pilihan)
        harga.append(harga_pilihan)
        amm.append(jumlah)
        total.append(total_harga)

def add_login():
    username = input('add your username : ')
    password = input('add your password : ')
    usn.append(username)
    pw.append(password)
def DF_usn():
    dfU = pd.DataFrame({
        'Username': usn,
        'Password': pw
    })
def DF_menu():
    dfM = pd.DataFrame({
        'Menu': menu,
        'Harga': harga,
        'Satuan': amm,
        'Total': total
    })
    return dfM

print('WELCOME TO THE CHRONICLE')
print('-------------------------')
ard = input('Do you want to continue?  (yes/no) : ')
print('------------------------------------------------')
if ard == 'yes':
    
    add_login()
    print('--------------------------------------------------------')
    DF_usn()
    print('1. Cashier')
    print('2. Report Selling')
    choice = input('Choose your option (1/2): ')
    #print('------------------------------------------------')
    if choice == '1' :
        print('------------------------------------------------')
        print('Welcome to Cashier')
        while True:
            display_menu()
            print('------------------------------------------------')
            menu_pilihanTemp = int(input ('add menu : '))
            if menu_pilihanTemp == 0:
                break
            try :
                c= (menu_pilihanTemp-1)
                jumlah = int(input('add the amount of the product :'))
                menu_pilihan = menuC[c]
                if menu_pilihan in dfZ['Menu'].values:
                    harga_pilihan = dfZ[dfZ['Menu'] == menu_pilihan]['Harga'].values[0]
                    total_harga = harga_pilihan * jumlah
                    menu.append(menu_pilihan)
                    harga.append(harga_pilihan)
                    amm.append(jumlah)
                    total.append(total_harga)
            except ValueError:
                print('Invalid input, please enter a valid number.')
                #DF_menu()
        df_new = DF_menu()   
        print(df_new)
        csv_all(df_new, 'tes_logic')
        total_sub = int(sum(total))
        print('Payment Method')
        print('1. Cash')
        print('2. Emoney')
        choose_P = input('Choose the payment method (1/2) : ')
        print('--------------------------------------------------------')
        if choose_P == '1' :
            print('Cash Payment')
            cash_m = int(input('Add the customer'))
            if cash_m >= total_sub :
                print('Cash : ', cash_m)
                print('Total Payment :', total_sub)
                print('Change :', cash_m - total_sub)
                print('------------------------------------------')
                print('Thank you for shopping at The Chronicle')
            elif cash_m <= total_harga:
                print('Insufficient Cash')
            else :
                print('Cash : ', cash_m)
                print('Total Payment :', total_sub)
                print('------------------------------------------')
                print('Thank you for shopping at The Chronicle')
        elif choose_P == '2':
            print('--------------------------------------------------------')
            print('E M O N E Y  P AY M E N T')
            print('1. Dana')
            print('2. OVO')
            print('3. Gopay')
            choose_E = input('Choose the e-money method : ')
            print('--------------------------------------------------------')
            print('Payment method   :', choose_E)
            print('Money in         : ', total_sub)
            print('Total Payment    :', total_sub)
            print('Thank you for shopping at The Chronicle')
    elif choice == '2':
        r = 'C:\\Users\\USER\\git rep\\CashierAndForecasting\\build new\\database\\tes_logic.csv'
        fg = pd.read_csv(r)
        print('--------------------------------------------------------')
        print('S E L L I N G   R E P O R T')
        print(fg)





else:
    print('Thank you for visiting')


    


