# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:29:05 2023

@author: DELL
"""

import numpy as np
import cv2
def display(path_Update):
    img1=cv2.imread(path_Update,1)
    img1.shape
    cv2.imshow("*UPDATED IMAGE*",img1)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    
def zoom(img, zoom_factor):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)
    
def rgb_editing_bright(img):
    tuple_a=np.shape(img)
    for k in range(tuple_a[2]):
        for i in range(tuple_a[0]):
            for j in range(tuple_a[1]):
                if(img[i][j][k]<215):
                    #for bright we + for dark we -
                    img[i][j][k]+=40
                else:
                    img[i][j][k]=255
    string=input("Enter the path where you want to Save the file :") 
    path_Update=string.replace("\\",r"\\\\")              
    cv2.imwrite(path_Update,img)
    display(path_Update)
    
def rgb_editing_dark(img):
    tuple_a=np.shape(img)
    for k in range(tuple_a[2]):
        for i in range(tuple_a[0]):
            for j in range(tuple_a[1]):
                if(img[i][j][k]>=40):
                    #for bright we + for dark we -
                    img[i][j][k]-=40
                else:
                    img[i][j][k]=0
    string=input("Enter the path where you want to Save the file :") 
    path_Update=string.replace("\\",r"\\\\")              
    cv2.imwrite(path_Update,img)
    display(path_Update)
                
def rgb_black_editing_crop(img):
    tuple_a=np.shape(img)
    print("Displaying the image shape",tuple_a)
    x1_start=int(input("Enter the Row Start Index :"))
    x1_end=int(input("Enter the Row End Index :"))
    y1_start=int(input("Enter the Column Start Index :"))
    y1_end=int(input("Enter the Column End Index :"))
    crop_image = img[x1_start:x1_end, y1_start:y1_end]
    cv2.imshow("Cropped", crop_image)
    cv2.waitKey(2000) 
    cv2.destroyAllWindows() 
    string=input("Enter the path where you want to Save the file :") 
    path_Update=string.replace("\\",r"\\\\")              
    cv2.imwrite(path_Update,crop_image)
    display(path_Update)
                     
def black_editing_Bright(img):
    tuple_a=np.shape(img)
    for i in range(tuple_a[0]):
        for j in range(tuple_a[1]):
            if(img[i][j]<215):
                #for bright we + for dark we -
                img[i][j]+=40
            else:
                img[i][j]=255
    string=input("Enter the path where you want to Save the file :") 
    path_Update=string.replace("\\",r"\\\\")              
    cv2.imwrite(path_Update,img)
    display(path_Update)
    
def black_editing_Dark(img):
    tuple_a=np.shape(img)
    for i in range(tuple_a[0]):
        for j in range(tuple_a[1]):
            if(img[i][j]>=40):
                #for bright we + for dark we -
                img[i][j]-=40
            else:
                img[i][j]=0
    string=input("Enter the path where you want to Save the file :") 
    path_Update=string.replace("\\",r"\\\\")              
    cv2.imwrite(path_Update,img)
    display(path_Update)

def rgb_black_editing_zoom(img):
    r=float(input("Enter the zoom in terms of times of zoom :"))
    zoomed = zoom(img, r)
    cv2.imshow("Zoomed Image", zoomed)
    cv2.waitKey(5000) 
    cv2.destroyAllWindows() 

print("PROGRAM : IMAGE EDITING AUTOMATED PYTHON TOOL")
print("Enter the Choice for Type of image You want to edit")
a=int(input("Enter 1:Black 2:RGB\n"))
if(a==1):
    string=input("Enter the Path of image From your desktop :")
    path_Updated=string.replace("\\",r"\\\\")
    img=cv2.imread(path_Updated,0)
    img.shape
    cv2.imshow("windows name",img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    b=int(input("Enter\n1: Bright\n2: Dark\n3: Crop\n4: Zoom\n"))
    if(b==1):
        black_editing_Bright(img)
    elif(b==2):
        black_editing_Dark(img)
    elif(b==3):
        rgb_black_editing_crop(img)
    elif(b==4):
        rgb_black_editing_zoom(img)
    else:
        print("WRONG CHOICE")
        
elif(a==2):
    string=input("Enter the Path of image From your desktop :")
    path_Updated=string.replace("\\",r"\\\\")
    img=cv2.imread(path_Updated,1)
    img.shape
    cv2.imshow("windows name",img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    b=int(input("Enter\n1: Bright\n2: Dark\n3: Crop\n4: Zoom\n"))
    if(b==1):
        rgb_editing_bright(img)
    elif(b==2):
        rgb_editing_dark(img)
    elif(b==3):
        rgb_black_editing_crop(img)
    elif(b==4):
        rgb_black_editing_zoom(img)
    else:
        print("WRONG CHOICE")
else:
    print("WRONG CHOICE")