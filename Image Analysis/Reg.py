
# This Python file uses the following encoding: utf-8
#from curses.ascii import isdigit
from operator import length_hint
import os
import sys
import unicodedata
import re
from datetime import datetime
from matplotlib.pyplot import text
import convert_numbers
from hijri_converter import Hijri, Gregorian
from ocr import*
from ocr_with_api import*
from Event import*
import numpy as np
import datetime
import pandas as pd


  
def returnDay(day):

    if day == "الأحد" or day == "الاحد" or day == "الإحد" or day == "احد" or day == "أحد" or day == "الاجد":
        day = "Sunday"
        return day

    elif day == "الاثنين" or day == "الأثنين" or day == "الإثنين" or day == "اثنين" or day == "أثنين":
        day = "Monday"
        return day

    elif day == "الثلاثاء" or day == "الثلوث" or day == " 'الثلاثاء " or day =="الثلاثاء:":
        day = "Tuesday"
        return day

    elif day == "الاربعاء" or day == "الإربعاء" or day == "الأربعاء" or day == "ربوع" or day == "الربوع":
        day = "Wednesday"
        return day

    elif day == "خميس" or day == "الخميس" or day == "الحميس":
        day = "Thursday"
        return day

    elif day == "جمعة" or day == "الجمعة" or day == "الحمعة":
        day = "Friday"
        return day

    elif day == "سبت" or day == "السبت":
        day = "Saturaday"
        return day

    return "nothing found"







# a method for removing spaces between dates ex: 12 / 3 / 2020 ==== 12/3/2020
'''
def removeSpace(dates):
    if " " in dates:
     for i, val in enumerate(dates):
        temp = ""
        temp = dates[i]
        temp = temp.replace(" ", "")
        dates[i] = temp
    else :
     return dates

    return dates
'''

def exteractTopic(words): 
    temp = 0
    index=0
    for i in words :
     temp = i
     if temp.find("دورة بعنوان") !=-1 or temp.find("دورة :") !=-1 or temp.find("ورشة عمل بعنوان") !=-1 or temp.find("محاضرة بعنوان") !=-1 or temp.find("لقاء ريادي بعنوان") !=-1 or temp.find("محاضرة") !=-1 or temp.find("مخاضرة") !=-1 or temp.find("دورة تدريبية بعنوان") !=-1 or temp.find("تدريبية بعنوان :")!=-1 or temp.find("تدريبية بعنوان")!=-1 or temp.find("تدريبية بعنوان ")!=-1 or temp.find("لحضور دورة:")!=-1 or temp.find("دورة في")!=-1 or temp.find("دورة تطوير")!=-1 or temp.find("مقدمة في")!=-1 or temp.find("Introduction to")!=-1 or temp.find("ورش عمل برنامج")!=-1 or temp.find("دورة")!=-1: 
       print("found topic")
       index=index+1
       return words[index]
     index=index+1

    
    print("topic not found")
    return "Topic not Found"


def exteractInstructor(words): 
    temp = 0
    index=0
    for i in words :
     temp = i
     if temp.find("الدكتور")!=-1 or temp.find("يقدمها الدكتودا")!=-1  or temp.find("يقدمها")!=-1 or temp.find("مقدم الدورة")!=-1 :
       print("found instructor")
       index=index+1
       return words[index]
     index=index+1
    print("instructor not found")
    return "Instructor not Found"

def nameCorrection(name):
    if(name.find("هافي")!=-1):
         name = name.replace("هافي","هاني")

    if(name.find("برديي")!=-1):
         name = name.replace("برديي","برديسي")
    if(name.find("دسين")!=-1):
         name = name.replace("دسين","حسين")
    if(name.find("ها دية")!=-1):
         name = name.replace("ها دية","هادية")
    if(name.find("الحاري")!=-1):
         name = name.replace("الحاري","الحارثي")

         

    return name


# def exteractInstructor(words): 
#     length = len(words)
#     k=0
#     while k<length :
#      temp = words[k] 
#      if temp.find("الدكتور")!=-1 or temp.find("يقدمها الدكتودا")!=-1  or temp.find("يقدمها")!=-1:
#        print("instructor found")
#        print(temp)
#        return temp
#      k=k+1
#     return 0

