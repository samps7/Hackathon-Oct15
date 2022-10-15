

import mysql.connector as msql
import config
import tkinter as tk
from cryptography.fernet import Fernet

def main():
    key = Fernet.generate_key()
    f = Fernet(key)
    

    main_window=tk.Tk()
    main_window.title('Homework Planner')
    main_window.geometry("500x200")
    main_window.eval('tk::PlaceWindow . center')
    main_window.mainloop()
    

    try: 
        # connection info
        usr = config.mysql['user']
        pwd = config.mysql['pass']
        hst = config.mysql['host']
        dab = 'ssovi_DB'
        # create a connection
        con = msql.connect(user=usr,password=pwd, host=hst, database=dab)
        user_input_1 = 0
        rs = con.cursor()
        #rs.reset()
        
        
    except msql.Error as err:
        print(err)

    finally:
        rs.close()
        con.close()

if __name__ == '__main__':
    main()