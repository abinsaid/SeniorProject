from asyncore import write
#from ocr import*
from ocr_with_api import *
from ImageAnalysis import*
import re
import os
# from ar_corrector.corrector import Corrector

numImages = input("Enter Number of images : ")
extension = input("Enter extension of images : ")
numImages=int(numImages)
image_url=""
counter=0
images=[]*numImages
precent=0
totalPrecent=0
#corr = Corrector()
path = r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\Image Analysis\testingOutput\\"
while counter<numImages: # loop for storing images in an array to be tested 
    imageName = str(counter+1)+extension
    images.insert(counter,imageName)
    counter=counter+1
 
print(images)
counter=1
for i in images:
 
 print(i)
 precent=0
 imageName = path+i
 print("image name is "+imageName)
 #sys.exit()
 jd= myReg(imageName,"0","",1)
 jsonObject = json.loads(jd)  
 print("back to testing")
 print(jsonObject)


 ocrDay= jsonObject["day"]
 ocrTopic= jsonObject["topic"]
 ocrInstructor=jsonObject["instructor"]
 ocrDate = jsonObject["date"]
 ocrSatrting=jsonObject["startingTime"]
 ocrEnding = jsonObject["endingTime"]

 ocrOnline =jsonObject["online"]
 ocrTech = jsonObject["intrestTechnology"]
 ocrSoftSkills = jsonObject["intrestSoftSkills"]


 dayStatus=False
 TopicStatus=False
 instructorStatus=False
 dateStatus = False
 startingStatus = False
 endingStatus = False

 onlineStatus = False
 techStatus = False
 softSkillsStatus= False


 topicCorrection = 0
 
 oldTopic=ocrTopic
 amount = 14.28
 imageFile= r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\Image Analysis\testingOutput\accuercy.txt"
 temp = i 
 #temp = temp.rep
 print("now counter is",counter)
 sample= r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\Image Analysis\testingOutput\sample"+str(counter)+".txt"
 f= open(imageFile, "a" ,encoding='utf-8')
 sampleFile=open(sample, "r" ,encoding='utf-8')
 counter=counter+1
 daySample=sampleFile.readline()
 topicSample=sampleFile.readline()
 instructorSample=sampleFile.readline()
 dateSample=sampleFile.readline()
 startingSample=sampleFile.readline()
 endingSample=sampleFile.readline()

 onlineSample=sampleFile.readline()
 techSample=sampleFile.readline()
 softSkillsSample=sampleFile.readline()

 daySample = daySample.strip()
 topicSample = topicSample.strip()
 instructorSample = instructorSample.strip()
 dateSample = dateSample.strip()
 startingSample = startingSample.strip()
 endingSample = endingSample.strip()

 onlineSample= onlineSample.strip()
 techSample = techSample.strip()
 softSkillsSample = softSkillsSample.strip()


 