def convertArabicDigitsToEnglish(x):
 
 newDate=convert_numbers.hindi_to_english(x)

 
 if x[2]=="/" and x[5]=="/":
    
    newDate = newDate[:2] + "/" +newDate[2:]
    newDate = newDate[:5] + "/" +newDate[5:]
 elif x[4]=="/" and x[7]=="/":
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate = newDate[:7] + "/" +newDate[7:]

 elif x[2]=="/" and x[4]=="/":
    
    newDate =newDate[:2] + "/" + newDate[2:]
    newDate =newDate[:4] + "/" + newDate[4:]

 elif x[1]=="/" and x[4]=="/":
    newDate = newDate[:1] + "/" + newDate[1:]
    newDate = newDate[:4] + "/" + newDate[4:]

 elif x[4]=="/" and x[6]=="/":
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate = newDate[:6] + "/" + newDate[6:]

 elif x[4]=="/" and x[7]=="/":
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate = newDate[:7] + "/" + newDate[7:]

 elif x[1]=="/" and x[3]=="/":
    newDate= newDate[:1] + "/" + newDate[1:]
    newDate= newDate[:3] + "/" + newDate[3:]

 elif x[4]=="/" and x[6]=="/":
    
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate= newDate[:6] + "/" + newDate[6:]
 else :
     print("somthing wrong")
  

 return newDate


def convertStringToDate(str):
    
    objDate = datetime.strptime(str, '%d%m%y')
    print ("The type of the date is now",  type(objDate))
    print ("The date is", objDate)
    return objDate

def convertFromHijri(y,m,d):
    convertedDate = Hijri(y, m, d).to_gregorian()
    convertedDate=x = datetime.datetime(convertedDate.year, convertedDate.month, convertedDate.day)
    return convertedDate


def cleanDate(date):
    date = date.replace("[","")
    date = date.replace("]","")
    date = date.replace(",","")
    date = date.replace("'","")
    return date

def compareTwoDates(d1,d2):
    if(d1==d2):
        return True
    else:
        return False


def addZero(s):

  s=s.replace(" ","")
  if(len(s)==10):
      return s
    
  if (s[0].isdigit() and s[1]=="/" )and (s[2].isdigit() and s[3]=="/" and s[1]=="/"):
    s= s[:0] + "0" + s[0:]
    s= s[:3] + "0" + s[3:]

  elif (s[0].isdigit() and s[1]=="/" and s[4]=="/"):
    
    s= s[:0] + "0" + s[0:]

  elif s[3].isdigit() and s[4]=="/"  and s[2]=="/":
    s= s[:3] + "0" + s[3:]

  elif (s[5].isdigit() and s[6]=="/" and s[4]=="/" )and (s[7].isdigit() and (len(s)-1)==7 and s[6]=="/")  :
    
    s= s[:5] + "0" + s[5:]
    s= s[:8] + "0" + s[8:]


  elif s[5].isdigit() and s[6].isdigit() and s[4]=="/" and s[7]=="/" and s[8].isdigit() and (len(s)-1==8) :
    s= s[:8] + "0" + s[8:]


  elif s[4]=="/" and s[5].isdigit() and s[6]=="/" and s[7].isdigit():
    s= s[:5] + "0" + s[5:]


  

  return s
    

def wordCorrection(words): 
    length = len(words)
    k =0

     
    while k<length :

      temp = words[k]
      temp=temp.replace("ف ","في ")
      words[k]=temp
      '''
      if temp.find("الدكتودا")!=-1 :
       temp = temp.replace("الدكتودا","الدكتور")
       words[k]=temp
       print("corrected")
       print(temp)

      if temp.find(" ف ")!=-1 :
       temp = temp.replace("ف ","في")
       words[k]=temp
       print("corrected")
       print(temp)

      if temp.find(" الدكتودا ")!=-1 :
       temp = temp.replace("الدكتودا","الدكتور")
       words[k]=temp
       print("corrected")
       print(temp)

      if temp.find(" الدكتودا")!=-1 :
       temp = temp.replace("الدكتودا","الدكتور")
       words[k]=temp
       print("corrected")
       print(temp)

      if temp.find("الدكنور")!=-1 :
        temp = temp.replace("الدكنور","الدكتور")
        words[k]=temp
        print("corrected")
        print(temp)

      if temp.find("الدكنورة")!=-1 :
       temp = temp.replace("الدكنورة","الدكتورة")
       words[k]=temp
       print("corrected")
       print(temp)
'''
      k=k+1
     
    return words
    
        

    


