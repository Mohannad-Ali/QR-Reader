import cv2 
from tkinter import * 
from tkinter import messagebox 
from tkinter import filedialog 
import os 

window = Tk()  # function make window and store it in variable
window.geometry('350x450+500+100') #determine width height and x y
window.title('QR-Code Scanner') # change window name 
def open():
    file = filedialog.askopenfile(mode='r' , filetypes=[('Files','*.jpg') ,('Files','*.png')])
    if file :
        filepath = os.path.abspath(file.name)
        Ent1.insert(0,str(filepath))
def scan():
    d = Ent1.get() # image path 
    res = cv2.QRCodeDetector() # for handle QR Code
    val,points, s_qr =res.detectAndDecode(cv2.imread(d)) # read photo and decode 
    messagebox.showinfo('Qr-Scan',val) 

text = Label(window , text='QR Scanner',fg='white',bg='black') #make text label 
text.pack(fill=X) #put the text label in window

label1 = Label(window ,text='QR-Code Scanner' , font=('arial',12))
label1.place(x=100 , y=250) 
Ent1 = Entry(window , font=('arial',12),width=31 )
Ent1.place(x=15 , y=290)
btn = Button(window , text='Select Image' , fg='white' , bg='blue', width=35 , font=('arial' ,12),command=open)
btn.place(x=10,y=340)

btn1 = Button(window , text='Read QR Code' , fg='white' , bg='red', width=35 , font=('arial' ,12) , command=scan)
btn1.place(x=10,y=385)
window.mainloop() # function for run window
