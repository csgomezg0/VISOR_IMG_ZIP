import zipfile
#from StringIO import StringIO
from PIL import Image
import imghdr
import io
import zipfile
import os
import random 
from tkinter import messagebox

# lista de imagenes en el zip
zip_file=r"C:\Users\STEVENS\Documents\PROYECTOS\VISOR_IMG_ZIP-main\shut.zip"
#zsip_file=r"C:\Users\STEVENS\Documents\PROYECTOS\VISOR_IMG_ZIP-main\ZZNueva carpeta.zip"

z = zipfile.ZipFile(zip_file)
# lista
imgzip = zipfile.ZipFile(zip_file)
inflist = imgzip.infolist()

# elegir img aleatoria 
files=inflist









#Import the required library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
#Create an instance of tkinter frame
win= Tk()

#Set the geometry
#wid_=1280
#heg_=720
wid_=int(1280)#*1.1)
heg_=int(900)#*1.1)### this is the value that matters


str_aux=str(wid_)+'x'+str(heg_)
win.geometry('1280x960')



### number over list
num_next_global=random.randint(0, len(files))
d=files[num_next_global]
### abrir imagen
ifile = imgzip.open(d)
imgxs = Image.open(ifile)

print(num_next_global)







##ACCIONES
#Define function to update the image
def update_back():
    global num_next_global
    num_next=random.randint(0, len(files))
    d=files[num_next_global-1]
    ### abrir imagen
    ifile = imgzip.open(d)
    imgxs = Image.open(ifile)
    #size img
    imgxs.thumbnail((wid_,heg_))
    #load image
    img2 = ImageTk.PhotoImage(imgxs)
    num_next_global=num_next_global-1
    print(num_next_global)
    print(d)
    canvas.itemconfig(image_container,image=img2)
    canvas.image = img2




def update_next():
    global num_next_global
    num_next=random.randint(0, len(files))
    d=files[num_next_global+1]
    ### abrir imagen
    ifile = imgzip.open(d)
    imgxs = Image.open(ifile)
    #size img
    imgxs.thumbnail((wid_,heg_))
    #load image
    img2 = ImageTk.PhotoImage(imgxs)
    num_next_global=num_next_global+1
    print(num_next_global)
    print(d)
    canvas.itemconfig(image_container,image=img2)
    canvas.image = img2


def update_random():
    global num_next_global
    num_next=random.randint(0, len(files))
    d=files[num_next]
    ### abrir imagen
    ifile = imgzip.open(d)
    imgxs = Image.open(ifile)
    #size img
    imgxs.thumbnail((wid_,heg_))
    #load image
    img2 = ImageTk.PhotoImage(imgxs)
    num_next_global=num_next
    print(num_next_global)
    print(d)
    canvas.itemconfig(image_container,image=img2)
    canvas.image = img2





running = False

# Define a function to print the text in a loop
def print_text():
   if running:
    global num_next_global
    num_next=random.randint(0, len(files))
    d=files[num_next]
    ### abrir imagen
    ifile = imgzip.open(d)
    imgxs = Image.open(ifile)
    #size img
    imgxs.thumbnail((wid_,heg_))
    #load image
    img2 = ImageTk.PhotoImage(imgxs)
    num_next_global=num_next
    print(num_next_global)
    print(d)
    canvas.itemconfig(image_container,image=img2)
    canvas.image = img2

   win.after(10000, print_text)

# Define a function to start the loop
def on_start():
   global running
   running = True


# Define a function to stop the loop
def on_stop():
   global running
   running = False

#Create a canvas and add the image into it
canvas= Canvas(win, width=wid_, height= heg_)
canvas.pack()

Pos_x=0.1
dist_Button=0.1
Posy=0.965
##### BOTONES
#Create a button to update the canvas image
back_button= Button ( win, text ="back",command=lambda:update_back())
back_button.pack()
back_button.place(relx=Pos_x, rely=Posy, anchor=CENTER)
#back_button.pack(side=RIGHT)

next_button= Button ( win, text ="next",command=lambda:update_next())
#button= ttk.Button(win, text="next",command=lambda:update_next())
next_button.pack()
next_button.place(relx=Pos_x+dist_Button+0.005, rely=Posy, anchor=CENTER)
Pos_x=Pos_x+dist_Button+0.005



random_button = Button ( win, text ="random",command=lambda:update_random())
random_button.pack()
random_button.place(relx=Pos_x+dist_Button, rely=Posy, anchor=CENTER)
Pos_x=Pos_x+dist_Button



# Add a Button to start/stop the loop
start = Button(win, text="Start_random_each_time", command=on_start)
start.pack(padx=10)
start.place(relx=Pos_x+dist_Button, rely=Posy, anchor=CENTER)
Pos_x=Pos_x+dist_Button



stop = Button(win, text="Stop_random_time", command=on_stop, anchor=CENTER)
stop.pack(padx=10)
stop.place(relx=Pos_x+dist_Button, rely=Posy, anchor=CENTER)


# Run a function to print text in window
win.after(1000, print_text)












#Open an Image in a Variable  #abrir imagen
from PIL import ImageTk, Image
img1 = ImageTk.PhotoImage(imgxs)

#img1= PhotoImage(file="logo.png")

#img2= PhotoImage(file="logo2.png")
#img3= PhotoImage(file="logo3.png")



wid_=imgxs.size[0]
heig_=imgxs.size[1]

#Add image to the canvas
image_container =canvas.create_image(0,0, anchor="nw",image=img1)
win.mainloop()

