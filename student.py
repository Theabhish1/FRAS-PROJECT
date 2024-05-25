from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
from tkinter import simpledialog
from tkinter import filedialog
import tkinter as tk
from tkcalendar import Calendar


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x1000+0+0")
        self.root.title("Face Recognition Attendence System")
    

        #"""""""""""""""""""""""""""Variables""""""""""""""""""""""""""
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_roll=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_phone=StringVar()
        self.var_gender=StringVar()
        self.var_session=StringVar()
        self.var_mail=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_parent=StringVar()
        self.var_update=StringVar()
        self.var_searchentry=StringVar()
        self.var_searchcombo=StringVar()

        # Frame for Treeview
        frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        frame.place(x=20, y=100, width=1300, height=560)

        # Treeview Scrollbars
        scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame, orient=VERTICAL)

        # Treeview Widget
        self.student_table = ttk.Treeview(frame, columns=("Course", "Department", "Semester", "Student_id", "Roll_No", "Name", "Session", "Gender", "Dob", "Phone", "email", "Parents_no"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Student_id", text="Student ID")
        self.student_table.heading("Roll_No", text="Roll No")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Session", text="Session")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Dob", text="Date of Birth")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("Parents_no", text="Parents No")
        self.student_table['show'] = 'headings'

        self.student_table.pack(fill=BOTH, expand=1)
        

        





        #""""""""""""""""""""""""""""""""image 1"""""""""""""""""""""""""""""""""""
        img=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\college.jpg")
        img=img.resize((500,160),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=160)        


        #""""""""""""""""""""""""""""""""""image 2"""""""""""""""""""""""""""
        img1=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\images.jpg")
        img1=img1.resize((500,160),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=160)


        #""""""""""""""""""""""""""""""""""""""image 3"""""""""""""""""""""""""""""""""""""
        img2=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\full.jpg")
        img2=img2.resize((500,160),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=160)


        #""""""""""""""""""""""""""""""""""""""""""""""""bg image"""""""""""""""""""""""
        img3=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\background.png")
        img3=img3.resize((1420,960),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1420,height=960)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")#bd-border
        main_frame.place(x=20,y=55,width=1400,height=600)

        #"""""""""""""""""""""""""""""""""""""""""""""""""""left label frame"""""""""""""
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=1,width=530,height=400)



        #""""""""""""""""""""""""""""""""""""""""current course"""""""""""""""""""
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="light skyblue",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=0,width=510,height=90)

        #"""""""""""""""""""""""""""""""""""""course label"""""""""""""""""
        course_Label = Label(current_course_frame, text="Course:", font=("times new roman", 8, "bold"), bg="white")
        course_Label.grid(row=0, column=0, padx=5)

        #"""""""""""""""""""""""""""""""course combo"""""""""""""""""
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",8,"bold"),state="readonly")
        course_combo["values"]=("Select Course", "B.Tech.","Polytechnic","BBA","BCA","BE")
        course_combo.current(0) #When we see on combo box always shows Select Department
        course_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)



        #"""""""""""""""""""""""""""""""""""""session label"""""""""""""""""
        course_Label = Label(current_course_frame, text="Session:", font=("times new roman", 8, "bold"), bg="white")
        course_Label.grid(row=0, column=2, padx=20)

        #"""""""""""""""""""""""""""""""session combo"""""""""""""""""          have to apply text variable
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_session,font=("times new roman",8,"bold"),state="readonly")
        course_combo["values"]=("Select Session", "2021-22","2022-23","2023-24","2024-25","2025-26")
        course_combo.current(0) #When we see on combo box always shows Select Department
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)


         #""""""""""""""""""""""""""""""""""""Department label"""""""""""""""""

        # Department Label
        dept_Label = Label(current_course_frame, text="Department:", font=("times new roman", 8, "bold"), bg="white")
        dept_Label.grid(row=1, column=0, padx=5)

        # Department Combo Box
        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dept, font=("times new roman", 8, "bold"), state="readonly")
        dept_combo["values"] = ("Select Department", "CSE", "ME", "CE", "EE", "EEE", "BBA", "BCA")
        dept_combo.current(0)  # When we see on combo box always shows Select Department
        dept_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)

         # Semester Label
        Semester_Label = Label(current_course_frame, text="Semester:", font=("times new roman", 8, "bold"), bg="white")
        Semester_Label.grid(row=1, column=2, padx=5)

         # Semester Combo Box
        Semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 8, "bold"), state="readonly")
        Semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        Semester_combo.current(0)  # When we see on combo box always shows Select Department
        Semester_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)  # Adjusted row parameter

        

        #"""""""""""""""""""""""""""""""Class Student info. Frame""""""""""""""""""""""""""""""""""""""""
        
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="light grey",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=100,width=510,height=270)

        #"""""""""""""""""""""""""" Student ID Label and Combobox"""""""""""""""""""""""""
        self.student_id_Label = Label(class_student_frame, text="Student ID:", font=("times new roman", 8, "bold"), bg="white")
        self.student_id_Label.grid(row=0, column=0, padx=0)  # Adding padding to the right

        self.studentid_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, width=20, font=("times new roman", 8, "bold"))
        self.studentid_entry.grid(row=0, column=1, padx=0, pady=10)  # Adjusting sticky parameter to "W" for left alignment

        self.var_id.trace("w", lambda *args: self.validate_id())  # Call validate_id function whenever the var_id changes



        #""""""""""""""""""""""Student Phone No."""""""""""""""""""""""""""
        self.var_phone = StringVar()
        self.phone_no_Label = Label(class_student_frame, text="Phone No:", font=("times new roman", 8, "bold"), bg="white")
        self.phone_no_Label.grid(row=0, column=2, padx=10)  # Adding padding to the right

        self.phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 8, "bold"))
        self.phone_no_entry.grid(row=0, column=3, padx=0, pady=10)

        # Add validation to allow only numbers
        vcmd = (self.root.register(self.validate_phone), '%P')
        self.phone_no_entry.config(validate='key', validatecommand=vcmd)

        self.var_phone.trace_add('write', self.validate_phone_number)



        #"""""""""""""""""""""""""" Roll No. Label and entrybox"""""""""""""""""""""""""""
        self.roll_no_Label = Label(class_student_frame, text="Roll No:", font=("times new roman", 8, "bold"), bg="white")
        self.roll_no_Label.grid(row=1, column=0)
        
        self.roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",8,"bold"))
        self.roll_no_entry.grid(row=1, column=1,padx=0, pady=2)
        # Set validation to accept only numbers
        self.roll_no_entry.config(validate="key", validatecommand=(self.root.register(self.validate_roll), '%S'))

           #""""""""""""""""""""""Gender and combo box"""""""""""""""""""""""""""
        
    
        self.gender_Label = Label(class_student_frame, text="Gender", font=("times new roman", 8, "bold"), bg="white")
        self.gender_Label.grid(row=1, column=2)


        self.gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman", 8, "bold"), state="readonly",width=18)
        self.gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        self.gender_combo.current(0)  # When we see on combo box always shows Select Department
        self.gender_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)


         #""""""""""""""""""""""' Name Label and entry box"""""""""""""""""
        self.stu_name_Label = Label(class_student_frame, text="Student Name", font=("times new roman", 8, "bold"), bg="white")
        self.stu_name_Label.grid(row=2, column=0)
        
        self.stu_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",8,"bold"))
        self.stu_name_entry.grid(row=2, column=1,padx=2, pady=5)

        # Inside the __init__ function where you define your GUI elements
        self.var_name.trace_add("write", self.validate_name)


        # #""""""""""""""""""""""""""""DOB Label and entry  box"""""""""""""""""""""""""
        #   # Name Label and entry box
        # self.calendar_icon = PhotoImage(file=r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\calendar.png")
        # img = img.resize((100,100), Image.Resampling.LANCZOS)
        # self.calendar_icon = ImageTk.PhotoImage(img)
        self.stu_dob_Label = Label(class_student_frame, text="D.O.B", font=("times new roman", 8, "bold"), bg="white")
        self.stu_dob_Label.grid(row=2, column=2)
        
        self.stu_dob_entry=tk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",8,"bold"))
        self.stu_dob_entry.grid(row=2, column=3,padx=2, pady=5)
    
        # Create a button to trigger the calendar with the icon
         # Create a button with text "Cal" to trigger the calendar
        select_date_button = Button(class_student_frame, text="Cal", command=self.show_calendar, width=3)
        select_date_button.grid(row=2, column=4, padx=2, pady=5)

        # Trace the changes in var_dob and call validate_dob function
        # Call the validate_dob function whenever needed
        self.stu_dob_entry.bind("<KeyRelease>", self.validate_dob)


        

        #"""""""""""""""""""""""""""""""""E-mail Label and entry box"""""""""""""""""
        self.var_mail = StringVar()
        self.email_Label = Label(class_student_frame, text="E-Mail", font=("times new roman", 8, "bold"), bg="white")
        self.email_Label.grid(row=3, column=0)
        
        self.email_entry=ttk.Entry(class_student_frame,textvariable=self.var_mail,width=20,font=("times new roman",8,"bold"))
        self.email_entry.grid(row=3, column=1,padx=2, pady=5)
        # Bind a function to validate the email when the content changes
        # Bind the validate_email function to the event when focus leaves the email entry field
        self.email_entry.bind("<FocusOut>", self.validate_email)

        #""""""""""""""""""'parent's number"""""""

        # Inside the __init__ function where you create the entry widget for the parent's phone number
        self.var_parent = StringVar()
        self.var_parent.trace_add('write', self.validate_parent_number)

        self.parents_Label = Label(class_student_frame, text="Parents No:", font=("times new roman", 8, "bold"), bg="white")
        self.parents_Label.grid(row=3, column=2, padx=10)  # Adding padding to the right

        self.parents_entry = ttk.Entry(class_student_frame,textvariable=self.var_parent, width=20, font=("times new roman", 8, "bold"))
        self.parents_entry.grid(row=3, column=3, padx=0, pady=10)
        

        


        #"""""""""""""""""""""""""""""""""""""radio button"""""""""""""""""""""""""""""""""
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=9,column=0,pady=15)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=9,column=  1,pady=15)

        #""""""""""""""""""""""""""""""""""""""""buttons_frame"""""""""""""""""""""""""
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=190,width=507,height=70)

        #"""""""""""""""""""""""""""""""""""""""""save data at Db""""""""""""""""""""""""""" 
        save_btn=Button(button_frame,text="Save",command=self.add_data,width=17,font=("times new roman",10,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0,padx=0,pady=0)

        update_btn=Button(button_frame,text="Update",width=17,font=("times new roman",10,"bold"),bg="green",fg="white",command=self.update_data)
        update_btn.grid(row=0,column=1,padx=0)

        delete_btn=Button(button_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",10,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2,padx=0)

        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",10,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3,padx=0)

        #""""""""""""""""""""""""""""""""""""""""buttons_frame 2"""""""""""""""""""""""""""
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=220,width=507,height=35)


        take_photo_btn=Button(button_frame,command=self.generate_dataset,text="Take a Photo Sample",width=32,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        take_photo_btn.grid(row=6,column=4,padx=0,pady=0)

        take_photo_btn=Button(button_frame,command=self.update_dataset,text="Update Photo Sample",width=43,font=("times new roman",10,"bold"),bg="sky blue",fg="black")
        take_photo_btn.grid(row=6,column=5,padx=0,pady=0)
        
       

        
        #"""""""""""""""""""""""""""""""""""right label frame"""""""""""""""""""""""""""""""""
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=550,y=1,width=690,height=430)

        #"""""""""""""""""""""""""""""""""""""""Search System"""""""""""""""""""""""""""""""""
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=10,width=670,height=70)

        #"""""""""""""""""""""""""""""""""""""""""Seach Label and Combobox"""""""""""""""""""""""""""""""""""
        search_Label = Label(search_frame, text="Search by:", font=("times new roman", 8, "bold"), bg="red", fg="white")
        search_Label.grid(row=0, column=0, padx=5, sticky=W)

        #"""""""""""""""""""""""""""""""""""""Combo box"""""""""""""""""""""""""""""""""""""""""""""
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchcombo,font=("times new roman", 8, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Course", "Department", "Semester", "Student_id", "Roll_No", "Name", "Session", "Gender", "Dob", "Phone", "email", "Parents_no")
        search_combo.current(0)  # When we see on combo box always shows Select Department
        search_combo.grid(row=0, column=1, padx=4)

        search_entry = ttk.Entry(search_frame,width=16,textvariable=self.var_searchentry,font=("times new roman", 8, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=0)  # grid have rows and columns

        Search_btn = Button(search_frame, text="Search", command=self.search_data,width=14, font=("times new roman", 10, "bold"), bg="green", fg="white")
        Search_btn.grid(row=0, column=3, padx=5)

         # Call fetch_data to populate the table with initial data
        self.fetch_data()

        show_all_btn = Button(search_frame, text="Show All",command=self.show_all_data,width=13, font=("times new roman", 10, "bold"), bg="green", fg="white")
        show_all_btn.grid(row=0, column=4, padx=5)


        # """"""""""""""""""""""""""""""""""Table Frame"""""""""""""""""""""""""""""""""""""""""""""

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=10,y=90,width=670,height=300)

        #""""""""""""""""""""""""""""""""scroll bar"""""""""""""""""""""""""""""""""""""""""""

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        #"""""""""""""""""""""""""""""""""student table""""""""""""""""""""""""""""""""""""""
        self.student_table=ttk.Treeview(table_frame,column=("course","dept","sem","id","roll","name","session","gender","dob","phone","email","parents","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("session",text="Session")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone",text="Phone No.")
        self.student_table.heading("email",text="E-mail") 
        self.student_table.heading("parents",text="Parent's No.")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("id",width=100,anchor='center')
        self.student_table.column("roll",width=100,anchor='center')

        self.student_table.column("course",width=100,anchor='center')
        self.student_table.column("dept",width=100,anchor='center')
        self.student_table.column("sem",width=100,anchor='center')
        self.student_table.column("session",width=100,anchor='center')
        self.student_table.column("gender",width=100,anchor='center')
        self.student_table.column("dob",width=100,anchor='center')
        self.student_table.column("phone",width=100,anchor='center')
        self.student_table.column("parents",width=100,anchor='center')
        self.student_table.column("photo",width=150,anchor='center')
        

        
        
        
        
        
        
        
        
        

        

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
       

    #"""""""""""""""""""""""""""""""""""""""""function declaration"""""""""""""""""""""""""'
    #or self.var_sem.get()=="Select Semester" or self.var_roll.get().isdigit()
    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_sem.get() == "Select Semester" or self.var_id.get() == "" or self.var_roll.get() == "" or self.var_name.get() == "" or self.var_session.get() == "" or self.var_gender.get() == "Select Gender" or self.var_dob.get() == "" or self.var_phone.get() == "" or self.var_mail.get() == "" or self.var_parent.get() == "" or self.var_radio1.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif not self.var_roll.get().isdigit():
            messagebox.showerror("Error", "Roll No. must be an integer", parent=self.root)
        elif self.var_radio1.get() not in ["Yes", "No"]:
            messagebox.showerror("Error", "Please select an option for photo sample", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)", (
    (
    self.var_course.get(),
    self.var_dept.get(), 
    self.var_sem.get(),
    self.var_id.get(),
    self.var_roll.get(), 
    self.var_name.get(),
    self.var_session.get(), 
    self.var_gender.get(),
    self.var_dob.get(),
    self.var_phone.get(),
    self.var_mail.get(),
    self.var_parent.get(),
    self.var_radio1.get()
)
       
))


            

                conn.commit()
                self.fetch_data()#mistake of closing this bracket leads to right side frame does'nt update on the spot
                conn.close()
                messagebox.showinfo("Success","Students details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    

#"""""""fetch data"""""""""""""""""""""""""""""""""""""""""""
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")

        #store data in variable"""""""""""
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            #insert all data by fetching through for loop
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()  #so that our data continiously adding
        conn.close()
    

    #"""""""""""""""""""""""""""""""""""""""""""""get cursor""""""""""""""""""
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)  #we arew taking content through item keyword
        data=content["values"]

        # def get_cursor(self, event=""):
        #     cursor_focus = self.student_table.focus()
        #     content = self.student_table.item(cursor_focus)
        #     data = content["values"]
        
        if data:  # Check if data is not empty
            self.var_course.set(data[0]),
            self.var_dept.set(data[1]),
            self.var_sem.set(data[2]),
            self.var_id.set(data[3]),
            self.var_roll.set(data[4]),
            self.var_name.set(data[5]),
            self.var_session.set(data[6]),
            self.var_gender.set(data[7]),
            self.var_dob.set(data[8]),
            self.var_phone.set(data[9]),
            self.var_mail.set(data[10]),
            self.var_parent.set(data[11]),
            self.var_radio1.set(data[12])


    #"""""""""""""""""""""""Update Function"""""""""""""""""""
    def update_data(self):
        if (self.var_dept.get() == "Select Department" or
            self.var_course.get() == "Select Course" or
            self.var_sem.get() == "Select Semester" or
            self.var_id.get() == "" or
            self.var_roll.get() == "" or
            self.var_name.get() == "" or
            self.var_session.get() == "" or
            self.var_gender.get() == "Select Gender" or
            self.var_dob.get() == "" or
            self.var_phone.get() == "" or
            self.var_mail.get() == "" or
            self.var_parent.get() == "" or
            self.var_radio1.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif not self.var_roll.get().isdigit():
            messagebox.showerror("Error", "Roll No. must be an integer", parent=self.root)
        elif self.var_radio1.get() not in ["Yes", "No"]:
            messagebox.showerror("Error", "Please select an option for photo sample", parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("Update","Do you want to update Student details",parent=self.root)
                if upadate>0:#upadate is written due to update already existing
                    conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE Student set Course=%s,Department =%s,Semester=%s,Roll_No=%s, Name=%s, Session=%s, Gender=%s, Dob=%s, Phone=%s, email=%s, Parents_no=%s, PhotoSample=%s WHERE Student_id=%s", (
    self.var_course.get(),
    self.var_dept.get(), 
    self.var_sem.get(),
    self.var_roll.get(), 
    self.var_name.get(),
    self.var_session.get(), 
    self.var_gender.get(),
    self.var_dob.get(),
    self.var_phone.get(),
    self.var_mail.get(),
    self.var_parent.get(),
    self.var_radio1.get(),
    self.var_id.get()  # You are using Student_id for the WHERE clause
))

                                                                                                                                                                            
    

                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success", "Students details Successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

        #""""""""""""""""""Delete function"""
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student is must be required",parent=self.root) #So that Std id can't get deleted.
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted Student details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

  #  """""""""""""Reset button Function """"""""""
    def reset_data(self):
            self.var_course.set("Select Course")
            self.var_dept.set("Select Department") 
            self.var_sem.set("Select Semester")
            self.var_roll.set("") 
            self.var_name.set("")
            self.var_session.set("Select Session") 
            self.var_gender.set("Select Gender")
            self.var_dob.set("")
            self.var_phone.set("")
            self.var_mail.set("")
            self.var_parent.set("")
            self.var_radio1.set("")
            self.var_id.set("")
    

