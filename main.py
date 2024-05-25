from tkinter import*
from tkinter import ttk
import tkinter.messagebox
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
class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x1000+0+0")
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

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=200,y=200,width=110,height=40)

        #DETECT FACE BUTTON

        img5=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\detect.jpg")
        img5=img5.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=110,height=110)

        b1_1=Button(bg_img,text="Mark Attendance",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=400,y=200,width=110,height=40)

        #attendence FACE BUTTON

        img6=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\attendence.png")
        img6=img6.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data,)
        b1.place(x=600,y=100,width=110,height=110)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        b1_1.place(x=600,y=200,width=110,height=40)

        #help BUTTON

        img7=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\help desk2.png")
        img7=img7.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data,)
        b1.place(x=800,y=100,width=110,height=110)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=800,y=200,width=110,height=40)


               #Train BUTTON

        img8=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\traun data.png")
        img8=img8.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=300,width=110,height=110)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=200,y=400,width=110,height=40)

                #Photos BUTTON

        img9=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\photo.jpg")
        img9=img9.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=110,height=110)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=400,y=400,width=110,height=40)



         #Developer BUTTON

        img10=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\developer.png")
        img10=img10.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=600,y=300,width=110,height=110)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=600,y=400,width=110,height=40)

        
         #Exit BUTTON

        img11=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\exit.jpg")
        img11=img11.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1.place(x=800,y=300,width=110,height=110)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",12,"bold"),bg="green",fg="white",activebackground="green",activeforeground="white")
        b1_1.place(x=800,y=400,width=110,height=40)


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


        


#Object
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()