def remove(dates):
        for i, val in enumerate(dates):
         value = ""
         temp1 = ""
         temp2 = ""
         value = dates[i]
         for j, val2 in enumerate(value):
            k = j+1
            length = len(value)
            if(length-k == 1):
                break

            if(value[j] == "/"):

                temp1 = value[j]
                value = value.replace(temp1, "")
                dates[i] = value
                break
        return dates

def formatingDate(dates):
#      for i, val in enumerate(dates):
        value = ""
#         temp1 = ""
#         temp2 = ""
#         value = dates[i]
#         print(value)
#         for j, val2 in enumerate(value):
#             k = j+1
#             length = len(value)
#             if(length-k == 1):
#                 break
        
#             if value[j][3] == "١" and value[j][4] == "٤" and value[j][5] == "٤" :
#                 value[j] = value[:2] + "٠" + value[2:]
#                 temp1 = value[j]
#                 dates[i] = value
#                 break


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
'''     
def isHijri(dates):
    if dates[0]=="١" and dates[1]=="٤":
        return True
    elif dates[4]=="١" and dates[5]=="٤":
        return True
    else :
     return False

def convertHijri(dates):
        day = dates[0]+dates[1]
        print(day)
        month = dates[2]+dates[3]
        print(month)
        year = dates[4]+dates[5]+dates[6]+dates[7]
        g = Hijri(year, month, day).to_gregorian()
        print(g)
        return g

def convertNumbers(dates):

    dates = convert_numbers.hindi_to_english(dates)
    return dates

def add(dates):
    dates = dates[:2] + "/" + dates[2:]
    dates = dates[:5] + "/" + dates[5:]
    return dates
'''

def validateDate(day, month, year):

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if(isValidDate):
        print("Input date is valid ..")
        return True
    else:
        print("Input date is not valid..")
        return False

def isHijri(date):

 if "144" in date:
  return True
 else :
  return False


def removeSpace(dates):

    for i, val in enumerate(dates):
        value = ""
        temp1 = ""
        temp2 = ""
        value = dates[i]
        for j, val2 in enumerate(value):
            k = j+1
            length = len(value)
            if(length-k == 1):
                break

            if(value[j] == " "):

                temp1 = value[j]
                value = value.replace(temp1, "")
                dates[i] = value
                break

    return dates

    

    return dates

# not yet ready, it will put / in dates if non existed ex: 3122020 === 3/12/2020


def reFactorDate(dates):
    for i, val in enumerate(dates):
        value = ""
        temp1 = ""
        temp2 = ""
        value = dates[i]
        length = len(value)
        for j, val2 in enumerate(value):
            k = j+1
            length = len(value)

            '''
            
            if(value[3] == "٧"):

                string_list = list(value)
                string_list[3] = "١/"
                new_string = "".join(string_list)
                dates[i] = new_string
                

            if(value[7] == "٨"):
                 print(7)
                 print(value[4])

                 string_list=""
                 new_string=""
                 string_list = list(value)
                 string_list[7] = "/"
                 new_string = "".join(string_list)
                 print("7"+  new_string)
                 dates[i] = new_string

            if value[7] != "/" and (value[length-1].isdigit() and value[length-2].isdigit() and value[length-3].isdigit() ):
                 

                 string_list=""
                 new_string=""
                 string_list = list(value)
                 string_list[7] = "/"
                 new_string = "".join(string_list)
                
                 dates[i] = new_string

            if(value[4] == "٧"):
                
                 string_list=""
                 new_string=""
                 string_list = list(value)
                 string_list[4] = "/"
                 new_string = "".join(string_list)
                
                 dates[i] = new_string

           


                  
            if(value[4] == "٨"):
               
                string_list=""
                new_string=""
                string_list = list(value)
                string_list[4] = "/"
                new_string = "".join(string_list)
              
                dates[i] = new_string

            if value[6] == "٨" and value[4]=="/" and value[5]!="0":
                
                string_list=""
                new_string=""
                string_list = list(value)
                string_list[6] = "/"
                new_string = "".join(string_list)
                
                dates[i] = new_string

            if value[6] == "٧" and value[4]=="/" and value[5]!="0":
                
               
                string_list=""
                new_string=""
                string_list = list(value)
                string_list[6] = "/"
                new_string = "".join(string_list)
                
                dates[i] = new_string

            if int(value[5]) >1 and value[6]=="١" :
                
               
                string_list=""
                new_string=""
                string_list = list(value)
                string_list[6] = "/"
                new_string = "".join(string_list)
                
                dates[i] = new_string

            if value[4]=="٠"  :
                string_list=""
                new_string=""
                string_list = list(value)
                string_list[4] = "/"
                new_string = "".join(string_list)
                
                dates[i] = new_string

            if (value[0].isdigit() and value[1].isdigit() and value[2].isdigit() and value[3].isdigit()) :
              
                 if(value[0]=="٢") :
                   string_list=""
                   new_string=""
                   string_list = list(value)
                   string_list[3] = "٢"
                   new_string = "".join(string_list)
            elif(value[0]=="١") :
                  string_list=""
                  new_string=""
                  string_list = list(value)
                  string_list[3] = "٣"
                  new_string = "".join(string_list)
                  
         '''


