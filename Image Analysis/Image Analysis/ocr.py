
import easyocr 
import re 
from ar_corrector.corrector import Corrector
from ArabicOcr import arabicocr
import arabic_reshaper
from bidi.algorithm import get_display
import cv2

def OCR1(myImage):
    print("i am  here")
    reader = easyocr.Reader(['en','ar'])
    correct = Corrector()
    text=""
    image = reader.readtext(myImage)
    f = open("output.txt", "w" ,encoding='utf-8')
    for  result in image :
      text = text +'\n' + result[1]+' '
    f.writelines(text)
    f.close
    return text

def OCR2(imageName)  :
  image_path=imageName
  out_image='out'+imageName
  results=arabicocr.arabic_ocr(image_path,out_image)
  print(results)
  words=[]
  for i in range(len(results)):	
             word=results[i][1]
             words.append(word)
  with open ('file.txt','w',encoding='utf-8')as myfile:
   myfile.write(str(words))

  #img = cv2.imread('out.jpg', cv2.IMREAD_UNCHANGED)
  #cv2.imshow("arabic ocr",img)
  #cv2.waitKey(0)
  return words





    