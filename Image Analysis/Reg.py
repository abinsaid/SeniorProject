
# This Python file uses the following encoding: utf-8
#from curses.ascii import isdigit
from operator import length_hint
import os
import sys
import unicodedata
import re # for using a regix 
from datetime import datetime
from matplotlib.pyplot import text
import convert_numbers  # for converting from arabic digits to english 
from hijri_converter import Hijri, Gregorian  # for converting from hijri 
from ocr import* 
from ocr_with_api import* # an ocr that uses api 
from Event import* # event object 
import numpy as np # used for array
import datetime # to create an object of type Date
import pandas as pd
import json
from datetime import datetime # maybe cause an erorr
# note : for extracting topic and instructor name we have two approches 
# approches 1 (line extaction) : detact a spesfic word such as "course about" and then return the word in the next line
# approches 2 (model extaction) : by feeding a set of images to model and then it will detact instructor and event 


  # the following method is for detacting the day using a set of pretected words that will be read 
def returnDay(day): 

    if day == "الأحد" or day == "الاحد" or day == "الإحد" or day == "احد" or day == "أحد" or day == "الاجد":
        day = "Sunday"
        return day

    elif day == "الاثنين" or day == "الأثنين" or day == "الإثنين" or day == "اثنين" or day == "أثنين" or day == "إثنين" :
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
#approches 1 (line extaction) for topic
def exteractTopic(words): 
    temp = 0
    index=0
    for i in words :
     temp = i
     print("temp is  ",temp )
     
     if temp.find("دورة بعنوان") !=-1 or temp.find("دورة :") !=-1 or temp.find("ورشة عمل بعنوان") !=-1 or temp.find("محاضرة بعنوان") !=-1 or temp.find("لقاء ريادي بعنوان") !=-1 or temp.find("محاضرة") !=-1 or temp.find("مخاضرة") !=-1 or temp.find("دورة تدريبية بعنوان") !=-1 or temp.find("تدريبية بعنوان :")!=-1 or temp.find("تدريبية بعنوان")!=-1 or temp.find("تدريبية بعنوان ")!=-1 or temp.find("لحضور دورة:")!=-1 or temp.find("دورة في")!=-1 or temp.find("دورة تطوير")!=-1 or temp.find("مقدمة في")!=-1 or temp.find("Introduction to")!=-1 or temp.find("ورش عمل برنامج")!=-1 or temp.find("دورة")!=-1 or temp.find("تقديم دورة بعنوان:")!=-1  or temp.find(" تقديم دورة بعنوان: ")!=-1 or temp.find("تقديم دورة بعنوان:")!=-1 or temp.find("ندوة بعنوان") !=-1:
       print("found topic")
       index=index+1
       return words[index]
     index=index+1

    
    print("topic not found")
    return "Topic not Found"

#approches 1 (line extaction) for instructor
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

# a method that correct expected errors in names 
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


# method for converting from arabic digits to english using a library 
# the problem with this library is that it will remove the (-,/) from dates, so we have to restore it manually
def convertArabicDigitsToEnglish(x,indian):
 if(indian ==1):
  newDate=convert_numbers.hindi_to_english(x)
 else:
  newDate=convert_numbers.persian_to_english(x)
 #newDate=convert_numbers.persian_to_english(x)
 #newDate=convert_numbers.hindi_to_english(x)
 #newDate=convert_numbers.arabic_to_english(x)
 #newDate=convert_numbers.__all__(x)
 print("new Date is",newDate)
 print("x ",x)
 x=x.replace(" ","")
 newDate=newDate.replace(" ","")
 if x[2]=="/" and x[5]=="/": # 20/01/2017 : dd/dd/dddd
    newDate = newDate[:2] + "/" +newDate[2:]
    newDate = newDate[:5] + "/" +newDate[5:]

 elif x[4]=="/" and x[7]=="/": # 2017/20/12 : dddd/dd/dd (duplicated)
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate = newDate[:7] + "/" +newDate[7:]

 elif x[2]=="/" and x[4]=="/": #12/3/2020 : dd/d/dddd
    newDate =newDate[:2] + "/" + newDate[2:]
    newDate =newDate[:4] + "/" + newDate[4:]

 elif x[1]=="/" and x[4]=="/": #9/12/2020 : d/dd/dddd
    newDate = newDate[:1] + "/" + newDate[1:]
    newDate = newDate[:4] + "/" + newDate[4:]

 elif x[4]=="/" and x[6]=="/": # 2012/1/12: dddd/d/dd
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate = newDate[:6] + "/" + newDate[6:]

 elif x[4]=="/" and x[7]=="/": #2003/12/22 yyyy/dd/dd (duplicated)
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate = newDate[:7] + "/" + newDate[7:]

 elif x[1]=="/" and x[3]=="/": #7/7/2020 : d/d/dddd
    newDate= newDate[:1] + "/" + newDate[1:]
    newDate= newDate[:3] + "/" + newDate[3:]

 elif x[4]=="/" and x[6]=="/": #2020/5/2 :dddd/dd/dd
    
    newDate = newDate[:4] + "/" + newDate[4:]
    newDate= newDate[:6] + "/" + newDate[6:]
 else :
     print("somthing wrong")
  

 return newDate