'''
            if value[3]!="/"and value[0].isdigit() and value[1].isdigit() and value[2].isdigit() and value[3].isdigit() :
                  string_list=""
                  new_string=""
                  string_list = list(value)
                  string_list[4] = "/"
                  new_string = "".join(string_list)
                  dates[i] = new_string
                  
            if value[7]!="/"and value[5].isdigit() and value[6].isdigit() :
                  string_list=""
                  new_string=""
                  string_list = list(value)
                  string_list[7] = "/"
                  new_string = "".join(string_list)
                  dates[i] = new_string
                     
                     
            if value[7]!="/"and value[5].isdigit() and  (value[6] =="٧" or value[6]=="٨"):
                  string_list=""
                  new_string=""
                  string_list = list(value)
                  string_list[7] = "/"
                  new_string = "".join(string_list)
                  dates[i] = new_string
                  
            if value[4]=="٠"and (value[3].isdigit() and value[3]!="٧" or value[3]!="٨"):
                   
                   string_list=""
                   new_string=""
                   string_list = list(value)
                   string_list[4] = "/"
                   new_string = "".join(string_list)
                   dates[i] = new_string

    return dates
'''


# this method will delete the 5 next to the hejri date
def remove5(dates):

    for i, val in enumerate(dates):
        value = ""
        temp1 = ""
        temp2 = ""
        value = dates[i]
        for j, val2 in enumerate(value):
            k = j+1
            length = len(value)
            if(length-k == 1):
                break

            if(value[j] == "/" and value[k] == "٥"):

                temp1 = value[k]
                value = value.replace(temp1, "")
                dates[i] = value
                break
            if(value[j] == "٥" and value[k] == "١" or value[j] == "٥" and value[k] == "٢"):

                temp1 = value[j]
                value = value.replace(temp1, "")
                dates[i] = value
                break

    return dates

def myReg(myImage) :

#image="8.png"
 print("*******************************************")
 index=0
 topic=""
 arrayText=ocrAPI()
 text=listToString(arrayText)

 #arrayText = text.splitlines()
 #text= OCR1(myImage)
 #text2 = OCR2(myImage)
 #text2= wordCorrection(text2)
 #print(text2)
 #print("================================================================************************************")
 topic= exteractTopic(arrayText)
 #instructor = exteractInstructor(arrayText)
 #instructor= nameCorrection(instructor)

#  if(index!=-1):
#   topic = arrayText[index]
#  elif index==-1:
#      topic="no topic was found"

