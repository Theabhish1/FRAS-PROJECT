from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x1000+0+0")
        self.root.title("Face Recognition Attendence System")

       

        title_lbl=Label(self.root,text="TRAIN DATASET ",font=("times new roman",35,"bold"),bg="Yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        


        #""""""""""""""""""""""""""""""""""""""image top"""""""""""""""""""""""""""""""""""""
        img_top=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\full.jpg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=45,width=1530,height=325)



         #""""""""""""button""
        btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",width=30,font=("times new roman",30,"bold"),bg="green",fg="white")
        btn.place(x=0,y=380,width=1530,height=60)
            
    #"""""""""""""""""""""""""""""""""""""img bottom"""
        img_bottom=Image.open(r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\full.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)


    

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)  for file in os.listdir(data_dir)]


        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  #here we get gray scale image
            #we have to now convert in grid so we need numpy array
            imageNp=np.array(img,'uint8') #UNIT8 IS datatype
            id=int(os.path.split(image)[1].split('.')[1])

             # C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\data\user.11.1.jpg
              #0                                                                      1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
         #""""""""""""train the classifier and save"""""""""
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")
            





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()