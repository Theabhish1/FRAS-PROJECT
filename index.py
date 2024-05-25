from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image,ImageTk
from student import Student 
import os
from train  import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help
import tkinter
from datetime import  datetime
from time import strftime
from main import Face_Recognition_system
import string
import secrets
import tkinter as tk
import mysql.connector
import cv2 
from tkinter import simpledialog
from tkinter import filedialog
import tkinter as tk
from tkcalendar import Calendar


def main():
    win=Tk()
    app=Login_Window(win)# win means window
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1500x1000+0+0")

        self.root.bind("<Return>", self.login)  # Bind the Enter key to the login method

    

           #text variable for taking data from entry fill and combobox
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        



        # Load the background image
        original_image = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\nature.jpg")

        # Resize the background image to match the window dimensions
        resized_image = original_image.resize((1550, 800), resample=Image.LANCZOS)

        # Convert the resized image to PhotoImage
        self.bg = ImageTk.PhotoImage(resized_image)
       # self.bg=ImageTk.PhotoImage(file=r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\nature.jpg")

        # Create a label to display the background image
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create other widgets, e.g., a frame and an image label
        frame = Frame(self.root, bg="black")
        frame.place(x=550, y=170, width=340, height=400)

#icon img
        img1 = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\user login.png")
        img1 = img1.resize((50, 50), resample=Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        
        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=700, y=170, width=50, height=50)

        get_str=Label(frame,text="Get Started",font=("times new roman",18,"bold"),fg="white",bg="black")
        get_str.place(x=109,y=48)

        #"""""""""""""username entryfill"""""""""
        username=lbl=Label(frame,text="Email",font=("times new roman",12,"bold"),fg="white",bg="black")
        username.place(x=70,y=105)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=130,width=270)

          #"""""""""""""pass entry fill"""""""""
        password=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="black")
        password.place(x=70,y=165)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=190,width=270)

        #"""""""icon images"""
        img2 = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\username.png")
        img2 = img2.resize((25, 25), resample=Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        
        lblimg1 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg1.place(x=590, y=275, width=25, height=25)

        #''''''''''''''''icon2
        img3 = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\pass1.png")
        img3 = img3.resize((30, 30), resample=Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        
        lblimg2 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg2.place(x=590, y=335, width=25, height=25)

        #""""""""""""login buttton""""
        loginbtn=Button(frame,command=self.login,text="login",font=("times new roman",15,"bold"),bd=2,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=130,y=230,width=100,height=30)    

        #"""""""""""""'register button"
        regibtn1=Button(frame,text="New user? Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        regibtn1.place(x=20,y=280,width=130) 

        #Forgot pass button"""""""
        forgbtn2=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgbtn2.place(x=10,y=300,width=130)  







        

    #         #""""""""""RESET PASS
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer", parent=self.root2)
        elif not self.is_strong_password(self.txt_newpass.get()):
            messagebox.showerror("Error", "Password must be strong and contain at least 8 characters, including uppercase, lowercase, digits, and special characters.", parent=self.root2)
        else:
            # Database validation and password reset logic
            conn=mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            my_cursor=conn.cursor()

            # Get text values from tkinter Entry widgets
            email = self.txtuser.get()
            security_q = self.combo_security_Q.get()
            security_a = self.txt_security.get()

            query=("Select * from register where email=%s and SecurityQ=%s and securityA=%s")
            value = (email, security_q, security_a)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Looks like You have Entered Incorrect Answer. Please, Enter the correct Answer", parent=self.root2)
            else:
                old_password = row[6]  # Assuming password is stored in the 7th column
                if self.txt_newpass.get() == old_password:
                    messagebox.showerror("Error", "You have entered your old password. Please enter a new password.", parent=self.root2)
                else:
                    query="Update register set password=%s where email=%s"
                    value=(self.txt_newpass.get(),email)
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Your Password has been reset. Please login with the new Password", parent=self.root2)
                    self.root2.destroy()

    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        # Additional check for specific special characters
        required_special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', ',', '.', '<', '>', '/', '?']
        if not any(char in required_special_characters for char in password):
            return False
        return True







    
    
    #""""""""""""""""""""""""""""forget pass windoww"""""
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset Password")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),) #get data from user id to reset password
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row) #output showing in terminal
            
            if row==None:
                messagebox.showerror("Error","Please enter a valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("350x450+550+130")#kbri298@gmail.com

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                 #"""""security Question in forget pass
                securityQ=Label(self.root2,text="Select Security Question",font=("times new roman",14,"bold"),bg="white")
                securityQ.place(x=30,y=80)
                
                self.combo_security_Q= ttk.Combobox(self.root2,font=("times new roman", 12, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your BestFriend Name", "Your Favorite Number", "Your Childhood Name","Your Favorite Food")
                self.combo_security_Q.place(x=30,y=110,width=250)
                self.combo_security_Q.current(0)  
            
                #""""""security ans in forget pass"""""
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",14,"bold"),bg="white")
                security_A.place(x=30,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",12,"bold"))
                self.txt_security.place(x=30,y=175,width=250)

                 #""""""new pass"""'
                new_password=Label(self.root2,text="New Password",font=("times new roman",14,"bold"),bg="white")
                new_password.place(x=30,y=210)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",12,"bold"))
                self.txt_newpass.place(x=30,y=240,width=250)
#reset button
                reset_btn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=2,relief=RIDGE,fg="white",bg="green",activeforeground="white",activebackground="green")
                reset_btn.place(x=100,y=290)  




        
  # "register window directly open forget pass."
    def register_window(self):
        self.new_window=Toplevel(self.root)  #register window open on top level on login page/login page ke upar
        self.app=Register(self.new_window)
        
#     # """"""""""""work on login button""""""""""""
    def login(self,event=None):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are Required",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
        ))
        
        row = my_cursor.fetchone()
        if row:
            messagebox.askquestion("Welcome", "Do you want to Login",parent=self.root)
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_system(self.new_window)
        else:
            messagebox.showerror("Invalid", "Invalid Username and password")
        conn.commit()
        conn.close()





# """""""""""""""""""register page data"""
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x1000+0+0")

        #text variable for taking data from entry fill and combobox
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_pass2 = tk.StringVar()

        #""""""""""""""""""background image"""""""""
        original_image = Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\register.jpg")

        # Resize the background image to match the window dimensions
        resized_image = original_image.resize((1550, 800), resample=Image.LANCZOS)

        # Convert the resized image to PhotoImage
        self.bg = ImageTk.PhotoImage(resized_image)

        # Create a label to display the background image
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #"""""""""""""""""""""""""""""left image"""""""
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\neelkanth.png")
        #now show it on windows
        left_lbl = Label(self.root, image=self.bg1)  # Change self.bg to self.bg1
        left_lbl.place(x=480, y=100, width=300, height=450)  # relation width and height place over whole window
        

        #"""""""""""""""""""""""main frame"""""""""
        frame=Frame(self.root,bg="white")
        frame.place(x=780,y=100,width=400,height=450)
       #register label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)
        
        #""""""label and entry fill"""""""""""""1st
        fname=Label(frame,text="First Name",font=("times new roman",10,"bold"),bg="white")
        fname.place(x=30,y=90)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
        fname_entry.place(x=30,y=110,width=140)

        #""""""label and entry fill"""""""""""""2nd
        l_name=Label(frame,text="Last Name",font=("times new roman",10,"bold"),bg="white")
        l_name.place(x=220,y=90)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",10,"bold"))
        self.txt_lname.place(x=220,y=110,width=160)

        # Bind validation functions to entry fields
        fname_entry.config(validate="key", validatecommand=(self.root.register(self.validate_fname), "%P"))
        self.txt_lname.config(validate="key", validatecommand=(self.root.register(self.validate_lname), "%P"))

        #""""""lbel and entry fill"""""""""""""3rd
        contact= Label(frame, text="Contact No", font=("times new roman", 10, "bold"), bg="white")
        contact.place(x=30, y=140)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 10, "bold"))
        self.txt_contact.place(x=30, y=160, width=140)
        self.txt_contact.insert(0, " Enter Only Numbers")  # Add sample text

        # Bind <FocusIn> event to remove sample text when clicked
        self.txt_contact.bind("<FocusIn>", self.contact_sample_text)


        # Configure entry to accept only numbers
        self.txt_contact.config(validate="key", validatecommand=(self.root.register(self.validate_contact_number), "%P"))
      
         #""""""label and entry fill"""""""""""""5th
        email=Label(frame,text="Email",font=("times new roman",10,"bold"),bg="white")
        email.place(x=220,y=140)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",10,"bold"))
        self.txt_email.place(x=220,y=160,width=160)
        self.txt_email.insert(0, "e.g. kbri298@gmail.com")  # Add sample text

        # Bind <FocusIn> event to remove sample text when clicked
        self.txt_email.bind("<FocusIn>", self.clear_sample_text)

        

        #""""""label and entry fill"""""""""""""6th
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",10,"bold"),bg="white")
        security_Q.place(x=30,y=190)
        
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 10, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your BestFriend Name", "Your Favorite Number", "Your Childhood Name","Your Favorite Food")
        self.combo_security_Q.place(x=30,y=210,width=140)
        self.combo_security_Q.current(0)  
       
          #""""""label and entry fill"""""""""""""7th
        security_A=Label(frame,text="Security Answer",font=("times new roman",10,"bold"),bg="white")
        security_A.place(x=220,y=187)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",10,"bold"))
        self.txt_security.place(x=220,y=205,width=160)



        #    #""""""label and entry fill"""""""""""""8th
        pswd=Label(frame,text="Password",font=("times new roman",10,"bold"),bg="white")
        pswd.place(x=30,y=240)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",10,"bold"))
        self.txt_pswd.place(x=30,y=260,width=140)
       
        generate_btn = tk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_btn.place(x=30,y=285,width=140)
       

         
        #     #""""""label and entry fill"""""""""""""thth
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",10,"bold"),bg="white")
        confirm_pswd.place(x=220,y=240)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",10,"bold"))
        self.txt_confirm_pswd.place(x=220,y=260,width=160)

        #"""""'Check button"""""""
        self.var_check = IntVar()
        Checkbtn = Checkbutton(frame, text="I Agree Terms and Conditions", font=("times new roman", 10, "bold"), variable=self.var_check, onvalue=1, offvalue=0)
        Checkbtn.place(x=30, y=320)

        
         #""""""""""""REGISTER buttton"""
        register_btn=Button(frame,command=self.register_data,cursor="hand2",text="Register Now",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="Green",activeforeground="white",activebackground="green")
        register_btn.place(x=30,y=355,width=170)    

           #""""""""""""login buttton""""
        login_btn=Button(frame,text="login Now",command=self.return_login,cursor="hand2",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_btn.place(x=220,y=355,width=170)   


        # """"""""""""""""""function declarartion and DATABSE Work""
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Eror","All fields are required",parent=self.root)
        if not self.is_strong_password(self.var_pass.get()):
            messagebox.showerror("Error", "Password must be strong and contain at least 8 characters, including uppercase, lowercase, digits, and special characters (. , @ $ % &)",parent=self.roo)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0: #we are taking 0 instead of empty because we have to work on integer
            messagebox.showerror("Error","Please agree our Terms and Conditions",parent=self.root)
        elif "@gmail.com" not in self.var_email.get():
            messagebox.showerror("Error", "Email must contain @gmail.com",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),) #getting email
            #taking from db
            my_cursor.execute(query,value)
            row=my_cursor.fetchone() #fetching data from db
            if row !=None:
                messagebox.showerror("Error","Email id already exist,Please try another email",parent=self.root)  #avoid duplicate email
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                  self.var_fname.get(),
                                                                                  self.var_lname.get(),
                                                                                  self.var_contact.get(),
                                                                                  self.var_email.get(),
                                                                                  self.var_securityQ.get(),
                                                                                  self.var_securityA.get(),
                                                                                  self.var_pass.get()

                                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully",parent=self.root)

                
               



               
            
           


    def clear_sample_text(self, event):
         #"""Clears the sample text when the entry box is clicked."""
        if self.txt_email.get() == "e.g. kbri298@gmail.com":
            self.txt_email.delete(0, END)  # Clear the entry box
            self.txt_email.config(foreground='black')  # Change text color to black


    def contact_sample_text(self, event):
        """Clears the sample text when the entry box is clicked."""
        if self.txt_contact.get() == " Enter Only Numbers":
            self.var_contact.set("")

    # Function to validate contact number input
    def validate_contact_number(self, input_text):
        # Allow empty entry
        if input_text == "":
            return True
        # Check if input consists only of digits and has a length of 10
        elif input_text.isdigit() and len(input_text) <= 10:
            return True
        else:
            return False


    
    def return_login(self):
        self.root.destroy()

    # Function to validate first name input
    def validate_fname(self, input_text):
        if input_text == "":
            return True
        elif input_text.isalpha():
            return True
        else:
            return False

    # Function to validate last name input
    def validate_lname(self, input_text):
        if input_text == "":
            return True
        elif input_text.isalpha():
            return True
        else:
            return False
    
    
    
    # Function to validate security answer
    def validate_security_answer(self, input_text):
        if input_text.isalpha() or input_text == "":
            return True
        else:
            return False
        
    import string
    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        # Additional check for specific special characters
        required_special_characters = ['.', ',', '@', '$', '%', '&']  # Add more if needed
        if not any(char in required_special_characters for char in password):
            return False
        return True
    def generate_password(self):
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
        self.var_pass.set(password)



class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x1000+0+0")
        # self.root.attributes('-fullscreen', True)  # Open in full-screen mode
        self.root.title("Face Recognition Attendance System")

        

#image 1
        img=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\download.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

#image 2
        img1=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\download.jpg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


#image 3
        img2=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\download.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

#bg image
        img3=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\Face\Imp_images\college-75535_1280.jpg")
        img3=img3.resize((1420,960),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1420,height=960)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        #""""""""show time"""""""""""""
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string) #place string in lbl/label
            lbl.after(1000,time) #1000ms=1s
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        

