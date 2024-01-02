from tkinter import*

from PIL import Image,ImageTk #installed pillow module 
from tkinter import ttk, messagebox
import mysql.connector
import traceback

class supplierclass:
    def __init__(ab,ba):
        ab.root=ba
        ab.root.geometry("1310x530+200+210")
        ab.root.title("Inventory management system")
        ab.root.config(bg="white")
        ab.root.focus_force()

        #variable defined

        ab.var_supplier=StringVar()
        ab.var_contact=StringVar()
        ab.var_name=StringVar()


        #title
        title=Label(ab.root,text="Supplier Details",font=("Montserrat",15),bg="darkblue",fg="white")
        title.place(x=50,y=20,width=1200) 

        #content
        label_supplier=Label(ab.root,text="Invoice",font=("Montserrat",15),bg="white").place(x=50,y=70)

        #row1
        txt_supplier=Entry(ab.root,text="Invoice",textvariable=ab.var_supplier,font=("Montserrat",15),bg="lightyellow").place(x=200,y=70,width=180)
        #row2
        label_name=Label(ab.root,text="Name",font=("Montserrat",15),bg="white").place(x=50,y=110)
        txt_name=Entry(ab.root,text="Name",textvariable=ab.var_name,font=("Montserrat",15),bg="lightyellow").place(x=200,y=110,width=180)
        #row3
        label_contact=Label(ab.root,text="Contact",font=("Montserrat",15),bg="white").place(x=50,y=150)
        txt_contact=Entry(ab.root,textvariable=ab.var_contact,font=("Montserrat",15),bg="lightyellow").place(x=200,y=150,width=180)

        #row4
        label_disc=Label(ab.root,text="Address",font=("Montserrat",15),bg="white").place(x=50,y=190)
        ab.txt_disc=Text(ab.root,font=("Montserrat",15),bg="lightyellow")
        ab.txt_disc.place(x=200,y=190,width=300,height=60)

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

        ab.supplier_table=ttk.Treeview(employee_frame,columns=("invoice","supplier_name","contact","disc"),yscrollcommand=scroll1.set,xscrollcommand=scroll.set)
        scroll.pack(side=BOTTOM,fill=X)
        scroll1.pack(side=LEFT,fill=Y)
        scroll.config(command=ab.supplier_table.xview)
        scroll1.config(command=ab.supplier_table.yview)

        ab.supplier_table.pack(fill=BOTH,expand=1)
        ab.supplier_table.heading("invoice",text="Supplier ID")
        ab.supplier_table.heading("supplier_name",text="Name")
        ab.supplier_table.heading("contact",text="Contact No.")
        ab.supplier_table.heading("disc",text="Discription")
        ab.supplier_table["show"]="headings"
        ab.supplier_table.bind("<ButtonRelease-1>",ab.get_data)

        ab.show()


#database
    def add(ab):
        conn = mysql.connector.connect(host='localhost', database='ims', user='root', password='Adityabetter1')
        cursor = conn.cursor()
        try:
            if ab.var_supplier.get() == "":
                messagebox.showerror("Error", "Supplier ID is required", parent=ab.root)
            else:
                cursor.execute("SELECT * FROM supplier WHERE invoice = %s", (ab.var_supplier.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already exists, try using a different ID", parent=ab.root)
                else:
                    cursor.execute(
                        "INSERT INTO table1 (eid, name_, email, gender, contact, birth, join_, pass, utype, address, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            ab.var_supplier.get(), ab.var_name.get(), ab.var_email.get(), ab.var_gender.get(),
                            ab.var_contact.get(), ab.var_birth.get(), ab.var_join.get(), ab.var_pass.get(),
                            ab.var_utype.get(), ab.txt_disc.get("1.0", END), ab.var_salary.get()
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
            ab.supplier_table.delete(*ab.supplier_table.get_children())
            for row in rows:
                ab.supplier_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            print(traceback.format_exc())
            
        
        finally:
            cursor.close()
            conn.close()

            
    def get_data(ab, ev):
        a=ab.supplier_table.focus()
        content=(ab.supplier_table.item(a))
        row=content['values']
        ab.var_supplier.set(row[0])
        ab.var_name.set(row[1])
        ab.var_email.set(row[2])
        ab.var_gender.set(row[3]) 
        ab.var_contact.set(row[4])
        ab.var_birth.set(row[5]) 
        ab.var_join.set(row[6])
        ab.var_pass.set(row[7])
        ab.var_utype.set(row[8]) 
        ab.txt_disc.delete("1.0", END)
        ab.txt_disc.insert(END,row[9])
        ab.var_salary.set(row[10]) 


    def update(ab):
        conn = mysql.connector.connect(host='localhost', database='ims', user='root', password='Adityabetter1')
        cursor = conn.cursor()
        try:
            if ab.var_supplier.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=ab.root)
            else:
                cursor.execute(
                    "SELECT * FROM table1 WHERE eid=%s",
                    (ab.var_supplier.get(),)
                )
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Employee ID is invalid", parent=ab.root)
                else:
                    cursor.fetchall() #clears all the previous data
                    cursor.execute(
                        "UPDATE table1 SET name_=%s, email=%s, gender=%s, contact=%s, birth=%s, join_=%s, pass=%s, utype=%s, address=%s, salary=%s WHERE eid=%s",
                        (
                            ab.var_name.get(), ab.var_email.get(), ab.var_gender.get(), ab.var_contact.get(),
                            ab.var_birth.get(), ab.var_join.get(), ab.var_pass.get(), ab.var_utype.get(),
                            ab.txt_disc.get("1.0", END), ab.var_salary.get(), ab.var_supplier.get()
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
            if ab.var_supplier.get() == "":
                messagebox.showerror("Error", "Employee ID is required", parent=ab.root)
            else:
                cursor.execute(
                    "SELECT * FROM table1 WHERE eid=%s",
                    (ab.var_supplier.get(),)
                )
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This Employee ID is invalid", parent=ab.root)
                else:
                    sure=messagebox.askyesno("Confirm","Are you sure you want to delete this employee?",parent=ab.root)
                    if sure==True:
                        cursor.fetchall()
                        cursor.execute("delete from table1 where eid=%s",(ab.var_supplier.get(),))

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
        ab.var_supplier.set("")
        ab.var_name.set("")
        ab.var_email.set("")
        ab.var_gender.set("Select") 
        ab.var_contact.set("")
        ab.var_birth.set("") 
        ab.var_join.set("")
        ab.var_pass.set("")
        ab.var_utype.set("Select") 
        ab.txt_disc.delete("1.0", END)
        ab.txt_disc.insert(END,"")
        ab.var_salary.set("")     
        ab.show()  
             
if __name__=="__main__":
    ba=Tk()
    obj= supplierclass(ba)
    ba.mainloop()
