from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import csv
from tkinter import filedialog
mydata=[]#global variable

class Attendence:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1600x1000+0+0")
        self.root.title("Face Recognition Attendance System")


        #"""""""""""""""""""""""Data fill in  entry fill in left side/text variable"""""
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_atten_date=StringVar()

        #""""""""""""""""""""""""""""""""image 1"""""""""""""""""""""""""""""""""""
        img=Image.open(r"Images\emptyclassroom.jpg")
        img=img.resize((700,200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=700,height=200)        


        #""""""""""""""""""""""""""""""""""image 2"""""""""""""""""""""""""""
        img1=Image.open(r"Images\nonemptyclassroom.jpg")
        img1=img1.resize((700,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=700,y=0,width=700,height=200)

        img3=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\background.png")
        img3=img3.resize((1500,600),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=185,width=1500,height=600)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")#bd-border
        main_frame.place(x=10,y=50,width=1400,height=600)

        #"""""""""""""""""""""""""""""""""""""""""""""""""""left label frame"""""""""""""
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=1,width=530,height=400)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")#bd-border
        left_inside_frame.place(x=5,y=0,width=510,height=370)

        # """""""""""""""'Labels and Entries"""
        #"""""""""""""""""""""""""" Attendence, ID Label and Combobox"""""""""""""""""""""""""
        attendence_id_Label = Label( left_inside_frame, text="Attendance ID:", font=("times new roman", 8, "bold"), bg="white")
        attendence_id_Label.grid(row=0, column=0, padx=0)

        attendenceid_entry = ttk.Entry( left_inside_frame, width=20,textvariable=self.var_atten_id, font=("times new roman", 8, "bold"))
        attendenceid_entry.grid(row=0, column=1, padx=0, pady=10)

        #Roll No
        rollLabel = Label( left_inside_frame, text="Roll No:", font=("times new roman", 8, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=0)

        rollentry = ttk.Entry( left_inside_frame, width=20,textvariable=self.var_atten_roll, font=("times new roman", 8, "bold"))
        rollentry.grid(row=0, column=3, padx=0, pady=10)

        #Name
        dateLabel = Label( left_inside_frame, text="Name", font=("times new roman", 8, "bold"), bg="white")
        dateLabel.grid(row=1, column=0, padx=0)

        dateentry = ttk.Entry( left_inside_frame, width=20,textvariable=self.var_atten_name,font=("times new roman", 8, "bold"))
        dateentry.grid(row=1, column=1, padx=0, pady=10)

        #Department
        departmentLabel = Label( left_inside_frame, text="Department", font=("times new roman", 8, "bold"), bg="white")
        departmentLabel.grid(row=1, column=2, padx=20)

        departmententry = ttk.Entry( left_inside_frame, width=20,textvariable=self.var_atten_dep, font=("times new roman", 8, "bold"))
        departmententry.grid(row=1, column=3, padx=0, pady=10)

        #Time
        timeLabel = Label( left_inside_frame, text="Time", font=("times new roman", 8, "bold"), bg="white")
        timeLabel.grid(row=2, column=0, padx=0)

        timeentry = ttk.Entry( left_inside_frame, width=20, textvariable=self.var_atten_time,font=("times new roman", 8, "bold"))
        timeentry.grid(row=2, column=1, padx=0, pady=10)

        #Attendence
        attendenceLabel = Label( left_inside_frame, text="Attendance", font=("times new roman", 8, "bold"), bg="white")
        attendenceLabel.grid(row=2, column=2, padx=5)

        self.attendencecombo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman", 8, "bold"), state="readonly",width=18)
        self.attendencecombo["values"] = ("Status", "Present", "Absent")
        self.attendencecombo.current(0)  # When we see on combo box always shows Select Department
        self.attendencecombo.grid(row=2, column=3, padx=2, pady=5)

        #Date
        #Date
        dateLabel = Label(left_inside_frame, text="Date", font=("times new roman", 8, "bold"), bg="white")
        dateLabel.grid(row=3, column=0, padx=5)

        dateentry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 8, "bold"))
        dateentry.grid(row=3, column=1, padx=2, pady=10)


     #"""""""""""""""""""""""""""""""""""""""Search System"""""""""""""""""""""""""""""""""
        search_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=170,width=500,height=55)

        #"""""""""""""""""""""""""""""""""""""""""Seach Label and Combobox"""""""""""""""""""""""""""""""""""
        search_Label = Label(search_frame, text="Search by:", font=("times new roman", 10, "bold"), bg="yellow", fg="black")
        search_Label.grid(row=0, column=0, padx=5, sticky=W)

        #"""""""""""""""""""""""""""""""""""""Combo box"""""""""""""""""""""""""""""""""""""""""""""
        self.search_combo= ttk.Combobox(search_frame,font=("times new roman", 8, "bold"), state="readonly")
        self.search_combo["values"] = ("Select", "Attendance ID", "Roll No", "Name", "Department", "Time", "Date", "Attendance Status")
        self.search_combo.current(0)  # When we see on combo box always shows Select Department
        self.search_combo.grid(row=0, column=1, padx=4)

        self.search_entry = ttk.Entry(search_frame,width=16,font=("times new roman", 8, "bold"))
        self.search_entry.grid(row=0, column=2, padx=2, pady=0)  # grid have rows and columns

        Search_btn = Button(search_frame, text="Search",width=14, font=("times new roman", 10, "bold"), bg="green", fg="white",command=self.search_data)
        Search_btn.grid(row=0, column=3, padx=5)

        

        #""""""""""""""""""""""""""""""""""""""""buttons_frame"""""""""""""""""""""""""
        button_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=340,width=507,height=30)

        #"""""""""""""""""""""""""""""""""""""""""save data at Db""""""""""""""""""""""""""" 
        import_btn=Button(button_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",10,"bold"),bg="green",fg="white")
        import_btn.grid(row=0,column=0,padx=0,pady=0)

        export_btn=Button(button_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",10,"bold"),bg="green",fg="white")
        export_btn.grid(row=0,column=1,padx=0)

        update_btn=Button(button_frame,text="Update",width=17,font=("times new roman",10,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=2,padx=0)

        reset_btn=Button(button_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3,padx=0)




         #"""""""""""""""""""""""""""""""""""right label frame"""""""""""""""""""""""""""""""""
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=550,y=1,width=690,height=430)

           #""""""""""""""""""""""""""""""""""""""""table_frame"""""""""""""""""""""""""
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=6,y=1,width=670,height=380)

        #"""""""""""""""""""""""""""""""""""""""Scroll bar table"
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("attendence",text="Attendance Status")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable['show']="headings"

        self.AttendanceReportTable.column("id",width=100,anchor='center')
        self.AttendanceReportTable.column("roll",width=100,anchor='center')
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100,anchor='center')
        self.AttendanceReportTable.column("time",width=100,anchor='center')
        self.AttendanceReportTable.column("attendence",width=125,anchor='center')
        self.AttendanceReportTable.column("date",width=100,anchor='center')
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #"""""""""""""""""""""""""""""""""""Fetch data"""""""
    def fetch_data(self,rows): #dlete all existing data of students and import csv data 
         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
         for i in rows:
              self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv

    def importCsv(self):#excel file data show in table
         global mydata#taken mydata which is globally defined by us
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root) #open file
         with open(fln) as myfile:
              csvread=csv.reader(myfile,delimiter=",") #delimeter used for csv
              for i in csvread:
                   mydata.append(i)
              self.fetch_data(mydata)

     #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root) #open file
            with open(fln,mode="w",newline="") as myfile:#data insert in new line
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                   exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Name "+os.path.basename(fln)+" Exported Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])
         self.var_atten_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_date.set(rows[5])
         self.var_atten_attendance.set(rows[6])

         #reset button's function
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        #We don't need to add data in mysql Db because mmostly we prefer excel to view attendence

     
    # Function to perform the search
    def search_data(self):
        search_by = self.search_combo.get()
        search_value = self.search_entry.get().strip()

        if search_by == "Select" or not search_value:
            messagebox.showerror("Error", "Please select a valid search criteria and enter a search term.", parent=self.root)
            return

        search_column_map = {
            "Attendance ID": 0,
            "Roll No": 1,
            "Name": 2,
            "Department": 3,
            "Time": 4,
            "Date": 5,
            "Attendance Status": 6
        }
        
        search_column_index = search_column_map.get(search_by)
        search_results = [row for row in mydata if row[search_column_index] == search_value]

        if not search_results:
            messagebox.showinfo("No Result", "No matching records found.", parent=self.root)
        else:
            self.fetch_data(search_results)
       




if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()