import cv2
from imutils import rotate
from pyzbar.pyzbar import decode

def decode_img(img):
    bar_type = None
    bar_code = None
    decode_objects = decode(img)
    if not decode_objects:
        return None, None, None
    for obj in decode_objects:
        img = draw_barcode(obj, img)
        bar_type = obj.type
        bar_code = obj.data

    return img, bar_type, bar_code
        
def draw_barcode(decoded, img):
    img = cv2.rectangle(img, (decoded.rect.left, decoded.rect.top),
                        (decoded.rect.left+decoded.rect.width,
                         decoded.rect.top + decoded.rect.height),
                        color=(0,255,0),
                        thickness=5)
    return img

def rotate_img(img):
    rot = rotate(img, angle=-1)
    return rot

def show_img(ip_cam=None):
    video = cv2.VideoCapture()
    video.open(ip_cam)
    while True:
        check, img = video.read()
        img_, bar_type, bar_code = None, None, None
        i=0
        while img_ is None and i < 180:
            img_, bar_type, bar_code = decode_img(img)
            img = rotate_img(img)
            i+=1
        if bar_code is not None:    
            return bar_type, bar_code      
if __name__ == "__main__":
    ip = 'https://192.168.1.7:8080/video'
    bar_type, bar_code = show_img(ip)
    print(bar_type, bar_code)
