from PIL import Image, ImageChops, ImageFilter
import cv2
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
import PIL.Image
import PIL.ImageTk
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk

# ____________________________________________________________________



def diff_images():

    #Opening Images
    img1 = Image.open('Picture1.1.jpg')
    img2 = Image.open('Picture1.2.jpg')

    #Subtracting Images
    diff1 = ImageChops.subtract(img1, img2)

    #Saving the subtraction
    diff1.save('diff1.png')

    #Finding image parameters
    width, height = img1.size

    #Finding the number of black pixels in the subtraction
    diff1 = cv2.imread('diff1.png', cv2.IMREAD_GRAYSCALE)
    n_black_pix = np.sum(diff1 == 0)
    print(width * height)
    print(n_black_pix)
    other_pixels = int(width * height - n_black_pix)

    #Subtracting that from the total amount of pixels
    print(other_pixels)
    hole_size = int(other_pixels / 10000)

    #Ranges of hole
    if hole_size >= 100:
      print("RED ALERT - Life threatning")
    if 100 > hole_size >= 50:
      print("YELLOW ALERT - Major Cut")
    if hole_size < 50:
      print("GREEN ALERT - Minor cut")

    #Finding the edges by setting edge parameters
    img = cv2.imread('diff1.png', 0)
    edges = cv2.Canny(img, 100, 200)
    cv2.imwrite('edges of image.png', edges)


def diff1():
    #Opening subtraction image
    diff1 = Image.open("diff1.png")
    diff1.show()

def edges():
    #Opening subtraction image
    edges = Image.open('edges of image.png')
    edges.show()

def image_selection():
    #selcting the image wanted
    window.directory = filedialog.askdirectory()
    print(window.directory)

    
# _______________________________________________________________

#Running function
diff_images()

#Setting geeral settings of tkinter window
window = Tk()
window.title("Robin-15")
window.attributes("-fullscreen", True)
window.configure(bg = "#FBFBFB")

#Creating Title
Product_Title = Label(window, text = "Robin-15", font = "helvetica 40", bg = "#FBFBFB", )
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
           command = lambda: image_selection())
Picture_Select_1_Button.pack()

#Creating Space
space4 = Label(window, text = "", font = "helvetica 20", bg = "#FBFBFB", )
space4.pack()

#Creating Button
Picture_Select_2_Button = Button(window, text = "Select Original Image", bg = "#F36F17", fg = "#FFFFFF",
           font = "helvetica 20", relief = 'flat', width = "15",
           command = lambda: image_selection())
Picture_Select_2_Button.pack()


    