#""""""""""""""Generate dataset or Take Photo Sample""""""""""""""""""'
    def generate_dataset(self):
        if (self.var_dept.get() == "Select Department" or self.var_id.get() == "" or self.var_sem.get() == "Select Semester" or not self.var_roll.get().isdigit()):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE Student SET Course=%s, Department=%s, Semester=%s, Roll_No=%s, Name=%s, Session=%s, Gender=%s, Dob=%s, Phone=%s, email=%s, Parents_no=%s, PhotoSample=%s WHERE Student_id=%s",(
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                 self.var_dept.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_session.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_mail.get(),
                                                                                                                                                                                    self.var_parent.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                               self.var_id.get()==id+1
                                                                                                                                                                                )) 
                               # Add the rest of your values here

                conn.commit()  # Commit the transaction
                self.fetch_data()
                self.reset_data()
                conn.close()   # Close the connection

                #"""""""""""""Load Predefined data on face frontal from open cv"
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # min. neighbor

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset completed!!!")




            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
    
    def update_dataset(self):
        if (self.var_dept.get() == "Select Department" or self.var_id.get() == "" or self.var_sem.get() == "Select Semester" or not self.var_roll.get().isdigit()):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
                my_cursor = conn.cursor()

                # Update student information
                my_cursor.execute("UPDATE Student SET Course=%s, Department=%s, Semester=%s, Roll_No=%s, Name=%s, Session=%s, Gender=%s, Dob=%s, Phone=%s, email=%s, Parents_no=%s WHERE Student_id=%s", (
                    self.var_course.get(),
                    self.var_dept.get(),
                    self.var_sem.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_session.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_mail.get(),
                    self.var_parent.get(),
                    self.var_id.get()
                ))

                # Commit the transaction
                conn.commit()

                # Load Predefined data on face frontal from open cv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(self.var_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                # Update photo sample path in the database
                photo_sample_path = file_name_path
                my_cursor.execute("UPDATE Student SET PhotoSample=%s WHERE Student_id=%s", (photo_sample_path, self.var_id.get()))
                conn.commit()

                messagebox.showinfo("Result", "Generating Dataset completed!!!")

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
            finally:
                if conn:
                    conn.close()


          


    def search_data(self):
    # Get the selected column name and row value entered by the user
        selected_column = self.var_searchcombo.get()
        search_value = self.var_searchentry.get()

          # Establish the database connection
        

    # Construct the SQL query
        if selected_column == "Select" or search_value == "":
            messagebox.showerror("Error", "Please select a column and enter search value")
            return
        
         # List of allowed columns to prevent SQL injection
        allowed_columns = ["Course", "Department","Semester","Student_id","Roll_No","Name","Session","Gender","Dob","Phone","email","Parents_no"]

        if selected_column not in self.allowed_columns:
            messagebox.showerror("Error", "Invalid column selected")
            return
        # else:
        try:
                 # Establish database connection and create cursor
            conn = mysql.connector.connect(host="localhost",username="root",password="Hi@itsabhish1",database="face_recognition"
                )
            if conn.is_connected():
                cursor = conn.cursor()
                
                    # Construct the SQL query using parameterized query
                sql = f"SELECT * FROM students WHERE {selected_column} LIKE %s"
                cursor.execute(sql, ('%' + search_value + '%',))
                    # Fetch all matching records
                results = cursor.fetchall()
            
                if results:
                # Example: Print results to console or update UI accordingly
                        result_text = '\n'.join([str(row) for row in results])
                        self.result_label.config(text=result_text)
                else:
                    self.result_label.config(text="No matching records found")
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

        finally:
            # Close the database connection
            if conn.is_connected():
                cursor.close()
                conn.close()
    # Function to validate Roll No. entry
    def validate_roll(self, input_char):
        return input_char.isdigit()  # Returns True if input is a digit, False otherwise
    
    def validate_id(self):
        if not self.var_id.get().isdigit():
            messagebox.showerror("Error", "Student ID should only contain digits",parent=self.root)
            self.var_id.set("")  # Clear the entry box if non-digit characters are entered

        # Add the validation function
    def validate_phone(self, new_text):
        if new_text.isdigit() or new_text == "":
            return True
        else:
            return False
        
    # Define the validate_phone_number function
    def validate_phone_number(self, *args):
        # Remove non-digit characters
        phone_number = ''.join(filter(str.isdigit, self.var_phone.get()))
        if len(phone_number) > 10:
            # Trim the phone number to 10 digits if it exceeds the length
            phone_number = phone_number[:10]
        self.var_phone.set(phone_number)
        
    # Define the validate_parent_number function
    # Define the validate_parent_number function
    def validate_parent_number(self, *args):
        # Remove non-digit characters
        parent_number = ''.join(filter(str.isdigit, self.var_parent.get()))
        if len(parent_number) > 10:
            # Trim the parent's phone number to 10 digits if it exceeds the length
            parent_number = parent_number[:10]
        self.var_parent.set(parent_number)

    # Define the validate_email function
    def validate_email(self, *args):
        email = self.var_mail.get()
        if email and not email.endswith('@gmail.com'):
            # If email doesn't end with '@gmail.com', clear the entry
            self.var_mail.set('')
            messagebox.showwarning("Invalid Email", "Email must end with '@gmail.com'")

     #Define the validation function
    def validate_name(self, *args):
        # Get the current value of the student name entry box
        name = self.var_name.get()
        
        # Check if the current value contains any digits
        if any(char.isdigit() for char in name):
            # If it contains digits, show an error message
            messagebox.showerror("Error", "Student name cannot contain numbers", parent=self.root)
            
            # Reset the entry box to remove the typed number
            self.var_name.set(name[:-1])

    def show_calendar(self):
        # Create a top-level window
        self.top = Toplevel(self.root)
        self.top.title("Select Date")
        self.cal = Calendar(self.top, selectmode="day", date_pattern="dd/mm/yyyy",year=1990, month=1, day=1)
        self.cal.pack()

        # Button to select the date
        select_button = Button(self.top, text="Select", command=self.get_date)
        select_button.pack()

    def get_date(self):
        # Get the selected date
        selected_date = self.cal.get_date()
        # Set it in the entry box
        self.var_dob.set(selected_date)
        # Close the calendar window
        self.top.destroy()

    def validate_dob(self, event):
        # Get the current value of the date of birth entry
        dob = self.var_dob.get()

        # Remove any non-numeric characters from the input
        dob = ''.join(filter(str.isdigit, dob))

        # Ensure that the date, month, and year have the appropriate number of digits
        if len(dob) > 8:
            dob = dob[:8]

        # Format the date, month, and year with slashes
        if len(dob) >= 2:
            dob = dob[:2] + '/' + dob[2:]
        if len(dob) >= 5:
            dob = dob[:5] + '/' + dob[5:]

        # Ensure that the entered date, month, and year are within valid ranges
        if len(dob) >= 2:
            day = int(dob[:2])
            dob = str(min(day, 31)).zfill(2) + dob[2:]
        if len(dob) >= 5:
            month = int(dob[3:5])
            dob = dob[:3] + str(min(month, 12)).zfill(2) + dob[5:]
        if len(dob) >= 10:
            year = int(dob[6:])
            dob = dob[:6] + str(min(year, 9999)).zfill(4)

        # Update the entry field with the formatted date of birth
        self.var_dob.set(dob)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")

        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def search_data(self):
    # Get the selected column name and the search value entered by the user
        selected_column = self.var_searchcombo.get()
        search_value = self.var_searchentry.get()

        # Check if the user has selected a column and entered a search value
        if selected_column == "Select" or search_value == "":
            messagebox.showerror("Error", "Please select a column and enter a search value", parent=self.root)
            return

        # List of allowed columns to prevent SQL injection
        allowed_columns = ["Course", "Department", "Semester", "Student_id", "Roll_No", "Name", "Session", "Gender", "Dob", "Phone", "email", "Parents_no"]

        # Ensure the selected column is valid
        if selected_column not in allowed_columns:
            messagebox.showerror("Error", "Invalid column selected", parent=self.root)
            return

        try:
            # Establish the database connection
            conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            cursor = conn.cursor()

            # Construct the SQL query using parameterized query
            sql = f"SELECT * FROM student WHERE {selected_column} LIKE %s"
            cursor.execute(sql, ('%' + search_value + '%',))

            # Fetch all matching records
            results = cursor.fetchall()

            if results:
                # Clear the current data in the student table
                self.student_table.delete(*self.student_table.get_children())

                # Insert fetched data into the student table
                for row in results:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)

            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def show_all_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
                conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching data: {str(e)}",parent=self.root)
        finally:
            if conn.is_connected():
                conn.close()
    
    

        


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

