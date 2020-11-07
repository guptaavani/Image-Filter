#! /usr/bin/env python3
from PIL import Image
im=Image.open(input("Enter image path \n")) #Taking the image path as input and saving it to im
print("This is the original image you entered \n")
im.show() #Showing the original image
while(True):
    n=int(input(" Enter 1 for black and white filter \n Enter 2 for magic filter \n Enter 3 for colour filter \n Enter 4 to exit \n"))
    if (n==1):
        img=im.convert('1') #Conver the image into black and white image
    if (n==2):
        r, g, b = im.split()
        img=Image.merge("RGB", (b,r,g)) #Reverse the r,g,b values
    if (n==3):
        colour=input("Enter valid colour \n")
        f=Image.new("RGB", im.size, colour) #Creating a filter of the entered colour
        img=Image.blend(im, f, 0.25) #Applying the filter to the image
    if (n==4): break #Exit the while loop
    img.show() #Showing the image