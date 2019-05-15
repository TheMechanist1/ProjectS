from Tkinter import *
import tkFileDialog
import PIL
import PIL.ImageDraw

import PIL.ImageFont

import PIL.ImageTk
import os
import numpy

root = Tk()
root.geometry("1000x1000")
frame = Frame(root)
buttonList = []
imgList = []
pImgList = []



def render(list):
    y = 0
    for index, img in enumerate(list):
        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype('K:\\EngineerTech\\AP Comp Science Principals\\14KeithA\\22Cooksleyd\\ProjectS\\Roboto-Bold.ttf', size=10)
        color = 'RGBA(255, 255, 255, 255)'
        draw.text((25, 25), "Cooksley Co.", fill=color, font=font)
        pi = PIL.ImageTk.PhotoImage(img)
        pImgList.append(pi)
        if(img.width*index > 1000):
            y += 100
            
        canvas.create_image((img.width/2 + index*img.width, img.height/2 + y),image=pi)

    canvas.update()

def file():
    #ask for the directory
    #Todo: remove the path before you deploy
    directory = tkFileDialog.askdirectory(initialdir="K:\\EngineerTech\\AP Comp Science Principals\\14KeithA\\22CooksleyD\\pics")
    
    #list all files in the directory
    files = os.listdir(directory)
    
    #Get the full path of the images. ex "img1.png" to "c:/users/22cooksleyd/pictures/img1.png"
    neatPath = [os.path.join(directory, i) for i in files]
    
    #go through all the files in the directory
    for paths in neatPath:
        try:

            imgList.append(PIL.Image.open(paths).resize((100, 100)).convert('RGBA'))

            
            #ignore the file if its not an image
        except IOError:
            continue

    #add all the images in imgList into the canvas and then update the canvas so they show up
    render(imgList)

def negate():
    i = 0
    for img in imgList:
        colors = numpy.asarray(img)
        
        for col in colors:
            for color in col:
                color[0] *= .5

        imgs = PIL.Image.fromarray(numpy.uint8(colors))
        imgList[i] = imgs
        i = i + 1
    render(imgList)
#make the canvas and button
canvas = Canvas(root, width = 1000, height = 1000)
buttonList.append(Button(root, text="Chose File", command=file))
buttonList.append(Button(root, text="Negative", command=negate))


#Init the button before the canvas so it shows up above the canvas
for button in buttonList:
    button.pack()
    


canvas.pack() 
#start the program
root.mainloop()
