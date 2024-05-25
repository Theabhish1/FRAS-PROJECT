from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import cv2.face
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x1000+0+0")
        self.root.title("Face Recognition Attendance System")

        title_lbl = Label(self.root, text="CLICK ON BELOW MARK ATTENDANCE BUTTON", font=("times new roman", 30, "bold"), bg="green", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Image on the left side/1st img
        img_top = Image.open("Images/blog-–-462-1.jpg")
        img_top = img_top.resize((1400,600), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_top)

        left_lbl = Label(self.root, image=self.photoimg_left)
        left_lbl.place(x=0, y=45, width=1400, height=600)

        # Button
        b1_1 = Button(left_lbl, text="Mark Attendence", cursor="hand2", font=("times new roman", 18, "bold"), bg="green", fg="white", command=self.face_recog)
        b1_1.place(x=970, y=455, width=200, height=40)
       # """"""""""""""""""""""""""""""""""""""""Mark attendence"""
    def mark_attendence(self, i, r, n, d):
        with open("abhi.csv", "r+", newline="\n") as f:
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry = line.split(",")
                name_list.append(entry[0])

            now = datetime.now()
            current_date = now.strftime("%d/%m/%Y")
            dt_string = now.strftime("%H:%M:%S")

            attendance_record = f"{i},{n},{r},{d},{dt_string},{current_date},Present\n"

            

            updated = False
            for index, line in enumerate(my_data_list):
                fields = line.split(",")
                if fields[0] == str(i) and fields[-2] == current_date:
                    my_data_list[index] = attendance_record
                    updated = True
                    break

            if not updated:
                f.write(attendance_record)








        #"""""""""""""""""""""Face recog"""""""""""""

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []  # list of coordinates
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Hi@itsabhish1", database="face_recognition")
                my_cursor = conn.cursor()
                
            # name
                my_cursor.execute("Select Name from student where Student_id=" + str(id))
                n =my_cursor.fetchone()
                n = "+".join(n)#concatinate

                # roll
                my_cursor.execute("Select Roll_No from student where Student_id=" + str(id))
                r =my_cursor.fetchone()
                r = "+".join(r)

            # Department
                my_cursor.execute("Select Department  from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
  # Id
                my_cursor.execute("Select Student_id  from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                print(f"Confidence: {confidence}")
                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                    cv2.putText(img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                    cv2.putText(img, f"Roll No:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)  # blur color 255,255,255
                    self.mark_attendence(i,n,r,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)  # for red color 0,255,255
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):#clf and facecascade are algorithm
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        # read written classifier
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)  # 0 for front camera
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
