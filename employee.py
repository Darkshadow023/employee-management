from tkinter import*

from PIL import Image,ImageTk #installed pillow module 
from tkinter import ttk, messagebox
import mysql.connector
import traceback

class employeeclass:
    def __init__(ab,ba):
        ab.root=ba
        ab.root.geometry("1310x530+200+210")
        ab.root.title("Inventory management system")
        ab.root.config(bg="white")
        ab.root.focus_force()

        #variable defined

        ab.var_employee=StringVar()
        ab.var_gender=StringVar()
        ab.var_contact=StringVar()
        ab.var_name=StringVar()
        ab.var_birth=StringVar()
        ab.var_join=StringVar()
        ab.var_email=StringVar()
        ab.var_pass=StringVar()
        ab.var_utype=StringVar()
        ab.var_salary=StringVar()
        #search bar


        #title
        title=Label(ab.root,text="Employee Details",font=("Montserrat",15),bg="darkblue",fg="white")
        title.place(x=50,y=20,width=1200) 

        #content
        label_employee=Label(ab.root,text="Employee ID",font=("Montserrat",15),bg="white").place(x=50,y=70)
        label_gender=Label(ab.root,text="Gender",font=("Montserrat",15),bg="white").place(x=400,y=70)
        label_contact=Label(ab.root,text="Contact",font=("Montserrat",15),bg="white").place(x=750,y=70)

        #row1
        txt_employee=Entry(ab.root,text="Employee ID",textvariable=ab.var_employee,font=("Montserrat",15),bg="lightyellow").place(x=200,y=70,width=180)
        text_contact=Entry(ab.root,text="Contact",textvariable=ab.var_contact,font=("Montserrat",15),bg="lightyellow").place(x=900,y=70,width=180)
        search_g=ttk.Combobox(ab.root,textvariable=ab.var_gender,values=("Select","Male","Female","Others"),state="readonly",justify=CENTER,font=("Montserrat",15))
        search_g.place(x=550,y=70,width=180)
        search_g.current(0)

        #row2
        label_name=Label(ab.root,text="Name",font=("Montserrat",15),bg="white").place(x=50,y=110)
        label_birth=Label(ab.root,text="Date of Birth",font=("Montserrat",15),bg="white").place(x=400,y=110)
        label_join=Label(ab.root,text="Joining Date",font=("Montserrat",15),bg="white").place(x=750,y=110)
        txt_name=Entry(ab.root,text="Name",textvariable=ab.var_name,font=("Montserrat",15),bg="lightyellow").place(x=200,y=110,width=180)
        txt_birth=Entry(ab.root,text="Date of Birth",textvariable=ab.var_birth,font=("Montserrat",15),bg="lightyellow").place(x=550,y=110,width=180)
        text_joining=Entry(ab.root,text="Joining Date",textvariable=ab.var_join,font=("Montserrat",15),bg="lightyellow").place(x=900,y=110,width=180) 

        #row3
        label_email=Label(ab.root,text="Email",font=("Montserrat",15),bg="white").place(x=50,y=150)
        label_password=Label(ab.root,text="Password",font=("Montserrat",15),bg="white").place(x=400,y=150)
        label_utype=Label(ab.root,text="User Type",font=("Montserrat",15),bg="white").place(x=750,y=150)
        txt_email=Entry(ab.root,textvariable=ab.var_email,font=("Montserrat",15),bg="lightyellow").place(x=200,y=150,width=180)
        txt_password=Entry(ab.root,textvariable=ab.var_pass,font=("Montserrat",15),bg="lightyellow").place(x=550,y=150,width=180)
        search_u=ttk.Combobox(ab.root,textvariable=ab.var_utype,values=("Select","Admin","Employee"),state="readonly",justify=CENTER,font=("Montserrat",15))
        search_u.place(x=900,y=150,width=180)
        search_u.current(0)

        #row4
        label_address=Label(ab.root,text="Address",font=("Montserrat",15),bg="white").place(x=50,y=190)
        label_salary=Label(ab.root,text="Salary",font=("Montserrat",15),bg="white").place(x=550,y=190)
        ab.txt_address=Text(ab.root,font=("Montserrat",15),bg="lightyellow")
        ab.txt_address.place(x=200,y=190,width=300,height=60)
        txt_salary=Entry(ab.root,textvariable=ab.var_salary,font=("Montserrat",15),bg="lightyellow").place(x=650,y=190,width=180)

        #buttons
        save_btn=Button(ab.root,text="Save",command=ab.add,font=("Old goudy style",15),bg="darkgreen",fg="white",cursor="hand2")
        save_btn.place(x=550,y=240,width=110,height=28) 
        up_btn=Button(ab.root,text="Update",command=ab.update,font=("Old goudy style",15),bg="darkgreen",fg="white",cursor="hand2")
        up_btn.place(x=680,y=240,width=110,height=28)
        delete_btn=Button(ab.root,text="Delete",command=ab.delete,font=("Old goudy style",15),bg="darkgreen",fg="white",cursor="hand2")
        delete_btn.place(x=810,y=240,width=110,height=28)     
        clear_btn=Button(ab.root,text="Clear",command=ab.clear,font=("Old goudy style",15),bg="darkgreen",fg="white",cursor="hand2")
        clear_btn.place(x=940,y=240,width=110,height=28)      

        #details
        employee_frame=Frame(ab.root,bd=3,relief=RIDGE)     
        employee_frame.place(x=0,y=300,relwidth=1,height=200) 
        scroll=Scrollbar(employee_frame,orient=HORIZONTAL)     
        scroll1=Scrollbar(employee_frame,orient=VERTICAL)

        ab.Employee_table=ttk.Treeview(employee_frame,columns=("Eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scroll1.set,xscrollcommand=scroll.set)
        scroll.pack(side=BOTTOM,fill=X)
        scroll1.pack(side=LEFT,fill=Y)
        scroll.config(command=ab.Employee_table.xview)
        scroll1.config(command=ab.Employee_table.yview)

        ab.Employee_table.pack(fill=BOTH,expand=1)
        ab.Employee_table.heading("Eid",text="Employee ID")
        ab.Employee_table.heading("name",text="Name")
        ab.Employee_table.heading("email",text="Email")
        ab.Employee_table.heading("gender",text="Gender")
        ab.Employee_table.heading("contact",text="Contact No.")
        ab.Employee_table.heading("dob",text="Birth Date")
        ab.Employee_table.heading("doj",text="Joining Date")
        ab.Employee_table.heading("pass",text="Password")
        ab.Employee_table.heading("utype",text="User Type")
        ab.Employee_table.heading("address",text="Address")
        ab.Employee_table.heading("salary",text="Salary")
        ab.Employee_table["show"]="headings"
        ab.Employee_table.bind("<ButtonRelease-1>",ab.get_data)

        ab.show()


#database
    def add(ab):
        conn = mysql.connector.connect(host='localhost', database='ims', user='root', password='Adityabetter1')
        cursor = conn.cursor()
        try:
            if ab.var_employee.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=ab.root)
            else:
                cursor.execute("SELECT * FROM table1 WHERE eid = %s", (ab.var_employee.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already exists, try using a different ID", parent=ab.root)
                else:
                    cursor.execute(
                        "INSERT INTO table1 (eid, name_, email, gender, contact, birth, join_, pass, utype, address, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            ab.var_employee.get(), ab.var_name.get(), ab.var_email.get(), ab.var_gender.get(),
                            ab.var_contact.get(), ab.var_birth.get(), ab.var_join.get(), ab.var_pass.get(),
                            ab.var_utype.get(), ab.txt_address.get("1.0", END), ab.var_salary.get()
                        )
                    )

                    conn.commit()
                    messagebox.showinfo("Success", "Employee added successfully", parent=ab.root)
                    ab.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
            print(traceback.format_exc())

        finally:
            cursor.close()
            conn.close()

    def show(ab):
        conn= mysql.connector.connect(host='localhost',database='ims',user='root',password='Adityabetter1')
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT * FROM table1")
            rows=cursor.fetchall()
            ab.Employee_table.delete(*ab.Employee_table.get_children())
            for row in rows:
                ab.Employee_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            print(traceback.format_exc())
            
        
        finally:
            cursor.close()
            conn.close()

            
    def get_data(ab, ev):
        a=ab.Employee_table.focus()
        content=(ab.Employee_table.item(a))
        row=content['values']
        ab.var_employee.set(row[0])
        ab.var_name.set(row[1])
        ab.var_email.set(row[2])
        ab.var_gender.set(row[3]) 
        ab.var_contact.set(row[4])
        ab.var_birth.set(row[5]) 
        ab.var_join.set(row[6])
        ab.var_pass.set(row[7])
        ab.var_utype.set(row[8]) 
        ab.txt_address.delete("1.0", END)
        ab.txt_address.insert(END,row[9])
        ab.var_salary.set(row[10]) 


    def update(ab):
        conn = mysql.connector.connect(host='localhost', database='ims', user='root', password='Adityabetter1')
        cursor = conn.cursor()
        try:
            if ab.var_employee.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=ab.root)
            else:
                cursor.execute(
                    "SELECT * FROM table1 WHERE eid=%s",
                    (ab.var_employee.get(),)
                )
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Employee ID is invalid", parent=ab.root)
                else:
                    cursor.fetchall()#clears all the previous data
                    cursor.execute(
                        "UPDATE table1 SET name_=%s, email=%s, gender=%s, contact=%s, birth=%s, join_=%s, pass=%s, utype=%s, address=%s, salary=%s WHERE eid=%s",
                        (
                            ab.var_name.get(), ab.var_email.get(), ab.var_gender.get(), ab.var_contact.get(),
                            ab.var_birth.get(), ab.var_join.get(), ab.var_pass.get(), ab.var_utype.get(),
                            ab.txt_address.get("1.0", END), ab.var_salary.get(), ab.var_employee.get()
                        )
                    )

                    conn.commit()
                    messagebox.showinfo("Success", "Employee updated successfully", parent=ab.root)
                    ab.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
            print(traceback.format_exc())

        finally:
            cursor.close()
            conn.close()

    def delete(ab):
        conn = mysql.connector.connect(host='localhost', database='ims', user='root', password='Adityabetter1')
        cursor = conn.cursor()   
        try:
            if ab.var_employee.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=ab.root)
            else:
                cursor.execute(
                    "SELECT * FROM table1 WHERE eid=%s",
                    (ab.var_employee.get(),)
                )
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Employee ID is invalid", parent=ab.root)
                else:
                    sure=messagebox.askyesno("Confirm","Are you sure you want to delete this employee?",parent=ab.root)
                    if sure==True:
                        cursor.fetchall()
                        cursor.execute("delete from table1 where eid=%s",(ab.var_employee.get(),))

                        conn.commit()
                        messagebox.showinfo("Delete","Employee Deleted Successfully",parent=ab.root)
                        ab.clear()
                    else:
                        messagebox.showinfo("Mind Changed?","Looks like someone was about to get fired :)", parent=ab.root)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            cursor.close()
            conn.close()


    def clear(ab):
        ab.var_employee.set("")
        ab.var_name.set("")
        ab.var_email.set("")
        ab.var_gender.set("Select") 
        ab.var_contact.set("")
        ab.var_birth.set("") 
        ab.var_join.set("")
        ab.var_pass.set("")
        ab.var_utype.set("Select") 
        ab.txt_address.delete("1.0", END)
        ab.txt_address.insert(END,"")
        ab.var_salary.set("")     
        ab.show()  
             
if __name__=="__main__":
    ba=Tk()
    obj= employeeclass(ba)
    ba.mainloop()