# convert a string to a date object 
def convertStringToDate(str):
    
    objDate = datetime.strptime(str, '%d%m%y')
    print ("The type of the date is now",  type(objDate))
    print ("The date is", objDate)
    return objDate

# convert from hifri date
def convertFromHijri(y,m,d):
    convertedDate = Hijri(y, m, d).to_gregorian()
    convertedDate=x = datetime(convertedDate.year, convertedDate.month, convertedDate.day)
    return convertedDate

# used for removing unwanted chars from date
def cleanDate(date):
    date = date.replace("[","")
    date = date.replace("]","")
    date = date.replace(",","")
    date = date.replace("'","")
    return date

# to check if the two dates are equal or not (used for comparing the georgian date and the converted hijri date)
def compareTwoDates(d1,d2):
    if(d1==d2):
        return True
    else:
        return False

# add zeros in single digits date, for standardization
def addZero(s):

  s=s.replace(" ","")
  if(len(s)==10): #03/09/2020
      return s
    
  if (s[0].isdigit() and s[1]=="/" )and (s[2].isdigit() and s[3]=="/" and s[1]=="/"): #3/4/
    s= s[:0] + "0" + s[0:]
    s= s[:3] + "0" + s[3:]

  elif (s[0].isdigit() and s[1]=="/" and s[4]=="/"): #1/02/
    
    s= s[:0] + "0" + s[0:]

  elif s[3].isdigit() and s[4]=="/"  and s[2]=="/": #10/2/
    s= s[:3] + "0" + s[3:]

  elif (s[5].isdigit() and s[6]=="/" and s[4]=="/" )and (s[7].isdigit() and (len(s)-1)==7 and s[6]=="/")  : #2000/5/2
    
    s= s[:5] + "0" + s[5:]
    s= s[:8] + "0" + s[8:]


  elif s[5].isdigit() and s[6].isdigit() and s[4]=="/" and s[7]=="/" and s[8].isdigit() and (len(s)-1==8) : #2012/12/1
    s= s[:8] + "0" + s[8:]


  elif s[4]=="/" and s[5].isdigit() and s[6]=="/" and s[7].isdigit(): #2007/5/13
    s= s[:5] + "0" + s[5:]


  

  return s
    
# used for correcting a set of words that are frequently read wrong by ocr
def wordCorrection(words): 
    length = len(words)
    k =0

     
    while k<length :

      temp = words[k]
      #temp=temp.replace("ف ","في ")
      #words[k]=temp
      if temp.find("البر مجة")!=-1 :
       temp = temp.replace("البر مجة","البرمجة")
       words[k]=temp
       print("corrected")
       print(temp)

      if temp.find("حفور")!=-1 :
       temp = temp.replace("حفور","حضور")
       words[k]=temp
       print("corrected")
       print(temp)
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
    
        

    

# i forgot what this dose (must remeber)
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


# i forgot what this dose (must remeber)
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
#check if the constucted date is valid date or not 
def validateDate(day, month, year):

    isValidDate = True
    try:
        datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if(isValidDate):
        print("Input date is valid ..")
        return True
    else:
        print("Input date is not valid..")
        return False

# to check if this date is hijri or not, if 144 was spotted this means that its a hijri
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


def addColon(time) :
 t = str(time)
 if(len(t)==3):
  t = t[:1] + ":" +t[1:]

 elif (len(t)==4):
     t = t[:2] + ":" +t[2:]

 return t

 
 
def checkAm(am,t):
   if  "ص"  in t: # ىخف صخقنهىل
       am=1
       print("found am")
   else :
    am = 0

   return am

def checkPm(pm,t):
   if   "م"  in t:
       print("found pm")
       pm=1

   else :
    pm = 0

   return pm

def is24(t):
    t= int(t)
    if((t>=13) and t<24)or t=="00":
        return True
    else :
        return False


def convertTo24H(t,am,pm):
    t=t[0]+t[1]
    
    if(am==1):

        if(t=="12"):
            t="00"

        return t 
    
    else : 
        

        if(t=="01"):
            t="13"

        elif (t=="02"):
            t=14

        elif (t=="03"):
            t=15

        elif (t=="04"):
            t=16

        elif (t=="05"):
            t=17

        elif (t=="06"):
            t=18

        elif (t=="07"):
            t=19

        elif (t=="08"):
            t=20

        elif (t=="09"):
            t=21

        elif (t=="10"):
            t=22

        elif (t=="11"):
            t=23

        
        return t



def addZeroToTime(t):
  t = t[:0] + "0" +t[0:]
  return t

def returnWeekDay(objDate,weekDays):
    day=weekDays[objDate.date().weekday()]
    return day


    