#  if(index!=-1):
#   topic = arrayText[index]
#  elif index==-1:
#      topic="no topic was found"
#  print(topic)

 print(topic)
 #print(instructor)


 #text=" شطر الطالبات يسر عمادة شؤون المكتبات ١٤٤٣ ضمن أنشطة نادي أصدقاء المكتبة للعام دورة بعنوان : هندسة المعرفة في تطبيقات الذكاء الاصطناعي أدوى نصار الميلبي تقدمها الأستاذة محاور الورشة : هندسة المعرفة ف الذكاء من المعلومات ولمزيد انقر على الصورة >مكونات وخطوات هندسة المعرفة Click here المكونات المادية في نظام هندسة المعرفة المهارات المطلوبة لمهندسي المعرفة الفية المستهدفة : يوع الثلاداء ٢١ ٢ ٥١٤٤٣ جامعه الملك عبدالعزيز جميع الموافق ٢٨ ٥٢٠٢٧٠٩ الشاعة : للحضول على الشهادة : الدخول بالاسم الثلاثي كامل ورشة السمل Librarykau 0569808352 عمادة شؤون المكتبات Kaulibrary Kaulib جامعة الملك عبدالعزيز f Kaulibrary Library@kau edu sa ت٠٢٨٥ .ر  UBRAFN _ الدراسي تقديم للحضور مفهوم الاصطناعي منسوي حمزر "
 dates = ""  # an array for storing all date
 listDates = np.array(["null","null"])
  # an array for storing all dates
 # text="asdasd asdasdasd asdooisdfopiopsd dsfsdofpsd[fpsdfo[ 11-12-2020   : ٢٠ / ٣ / ٥١٤٤٣ الاربعاء 1999/2/2" # ocr text
 # the follwing are 12 patterns for extracting the dates with all the expected outcome
 datePattern1 = "\s?\d{4}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{1,2}م?\s?"
 #datePattern2 = "\s?\d{1,2}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?هـ\s?ا\d{3}[^٥]م?\s?"
 datePattern2 = "\s?\d{1,2}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{4}[^٥]م?\s?"
