import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/home/smsc/Downloads/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe"
img = cv2.imread("img_read.jpg")
text = pytesseract.image_to_string(img)
print(text)