def processDate(DatesLength,listobjDates,weekDays,dates,day,indian):
 day="no day was found"
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
     print("temp is ",temp)
     
     #temp = cleanDate(temp)
     temp= temp.replace("م","")
     temp= temp.replace(" ","")
     temp = os.linesep.join([s for s in temp.splitlines() if s]) # remove empty lines
     print("insed loop temp is ",temp)
     print("$$$$$$$")
     temp = str(temp)
     print("temp after conversion ",temp)
     temp =convertArabicDigitsToEnglish(temp,indian)
    # temp = temp.replace("/","") 
     #temp=convertStringToDate(temp)
     temp = addZero(temp)
     print("temp after zero ",temp)
     objDate= datetime(1999, 9, 9)
      
     
     if temp[2].isdigit() and temp[3].isdigit() and temp[1].isdigit() and temp[4]=="/" and temp[0].isdigit():
      temp = datetime.strptime(temp, "%Y/%m/%d").strftime("%d/%m/%Y")
      objDate = datetime.strptime(temp, '%d/%m/%Y')
      t = datetime(objDate.year, objDate.month, objDate.day, 0, 0)
      t.strftime('%d/%m/%Y')

     elif temp[0].isdigit() and temp[1].isdigit() and temp[2]=="/":
      temp = datetime.strptime(temp, "%d/%m/%Y").strftime("%d/%m/%Y")
      objDate = datetime.strptime(temp, '%d/%m/%Y')
      t = datetime(objDate.year, objDate.month, objDate.day, 0, 0)
      t.strftime('%d/%m/%Y')

     dateSatus = isHijri(temp)
     if(dateSatus==True) :
        print(temp)
        objDate= convertFromHijri(objDate.date().year,objDate.date().month,objDate.date().day)
     if(objDate.date().year>=2024):
         #yearStatus=True
         continue

     if(day=="no day was found"):
         print("i am here and index is ",objDate.date().weekday())
         day = returnWeekDay(objDate,weekDays)
         
         
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
 return listobjDates,day

def returnMonthNumber(oldDates):
    #month=month.replace(" ","")
    if "January"  in oldDates:
        oldDates = "01"
    elif "February" in oldDates:
        oldDates = "02"
    elif "March" in oldDates:
        oldDates = "03"
    elif "April" in oldDates:
        oldDates = "04"
    elif "May"  in oldDates:
        oldDates = "05"
    elif "June"   in oldDates:
        oldDates = "06"
    elif "July" in oldDates:
        oldDates = "07"
    elif "August"  in oldDates:
        oldDates = "08"
    elif "September" in oldDates: 
        oldDates = "09"
    elif "October"  in oldDates: 
        oldDates = "10"
    elif "November"  in oldDates:
        oldDates = "11"
    elif "December"  in oldDates:
        oldDates = "12"
    else:
        oldDates="00"
    
    return oldDates

def returnMonth(month):

    if month =="01":
      month ="January"

    elif month =="02":
      month ="February"

    elif month =="03":
      month ="March"

    elif month=="04":
        month ="April"

    elif month =="05":
      month ="May"

    elif month =="06":
      month ="June"

    elif month =="07":
      month ="July"

    elif month =="08":
      month ="August"

    elif month =="09":
      month ="September"

    elif month =="10":
      month ="October"

    elif month =="11":
      month ="November"

    elif month =="12":
      month ="December"

    return month

def replaceArabicMonth(text):

    text = text.replace("يناير","January")
    text = text.replace("فبراير","February")
    text = text.replace("مارس","March")
    text = text.replace("ابريل","April")
    text = text.replace("مايو","May")
    text = text.replace("يونيو","June")
    text = text.replace("يوليو","July")
    text = text.replace("اغسطس","August")
    text = text.replace("سبتمبر","September")
    text = text.replace("اكتوبر","October")
    text = text.replace("نوفمبر","November")
    text = text.replace("ديسمبر","December")

    text = text.replace("إكتوبر","October")
    text = text.replace("أكتوبر","October")

    text = text.replace("إغسطس","August")
    text = text.replace("أغسطس","August")

    text = text.replace("إبريل","April")
    text = text.replace("أبريل","April")

    return text

def isEvent(text):
     temp = 0
     index=0
     for i in text :
      temp = i
      print("temp is  ",temp )
      if temp.find("دورة بعنوان") !=-1 or temp.find("دورة :") !=-1 or temp.find("ورشة عمل بعنوان") !=-1 or temp.find("محاضرة بعنوان") !=-1 or temp.find("لقاء ريادي بعنوان") !=-1 or temp.find("محاضرة") !=-1 or temp.find("مخاضرة") !=-1 or temp.find("دورة تدريبية بعنوان") !=-1 or temp.find("تدريبية بعنوان :")!=-1 or temp.find("تدريبية بعنوان")!=-1 or temp.find("تدريبية بعنوان ")!=-1 or temp.find("لحضور دورة:")!=-1 or temp.find("دورة في")!=-1 or temp.find("دورة تطوير")!=-1 or temp.find("مقدمة في")!=-1 or temp.find("Introduction to")!=-1 or temp.find("ورش عمل برنامج")!=-1 or temp.find("دورة")!=-1 or temp.find("تقديم دورة بعنوان:")!=-1  or temp.find(" تقديم دورة بعنوان: ")!=-1 or temp.find("تقديم دورة بعنوان:")!=-1 or temp.find("ندوة بعنوان") !=-1 or temp.find("ندوة")!=-1 or temp.find("اللقاء")!=-1 or temp.find("شهادات حضور") !=-1 or temp.find("شهادة حضور") !=-1 or temp.find("ساعدك هذا البرنامج")!=-1:        
           return True
     return False

