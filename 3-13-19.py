from Tkinter import *
import tkFileDialog
import PIL
import PIL.ImageDraw

import PIL.ImageFont

import PIL.ImageTk
import os

root = Tk()
root.geometry("1000x1000")
frame = Frame(root)
buttonList = []
imgList = []
pImgList = []





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
    for index, img in enumerate(imgList):

        draw = PIL.ImageDraw.Draw(img)
        font = PIL.ImageFont.truetype('K:\\EngineerTech\\AP Comp Science Principals\\14KeithA\\21AbbeE\\ProjectS\\Roboto-Bold.ttf', size=30)
        color = 'RGBA(255, 0, 0, 100)'
        draw.text((0, 0), ":)", fill=color, font=font)
        pi = PIL.ImageTk.PhotoImage(img)
        pImgList.append(pi)
        canvas.create_image((img.width/2 + index*img.width, img.height/2),image=pi)

    canvas.update()

#make the canvas and button
canvas = Canvas(root, width = 1000, height = 1000)
buttonList.append(Button(root, text="Chose File", command=file))

#Create a rectangle for the buttons to go in
canvas.create_rectangle(0, 0, 75, 700, fill="#476042")


#Init the button before the canvas so it shows up above the canvas
for button in buttonList:
    button.pack()
    
canvas.pack() 


root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill =Y)
mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
    mylist .insert(END, "This is line number" +str (line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar .config( command = mylist.yview )

mainloop()
canvas.update()

#start the program
root.mainloop()