# ٢٩ /٦/ ٤٤٣اهـ
 '''
 datePattern3 = "\s?\d{4}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{1,2}٥?\s?"
 datePattern4 = "\s?\d{1,2}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{4}٥?\s?"
 datePattern3 = "\s?\d{4}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{1,2}ه?\s?"
 datePattern4 = "\s?\d{1,2}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{4}ه?\s?"
 datePattern5 = "d{4}\s?\d{1,2}\s?\d{1,2}"
 datePattern6 = "d{1,2}\s?\d{1,2}\s?\d{4}"
 datePattern7 = "[\u0660-\u0669]{4}\s?[\u0660-\u0669]{1,2,3,4}\s?[\u0660-\u0669]{1,2,3,4}"
 datePattern8 = "[\u0660-\u0669]{1,2,3,4}\s?[\u0660-\u0669]{1,2,3,4}\s?[\u0660-\u0669]{4,5,6}"
 datePattern9 = "\s?[\u0660-\u0669]{9,10}\s?"
 datePattern10 = "\s?[\u0660-\u0669]{7}/[\u0660-\u0669]{2}"
 datePattern11 = "\s?[\u0660-\u0669]{10}\s?"
 datePattern12 = "\s?[\u0660-\u0669]{12}\s?"
 '''
 datePattern3 = "\s?\d{1,2}\s?\d{1,2}\s?\d{4,5}"
 datePattern4 = "\s?\d{4}\s?\d{1,2}\s?\d{1,2}"

 # 1 = days without Hamza
 # 2 = days with an upper Hamza
 # 3 = days with an lower Hamza
 # 4 = days spelled wrong
 dayPattern1 = r'\االاثنين |الثلوث | الثلاثاء: |الربوع |الخميس | الجمعة | السبت | الاربعاء|الاحد| الثلاثاء\b'
 dayPattern2 = r'\ الأثنين|الأربعاء|الأحد \b'
 dayPattern3 = r'\ الإربعاء| الإثنين|الإحد \b'
 dayPattern4 = r'\ الثلاداء|الاثنين |الثلاثاء |الثلاثاء :|الحميس |الأجد|الحمعة|الاجد \b'
 weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

 #namePattern1=r' د.\s+((?:\w+(?:\s+|$)){2})'
 namePattern1=r'د\.\s+((?:\w+(?:\s+|$)){2})'
 namePattern2=r'الدكتورة\s+((?:\w+(?:\s+|$)){2})'
 namePattern3=r'الدكتور\s+((?:\w+(?:\s+|$)){2})'
 namePattern4=r'الاستاذ\s+((?:\w+(?:\s+|$)){2})'
 namePattern5=r'الاستاذة\s+((?:\w+(?:\s+|$)){2})'
 namePattern6=r'الأستاذ\s+((?:\w+(?:\s+|$)){2})'
 namePattern7=r'الأستاذة\s+((?:\w+(?:\s+|$)){2})'
 namePattern8=r'أ\.\s+((?:\w+(?:\s+|$)){2})'
 #namePattern8=r'أ\s?.\s?\s?((?:\w+(?:\s+|$)){2})'
 namePattern9=r'الأستاذة /\s+((?:\w+(?:\s+|$)){2})'
 #namePattern10=r' الدكتورة/\s+((?:\w+(?:\s+|$)){2})'
 namePattern10=r'الدكتورة\s?/\s+((?:\w+(?:\s+|$)){2})'
 namePattern11=r'الدكتور\s?/\s+((?:\w+(?:\s+|$)){2})'
 #namePattern11=r'الدكتور/ /\s+((?:\w+(?:\s+|$)){2})'
 namePattern12=r'الطالبة:/\s+((?:\w+(?:\s+|$)){2})'
 namePattern13=r'الطالبة:\s+((?:\w+(?:\s+|$)){2})' 
 namePattern14=r'الأستاذ /\s+((?:\w+(?:\s+|$)){2})'
 namePattern15=r'المهندس\s?/\s+((?:\w+(?:\s+|$)){2})'
 namePattern16=r'المهندسة\s?/\s+((?:\w+(?:\s+|$)){2})'
 #namePattern14=r'تقديم\s+((?:\w+(?:\s+|$)){2})' 
 
 day=""

 if(re.search(dayPattern1, text)):
      print("day found")
      day = re.search(dayPattern1, text).group()
      day = day.replace(" ", "")
      print(day)
      day = returnDay(day)
      print("d1")
      print(day)

 elif(re.search(dayPattern2, text)):
    print("day found")
    day = re.search(dayPattern2, text).group()
    day = day.replace(" ", "")
    print(day)
    day = returnDay(day)
    print("d2")
    print(day)

 elif(re.search(dayPattern3, text)):
    print("day found")
    day = re.search(dayPattern3, text).group()
    day = day.replace(" ", "")
    day = returnDay(day)
    print("d3")
    print(day)

 elif(re.search(dayPattern4, text)):

    day = re.search(dayPattern4, text).group()
    day = day.replace(" ", "")
    print("day found")
    print(day)
    if day == "الأجد":
        day = "الأحد"
    elif day == "الحميس":
        day = "الخميس"
    elif day == "الحمعة":
        day = "الجمعة"
    elif day == "الثلاداء":
        day = "الثلاثاء"
    elif day == " 'الثلاثاء ":
        day = "الثلاثاء"
    elif day=="الاثنين ":
        day="الاثنين"
    elif day=="الثلاثاء :":
        day="الثلاثاء"
    elif day=="الثلاثاء ":
        day="الثلاثاء"
       
    
    day = returnDay(day)
    print("d4")
    print(day)

 else:
     day="no day was found"
     


 if((re.search(datePattern1, text))):
       print("date found 1")
       oldDates = re.findall(datePattern1, text, re.MULTILINE)
       dates = removeSpace(oldDates)
       dates = remove5(oldDates)
       dates = [i.replace("م", "") for i in oldDates]
       dates = [i.replace("ه", "") for i in oldDates]
       "2/2/2025"
       print(1)
       

 elif((re.search(datePattern2, text))):
         print("date found 2")
         oldDates = re.findall(datePattern2, text, re.MULTILINE)
         dates = removeSpace(oldDates)
         dates = remove5(oldDates)
         dates = [i.replace("م", "") for i in oldDates]
         dates = [i.replace("ه", "") for i in dates]
         print(2)
        
        


 DatesLength = len(dates)
 listobjDates=[] 
 j=0
 print("the length is ")
 print(DatesLength)
 print(" ")
 print(" ")
 finalDateSatus=""

 while j <DatesLength:
     yearStatus=False
     print("start of loop")
     temp=str(dates[j])
     
     
     #temp = cleanDate(temp)
     temp =convertArabicDigitsToEnglish(temp) 
     #temp=convertStringToDate(temp)
     temp = addZero(temp)
     objDate= datetime.datetime(2020, 5, 17)
      
     
     if temp[2].isdigit() and temp[3].isdigit() and temp[1].isdigit() and temp[4]=="/" and temp[0].isdigit():
      temp = datetime.datetime.strptime(temp, "%Y/%m/%d").strftime("%d/%m/%Y")
      objDate = datetime.datetime.strptime(temp, '%d/%m/%Y')

     elif temp[0].isdigit() and temp[1].isdigit() and temp[2]=="/":
      temp = datetime.datetime.strptime(temp, "%d/%m/%Y").strftime("%d/%m/%Y")
      objDate = datetime.datetime.strptime(temp, '%d/%m/%Y')

     dateSatus = isHijri(temp)
     if(dateSatus==True) :
        print(temp)
        objDate= convertFromHijri(objDate.date().year,objDate.date().month,objDate.date().day)
     if(objDate.date().year>=2024):
         #yearStatus=True
         continue

     if(day=="no day was found"):
         print("i am here and index is ",objDate.date().weekday())
         
         day=weekDays[objDate.date().weekday()]
     #dates=np.delete(dates,j)
     #dates=np.insert(dates,0,temp)

     j=j+1
     
     #print(objDate.date())
     print("=============================")
     #x=np.insert(x,0,objDate)
     #if yearStatus==False:
     listobjDates.insert(0,objDate.date())

     
 if(len(listobjDates)==2):
      finalDateSatus=compareTwoDates(listobjDates[0],listobjDates[1])
      

    

 print(listobjDates)
 
 print(finalDateSatus)
 #sys.exit()
 x = "١٤٤٣/٣/٢١هـ"


 instructor="not found"
