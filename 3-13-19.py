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
pImgList = []

canvas = Canvas(root, width = 1000, height = 500)
canvas.pack() 

def file():
    
    directory = tkFileDialog.askdirectory()
    files = os.listdir(directory)
    neatPath = [os.path.join(directory, i) for i in files]
    
    for paths in neatPath:
        try:
            imgList.append(PIL.Image.open(paths).resize((100, 100)))
        except IOError:
            continue

    for index, img in enumerate(imgList):
        pi = PIL.ImageTk.PhotoImage(img)
        pImgList.append(pi)
        canvas.create_image((img.width/2 + index*100, img.height/2),image=pi)
    canvas.update()

b = Button(root, text="Chose File", command=file)
b.pack()

     
root.mainloop()
