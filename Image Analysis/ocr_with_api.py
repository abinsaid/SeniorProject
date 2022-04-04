from tkinter import image_names
import cv2
import numpy as np
import requests
import io
import json
import os
import sys
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests 
from PIL import Image,ImageDraw,ImageFont
from google.cloud import vision
from google.cloud import vision_v1
import pandas as pd
import requests, os, json

def nanoNetsAPI(myImage):
 credentials = json.load(open('credentials.json','r'))
 API_Key= credentials['NanoNets_API_KEY']
 MODEL_ID= credentials['NanoNets_Model_ID']
 url = 'https://app.nanonets.com/api/v2/OCR/Model/'+MODEL_ID+'/LabelFile/'

 data = {'file': open(myImage, 'rb')}

 response = requests.post(url, auth=requests.auth.HTTPBasicAuth(API_Key, ''), files=data)
 x = response.json()
 print("response is ",x)
 try:
    topic = x["result"][0] ["prediction"][0]['ocr_text']
    print( x["result"][0] ["prediction"][0]['ocr_text']   )
 except IndexError:
  return "Topic not Found"
 return topic


 #print(response.text)

 
def GoogleAPI(myImage):
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\Ammar\Desktop\test\Image Analysis\Vision_API_Demo\gooleAPIToken.json"

  client = vision.ImageAnnotatorClient()

 
  image_path = myImage

  with io.open(image_path, 'rb') as image_file: 
    content = image_file.read()

  # construct an iamge instance
  image = vision_v1.Image(content=content)

  """
  # or we can pass the image url
  image = vision.types.Image()
  image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
  """

  # annotate Image Response
  response = client.document_text_detection(image=image)  # returns TextAnnotation
  df = pd.DataFrame(columns=['locale', 'description'])

  texts = response.text_annotations
  for text in texts:
     df = df.append(
        dict(
            #locale=text.local,
            description=text.description,
            lang = 'ar',
            feature = "DOCUMENT_TEXT_DETECTION "
            
        ),
        ignore_index=True
    )

  print(df['description'][0])
  return df['description'][0]

def ocrAPI2(): # Azure
   
   credentials = json.loads(open('credentials.json'))
   AZURE_API_KEY= credentials['AZURE_API_KEY']
   AZURE_END_POINT= credentials['AZURE_EMD_POINT']
   cv_clinet = ComputerVisionClient(AZURE_END_POINT,CognitiveServicesCredentials(AZURE_API_KEY))
   image_url = 'https://i2-prod.liverpoolecho.co.uk/incoming/article17096840.ece/ALTERNATES/s810/0_whatsappweb1_censored.jpg'
   response=cv_clinet.read(image_url,language='en')
   opLocation = response.headers['Operation-Location']
   opID = opLocation.split('/')[-1] 
   result = cv_clinet.get_read_result(opID)
   print(result)
   print(result.status)
   print(result.analyze_result)
   '''
 import requests
 # If you are using a Jupyter Notebook, uncomment the following line.
 # %matplotlib inline
 import matplotlib.pyplot as plt
 import json
 from PIL import Image
 from io import BytesIO

 # Add your Computer Vision subscription key and endpoint to your environment variables.
 if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['7066e4f234b84b7da7e72c97474a8d0f']
 else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

 if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

 analyze_url = endpoint + "vision/v3.1/analyze"

 # Set image_url to the URL of an image that you want to analyze.
 image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
    "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

 headers = {'Ocp-Apim-Subscription-Key': subscription_key}
 params = {'visualFeatures': 'Categories,Description,Color'}
 data = {'url': image_url}
 response = requests.post(analyze_url, headers=headers,
                         params=params, json=data)
 response.raise_for_status()

 # The 'analysis' object contains various fields that describe the image. The most
 # relevant caption for the image is obtained from the 'description' property.
 analysis = response.json()
 print(json.dumps(response.json()))
 image_caption = analysis["description"]["captions"][0]["text"].capitalize()

 # Display the image and overlay it with the caption.
 image = Image.open(BytesIO(requests.get(image_url).content))
 plt.imshow(image)
 plt.axis("off")
 _ = plt.title(image_caption, size="x-large", y=-0.1)
 plt.show()
'''

def ocrAPI(myImage):





 
 #img = cv2.imread(r"C:\Users\Ammar\Desktop\test\Image Analysis\images\6.png")
 img = cv2.imread(myImage)

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


 

   