#  text = text.replace("يسر عمادة شؤون","ن")
#  print(text)
#  print("000000000000000000000000000")

   
 if((re.search(namePattern1, text))):
        print("found 1")
        instructor = re.search(namePattern1, text).group()

 elif((re.search(namePattern2, text))):
        print("found 2")
        instructor = re.search(namePattern2, text).group()

 elif((re.search(namePattern3, text))):
        print("found 3")
        instructor = re.search(namePattern3, text).group()

 elif((re.search(namePattern4, text))):
        print("found 4")
        instructor = re.search(namePattern4, text).group()

 elif((re.search(namePattern5, text))):
        print("found 5")
        instructor = re.search(namePattern5, text).group()

 elif((re.search(namePattern6, text))):
        print("found 6")
        instructor = re.search(namePattern6, text).group()

 elif((re.search(namePattern7, text))):
        print("found 7")
        instructor = re.search(namePattern7, text).group()

 elif((re.search(namePattern8, text))):
        print("found 8")
        instructor = re.search(namePattern8, text).group()
 elif((re.search(namePattern9, text))):
        print("found 9")
        instructor = re.search(namePattern9, text).group()

 elif((re.search(namePattern10, text))):
        print("found 10")
        instructor = re.search(namePattern10, text).group()

 elif((re.search(namePattern11, text))):
        print("found 11")
        instructor = re.search(namePattern11, text).group()

 elif((re.search(namePattern12, text))):
        print("found 12")
        instructor = re.search(namePattern12, text).group()

 elif((re.search(namePattern13, text))):
        print("found 13")
        instructor = re.search(namePattern13, text).group()

 elif((re.search(namePattern14, text))):
        print("found 14")
        instructor = re.search(namePattern14, text).group()

 elif((re.search(namePattern15, text))):
        print("found 15")
        instructor = re.search(namePattern15, text).group()

 elif((re.search(namePattern16, text))):
        print("found 16")
        instructor = re.search(namePattern16, text).group()

 if(instructor=="not found"):
     print("regex did not work for instructor")
     instructor=exteractInstructor(arrayText)

    

 print("hatha ","." in instructor)
 
 instructor=nameCorrection(instructor)
 event = Event(topic,dates,day,instructor)
 print("after")
 print(instructor)
 print(" ")
 print(" ")
 print("topic : ",topic)
 print("instructor",instructor)
 print("day : ",day)
 if(len(listobjDates)!=0):
  print("date",listobjDates[0])
 else:
  print("date","no date was found")    




 #print(event)
 return event
    




    
















# if((re.search(datePattern1, text))):
#     print("date found")
#     oldDates = re.findall(datePattern1, text, re.MULTILINE)
#     dates = removeSpace(oldDates)
#     dates = remove5(oldDates)
#     dates = [i.replace("م", "") for i in oldDates]
#     dates = [i.replace("ه", "") for i in oldDates]
#     print(1)
#     listDates.insert(0, dates)


