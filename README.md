# QR_DM_Decoder

This file demonstrate how to create QR code and Data Matrix decoders using Python

##Setup

pyzbar is a bult-in QR code decoding package for Python
pylibdmtx is a bult-in Data Matrix decoding package for Python

'''bash
pip install pyzbar
pip install pyzbar[scripts]
pip install pylibdmtx
pip install pylibdmtx[scripts]
'''

On Window Power Shell

'''powershell
py -3 -m pip install pyzbar
py -3 -m pip install pyzbar[scripts]
py -3 -m pip install pylibdmtx
py -3 -m pip install pylibdmtx[scripts]
'''

##Functions

Example functions to generate output strings
Feel free to process the image using OpenCV. 
Noted that long processing technique may not benifits its overall performance.

'''python
qr_str = qr_reader(image_file_path) prints and return the decoded output string from QR code
dm_str = dm_reader(image_file_path) prints and return the decoded output string from Data Matrix
'''