#  print(ocrDay)
#  print(ocrTopic)
#  print(ocrInstructor)
#  print(daySample)
#  print(topicSample)
#  print(instructorSample)
 f.writelines(i)
 f.writelines("\n")


 if daySample.lower()==ocrDay.lower():
     dayStatus=True
     print("both days are the same")
     f.writelines("both days are the same")
     f.writelines("\n")
     precent=precent+amount

 tempTopicSample= topicSample
 tempTopicOcr = ocrTopic
 tempTopicSample=tempTopicSample.replace(" ","")
 tempTopicOcr=tempTopicOcr.replace(" ","")
 tempTopicSample = topicSample.encode(encoding="ascii",errors="ignore")
 tempTopicOcr = ocrTopic.encode(encoding="ascii",errors="ignore")

 temp1Sample = str(tempTopicSample).replace(" ","")
 temp2OCR = str(tempTopicOcr).replace(" ","")

 if temp1Sample in temp2OCR:
      print("both topics are the same")
      f.writelines("both topics are the same")
      f.writelines("\n")
      TopicStatus=True
      precent=precent+amount

 tempOcrInstructor = ocrInstructor.encode(encoding="ascii",errors="ignore")
 tempInstructorSample = instructorSample.encode(encoding="ascii",errors="ignore")

 if tempInstructorSample in tempOcrInstructor:
      print("both instructors are the same")
      f.writelines("both instructors are the same")
      f.writelines("\n")
      instructorStatus=True
      precent=precent+amount


 if dateSample==ocrDate:
      print("both dates are the same")
      f.writelines("both dates are the same")
      f.writelines("\n")
      dateStatus=True
      precent=precent+amount

 if startingSample==ocrSatrting:
      print("both starting are the same")
      f.writelines("both starting time are the same")
      f.writelines("\n")
      startingStatus=True
      precent=precent+amount
 if endingSample==ocrEnding:
      print("both ending are the same")
      f.writelines("both ending time are the same")
      f.writelines("\n")
      endingStatus=True
      precent=precent+amount

 if onlineSample.lower()==ocrOnline.lower():
      print("both online are the same")
      f.writelines("both online are the same")
      f.writelines("\n")
      onlineStatus=True
      precent=precent+amount

 totalPrecent = precent+totalPrecent
 
 precent=str(precent)


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
 f.write("Image Instructor : ")
 f.writelines(instructorSample)
 f.writelines("\n")
 f.write("OCR Instructor : ")
 f.writelines(ocrInstructor)
 f.writelines("\n")


 f.write("Image Date : ")
 f.writelines(dateSample)
 f.writelines("\n")
 f.write("OCR Date : ")
 f.writelines(str(ocrDate))
 f.writelines("\n")

 f.write("Image Starting : ")
 f.writelines(startingSample)
 f.writelines("\n")
 f.write("OCR starting : ")
 f.writelines(ocrSatrting)
 f.writelines("\n")

 f.write("Image ending : ")
 f.writelines(endingSample)
 f.writelines("\n")
 f.write("OCR ending : ")
 f.writelines(ocrEnding)
 f.writelines("\n")


 f.write("Image online : ")
 f.writelines(onlineSample)
 f.writelines("\n")
 f.write("OCR online : ")
 f.writelines(ocrOnline)
 f.writelines("\n")
 f.writelines("=============================================")
 f.writelines("\n")



 #instructorSample = str(instructorSample)
 #ocrInstructor = str(ocrInstructor)
 

#if instructorSample in ocrInstructor and instructorStatus==False:
       # precent=precent+16.6

# if TopicStatus==False:
#       ocrTopic=corr.contextual_correct(ocrTopic)
#       print("after correction is : ")
#       print(ocrTopic)
#       print(topicSample==ocrTopic)
#       if topicSample==ocrTopic:
#           TopicStatus=True
#           precent=precent+amount
#           topicCorrection=1



      



#precent=str(precent)

#techSample= str(techSample)
#softSkillsSample= str(softSkillsSample)

#ocrTech= str(ocrTech)
#ocrSoftSkills= str(ocrSoftSkills)


'''
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
f.write("Image Instructor : ")
f.writelines(instructorSample)
f.writelines("\n")
f.write("OCR Instructor : ")
f.writelines(ocrInstructor)
f.writelines("\n")


f.write("Image Date : ")
f.writelines(dateSample)
f.writelines("\n")
f.write("OCR Date : ")
f.writelines(str(ocrDate))
f.writelines("\n")

f.write("Image Starting : ")
f.writelines(startingSample)
f.writelines("\n")
f.write("OCR starting : ")
f.writelines(ocrSatrting)
f.writelines("\n")

f.write("Image ending : ")
f.writelines(endingSample)
f.writelines("\n")
f.write("OCR ending : ")
f.writelines(ocrEnding)
f.writelines("\n")


f.write("Image online : ")
f.writelines(onlineSample)
f.writelines("\n")
f.write("OCR online : ")
f.writelines(ocrOnline)
f.writelines("\n")

'''

# f.write("Image tech : ")
# f.writelines(techSample)
# f.writelines("\n")
# f.write("OCR tech : ")
# f.writelines(ocrTech) 
# f.writelines("\n")


# f.write("Image softSkills : ")
# f.writelines(softSkillsSample)
# f.writelines("\n")
# f.write("OCR softskills : ")
# f.writelines(ocrSoftSkills)
# f.writelines("\n")



f.write("accuercy : ")
accuercy= totalPrecent/numImages
accuercy = "{:.2f}".format(accuercy)
accuercy=str(accuercy)
f.writelines(accuercy)
f.writelines("%")
f.writelines("\n")
#if(topicCorrection!=0):
    # f.writelines("the topic has been corrected from \n")
    # f.writelines(oldTopic+"\n")
#f.writelines("==================================")
#f.writelines("\n")

