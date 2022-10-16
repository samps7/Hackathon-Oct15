import mysql.connector as msql
import tkinter as tk
from tkcalendar import DateEntry
#from getpass import getpass
from cryptography.fernet import Fernet

def main():
    #key = Fernet.generate_key()
    #print(sys.path)
    key = b'tUkvAk_eCodv08W4p_o62yhSZ8XRVX3-9sRpjZu805k='
    fernet = Fernet(key)

    try: 

        with open('license.txt', 'rb') as file:
            str_lit = file.read()
        
        str_lit = fernet.decrypt(str_lit)
        str_lit = str_lit.decode('utf-8')
        lines_1 = str_lit.split(",")
        lines_2 = []
        for i in range(len(lines_1)):
            lines_2.append(lines_1[i].encode('utf-8'))
        



        usr = lines_2[1]
        pwd = lines_2[2]
        hst = lines_2[0]
        dab = "ssovi_DB"
        # create a connection
        
        con = msql.connect(user=usr,password=pwd, host=hst, database=dab)
        user_input_1 = 0
        rs = con.cursor()

        print("Database connected successfully")


        def show_asgn_window():
            main_window=tk.Tk()
            main_window.title('Show Assignments')
            main_window.geometry("340x600")
            main_window.eval('tk::PlaceWindow . center')
            main_window.configure(bg='light blue')

            #cal = DateEntry(main_window, width=12, year=2019, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
            #cal.pack(padx=10, pady=10)

            text_entry1 = 0
            text_entry2 = 0
            text_entry3 = 0
            date_entry1 = 0
            frame1 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame1.grid(row=1, column=0)

            rs = con.cursor()
            query = 'SELECT class_name, asgn_name FROM assignment'

            # execute the query
            rs.execute(query)
            # pretty print the query results:
            row_count = 0
            row_count+=1
            for (class_name, asgn_name) in rs:
                ##print()
                row_count += 1
                label1 = tk.Label(frame1, text='class: {}, asgn: {}'.format(class_name, asgn_name), bg="dark grey", fg="white", font="none 12 bold")
                label1.grid(row = row_count, column = 1, sticky= 'w')
            
            def leave_classes():
                
                main_window.destroy()
                
                
                
            
            #query = 'CREATE TABLE '
            # execute the query
            #rs.execute(query)

            

            frame4 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame4.grid(row=3, column=0)

            row_count = 0
            row_count+=1

            
            output = tk.Button(frame4, text = "Return", width = 6, command = leave_classes)
            output.grid(row = 1, column = 0)
            

            main_window.mainloop()

        def show_classes_window():
            main_window=tk.Tk()
            main_window.title('Show Classes')
            main_window.geometry("340x600")
            main_window.eval('tk::PlaceWindow . center')
            main_window.configure(bg='light blue')

            #cal = DateEntry(main_window, width=12, year=2019, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
            #cal.pack(padx=10, pady=10)

            text_entry1 = 0
            text_entry2 = 0
            text_entry3 = 0
            date_entry1 = 0

            frame1 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame1.grid(row=1, column=0)

            rs = con.cursor()
            query = 'SELECT * FROM class'

            # execute the query
            rs.execute(query)
            # pretty print the query results:
            row_count = 0
            row_count+=1
            for (class_name) in rs:
                ##print()
                row_count += 1
                label1 = tk.Label(frame1, text='{}'.format(class_name), bg="dark grey", fg="white", font="none 12 bold")
                label1.grid(row = row_count, column = 1, sticky= 'w')


            
            def leave_classes():
                
                main_window.destroy()
                
                
                
            
            #query = 'CREATE TABLE '
            # execute the query
            #rs.execute(query)
            

            frame4 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame4.grid(row=3, column=0)

            

            
            output = tk.Button(frame4, text = "Return", width = 6, command = leave_classes)
            output.grid(row = 1, column = 0)
            

            main_window.mainloop()

        def create_class_window():
            main_window=tk.Tk()
            main_window.title('Add an Class')
            main_window.geometry("340x600")
            main_window.eval('tk::PlaceWindow . center')
            main_window.configure(bg='light blue')

            #cal = DateEntry(main_window, width=12, year=2019, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
            #cal.pack(padx=10, pady=10)

            text_entry1 = 0
            text_entry2 = 0
            text_entry3 = 0
            date_entry1 = 0
            
            def enter_class():
                q = "SELECT * FROM class WHERE class_name = %s"
                rs.execute(q, (text_entry1.get(),))
                if rs.fetchone() == None: 
                    print("")
                    # inserting query:
                    q = "INSERT INTO class (class_name) VALUES (%s)"
                    rs.execute(q, (text_entry1.get(),))
                    # commit the changes to the DB
                    con.commit()
                main_window.destroy()
                
            def go_back():
                main_window.destroy()   
                
            
            #query = 'CREATE TABLE '
            # execute the query
            #rs.execute(query)

            frame1 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame1.grid(row=1, column=0)
            

            frame4 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame4.grid(row=3, column=0)

            row_count = 0
            row_count+=1
            label1 = tk.Label(frame1, text="Class Name", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = row_count, column = 1, sticky= 'w')
            text_entry1 = tk.Entry(frame1, width = 20, bg="white")
            text_entry1.grid(row = row_count, column=2, sticky='w')
            row_count+=1
            

            
            output = tk.Button(frame4, text = "Enter", width = 6, command = enter_class)
            output.grid(row = 1, column = 0)

            output = tk.Button(frame4, text = "Return", width = 6, command = go_back)
            output.grid(row = 1, column = 1)
            

            main_window.mainloop()


        def delete_asgn_window():
            main_window=tk.Tk()
            main_window.title('Delete an Assignment')
            main_window.geometry("340x600")
            main_window.eval('tk::PlaceWindow . center')
            main_window.configure(bg='light blue')


            text_entry1 = 0
            text_entry2 = 0
            text_entry3 = 0
            date_entry1 = 0
            
            def delete_asgn():
                
                main_window.destroy()
                
            frame1 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame1.grid(row=0, column=0)

            frame4 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame4.grid(row=3, column=0)

            row_count = 0
            row_count+=1
            label1 = tk.Label(frame1, text="Class Name", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = row_count, column = 1, sticky= 'w')
            text_entry1 = tk.Entry(frame1, width = 20, bg="white")
            text_entry1.grid(row = row_count, column=2, sticky='w')
            row_count+=1

            label1 = tk.Label(frame1, text="Assignment Name", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = row_count, column = 1, sticky= 'w')
            text_entry2 = tk.Entry(frame1, width = 20, bg="white")
            text_entry2.grid(row = row_count, column=2, sticky='w')
            
            row_count+=1

            output = tk.Button(frame4, text = "Delete", width = 6, command = delete_asgn)
            output.grid(row = 1, column = 0)
            #cal.pack(padx=10, pady=10)
            

            main_window.mainloop()
        
        def delete_class_window():
            main_window=tk.Tk()
            main_window.title('Delete a Class')
            main_window.geometry("340x600")
            main_window.eval('tk::PlaceWindow . center')
            main_window.configure(bg='light blue')


            text_entry1 = 0
            text_entry2 = 0
            text_entry3 = 0
            date_entry1 = 0
            
            def delete_asgn():
                
                main_window.destroy()
                
            frame1 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame1.grid(row=0, column=0)

            frame4 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame4.grid(row=3, column=0)

            row_count = 0
            row_count+=1
            label1 = tk.Label(frame1, text="Class Name", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = row_count, column = 1, sticky= 'w')
            text_entry1 = tk.Entry(frame1, width = 20, bg="white")
            text_entry1.grid(row = row_count, column=2, sticky='w')
            row_count+=1
            

            output = tk.Button(frame4, text = "Delete", width = 6, command = delete_asgn)
            output.grid(row = 1, column = 0)
            #cal.pack(padx=10, pady=10)
            

            main_window.mainloop()
        
        def create_asgn_window():
            main_window=tk.Tk()
            main_window.title('Add an Assignment')
            main_window.geometry("340x600")
            main_window.eval('tk::PlaceWindow . center')
            main_window.configure(bg='light blue')

            #cal = DateEntry(main_window, width=12, year=2019, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
            #cal.pack(padx=10, pady=10)

            text_entry1 = 0
            text_entry2 = 0
            text_entry3 = 0
            date_entry1 = 0
            
            def enter_asgn():
                
                q = "SELECT * FROM class WHERE class_name = %s"
                print(text_entry1.get())
                rs.execute(q, (text_entry1.get(),))
                if rs.fetchone() == None: 
                    print("class does not exist")
                else:
                    print("class exists")
                    q = "INSERT INTO assignment (class_name, asgn_name, asgn_desc) VALUES (%s,%s,%s)"
                    rs.execute(q, (text_entry1.get(),text_entry2.get(),text_entry2.get()))
                    # commit the changes to the DB
                    con.commit()
                main_window.destroy()
            
            def go_back():
                
                main_window.destroy()
                
                
                
            
            #query = 'CREATE TABLE '
            # execute the query
            #rs.execute(query)
            frame1 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame1.grid(row=0, column=0)
            
            frame2 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame2.grid(row=1, column=0)

            frame3 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame3.grid(row=2, column=0)

            frame4 = tk.LabelFrame(main_window, bg="navy", fg="white", padx=15, pady=15)
            frame4.grid(row=3, column=0)

            row_count = 0
            row_count+=1
            label1 = tk.Label(frame1, text="Class Name", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = row_count, column = 1, sticky= 'w')
            text_entry1 = tk.Entry(frame1, width = 20, bg="white")
            text_entry1.grid(row = row_count, column=2, sticky='w')
            row_count+=1

            label1 = tk.Label(frame1, text="Assignment Name", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = row_count, column = 1, sticky= 'w')
            text_entry2 = tk.Entry(frame1, width = 20, bg="white")
            text_entry2.grid(row = row_count, column=2, sticky='w')
            
            row_count+=1

            label1 = tk.Label(frame2, text="Assignment Description", bg="dark grey", fg="white", font="none 12 bold")
            label1.grid(row = 0, column = 2, sticky= 'w')
            row_count+=1
            text_entry3 = tk.Text(frame2, bg="white", width = 41)
            text_entry3.grid(row = 1, column=2, sticky='w')
            row_count+=1
            output = tk.Button(frame4, text = "Enter", width = 6, command = enter_asgn)
            output.grid(row = 1, column = 0)

            output = tk.Button(frame4, text = "Return", width = 6, command = go_back)
            output.grid(row = 1, column = 1)

            row_count+=1
            calendar = DateEntry(frame3, width=12, year=2019, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
            calendar.grid(row = 1, column = 0)
            #cal.pack(padx=10, pady=10)
            

            main_window.mainloop()
        
        # start of main UI
        home_window=tk.Tk()
        home_window.title('Homework Planner')
        home_window.geometry("340x600")
        home_window.eval('tk::PlaceWindow . center')
        home_window.configure(bg='light blue')

        hframe1 = tk.LabelFrame(home_window, bg="navy", fg="white", padx=15, pady=13)
        hframe1.grid(row=0, column=0)

        hbtn1 = tk.Button(hframe1, text = "Add a Class", width = 30, command = create_class_window, pady = 10)
        hbtn1.grid(row = 1, column = 0, pady = 15)

        hbtn2 = tk.Button(hframe1, text = "Add an Assignment", width = 30, command = create_asgn_window, pady = 10)
        hbtn2.grid(row = 2, column = 0, pady = 15)

        hbtn3 = tk.Button(hframe1, text = "Remove a Class", width = 30, command = delete_class_window, pady = 10)
        hbtn3.grid(row = 3, column = 0, pady = 15)

        hbtn2 = tk.Button(hframe1, text = "Remove an Assignment", width = 30, command = delete_asgn_window, pady = 10)
        hbtn2.grid(row = 4, column = 0, pady = 15)

        hbtn2 = tk.Button(hframe1, text = "Display Classes", width = 30, command = show_classes_window, pady = 10)
        hbtn2.grid(row = 5, column = 0, pady = 15)

        hbtn2 = tk.Button(hframe1, text = "Display Assignments", width = 30, command = show_asgn_window, pady = 10)
        hbtn2.grid(row = 6, column = 0, pady = 15)

        hbtn2 = tk.Button(hframe1, text = "Exit", width = 30, command = home_window.destroy, pady = 10)
        hbtn2.grid(row = 7, column = 0, pady = 15)

        home_window.mainloop()

    except msql.Error as err:
        print(err)

    finally:
        rs.close()
        con.close()

if __name__ == '__main__':
    main()