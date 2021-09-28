import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import cv2
#--------------------------------- M A I N      P A G E ---------------------------------------------------------

def getpath():
    
    path=imagepath.get()
    name1=name.get()
    print("Path: " + path)
    showinfo('Show','PREDICTION IS HAPPENING')
    #path= 'C:\Local Disk\ML Project\Machine Learning\MLetter.png'
    #print(path)
    return path

def twoline():
    path1= getpath()
    img = cv2.imread(path1)
    img_copy = img.copy()
    print (img_copy)


root =tk.Tk()
root.title("Home Page")
root.geometry("800x800")
root.minsize(400,400)
root.maxsize(600,600)
root.configure(background='LightSkyBlue')
w=tk.Label(root,text="Character Prediction",bg="blue3",fg="cyan2",width="20",height="2",font="Castellar 22   bold ",relief="raised",bd=15,highlightbackground="cyan")
w.pack(fill=tk.X,padx=50,pady=50)
name=StringVar()
imagepath= StringVar()

w=tk.Label(root, text="Name :",bg="LightSkyBlue",width="5",height="2",font="Algerian 15").place(x=120,y=250,width=110,height=50)
e1 = tk.Entry(root,textvariable=name)
e1.place(x=240,y=250,width=150,height=35)


w=tk.Label(root, text="ImagePath :",bg="LightSkyBlue",width="5",height="2",font="Algerian 15").place(x=80,y=300,width=180,height=50)
e1 = tk.Entry(root,textvariable=imagepath)
e1.place(x=240,y=300,width=150,height=35)


b1 =tk.Button(root,text=" Start Prediction ",bg="goldenrod2",fg="white",width="18",height="3",font="Algerian 11 bold",relief="raised",bd=5,command= twoline)
b1.place(x=200,y=400,width=200,height=50)
tk.mainloop()




