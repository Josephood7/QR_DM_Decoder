#!/usr/bin/env python
# coding: utf-8
#import numpy as np
from pyzbar.pyzbar import decode as qr_decode
import cv2 as cv
from pylibdmtx.pylibdmtx import decode as dm_decode
import matplotlib.pyplot as plt

def qr_reader(image):
    
    # read image in numpy array
    img = cv.imread(image)
    # detect multi barcode in the ig (detected barcode)
    dct_qr = qr_decode(img)
    
    if not dct_qr:
        print("QR code not detected in the image")
    else:
        for qr in dct_qr:
            (x, y, w, h) = qr.rect    # locate barcode position
            cv.rectangle(img, (x-10, y-10), (x+(w+10), y+(h+10)), (255, 0, 0), 2)    # highlight and enhance barcode in the image
                             # (image, start_point, end_point, color, thickness)
            if qr.data != "":
                print(f"Quick Response Code: {qr.data.decode('utf-8')}")
        im = img[:,:,::-1]
        plt.imshow(im)
        plt.show

def dm_reader(image):
    global error 
    img = cv.imread(image)
    N = 60
    dct_dm = dm_decode(img)
    
    if not dct_dm:
        error = True
        print("Data matrix not detected in the image")
    else:
        error = False
        
        for dm in dct_dm:
            (x, y, w, h) = dm.rect    # locate barcode position
            cv.rectangle(img, (x-10, y-10), (x+(w+10), y+(h+10)), (255, 0, 0), 2)    # highlight and enhance barcode in the image
                             # (image, start_point, end_point, color, thickness)
            if dm.data != "":
                print(f"Data Matrix: {dm.data.decode('utf-8')}")
                break
        im = img[:,:,::-1]
        plt.imshow(im)
        plt.show

if __name__ == "__main__":
    qr_reader("qr.png")
    dm_reader("dm.png")