# elif(re.search(datePattern2, text)):
#     print("date found")
#     oldDates = re.findall(datePattern2, text, re.MULTILINE)
#     dates = removeSpace(oldDates)
#     dates = remove5(dates)
#     dates = [i.replace("م", "") for i in oldDates]
#     #dates = [oldDates[1].replace("م","")]
#     '''
#     for i in dates:
#      dates= convertNumbers(i)
#      print(i)
#      '''
#     i = 0
#     k = 0
#     dateIndex=1000
#     while (i < len(dates)):
#         dates[i] = convertNumbers(dates[i])
#         i = i+1

#     while (k < len(dates)):
#         length = len(dates[k])
#         print(length)
#         if length != 10:
#             k = k+1
#             continue
#         day = dates[k][0]+dates[k][1]
#         print(day)
#         month = dates[k][3]+dates[k][4]
#         print(month)
#         year = dates[k][6]+dates[k][7]+dates[k][8]+dates[k][9]
#         print(year)
#         dateStatus = validateDate(day, month, year)
#         if(dateStatus == True):
#             dateIndex=k
#             break
#         k = k+1
#     date=dates[k]
#     print(date)
#     print(2)
#     #listDates.insert(0, dates)

# elif(re.search(datePattern3, text)):
#     hijriSatus =False
#     print(3)
#     print("date found")
#     oldDates = re.findall(datePattern3, text, re.MULTILINE)
#     dates=remove(dates)
#     dates = removeSpace(oldDates)
#     dates = remove5(dates)
#     i=0
#     while (i < len(dates)):
#          dates = dates[i]
#          print("date is down")
#          dates=formatingDate(dates)
#          print(dates)
#          hijriSatus=isHijri(dates)
#          print(hijriSatus)
#          if(hijriSatus==True):
#             dates[i]=convertHijri(dates[i]) 
#          i = i+1
   
#     print(dates)
#     dates = [i.replace("م", "") for i in oldDates]
#     #dates = [oldDates[1].replace("م","")]
#     '''
#     for i in dates:
#      dates= convertNumbers(i)
#      print(i)
#      '''
#     i = 0
#     k = 0
#     dateIndex=1000
#     while (i < len(dates)):
#          dates[i] = convertNumbers(dates[i])
#          i = i+1

#     while (k < len(dates)):
#         length = len(dates[k])
#         print(length)
#         if length != 10:
#             k = k+1
#             continue
#         day = dates[k][0]+dates[k][1]
#         print(day)
#         month = dates[k][3]+dates[k][4]
#         print(month)
#         year = dates[k][6]+dates[k][7]+dates[k][8]+dates[k][9]
#         print(year)
#         dateStatus = validateDate(day, month, year)
#         if(dateStatus == True):
#             dateIndex=k
#             break
#         k = k+1
#     date=dates[k]
#     print(date)
    
#     #listDates.insert(0, dates)

# elif(re.search(datePattern4, text)):
    
#     print("date found")
#     oldDates = re.findall(datePattern4, text, re.MULTILINE)
#     dates = removeSpace(oldDates)
#     dates = remove5(dates)
#     dates = [i.replace("م", "") for i in oldDates]
#     #dates = [oldDates[1].replace("م","")]
#     '''
#     for i in dates:
#      dates= convertNumbers(i)
#      print(i)
#      '''
#     i = 0
#     k = 0
#     dateIndex=1000
#     while (i < len(dates)):
#         dates[i] = convertNumbers(dates[i])
#         i = i+1

#     while (k < len(dates)):
#         length = len(dates[k])
#         print(length)
#         if length != 10:
#             k = k+1
#             continue
#         day = dates[k][0]+dates[k][1]
#         print(day)
#         month = dates[k][3]+dates[k][4]
#         print(month)
#         year = dates[k][6]+dates[k][7]+dates[k][8]+dates[k][9]
#         print(year)
#         dateStatus = validateDate(day, month, year)
#         if(dateStatus == True):
#             dateIndex=k
#             break
#         k = k+1
#     date=dates[k]
#     print(date)
#     print(4)
#     #listDates.insert(0, dates)

# else:
#     print("no date was found")

#print(listDates)

myReg("40.jpg")

