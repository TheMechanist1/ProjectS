from Tkinter import *
import tkFileDialog
import PIL
import PIL.ImageDraw
import PIL.ImageTk
import os



root = Tk()
root.geometry("1000x1000")
frame = Frame(root)
imgList = []

canvas = Canvas(root, width = 500, height = 500)
canvas.pack() 

def file():
    files = tkFileDialog.askopenfiles()
    for i in files:
        imgList.append(i)
        
    
    img = PIL.Image.open(root.filename).resize((100, 100))
    
    pi = PIL.ImageTk.PhotoImage(img)
    
    canvas.create_image((img.width/2 ,img.height/2),image=pi)
    PIL.ImageDraw.Draw(pi)

b = Button(root, text="Chose File", command=file)
b.pack()

     
root.mainloop()