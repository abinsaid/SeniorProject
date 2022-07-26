from asyncore import write
from ocr import*
from Reg import*
import re
from ar_corrector.corrector import Corrector

numImages = input("Enter Number of images : ")
numImages=int(numImages)
counter=0
images=[]*numImages
corr = Corrector()

while counter<numImages: # loop for storing images in an array to be tested 
    imageName = input("Enter images name : ")
    images.insert(counter,imageName)
    counter=counter+1

print(images)

for i in images:
 
 print(i)
 keys= myReg(i)
 print("back to testing")
 ocrDay= keys[0]
 ocrTopic= keys[1]
 #ocrInstructor=keys[2]
 dayStatus=False
 TopicStatus=False
 instructorStatus=False
 precent=0
 topicCorrection = 0
 oldTopic=ocrTopic
 amount = 50
 imageFile= i+"accuercy.txt"
 sample="sample-"+i+"-.txt"
 f= open(imageFile, "w" ,encoding='utf-8')
 sampleFile=open(sample, "r" ,encoding='utf-8')

 daySample=sampleFile.readline()
 topicSample=sampleFile.readline()
 #instructorSample=sampleFile.readline()
 daySample = daySample.strip()
 topicSample = topicSample.strip()
 #instructorSample= instructorSample.strip()

 print(ocrDay)
 print(ocrTopic)
 #print(ocrInstructor)
 print(daySample)
 print(topicSample)
 #print(instructorSample)


 if daySample.lower()==ocrDay.lower():
     dayStatus=True
     print("both days are the same")
     precent=precent+amount

 if topicSample==ocrTopic:
      TopicStatus=True
      precent=precent+amount
'''
 if instructorSample==ocrInstructor:
      instructorStatus=True
      precent=precent+33.33
'''

 #instructorSample = str(instructorSample)
 #ocrInstructor = str(ocrInstructor)
 

#if instructorSample in ocrInstructor and instructorStatus==False:
       # precent=precent+16.6

if TopicStatus==False:
      ocrTopic=corr.contextual_correct(ocrTopic)
      print("after correction is : ")
      print(ocrTopic)
      print(topicSample==ocrTopic)
      if topicSample==ocrTopic:
          TopicStatus=True
          precent=precent+amount
          topicCorrection=1



      



precent=str(precent)

f.writelines(i)
f.writelines("\n")
f.write("Image day : ")
f.writelines(daySample)
f.writelines("\n")
f.write("OCR day : ")
f.writelines(ocrDay)
f.writelines("\n")
f.write("Image Topic : ")
f.writelines(topicSample)
f.writelines("\n")
f.write("OCR Topic : ")
f.writelines(ocrTopic)
f.writelines("\n")
#f.write("Image Instructor : ")
#f.writelines(instructorSample)
#f.writelines("\n")
#f.write("OCR Instructor : ")
#f.writelines(ocrInstructor)
#f.writelines("\n")
f.write("accuercy : ")
f.writelines(precent)
f.writelines("%")
f.writelines("\n")
if(topicCorrection!=0):
     f.writelines("the topic has been corrected from \n")
     f.writelines(oldTopic+"\n")
f.writelines("==================================")
f.writelines("\n")

