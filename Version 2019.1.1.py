from PIL import Image, ImageChops, ImageFilter
import cv2
import numpy as np
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import PIL.Image
import PIL.ImageTk
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfilename


# ____________________________________________________________________

imagelink1 = None
imagelink1 = lambda: askopenfilename()

def openlink1():
    imagelink1 = askopenfilename()

def openlink2():
    imagelink2 = askopenfilename()


def diff1():

    #Opening Images
    img1 = Image.open(imagelink1)
    img2 = Image.open(imagelink2)

    #Subtracting Images
    diff1 = ImageChops.subtract(img1, img2)

    #Saving the subtraction
    diff1.save('diff1.png')
    
    #Opening subtraction image
    diff1 = Image.open("diff1.png")
    diff1.show()

def edges():
    img1 = Image.open(imagelink1)
    img2 = Image.open(imagelink2)

    #Subtracting Images
    diff1 = ImageChops.subtract(img1, img2)

    #Saving the subtraction
    diff1.save('diff1.png')
    
    #Finding the edges by setting edge parameters
    img = cv2.imread('diff1.png', 0)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite('edges_of_image.png', edges)


    
# _______________________________________________________________

#Running function


#Setting geeral settings of tkinter window
window = Tk()
window.title("Robin-15")
window.attributes("-fullscreen", True)
window.configure(bg = "#FBFBFB")

#Creating Title
Product_Title = Label(window, text = "Robin 15", font = "helvetica 40", bg = "#FBFBFB", )
Product_Title.pack()

#Creating Space
space1 = Label(window, text = "", font = "helvetica 60", bg = "#FBFBFB", )
space1.pack()

#Creating button
Difference_Button = Button(window, text = "Difference", bg = "#F36F17", fg = "#FFFFFF",
           font = "helvetica 20", relief = 'flat', width = "15",
           command = lambda: diff1())
Difference_Button.pack()

#Creating Space
space2 = Label(window, text = "", font = "helvetica 20", bg = "#FBFBFB", )
space2.pack()

#Creating Button
Edges_Button = Button(window, text = "Edges", bg = "#F36F17", fg = "#FFFFFF",
           relief = 'flat', font = "helvetica 20", width = "15",
           command = lambda: edges())
Edges_Button.pack()

#Creating Space
space3 = Label(window, text = "", font = "helvetica 120", bg = "#FBFBFB", )
space3.pack()

#Creating Button
Picture_Select_1_Button = Button(window, text = "Select Original Image", bg = "#F36F17", fg = "#FFFFFF",
           font = "helvetica 20", relief = 'flat', width = "15",
           command = lambda: openlink1())
Picture_Select_1_Button.pack()

#Creating Space
space4 = Label(window, text = "", font = "helvetica 20", bg = "#FBFBFB", )
space4.pack()

#Creating Button
Picture_Select_2_Button = Button(window, text = "Select Changed Image", bg = "#F36F17", fg = "#FFFFFF",
           font = "helvetica 20", relief = 'flat', width = "15",
           command = lambda: openlink2())
Picture_Select_2_Button.pack()


    