def processTime(timePattern1,timeText,timeNum,patternNum,time1):
      am = "0"
      pm = "0"
      temp=""
      print("time  found")
      if(patternNum==1):
       time1 = re.search(timePattern1, timeText).group()
      stringT1 = time1
      am = checkAm(am,time1)
      pm = checkPm(pm,time1)
      if(am ==0 and pm ==0): # this means that its written an 24-H  7:40 (no mention to am or pm)
          am=1
      print("am : ",am)
      print("pm : ",pm)
      print(time1)
      time1=time1.replace(" ","")
      time1=time1.replace("م","")
      time1=time1.replace("ص","")
      time1=time1.replace(":","")
      print("before erorr,",time1)
      time1=int(time1)
      time1=addColon(time1)
      print("len of time is ",len(time1) ,time1)
      #if
      if(len(time1)==4): # it became 4 due to adding : 
          time1 = addZeroToTime(time1)
          
      oldHours= time1[0]+time1[1]
      status24 = is24(oldHours)
      if(status24==False ): # and am ==0
       hours = convertTo24H(time1,am,pm)
       print("hours is ",hours)
       time1=time1.replace(" ","")
       remove = oldHours+":"
       print("rem",remove)
       time1 =time1.replace(remove,"")
       #time1 = time1[:0] + "" + time1[1:]
       # time1 = time1[:1] + "" + time1[2:]
       #time1 = time1[:1] +"" +time1[2:]
       time1 = time1[:0] +str(hours) +time1[0:]
       time1=addColon(time1)
       time1PM=pm
       time1Temp=time1
       if(timeNum==2):
        return time1,time1PM,time1Temp,temp,oldHours
      print("starting time is ",time1)
      temp =timeText.replace(stringT1, "")
      
      return time1,time1PM,time1Temp,temp,oldHours

def updateTime(time,time1Temp): # frogot wha this do 
           time1=time1Temp
           print("no the time1 is ,",time1)
           hours = convertTo24H(time1,0,1)
           time1=time1.replace(" ","")
           oldHours= time1[0]+time1[1]
           remove = oldHours+":"
           print("rem",remove)
           time1 =time1.replace(remove,"")
           #time1 = time1[:0] + "" + time1[1:]
           # time1 = time1[:1] + "" + time1[2:]
            #time1 = time1[:1] +"" +time1[2:]
           time1 = time1[:0] +str(hours) +time1[0:]
           time1=addColon(time1)
           return time1

def formatTime(time):
      time=time.replace(" ","")
      time=time.replace("م","")
      time=time.replace("ص","")
      time=time.replace(":","")
      time=time.replace("من","")
      time=time.replace("من","")

      time = os.linesep.join([s for s in time.splitlines() if s]) # remove empty lines
      timeLen = len(time)
      print("t2 foramt ",timeLen,time)
      time1=""
      time2=""
      if(time[2]=="-"): #10-
          time1=time[0]+time[1]
          time1 = time1[:2]+ "00" +time1[2:]
          if(timeLen==5):#10-11
           time2=time[3]+time[4]
           time2 = time2[:5]+ "00" +time2[5:]
          elif(timeLen==4):#10-11
           time2=time[3]
           time2 = time2[:4]+ "00" +time2[4:]

      elif(time[1]=="-"): #10-
          time1=time[0]
          time1 = time1[:1]+ "00" +time1[1:]
          if(timeLen==4):#10-11
           time2=time[2]+time[3]
           time2 = time2[:4]+ "00" +time2[4:]
          elif(timeLen==3):#10-11
           time2=time[2]
           time2 = time2[:3]+ "00" +time2[3:]


      return time1,time2


    
      


def myReg(myImage) :

