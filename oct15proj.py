

import mysql.connector as msql
import config
import tkinter as tk
from cryptography.fernet import Fernet
import ast

def main():
    file = open('key.key', 'rb')  # Open the file as wb to read bytes
    key = file.read()  # The key will be type bytes
    file.close()
    key = Fernet.generate_key()
    fernet = Fernet(key)



    

    '''
    main_window=tk.Tk()
    main_window.title('Homework Planner')
    main_window.geometry("500x200")
    main_window.eval('tk::PlaceWindow . center')
    main_window.mainloop()
    '''


    try: 
        '''
        with open('account.txt') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        
        for i in range(len(lines)):
            lines[i] = fernet.encrypt(lines[i].encode())
           
        
        with open('account1.txt', 'w') as f:
            for line in lines:
                f.write("%s\n" %(line))
        
        
        for i in range(len(lines)):
            lines[i] = fernet.decrypt(lines[i])
        '''
        
        with open('account.txt') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        
        string_lit = f"{lines[0]}{','}{lines[1]}{','}{lines[2]}"
        print(string_lit)

        for i in range(len(lines)):
            lines[i] = fernet.encrypt(lines[i].encode())
        
        #with open('account1.txt', 'w') as f:
        #    for line in lines:
        #        f.write("%s\n" %(line))

        encrypted_string_lit = fernet.encrypt(string_lit.encode())
        with open('license.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_string_lit)

        #with open('file.txt', 'rb') as file:
            #original = file.read()
        
        
        for i in range(len(lines)):
            lines[i] = fernet.decrypt(lines[i])
        

        usr = lines[1]
        pwd = lines[2]
        hst = lines[0]
        dab = 'ssovi_DB'
        # create a connection
        
        con = msql.connect(user=usr,password=pwd, host=hst, database=dab)
        user_input_1 = 0
        rs = con.cursor()
        
    except msql.Error as err:
        print(err)

    finally:
        rs.close()
        con.close()

if __name__ == '__main__':
    main()