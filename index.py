from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
import sys
from stegano import lsb  

window=Tk()
window.title("Steganography - Hide a Secret Text Message in an Image")
window.geometry("900x550+250+80")
window.resizable(False,False)
window.configure(bg="#FFE5B4")

def resolve_path(path):
    if getattr(sys, "frozen", False):
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
    else:
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path

 
def showimage():
	global filename
	filename = filedialog.askopenfilename(initialdir = os.getcwd(), title= 'Select Image File', filetype= (("PNG file","*.png"), ("JPG file", "*.jpg"), ("All file", "*.txt")))
	img = Image.open(filename)
	img =  ImageTk.PhotoImage(img)
	lbl.configure(image= img, width= 250, height = 250)
	lbl.image = img					


def Hide():
	global secret
	message=text1.get(1.0, END)
	secret = lsb.hide(str(filename), message)

def Show():
	clear_message = lsb.reveal(filename)
	text1.delete(1.0, END )
	text1.insert(END, clear_message)

def save():
	secret.save("hidden.png")

#icon
image_icon=PhotoImage(file=resolve_path("logo.jpg"))
window.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file=resolve_path("logo.png"))
#Label(window,text=logo,bg="#2f4155").place(x=10,y=0)
Label(window,text="IMAGE STEGANOGRAPHY",bg="#FFE5B4",fg="#4b2782",font="Cambria 25 bold").place(x=260,y=15)

#first frame
f= Frame(window, bd=3, bg= "black", width = 400, height= 280, relief = GROOVE)
f.place(x=30, y = 80)

lbl = Label (f, bg="black")
lbl.place(x=40, y=10)

#Second Frame
frame2= Frame(window, bd=3,width =400, height= 280, bg="white", relief=GROOVE)
frame2.place(x=470, y=80)

text1 = Text(frame2, font = "Robote 20", bg= "white", fg= "black", relief = GROOVE, wrap = WORD)
text1.place(x=0, y=0, width = 400, height = 295)

scrollbar1= Scrollbar(frame2)
scrollbar1.place(x= 400, y=0, height = 300)

scrollbar1.configure(command= text1.yview)
text1.configure(yscrollcommand= scrollbar1.set)

# third frame

frame3= Frame(window, bd=3, bg= "#2f4155", width= 400, height = 100,relief = GROOVE)
frame3.place(x=30, y= 400)

Button(frame3, text= "Open Image", width = 13, height = 2, font = "arial 14 bold", command =showimage).place(x=20, y = 30)
Button(frame3, text= "Save Image", width = 13, height = 2, font = "arial 14 bold", command = save).place(x=220, y = 30)

Label(frame3, text="Picture, Image, Photo File", bg = "#2f4155", fg = "yellow").place(x=20 ,y= 5)

# fourth frame

frame4= Frame(window, bd=3, bg= "#2f4155", width= 400, height = 100,relief = GROOVE)
frame4.place(x=470, y= 400)

Button(frame4, text= "Hide Data", width = 13, height = 2, font = "arial 14 bold", command = Hide).place(x=20, y = 30)
Button(frame4, text= "Show Data", width = 13, height = 2, font = "arial 14 bold", command = Show ).place(x=220, y = 30)

Label(frame4, text="Picture, Image, Photo File", bg = "#2f4155", fg = "yellow").place(x=20 ,y= 5)

window.mainloop()