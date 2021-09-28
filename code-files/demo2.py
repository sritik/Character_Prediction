import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import cv2 
from tkinter import filedialog

LOOP_ACTIVE = True
while LOOP_ACTIVE:
    
    USER_INPUT = input("Give me your command! Just type \"exit\" to close: ")
    if USER_INPUT == "exit":
        root.quit()
        LOOP_ACTIVE = False
    else:
        import cv2
        root =tk.Tk()
        root.title("Home Page")
        root.geometry("800x800")
        root.minsize(400,400)
        root.maxsize(600,600)
        root.configure(background='LightSkyBlue')
        w=tk.Label(root,text="Character Prediction",bg="blue3",fg="cyan2",width="20",height="2",font="Castellar 22   bold ",relief="raised",bd=15,highlightbackground="cyan")
        w.pack(fill=tk.X,padx=50,pady=50)
        imagepath= StringVar()
        w=tk.Label(root, text="ImagePath :",bg="LightSkyBlue",width="5",height="2",font="Algerian 15").place(x=80,y=200,width=180,height=50)
        e1 = tk.Entry(root,textvariable=imagepath)
        e1.place(x=240,y=200,width=150,height=35)

        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Images files","*.png*"),("all files","*.*")))
            return filename
        

        def getpath():
            p=browseFiles()
            #path=filename.get()
            showinfo('Show','PREDICTION IS HAPPENING')
            return p
            


        def twoline():
            path1= getpath()
            img = cv2.imread(path1)
            img_copy = img.copy()
            print (img_copy)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (400,440))

            img_copy = cv2.GaussianBlur(img_copy, (7,7), 0)
            img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
            _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

            img_final = cv2.resize(img_thresh, (28,28))
            img_final =np.reshape(img_final, (1,28,28,1))


            img_pred = word_dict[np.argmax(model.predict(img_final))]

            cv2.putText(img, "Machine Learning _ _ _ ", (20,25), cv2.FONT_HERSHEY_TRIPLEX, 0.7, color = (0,0,230))
            cv2.putText(img, "Prediction: " + img_pred, (20,410), cv2.FONT_HERSHEY_DUPLEX, 1.3, color = (255,0,30))
            cv2.imshow('character prediction _ _ _ ', img)


            while (1):
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    break
            cv2.destroyAllWindows()
            
        
        
        btn2 =tk.Button(root,text=" Start Prediction ",bg="goldenrod2",fg="white",width="18",height="3",font="Algerian 11 bold",relief="raised",bd=5,command= twoline)
        btn2.place(x=200,y=300,width=200,height=50)
        tk.mainloop()
