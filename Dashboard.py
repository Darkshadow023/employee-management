from tkinter import* 
from tkinter import messagebox
from PIL import Image,ImageTk #installed pillow module 
from employee import employeeclass
from supplier import supplierclass
import mysql.connector
import traceback
import time

class Dash:
    def __init__(ab,ba):
        ab.root=ba
        ab.root.geometry("1920x1080+0+0")
        ab.root.title("Employee management system")
        ab.root.config(bg="#909090")
        #title
        ab.icon_title=PhotoImage(file="imgs\logo-removebg-preview (2).png")
        title=Label(ab.root,text="Nexus AI",image=ab.icon_title,compound=LEFT,font=("Montserrat",40,"bold"),bg="#0c0c0f",fg="#fff",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=150)
        
        #button
        Btn_Logout=Button(ab.root,text="Logout",font=("Montserrat",15,"bold"),bg="light blue",bd=3,cursor="hand2").place(x=1350,y=50,height=50,width=150)
        
        #timestamp
        ab.clock=Label(ab.root,text="Welcome Darkshadow\t\t  Date: DD-MM-YYYY\t\t  HH:MM:SS",font=("Montserrat",15,),bg="light gray",fg="#000")
        ab.clock.place(x=0,y=150,relwidth=1,height=30)
        
        #menu
        ab.Menulogo=Image.open("imgs\logo.png")
        ab.Menulogo=ab.Menulogo.resize((200,200),Image.LANCZOS)
        ab.Menulogo=ImageTk.PhotoImage(ab.Menulogo)
        LeftMenu=Frame(ab.root,bd=2,relief=RIDGE,bg="black")
        LeftMenu.place(x=0,y=182,width=200,height=523)
        lblmenulogo=Label(LeftMenu,image=ab.Menulogo)
        lblmenulogo.pack(side=TOP,fill=X)
        Label_menu1=Label(LeftMenu,text="MENU",font=("Montserrat",15,"bold"),bg="dark green",fg="white").pack(side=TOP,fill=X)
        btn_menu1=Button(LeftMenu,text="Employees",command=ab.employee,font=("Montserrat",15,"bold"),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)
        btn_menu2=Button(LeftMenu,text="Suppliers",font=("Montserrat",15,"bold"),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)
        btn_menu3=Button(LeftMenu,text="Categories",font=("Montserrat",15,"bold"),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)
        btn_menu4=Button(LeftMenu,text="Products",font=("Montserrat",15,"bold"),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)
        btn_menu5=Button(LeftMenu,text="Sales",font=("Montserrat",15,"bold"),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)
        btn_menu6=Button(LeftMenu,text="Exit",font=("Montserrat",15,"bold"),bg="light blue",cursor="hand2").pack(side=TOP,fill=X)

        #content
        ab.Label_employee=Label(ab.root,text=" \n Total Employees\n [ 0 ]\n",bg="#00917C",fg="white",relief=RIDGE,font=("Montserrat",20,"bold"))
        ab.Label_employee.place(x=300,y=300,width=300)
        ab.Label_Suppliers=Label(ab.root,text=" \n Total Suppliers\n [ 0 ]\n",bg="#710C04",fg="white",relief=RIDGE,font=("Montserrat",20,"bold"))
        ab.Label_Suppliers.place(x=700,y=300,width=300)        
        ab.Label_Products=Label(ab.root,text=" \n Total Products\n [ 0 ]\n",bg="#CC7722",fg="white",relief=RIDGE,font=("Montserrat",20,"bold"))
        ab.Label_Products.place(x=1100,y=300,width=300)        
        ab.Label_Category=Label(ab.root,text=" \n Total Categories\n [ 0 ]\n",bg="#1450A3",fg="white",relief=RIDGE,font=("Montserrat",20,"bold"))
        ab.Label_Category.place(x=500,y=500,width=300)        
        ab.Label_sales=Label(ab.root,text=" \n Total Sales\n [ 0 ]\n",bg="#C70039",fg="white",relief=RIDGE,font=("Montserrat",20,"bold"))
        ab.Label_sales.place(x=900,y=500,width=300)
        #footer
        Lbl_footer=Label(ab.root,text="Inventory Management System | Developed by Aditya Kapoor & Aryan Sinha\n For any technical assistance contact +919310795008 | +919582372955",font=("Montserrat",12),bg="light gray",fg="#000")
        Lbl_footer.pack(side=BOTTOM,fill=X)  
        ab.update_content_employee()


    def employee(ab):
        ab.new_win=Toplevel(ab.root)
        ab.new_obj=employeeclass(ab.new_win)
    def supplier(ab):
        ab.new_win=Toplevel(ab.root)
        ab.new_obj=supplierclass(ab.new_win)
    
    def update_content_employee(ab):
        conn = mysql.connector.connect(host='localhost', database='ims', user='root', password='Adityabetter1')
        cursor = conn.cursor()
        try:
            cursor.execute ("select * from table1")
            employee_fetch= cursor.fetchall()
            ab.Label_employee.config(text=f' \n Total Employees\n  [ {str(len(employee_fetch))} ] \n')



            timenow=time.strftime("%H:%M:%S")
            datenow=time.strftime("%d-%m-%Y")
            ab.clock.config(text=f"Welcome Darkshadow\t\t  Date: {datenow}\t\t\t {timenow}")
            ab.clock.after(200,ab.update_content_employee)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            print(traceback.format_exc())






if __name__=="__main__":
    ba=Tk()
    obj= Dash(ba)
    ba.mainloop()
