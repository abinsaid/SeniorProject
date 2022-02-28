import cv2
import numpy as np
import requests
import io
import json
def ocrAPI():

 img = cv2.imread(r"C:\Users\Ammar\Desktop\test\Image Analysis\images\66.jpg")
 print("ddddddddddddddddddddddddddd")
 print(img)
 height, width, _ = img.shape


# Cutting image
# roi = img[0: height, 400: width]
 roi = img

# Ocr
 url_api = "https://api.ocr.space/parse/image"
 _, compressedimage = cv2.imencode(".jpg", roi, [1000, 1000])
 file_bytes = io.BytesIO(compressedimage)

 result = requests.post(url_api,
              files = {"screenshot.jpg": file_bytes},
              data = {"apikey": "K84306774188957",
                      "language": "ara",
                      #"language": "eng",
                       "OCREngine": "1" ,
                        "scale":"true"                
                        })
                      

 result = result.content.decode()
 result = json.loads(result)

 parsed_results = result.get("ParsedResults")[0]
 text_detected = parsed_results.get("ParsedText")
 x= parsed_results.get("TextOverlay")
 #x.sho

 print(text_detected)
 print("====================================================")
 arrayText = text_detected.splitlines()
 return arrayText


   

# cv2.imshow("roi", roi)
# cv2.imshow("Img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()