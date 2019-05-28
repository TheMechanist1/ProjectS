from tkinter import *
from tkinter import filedialog
import PIL
import PIL.ImageDraw

import PIL.ImageFont

import PIL.ImageTk
import os
import numpy
import math

root = Tk()
root.geometry("1000x1000")
frame = Frame(root)
buttonList = []
imgList = []
pImgList = []
width = 300
height = 300
red = Scale(root, from_=0, to=255, orient=HORIZONTAL)
green = Scale(root, from_=0, to=255, orient=HORIZONTAL)
blue = Scale(root, from_=0, to=255, orient=HORIZONTAL)
help(red)
red.pack()
green.pack()
blue.pack()

def render(list):
    y = 0
    x = 0
    otherIndex = 0
    for index, img in enumerate(list):
        draw = PIL.ImageDraw.Draw(img)
        # font = PIL.ImageFont.truetype('Roboto-Bold.ttf', size=10)
        color = 'RGBA(255, 255, 255, 255)'
        # draw.text((25, 25), "Cooksley Co.", fill=color, font=font)
        pi = PIL.ImageTk.PhotoImage(img)
        pImgList.append(pi)
        if(otherIndex*img.width >= 1000):
            y += img.height
            otherIndex = 0
            x = 0
        else:
            x = otherIndex*img.width
        otherIndex += 1

        canvas.create_image((img.width/2 + x, img.height/2 + y),image=pi)

    canvas.update()

def file():
    #ask for the directory
    #Todo: remove the path before you deploy
    directory = filedialog.askdirectory(initialdir="c:\\users\\22cooksleyd\\pictures\\")
    
    #list all files in the directory
    files = os.listdir(directory)
    
    #Get the full path of the images. ex "img1.png" to "c:/users/22cooksleyd/pictures/img1.png"
    neatPath = [os.path.join(directory, i) for i in files]
    
    #go through all the files in the directory
    for paths in neatPath:
        try:

            imgList.append(PIL.Image.open(paths).resize((width, height)).convert('RGBA'))

            
            #ignore the file if its not an image
        except IOError:
            continue

    #add all the images in imgList into the canvas and then update the canvas so they show up
    render(imgList)

def swirlPic():
    i = 0
    x = 0
    y = 0
    for img in imgList:

       
        for y in range(img.height):
            for x in range(img.width):
                pixelX = x - img.width/2
                pixelY = y - img.height/2
                pixelDistance = math.sqrt((pixelX * pixelX) + (pixelY * pixelY))
                pixelAngle = math.atan2(pixelY, pixelX)

                # work out how much of a swirl to apply (1.0 in the center fading out to 0.0 at the radius):
                swirlAmount = 1.0 - (pixelDistance / 150)
                # print(str(pixelDistance) + " " + str(swirlAmount))
                if(swirlAmount > 0):
                    twistAngle = 1 * swirlAmount * math.pi
                    #  adjust the pixel angle and compute the adjusted pixel co-ordinates:
                    pixelAngle += twistAngle
                    pixelX = math.cos(pixelAngle) * pixelDistance
                    pixelY = math.sin(pixelAngle) * pixelDistance
                
                # read and write the pixel
                img.putpixel((x, y), img.getpixel((img.width/2 + pixelX, img.height/2 + pixelY)))

                # offsetx = int(30.0 * math.sin(2 * 3.14 * x / 150))
                # offsety = int(30.0 * math.cos(2 * 3.14 * y / 150))
                # if x+offsety < img.width and y+offsetx < img.height:
                #     img.putpixel((x, y), img.getpixel(((x+offsety)%img.width,(y+offsetx)%img.height)))
                # else:
                #     img.putpixel((x, y), (0, 0, 0, 255))
                

        # colors = numpy.asarray(img)
        # result = []
        # co = 0
        # for y in colors:
        #     r = []
        #     row = 0
        #     for x in y:
        #         c = list(x)
        #         c[0] = colors[int(abs(math.sin(co)*5))][int(abs(math.sin(row)*5))][0]
        #         c[1] = colors[int(abs(math.sin(co)*5))][int(abs(math.sin(row)*5))][1]
        #         c[2] = colors[int(abs(math.sin(co)*5))][int(abs(math.sin(row)*5))][2]
        #         r.append(c)
        #         row += 1
        #     result.append(r)
        #     co += 1
        # imgs = PIL.Image.fromarray(numpy.uint8(result))
        # imgList[i] = imgs

        i = i + 1

    render(imgList)
    
def brighten():
    i = 0
    x = 0
    y = 0
    for img in imgList:

       #multiply the colors by 2 to brighten the img
        for y in range(img.height):
            for x in range(img.width):
                # read and write the pixel
                r = img.getpixel((x,y))[0]
                g = img.getpixel((x,y))[1]
                b = img.getpixel((x,y))[2]
                r *= 2
                g *= 2
                b *= 2
                img.putpixel((x, y), (r, g, b))

        i = i + 1

    render(imgList)
    
def paint( event ):
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   canvas.create_oval( x1, y1, x2, y2, fill = python_green )

#make the canvas and buttons
canvas = Canvas(root, width = 1000, height = 1000)
choseFile = Button(root, text="Chose File", command=file)
swirl = Button(root, text="Swirl", command=swirlPic)
brighten = Button(root, text="brighten", command=brighten)
buttonList.append(choseFile)
buttonList.append(swirl)
buttonList.append(brighten)


#Init the button before the canvas so it shows up above the canvas
for button in buttonList:
    button.pack()
    
canvas.bind( "<B1-Motion>", paint )

canvas.pack(expand = YES, fill = BOTH) 
#start the program
root.mainloop()