#image="8.png"
 print("*******************************************")
 index=0
 topic=""
 imageTest= r"C:\Users\Ammar\Desktop\test\Image Analysis\images\4.jpg"

 #arrayText=ocrAPI(imageTest)
 #text=listToString(arrayText)
 try:
  text =GoogleAPI(imageTest)
  arrayText =ocrAPI(imageTest)
 except :
     print("BAD request from the API")
     sys.exit()

 print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
 print("arraytext[2] ",arrayText[2])
 #arrayText = text.splitlines()
 arrayText= wordCorrection(arrayText)
   
 if(isEvent(arrayText) == False):
     print("This is not an event")
     sys.exit()
   
 
 

 #timeText=OCR2(imageTest)
 #timeText=listToString(timeText)
 #arrayText = text.splitlines()
 #text=listToString(arrayText)
 #arrayText = text.splitlines()
 #text= OCR1(myImage)
 #text2 = OCR2(myImage)
 #text2= wordCorrection(text2)
 #print(text2)
 #print("================================================================************************************")

 topic= exteractTopic(arrayText) # it was arraytext
 if(topic=="Topic not Found"):
     print("nano is stopped temp")
     #topic = nanoNetsAPI(imageTest)

 #arrayText = arrayText.replace("إبريل","April")



 #topic= exteractTopic(text)

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
 m1 ="يناير"
 m2 ="فبراير"
 m3 ="مارس"
 m4 ="ابريل"
 m5 ="مايو"
 m6 ="يونيو"
 m7 ="يوليو"
 m8 ="اغسطس"
 m9 ="اكتوبر"
 m10 ="نوفمبر"
 m11 ="ديسمبر"
 m12 ="إبريل"
 m13 ="أبريل"
 m14 ="أغسطس"
 m15 ="إكتوبر"
 m16 ="أكتوبر"



 #datePattern3 = "\s?\d{4}\s?(March|word2)\s?\d{1,2}\s?"
 #datePattern3 = "\s?\d{4}\s?(January|February|March|April|May|June|July|August|September|October|November|December|يناير|فبراير|مارس|ابريل|مايو|يونيو|يوليو|اغسطس|سبتمبر|اكتوبر|نوفمبر|ديسمبر|إبريل|أغسطس|أكتوبر|)\s?\d{1,2}\s?"
 #datePattern3 = "\s?\d{4}\s?(January|February|March|April|May|June|July|August|September|October|November|December|"+m1+"|"+m2+"|"+m3+"|"+m4+"|"+m5+"|"+m6+"|"+m7+"|"+m8+"|"+m9+"|"+m10+"|"+m11+"|"+m12+"|"+m13+"|"+m14+"|"+m15+"|"+m16+"|"+")\s?\d{1,2}\s?"

 #datePattern4 = "\s?\d{1,2}\s?(January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{4}\s?"
 #datePattern4 = "\d{1,2}\s? |February|March|April|May|June|July|August|September|October|November|December|\s?\d{4}\s?"
 #datePattern4 = "\s?\d{1,2}\s?(|January|February|March|April|May|June|July|August|September|October|November|December|"+m1+"|"+m2+"|"+m3+"|"+m4+"|"+m5+"|"+m6+"|"+m7+"|"+m8+"|"+m9+"|"+m10+"|"+m11+"|"+m12+"|"+m13+"|"+m14+"|"+m15+"|"+m16+"|"")\s?\d{4}\s?"

 #datePattern4 = "\s?\d{1,2}\s?(March|word2)\s?\d{4}\s?"
 #datePattern4 = "\s?\d{1,2}\s?\January|February|March|April|May|June|July|August|September|October|November|December|\s?\d{4}\s?"
 datePattern3 = "\s?\d{4}\s?(January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{1,2}\s?"
 datePattern4 = "\d{1,2}\s? (?:January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{4}\s?"
 
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
 #datePattern3 = "\s?\d{1,2}\s?\d{1,2}\s?\d{4,5}"
 #datePattern4 = "\s?\d{4}\s?\d{1,2}\s?\d{1,2}"

 # 1 = days without Hamza
 # 2 = days with an upper Hamza
 # 3 = days with an lower Hamza
 # 4 = days spelled wrong
 dayPattern1 = r'\االاثنين |الثلوث | الثلاثاء: |الربوع |إثنين|الخميس | الجمعة | السبت | الاربعاء|الاحد| الثلاثاء\b'
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
 v1="أ"
 v2="د"
 v3="م"
 namePattern17=r'\s?'+v1+'\.\s?((?:\w+(?:\s+|$)){2})'
 namePattern18=r'\s?'+v2+'\.\s?((?:\w+(?:\s+|$)){2})'
 namePattern19=r'\s?'+v3+'\.\s?((?:\w+(?:\s+|$)){2})'
 namePattern20=r'المدرب:\s+((?:\w+(?:\s+|$)){2})' 
 namePattern21=r'المدربة:\s+((?:\w+(?:\s+|$)){2})' 
 namePattern22=r'المقدم:\s+((?:\w+(?:\s+|$)){2})' 
 namePattern23=r'المقدمة:\s+((?:\w+(?:\s+|$)){2})' 
 namePattern24=r'تقديم:\s+((?:\w+(?:\s+|$)){2})' 




 namePattern1Bin=r'د\.\s+((?:\w+(?:\s+|$)){3})'
 namePattern2Bin=r'الدكتورة\s+((?:\w+(?:\s+|$)){3})'
 namePattern3Bin=r'الدكتور\s+((?:\w+(?:\s+|$)){3})'
 namePattern4Bin=r'الاستاذ\s+((?:\w+(?:\s+|$)){3})'
 namePattern5Bin=r'الاستاذة\s+((?:\w+(?:\s+|$)){3})'
 namePattern6Bin=r'الأستاذ\s+((?:\w+(?:\s+|$)){3})'
 namePattern7Bin=r'الأستاذة\s+((?:\w+(?:\s+|$)){3})'
 namePattern8Bin=r'أ\.\s+((?:\w+(?:\s+|$)){3})'
 #namePattern8=r'أ\s?.\s?\s?((?:\w+(?:\s+|$)){2})'
 namePattern9Bin=r'الأستاذة /\s+((?:\w+(?:\s+|$)){3})'
 #namePattern10=r' الدكتورة/\s+((?:\w+(?:\s+|$)){2})'
 namePattern10Bin=r'الدكتورة\s?/\s+((?:\w+(?:\s+|$)){3})'
 namePattern11Bin=r'الدكتور\s?/\s+((?:\w+(?:\s+|$)){3})'
 #namePattern11=r'الدكتور/ /\s+((?:\w+(?:\s+|$)){2})'
 namePattern12Bin=r'الطالبة:/\s+((?:\w+(?:\s+|$)){3})'
 namePattern13Bin=r'الطالبة:\s+((?:\w+(?:\s+|$)){3})' 
 namePattern14Bin=r'الأستاذ /\s+((?:\w+(?:\s+|$)){3})'
 namePattern15Bin=r'المهندس\s?/\s+((?:\w+(?:\s+|$)){3})'
 namePattern16Bin=r'المهندسة\s?/\s+((?:\w+(?:\s+|$)){3})'
 namePattern17Bin=r'\s?'+v1+'\.\s?((?:\w+(?:\s+|$)){3})'
 namePattern18Bin=r'\s?'+v2+'\.\s?((?:\w+(?:\s+|$)){3})'
 namePattern19Bin=r'\s?'+v3+'\.\s?((?:\w+(?:\s+|$)){3})'
 namePattern20Bin=r'المدرب:\s+((?:\w+(?:\s+|$)){3})' 
 namePattern21Bin=r'المدربة:\s+((?:\w+(?:\s+|$)){3})' 
 namePattern22Bin=r'المقدم:\s+((?:\w+(?:\s+|$)){3})' 
 namePattern23Bin=r'المقدمة:\s+((?:\w+(?:\s+|$)){3})' 
 namePattern24Bin=r'تقديم:\s+((?:\w+(?:\s+|$)){3})' 

 #namePattern14=r'تقديم\s+((?:\w+(?:\s+|$)){2})' 
 to1 = "الى"
 to2 = "إلى"
 s1 = "p.m"
 s2="a.m"
 #timePattern1= "\s?م?ص?\d{1,2}\s?[:]\s? م?ص? \d{1,2}\s?[:]\s?م?ص?\s?"
 #timePattern1 = "\s?\ص?\م?\d{1,2}\s?\ص?\م?[-,"+to1+","+to2+"][?:,?.]\s?\ص?\م?\d{1,2}?\s?\ص?\م?"
 timePattern1 = "\s?\a\ص?\م?\p?\d{1,2}\s?\ص?\م?[:,.]\s?\ص?\م?\d{1,2}\s?\ص?\م?"
 timePattern2 = "\s?\ص?\م?\d{1,2}\s?\ص?\م?[-]\s?\ص?\م?\d{1,2}\s?\ص?\م?"
 

 # "\s?م?ص?\d{1,2}\s?[:]\s? م?ص? \d{1,2}\s?[:]\s?م?ص?\s?"

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
     
 datePatternStatus= False # for 12 march 2020
 regexFound = False 
 listobjDates=[] 
 x=2
 tempText=""
 Parisian = 0
 indian = 0
 #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
 #print(text)
 #print(0000000000000000000000000000000)
 #print(text.replace("إبريل","April"))
 while (x!=0) :
  print("here") 
  #text = text.replace("إبريل","April")
  text = replaceArabicMonth(text)
  if((re.search(datePattern1, text))):
       regexFound = True 
       datePatternStatus= True
       print("date found 1")
       oldDates = re.findall(datePattern1, text, re.MULTILINE)
       print("old date is",oldDates)
       dates = removeSpace(oldDates)
       dates = remove5(oldDates)
       dates = [i.replace("م", "") for i in oldDates]
       dates = [i.replace("ه", "") for i in oldDates]
       "2/2/2025"
       x=0
       print(1)
       

  elif((re.search(datePattern2, text))):
         regexFound = True 
         datePatternStatus= True
         print("date found 2")
         oldDates = re.findall(datePattern2, text, re.MULTILINE)
         print("old date is",oldDates)
         dates = removeSpace(oldDates)
         dates = remove5(oldDates)
         dates = [i.replace("م", "") for i in oldDates]
         dates = [i.replace("ه", "") for i in dates]
         x=0
         print(2)

  elif((re.search(datePattern3, text))):
         regexFound = True 
         print("date found 3")
         oldDates = re.findall(datePattern3, text, re.MULTILINE)
         oldDates=str(oldDates[0])
         print("old date is",oldDates)
         oldDates= oldDates.replace(" ","")
         day=""
         year=""
         monthNum = returnMonthNumber(oldDates)
         month= returnMonth(monthNum)
         print("the month num is ",monthNum)
        
         oldDates= oldDates.replace(month,monthNum)
         print("old date is now",oldDates)
         print("length is ,",len(oldDates))

         if(len(oldDates)==9): # day consist of two digits
              day =oldDates[6]+oldDates[7]
              year=oldDates[0]+oldDates[1]+oldDates[2]+oldDates[3]

         elif(len(oldDates)==8): # day consist of one digits
              day =oldDates[6]
              year=oldDates[0]+oldDates[1]+oldDates[2]+oldDates[3]
              day= day[:6] + "0" + day[6:]
         print("the day is ",day)
         print("the year is ",day)
         print("the month num is ",monthNum)
         newDate = day+"/"+monthNum+"/"+year
         newDate=newDate.replace(" ","")
         newDate=newDate.replace("  ","")
         if(indian ==1):
           ConvertedDateObject=convert_numbers.hindi_to_english(newDate)
         else:
             ConvertedDateObject=convert_numbers.persian_to_english(newDate)
         print("date after conversion is",ConvertedDateObject)
         newDate = str(ConvertedDateObject)
         newDate= newDate[:4] + "/" + newDate[4:]
         newDate= newDate[:6] + "/" + newDate[6:]
         print("newDate  is ",newDate)
         #dates = removeSpace(oldDates)
         #newDate = remove5(newDate)
         #newDate = [i.replace("م", "") for i in newDate]
         #newDate = [i.replace("ه", "") for i in newDate]
         #objDate = datetime.datetime.strptime(newDate, '%d/%m/%Y')
         day=returnWeekDay(objDate,weekDays)
         listobjDates.insert(0,objDate.date())
         x=0
         print(3)
         

  elif((re.search(datePattern4, text))):
         regexFound = True 
         print("date found 4")
         oldDates = re.findall(datePattern4, text, re.MULTILINE)
         oldDates=str(oldDates[0])
         print("old date is",oldDates)
         oldDates= oldDates.replace(" ","")
         day=""
         year=""
         monthNum = returnMonthNumber(oldDates)
         month= returnMonth(monthNum)
         print("the month num is ",monthNum)
        
         oldDates= oldDates.replace(month,monthNum)
         print("old date is now",oldDates)
         print("length is ,",len(oldDates))

         if(len(oldDates)==9): # day consist of two digits
              day =oldDates[0]+oldDates[1]
              year=oldDates[4]+oldDates[5]+oldDates[6]+oldDates[7]

         elif(len(oldDates)==8): # day consist of one digits
              day =oldDates[0]
              year=oldDates[3]+oldDates[4]+oldDates[5]+oldDates[6]
              day= day[:0] + "0" + day[0:]
         print("the day is ",day)
         print("the year is ",day)
         print("the month num is ",monthNum)
         newDate = day+"/"+monthNum+"/"+year
         newDate=newDate.replace(" ","")
         newDate=newDate.replace("  ","")
         if(indian ==1):
           ConvertedDateObject=convert_numbers.hindi_to_english(newDate)
         else:
             ConvertedDateObject=convert_numbers.persian_to_english(newDate)

         print("date after conversion is",ConvertedDateObject)
         objDate=newDate
         #newDate = str(ConvertedDateObject)
         #newDate= newDate[:2] + "/" + newDate[2:]
         #newDate= newDate[:5] + "/" + newDate[5:]
        # print("newDate  is ",newDate)
         #dates = removeSpace(oldDates)
         #newDate = remove5(newDate)
         #newDate = [i.replace("م", "") for i in newDate]
         #newDate = [i.replace("ه", "") for i in newDate]
         listobjDates.insert(0,newDate)
         objDate = datetime.strptime(newDate, '%d/%m/%Y')
         day=returnWeekDay(objDate,weekDays)
         print("day is now.",day)
         x=0
         print(4)
         
  else :
     print("no date was found")
        
        

  if(datePatternStatus):
   DatesLength = len(dates)
   listobjDates,day= processDate(DatesLength,listobjDates,weekDays,dates,day,indian)
   
  if(x==1):
      break
  if(regexFound==False):
    tempText = text
    text = str(arrayText)
    x=x-1
    indian = 1  

  #replacedText = text.replace("إبريل","April")
  #text = replacedText
 




 instructor="not found"
 


 