#Student BUTTONS
        img4=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\student_information.png")
        img4=img4.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=110,height=110)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_1.place(x=200,y=200,width=110,height=40)

        #DETECT FACE BUTTON

        img5=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\detect.jpg")
        img5=img5.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=110,height=110)

        b1_2=Button(bg_img,text="Mark Attendance",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="green",fg="white")
        b1_2.place(x=400,y=200,width=110,height=40)

        #attendence FACE BUTTON

        img6=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\attendence.png")
        img6=img6.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data,)
        b1.place(x=600,y=100,width=110,height=110)

        b1_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_3.place(x=600,y=200,width=110,height=40)

        #help BUTTON

        img7=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\help desk2.png")
        img7=img7.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data,)
        b1.place(x=800,y=100,width=110,height=110)

        b1_4=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_4.place(x=800,y=200,width=110,height=40)


               #Train BUTTON

        img8=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\traun data.png")
        img8=img8.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=300,width=110,height=110)

        b1_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_5.place(x=200,y=400,width=110,height=40)

                #Photos BUTTON

        img9=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\photo.jpg")
        img9=img9.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=110,height=110)

        b1_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_6.place(x=400,y=400,width=110,height=40)



         #Developer BUTTON

        img10=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\developer.png")
        img10=img10.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=600,y=300,width=110,height=110)

        b1_7=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_7.place(x=600,y=400,width=110,height=40)

        
         #Exit BUTTON

        img11=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\exit.jpg")
        img11=img11.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1.place(x=800,y=300,width=110,height=110)

        b1_8=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_8.place(x=800,y=400,width=110,height=40)


    def open_img(self):
        os.startfile("data")

    def iexit(self):
        self.iexit =tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
    

    #""""""""""""""Function button"""""""""""""""""""""""""""""""""
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app =  Face_Recognition(self.new_window)


    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app =  Attendence(self.new_window)
    
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app =  Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app =  Help(self.new_window)

   





                
if __name__ == "__main__":
    main()#call main


    #performance to open a new windows will increase if we create 2 windows in one class which is done in this project for new user register
