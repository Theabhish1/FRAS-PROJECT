from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import csv
import webbrowser
from tkinter import filedialog

class Developer:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1630x1000+0+0")
        self.root.title("Face Recognition Attendance System")


        
        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",35,"bold"),bg="Pink",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        


        #""""""""""""""""""""""""""""""""""""""image full"""""""""""""""""""""""""""""""""""""
        img_top=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\developers.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=45,width=1530,height=720)


            #   "main frame"
        main_frame=Frame(f_lbl,bd=2,bg="white")#bd-border
        main_frame.place(x=1000,y=0,width=500,height=330)

        
        #""""""""""""""""""""""""""""""""""""""image frame's"""""""""""""""""""""""""""""""""""""
        img_top1=Image.open(r"Images\abhi4.jpg")
        img_top1=img_top1.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img_top1)
        

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1005,y=47,width=150,height=150)

        img_top2=Image.open(r"Images\kushal.jpg")
        img_top2=img_top2.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img_top2)
        

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1150,y=47,width=150,height=150)

        
        dev_Label = Label(main_frame, text="Developed By Jaiswal Abhishek M. and Kushal", font=("times new roman", 10, "bold"), bg="white")
        dev_Label.place(x=0,y=150)
        
        dev1_Label = Label(main_frame, text="Roll No: 2103730109002 and 2003730100010", font=("times new roman", 10, "bold"), bg="white")
        dev1_Label.place(x=0,y=170)

        dev2_Label = Label(main_frame, text="Course : B.Tech. C.S.E(Final Year)", font=("times new roman", 10, "bold"), bg="white")
        dev2_Label.place(x=0,y=190)
         
          
        dev3_Label = Label(main_frame, text="Student of Neelkanth Insitite of Technology,Meerut", font=("times new roman", 7, "bold"), bg="white")
        dev3_Label.place(x=0,y=210)
        
        dev4_Label = Label(main_frame, text="For any issue contact us on:", font=("times new roman", 13, "bold"), bg="white")
        dev4_Label.place(x=0,y=240)
         
       # LinkedIn link
        linkedin_label = Label(main_frame, text="Linkedin- Abhishek", font=("times new roman", 12, "bold"), fg="black", cursor="hand2", bg="Yellow")
        linkedin_label.place(x=0, y=260)
        linkedin_label.bind("<Button-1>", self.open_linkedin)

           
       # LinkedIn link
        linkedin_label_1= Label(main_frame, text="Linkedin- Kushal", font=("times new roman", 12, "bold"), fg="black", cursor="hand2", bg="yellow")
        linkedin_label_1.place(x=0, y=290)
        linkedin_label_1.bind("<Button-1>", self.open_linkedin1)

    def open_linkedin(self, event):
    # Function to open LinkedIn profile in web browser
            webbrowser.open_new("https://www.linkedin.com/in/abhishek-jaiswal-84608b227/")

    def open_linkedin1(self, event):
    # Function to open LinkedIn profile in web browser
            webbrowser.open_new("https://www.linkedin.com/in/kushal-chauhan-a96650228/")



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