#  text = text.replace("يسر عمادة شؤون","ن")
#  print(text)
#  print("000000000000000000000000000")

 print ("testing instructor ")
 
 if((re.search(namePattern1, text))):
        print("found 1")
        instructor = re.search(namePattern1, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern1Bin, text).group()
        
 elif((re.search(namePattern2, text))):
        print("found 2")
        instructor = re.search(namePattern2, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern2Bin, text).group()

 elif((re.search(namePattern3, text))):
        print("found 3")
        instructor = re.search(namePattern3, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern3Bin, text).group()

 elif((re.search(namePattern4, text))):
        print("found 4")
        instructor = re.search(namePattern4, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern4Bin, text).group()

 elif((re.search(namePattern5, text))):
        print("found 5")
        instructor = re.search(namePattern5, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern5Bin, text).group()

 elif((re.search(namePattern6, text))):
        print("found 6")
        instructor = re.search(namePattern6, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern6Bin, text).group()

 elif((re.search(namePattern7, text))):
        print("found 7")
        instructor = re.search(namePattern7, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern7Bin, text).group()

 elif((re.search(namePattern8, text))):
        print("found 8")
        instructor = re.search(namePattern8, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern8Bin, text).group()

 elif((re.search(namePattern9, text))):
        print("found 9")
        instructor = re.search(namePattern9, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern9Bin, text).group()

 elif((re.search(namePattern10, text))):
        print("found 10")
        instructor = re.search(namePattern10, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern10Bin, text).group()

 elif((re.search(namePattern11, text))):
        print("found 11")
        instructor = re.search(namePattern11, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern11Bin, text).group()

 elif((re.search(namePattern12, text))):
        print("found 12")
        instructor = re.search(namePattern12, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern12Bin, text).group()

 elif((re.search(namePattern13, text))):
        print("found 13")
        instructor = re.search(namePattern13, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern13Bin, text).group()

 elif((re.search(namePattern14, text))):
        print("found 14")
        instructor = re.search(namePattern14, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern14Bin, text).group()

 elif((re.search(namePattern15, text))):
        print("found 15")
        instructor = re.search(namePattern15, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern15Bin, text).group()

 elif((re.search(namePattern16, text))):
        print("found 16")
        instructor = re.search(namePattern16, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern16Bin, text).group()

 elif((re.search(namePattern17, text))):
        print("found 17")
        instructor = re.search(namePattern17, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern17Bin, text).group()

 elif((re.search(namePattern18, text))):
        print("found 18")
        instructor = re.search(namePattern18, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern18Bin, text).group()

 elif((re.search(namePattern19, text))):
        print("found 19")
        instructor = re.search(namePattern19, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern19Bin, text).group()

 elif((re.search(namePattern20, text))):
        print("found 19")
        instructor = re.search(namePattern20, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern20Bin, text).group()

 elif((re.search(namePattern21, text))):
        print("found 21")
        instructor = re.search(namePattern21, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern21Bin, text).group()

 elif((re.search(namePattern22, text))):
        print("found 22")
        instructor = re.search(namePattern22, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern22Bin, text).group()

 elif((re.search(namePattern23, text))):
        print("found 23")
        instructor = re.search(namePattern23, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern23Bin, text).group()

 elif((re.search(namePattern24, text))):
        print("found 24")
        instructor = re.search(namePattern24, text).group()
        if "بن" in instructor:
            instructor = re.search(namePattern24Bin, text).group()
    

 if(instructor=="not found"):
     print("regex did not work for instructor")
     instructor=exteractInstructor(arrayText)

    

 #print("hatha ","." in instructor)
 
 instructor=nameCorrection(instructor)


 timePattern1 = "\s?\ص?\م?\d{1,2}\s?\ص?\م?[:]\s?\ص?\م?\d{1,2}\s?\ص?\م?"
 timeText=GoogleAPI(imageTest)
 time1=""
 time2=""
 time1PM=0
 time2PM=0
 time1Temp=""
 print("==============================")

 if(re.search(timePattern1, timeText)):
    
      time1,time1PM,time1Temp,temp,oldHours=processTime(timePattern1,timeText,1,1,time1)
        
      if(re.search(timePattern1, temp)):
        time2,time2PM,time2Temp,temp,oldHours=processTime(timePattern1,temp,2,1,time2)
        
       #if(len(time2)==2):
          # time2 = time2[:2] + "0" +time2[2:]
           #time2 = time2[:3] + "0" +time2[3:]

      #time1 = time1[:0] + "" + time1[1:]
      # time1 = time1[:1] + "" + time1[2:]
      #time1 = time1[:1] +"" +time1[2:]
   

      if(time2PM ==1 and oldHours!=12):
          time1=updateTime(time1,time1Temp)

      #print("finishing time is ",time2)
      print("T1")

 elif(re.search(timePattern2, timeText)) :
     time = re.search(timePattern2, timeText).group()
     print("t2 time is, ",time)
     time1,time2 = formatTime(time)
     print("time 1,",time1)
     print("time 2,",time2)
     time1,time1PM,time1Temp,temp,oldHours=processTime(timePattern2,timeText,1,2,time1)

     if(re.search(timePattern2, temp)):
        time2,time2PM,time2Temp,temp,oldHours=processTime(timePattern2,temp,2,2,time2)
   
        if(time2PM ==1 and oldHours!=12):
          time1=updateTime(time1,time1Temp)

      #print("finishing time is ",time2)
        print("T2")



 else:
      print(" time not found")
 print("len of dates is : ",len(listobjDates))

 instructor=instructor.replace("\n","")
 topic=topic.replace("\n","")
 day=day.replace("\n","")
 if(len(listobjDates)==0):
   event = Event(topic,0.0,day,instructor,time1,time2)

 else:
  event = Event(topic,listobjDates[0],day,instructor,time1,time2)
 #jsonEvent = json.dumps(event.__dict__)
 jd = json.dumps(event.__dict__, ensure_ascii=False,indent=4, sort_keys=True, default=str)
 #jsonEvent.encode
 #jsonEvent=json.dumps(event, ensure_ascii = False)

 print(jd)
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

 print(text)


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
