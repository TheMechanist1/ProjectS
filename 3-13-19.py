from Tkinter import *
import tkFileDialog
import PIL
import PIL.ImageDraw
import PIL.ImageTk
import os



root = Tk()
root.geometry("500x500")
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
frame = Frame(root)

canvas = Canvas(root, width = 300, height = 300)      
canvas.pack() 

def file():
    root.filename = tkFileDialog.askopenfilename()
    img = PIL.Image.open(root.filename)
    pi = ImageTk.PhotoImage(img)
    canvas.create_image((1,1),image=pi)
    # canvas.create_image(20,20,image=img)
    # PIL.ImageDraw.Draw(img)

b = Button(root, text="OK", command=file)
b.pack()

     
root.mainloop()