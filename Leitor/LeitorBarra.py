import cv2
from pyzbar.pyzbar import decode

def BarcodeReader(image):     
    bar_code = None
    bar_type = None
    detectedBarcodes = decode(image) 
       
    
    if detectedBarcodes:    
      for barcode in detectedBarcodes:   
        # (x, y, w, h) = barcode.rect 
        # cv2.rectangle(image, (x-10, y-10), 
        #             (x + w+10, y + h+10),  
        #             (255, 0, 0), 2) 
        bar_code = barcode.data
        bar_type = barcode.type
        
                  
    
    return bar_type, bar_code

def show_img(ip_cam=None):
    if ip_cam is not None:
        video = cv2.VideoCapture()
        video.open(ip_cam)
        while True:
            check, img = video.read()
            bar_type, bar_code = BarcodeReader(img)
            if bar_code is not None and bar_type == 'EAN13' :
                return bar_code
    return None



