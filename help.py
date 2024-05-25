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


class Help:
    def __init__(self,root):
        self.root=root
        
       
        self.root.geometry("1500x1000+0+0")
        self.root.title("Face Recognition Attendance System")



        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg="skyblue",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        


        #""""""""""""""""""""""""""""""""""""""image full"""""""""""""""""""""""""""""""""""""
        img_top=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\help desk1.png")
        img_top=img_top.resize((1050,600),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=45,width=1050,height=600)


        email_button = Button(self.root, text="Click here to Email Us", font=("times new roman", 10, "bold"), bg="white",
                              command=self.open_email)
        email_button.place(x=410, y=410)

         # Button for contact details
        contact_button = Button(self.root, text="Contact Us via Phone", font=("times new roman", 10, "bold"), bg="white",
                                command=self.open_contact_details)
        contact_button.place(x=440, y=430)

    def open_email(self):
        try:
             webbrowser.open("mailto:kbri298@gmail.com")
        except Exception as e:
             messagebox.showerror("Error", f"An error occurred: {str(e)}")

    
        
   

    def open_contact_details(self):
        # Open contact details page or perform action to display contact details
        messagebox.showinfo("Contact Details", "Contact us at: 7387709867")
        
        

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
