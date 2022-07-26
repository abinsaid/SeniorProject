
# This Python file uses the following encoding: utf-8
#from curses.ascii import isdigit
from ntpath import join
from operator import length_hint
import os
import sys
import unicodedata
import re  # for using a regix
from datetime import datetime
from matplotlib.pyplot import text
import convert_numbers  # for converting from arabic digits to english
from hijri_converter import Hijri, Gregorian  # for converting from hijri
#from ocr import*
from ocr_with_api import*  # an ocr that uses api
from Event import*  # event object
#import numpy as np  # used for array
import datetime  # to create an object of type Date
# import pandas as pd
import json
import pymongo
from GoogleCalendar import addToGoogleCalendar
from datetime import datetime  # maybe cause an erorr
# note : for extracting topic and instructor name we have two approches
# approches 1 (line extaction) : detact a spesfic word such as "course about" and then return the word in the next line
# approches 2 (model extaction) : by feeding a set of images to model and then it will detact instructor and event

# the following method is for detacting the day using a set of pretected words that will be read


def returnDay(day):

    if day == "الأحد" or day == "الاحد" or day == "الإحد" or day == "احد" or day == "أحد" or day == "الاجد":
        day = "Sunday"
        return day

    elif day == "الاثنين" or day == "الأثنين" or day == "الإثنين" or day == "اثنين" or day == "أثنين" or day == "إثنين":
        day = "Monday"
        return day

    elif day == "الثلاثاء" or day == "الثلوث" or day == " 'الثلاثاء " or day == "الثلاثاء:":
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



def exteractTopic(words):
    temp = 0
    index = 0
    for i in words:
        temp = i
        if temp.find("دورة بعنوان") != -1 or temp.find("دورة :") != -1 or temp.find("ورشة عمل بعنوان") != -1 or temp.find("محاضرة بعنوان") != -1 or temp.find("لقاء ريادي بعنوان") != -1 or temp.find("محاضرة") != -1 or temp.find("مخاضرة") != -1 or temp.find("دورة تدريبية بعنوان") != -1 or temp.find("تدريبية بعنوان :") != -1 or temp.find("تدريبية بعنوان") != -1 or temp.find("تدريبية بعنوان ") != -1 or temp.find("لحضور دورة:") != -1 or temp.find("دورة في") != -1 or temp.find("دورة تطوير") != -1 or temp.find("مقدمة في") != -1 or temp.find("Introduction to") != -1 or temp.find("ورش عمل برنامج") != -1 or temp.find("دورة") != -1 or temp.find("تقديم دورة بعنوان:") != -1 or temp.find(" تقديم دورة بعنوان: ") != -1 or temp.find("تقديم دورة بعنوان:") != -1 or temp.find("ندوة بعنوان") != -1:
            index = index+1
            return words[index]
        index = index+1


    return "Topic not Found"



def exteractInstructor(words):
    temp = 0
    index = 0
    for i in words:
        temp = i
        if temp.find("الدكتور") != -1 or temp.find("يقدمها الدكتودا") != -1 or temp.find("يقدمها") != -1 or temp.find("مقدم الدورة") != -1:
            print("found instructor")
            index = index+1
            return words[index]
        index = index+1
    return "Instructor not Found"




def isOnline(words):
    temp = 0
    index = 0
    for i in words:
        temp = i
        if ( temp.find("اونلاين")!=-1 or temp.find("أونلاين")!=-1 or temp.find("online")!=-1 or temp.find("blackboard")!=-1 or temp.find("BlackBoard")!=-1 or temp.find("Blackboard")!=-1 or temp.find("zoom")!=-1 or temp.find("Zoom")!=-1 or temp.find("عن بعد")!=-1 or temp.find(" zoom ")!=-1 or temp.find("البلاك بورد") !=-1):
            temp = "Online"
            return temp
       # index = index+1
    return "in Person"


def interestTechnology(words):
    temp = 0
    index = 0
    for i in words:
        temp = i
        if (temp.find("برمجة")!=-1 or  temp.find("البرمجة")!=-1 or temp.find("امن المعلومات")!=-1 or temp.find("أمن المعلومات")!=-1 or temp.find("السيبراني")!=-1 or temp.find("تطوير التطبيقات")!=-1 or temp.find("تصميم الواجهات")!=-1 or temp.find("تحليل البيانات")!=-1 or temp.find("بايثون")!=-1 or temp.find("البايثون")!=-1 or temp.find("جافا")!=-1 or temp.find("الجافا")!=-1 or temp.find("اونلاين")!=-1 or temp.find("تصميم الواجهات")!=-1 or temp.find("اونلاين")!=-1 or temp.find("تطوير الواجهة")!=-1 or temp.find("تعليم الالة")!=-1 or temp.find("تعليم الآلة")!=-1 or temp.find("تعلم الالة")!=-1 or temp.find("تعلم الآلة")!=-1 or temp.find("قواعد البيانات")!=-1 or temp.find("قاعدة بيانات")!=-1 or  temp.find("قاعدة البيانات")!=-1 ):
            #temp = "Online"
            return "1"
       # index = index+1
    return "0"


def interestSoftSkills(words):
    temp = 0
    index = 0
    for i in words:
        temp = i
        if temp.find("الهندسة الاجتماعية")!=-1 or temp.find("الهندسة الإجتماعية")!=-1 or temp.find("علم الاجتماع")!=-1 or temp.find("علم الإجتماع")!=-1  or temp.find("تطوير الذات")!=-1 or  temp.find("بناء الشخصية")!=-1 or temp.find("اختيار التخصص")!=-1 or temp.find("إختيار التخصص")!=-1 or temp.find("المهارات الشخصية")!=-1 :
            return "1"
    return "0"


def interestManagment(words):
    temp = 0
    index = 0
    for i in words:
        temp = i
        if temp.find("ادارة الوقت")!=-1 or temp.find("إدراة الوقت") or temp.find("إدراة المشاريع") or temp.find("ادارة المشاريع")   :
            return "1"
    return "0"







# a method that correct expected errors in names


def nameCorrection(name):
    if(name.find("هافي") != -1):
        name = name.replace("هافي", "هاني")

    if(name.find("برديي") != -1):
        name = name.replace("برديي", "برديسي")
    if(name.find("دسين") != -1):
        name = name.replace("دسين", "حسين")
    if(name.find("ها دية") != -1):
        name = name.replace("ها دية", "هادية")
    if(name.find("الحاري") != -1):
        name = name.replace("الحاري", "الحارثي")
    if(name.find("معصم") != -1):
        name = name.replace("معصم", "معتصم")
    if(name.find("حالد") != -1):
        name = name.replace("حالد", "خالد")

    return name


def convertArabicDigitsToEnglish(x, indian): # x = the number before conversion
    temp1 =""
    temp2 =""
    newDate=""
     # Google OCR
    #print("date before indian",x)
    temp1 = convert_numbers.hindi_to_english(x)
    #print("date after indian",temp1)
   # print("i am indian")
    # Space OCR
    temp2 = convert_numbers.persian_to_english(x)
    temp1=temp1.replace(" ","")
    temp2=temp2.replace(" ","")
    print("temp1 is : ",temp1)
    print("temp2 is : ",temp2)
    if(temp1=="1443//" or temp1=="//" or "1443" or "/"):
        newDate=temp2
    elif(temp2=="1443//" or temp2=="//" or "1443" or "/"):
        newDate=temp1

    print("newDate is :",newDate)

    x = x.replace(" ", "")
    newDate = newDate.replace(" ", "")
    if x[2] == "/" and x[5] == "/":  # 20/01/2017 : dd/dd/dddd  2 dig 2 dig 4 dig
        newDate = newDate[:2] + "/" + newDate[2:]
        newDate = newDate[:5] + "/" + newDate[5:]

    elif x[4] == "/" and x[7] == "/":  # 2017/20/12 : dddd/dd/dd  
        newDate = newDate[:4] + "/" + newDate[4:]
        newDate = newDate[:7] + "/" + newDate[7:]

    elif x[2] == "/" and x[4] == "/":  # 12/3/2020 : dd/d/dddd
        newDate = newDate[:2] + "/" + newDate[2:]
        newDate = newDate[:4] + "/" + newDate[4:]

    elif x[1] == "/" and x[4] == "/":  # 9/12/2020 : d/dd/dddd
        newDate = newDate[:1] + "/" + newDate[1:]
        newDate = newDate[:4] + "/" + newDate[4:]

    elif x[4] == "/" and x[6] == "/":  # 2012/1/12: dddd/d/dd
        newDate = newDate[:4] + "/" + newDate[4:]
        newDate = newDate[:6] + "/" + newDate[6:]

    elif x[4] == "/" and x[7] == "/":  # 2003/12/22 yyyy/dd/dd (duplicated)
        newDate = newDate[:4] + "/" + newDate[4:]
        newDate = newDate[:7] + "/" + newDate[7:]

    elif x[1] == "/" and x[3] == "/":  # 7/7/2020 : d/d/dddd
        newDate = newDate[:1] + "/" + newDate[1:]
        newDate = newDate[:3] + "/" + newDate[3:]

    elif x[4] == "/" and x[6] == "/":  # 2020/5/2 :dddd/dd/dd

        newDate = newDate[:4] + "/" + newDate[4:]
        newDate = newDate[:6] + "/" + newDate[6:]


    return newDate



# convert from hifri date
def convertFromHijri(y, m, d):
    convertedDate = Hijri(y, m, d).to_gregorian() # output is of type hijri_converter 
    convertedDate = x = datetime(convertedDate.year, convertedDate.month, convertedDate.day) # output = date obj
    return convertedDate



# to check if the two dates are equal or not (used for comparing the georgian date and the converted hijri date)

def compareTwoDates(d1, d2):
    if(d1 == d2):
        return True
    else:
        return False

# add zeros in single digits date, for standardization

def addZero(s):

    s = s.replace(" ", "")
    s = s.replace("  ", "")
    s = os.linesep.join([s for s in s.splitlines() if s])
    if(len(s) == 10):  # 03/09/2020
        return s
        
    try : 
       if (s[0].isdigit() and s[1] == "/") and (s[2].isdigit() and s[3] == "/" and s[1] == "/"):  # 3/4/
        s = s[:0] + "0" + s[0:]
        s = s[:3] + "0" + s[3:]

       elif (s[0].isdigit() and s[1] == "/" and s[4] == "/"):  # 1/02/
        s = s[:0] + "0" + s[0:]

       elif s[3].isdigit() and s[4] == "/" and s[2] == "/":  # 10/2/
        s = s[:3] + "0" + s[3:]

       elif (s[5].isdigit() and s[6] == "/" and s[4] == "/") and (s[7].isdigit() and (len(s)-1) == 7 and s[6] == "/"):  # 2000/5/2

        s = s[:5] + "0" + s[5:]
        s = s[:8] + "0" + s[8:]

       elif s[5].isdigit() and s[6].isdigit() and s[4] == "/" and s[7] == "/" and s[8].isdigit() and (len(s)-1 == 8):  # 2012/12/1
        s = s[:8] + "0" + s[8:]

       elif s[4] == "/" and s[5].isdigit() and s[6] == "/" and s[7].isdigit():  # 2007/5/13
        s = s[:5] + "0" + s[5:]
    except IndexError : 
        print("")
    finally : 
     return s




# used for correcting a set of words that are frequently read wrong by ocr


def wordCorrection(words,num):

 if(num==2): # space ocr
    length = len(words)
    k = 0
    while k < length: # looping throug the array of space ocr text 

        temp = words[k]
        if temp.find("البر مجة") != -1:
            temp = temp.replace("البر مجة", "البرمجة")
            words[k] = temp
            print("corrected")
            print(temp)

        if temp.find("حفور") != -1:
            temp = temp.replace("حفور", "حضور")
            words[k] = temp
            print("corrected")
            print(temp)

        if temp.find("صباگا") != -1:
            temp = temp.replace("صباگا", "صباحا")
            words[k] = temp
            print("corrected")
            print(temp)

        if temp.find("لاورة") != -1:
            temp = temp.replace("لاورة", "دورة")
            words[k] = temp
            print("corrected")
            print(temp)

        k = k+1

    return words

 if (num==1):
     words = words.replace("صباگا","صباحا")
     words = words.replace("لاورة","دورة")
     return words







# check if the constucted date is valid date or not

def validateDate(day, month, year):

    isValidDate = True
    try:
        datetime(int(year), int(month), int(day)) # an exeption will be thrown if the data was not valid ex: 20222
    except ValueError: 
        isValidDate = False

    if(isValidDate):
        return True
    else:
        return False

# to check if this date is hijri or not, if 144 was spotted this means that its a hijri


def isHijri(date):

    if "144" in date:
        return True
    else:
        return False


def removeSpace(dates):

    for i, val in enumerate(dates):  # using enumerate bacuse dates is an array 
        value = ""
        val2=""
        temp1 = ""
        value = dates[i] # value will store the date 
        for j, val2 in enumerate(value):
            k = j+1 # to check if findished or not
            length = len(value)
            if(length-k == 1): # if len =4 and k=3 .. this means that it is the final index
                break

            if(value[j] == " "):

                temp1 = value[j]
                value = value.replace(temp1, "")
                dates[i] = value
                break

    return dates



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

            if(value[j] == "/" and value[k] == "٥"): #/ه

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


def addColon(time):
    t = str(time)
    if(len(t) == 3):
        t = t[:1] + ":" + t[1:]

    elif (len(t) == 4):
        t = t[:2] + ":" + t[2:]

    return t


def checkAm(am, t):
    if "ص" in t or "صباحا" in t or "الصباح" in t or "am" in t or "AM" in t or "A.M"in t or "a.m" in t:  # ىخف صخقنهىل
        am = 1
        print("found am")
    else:
        am = 0

    return am


def checkPm(pm, t):
    if "م" in t or "مساءا" in t or "مساء" in t or "المساء"  in t  or "pm" in t or "PM" in t or "P.M"in t or "p.m" in t:
        print("found pm")
        pm = 1

    else:
        pm = 0

    return pm





def is24(t, am, pm):
    t = int(t)
    if(am == "0" and pm == "0"):
        return True
    if((t >= 13) and t < 24) or t == "00":
        return True
    else:
        return False


def convertTo24H(t, am, pm):
    t = t[0]+t[1]
    if(am == 0 and pm == 0):
        return t

    if(am == 1):

        if(t == "12"):
             t="00"

        return t

    else:

        if(t == "01"):
            t = "13"

        elif (t == "02"):
            t = 14

        elif (t == "03"):
            t = 15

        elif (t == "04"):
            t = 16

        elif (t == "05"):
            t = 17

        elif (t == "06"):
            t = 18

        elif (t == "07"):
            t = 19

        elif (t == "08"):
            t = 20

        elif (t == "09"):
            t = 21

        elif (t == "10"):
            t = 22

        elif (t == "11"):
            t = 23

        return t


def addZeroToTime(t):
    t = t[:0] + "0" + t[0:]
    return t


def returnWeekDay(objDate, weekDays):
    day = weekDays[objDate.date().weekday()]
    return day


def processDate(DatesLength, listobjDates, weekDays, dates, day, indian):
    day = "no day was found"
    j = 0
    finalDateSatus = ""
    while j < DatesLength:
        temp = str(dates[j])
        print("dates are ,",dates)
        j = j+1
        temp = temp.replace("م", "")
        temp = temp.replace(" ", "")
        temp = temp.replace("00:00:00","")
        temp = os.linesep.join([s for s in temp.splitlines() if s])
        temp = temp.replace("۱۶۶۳","1443")
        temp = str(temp)
        print("date before ",temp)
        temp = convertArabicDigitsToEnglish(temp, indian) 
        print("date after arabic ",temp)
        temp = addZero(temp)
        print("date after ",temp)
        objDate = datetime(1999, 8, 3) # temp value
        if(len(temp)<5):
             continue
        #2020/
        if temp[2].isdigit() and temp[3].isdigit() and temp[1].isdigit() and temp[4] == "/" and temp[0].isdigit(): #2020/

            temp = datetime.strptime(temp, "%Y/%m/%d").strftime("%d/%m/%Y")
            objDate = datetime.strptime(temp, '%d/%m/%Y')
            #objDate = temp
            t = datetime(objDate.year, objDate.month, objDate.day, 0, 0)
            t.strftime('%d/%m/%Y')

        elif temp[0].isdigit() and temp[1].isdigit() and temp[2] == "/": #03/
            temp = datetime.strptime(temp, "%d/%m/%Y").strftime("%d/%m/%Y")
            objDate = datetime.strptime(temp, '%d/%m/%Y')
            #objDate = temp
            t = datetime(objDate.year, objDate.month, objDate.day, 0, 0)
            t.strftime('%d/%m/%Y')

        dateSatus = isHijri(temp)
        if(dateSatus == True):
            objDate = convertFromHijri(
                objDate.date().year, objDate.date().month, objDate.date().day)
        if(day == "no day was found"):
            day = returnWeekDay(objDate, weekDays)


        listobjDates.insert(0, objDate.date())

    if(len(listobjDates) == 2):
        finalDateSatus = compareTwoDates(listobjDates[0], listobjDates[1])



    return listobjDates, day


def returnMonthNumber(oldDates):
    #month=month.replace(" ","")
    if "January" in oldDates:
        oldDates = "01"
    elif "February" in oldDates:
        oldDates = "02"
    elif "March" in oldDates:
        oldDates = "03"
    elif "April" in oldDates:
        oldDates = "04"
    elif "May" in oldDates:
        oldDates = "05"
    elif "June" in oldDates:
        oldDates = "06"
    elif "July" in oldDates:
        oldDates = "07"
    elif "August" in oldDates:
        oldDates = "08"
    elif "September" in oldDates:
        oldDates = "09"
    elif "October" in oldDates:
        oldDates = "10"
    elif "November" in oldDates:
        oldDates = "11"
    elif "December" in oldDates:
        oldDates = "12"
    else:
        oldDates = "00"

    return oldDates


def returnMonth(month):

    if month == "01":
        month = "January"

    elif month == "02":
        month = "February"

    elif month == "03":
        month = "March"

    elif month == "04":
        month = "April"

    elif month == "05":
        month = "May"

    elif month == "06":
        month = "June"

    elif month == "07":
        month = "July"

    elif month == "08":
        month = "August"

    elif month == "09":
        month = "September"

    elif month == "10":
        month = "October"

    elif month == "11":
        month = "November"

    elif month == "12":
        month = "December"

    return month


def replaceArabicMonth(text):

    text = text.replace("يناير", "January")
    text = text.replace("فبراير", "February")
    text = text.replace("مارس", "March")
    text = text.replace("ابريل", "April")
    text = text.replace("مايو", "May")
    text = text.replace("يونيو", "June")
    text = text.replace("يوليو", "July")
    text = text.replace("اغسطس", "August")
    text = text.replace("سبتمبر", "September")
    text = text.replace("اكتوبر", "October")
    text = text.replace("نوفمبر", "November")
    text = text.replace("ديسمبر", "December")

    text = text.replace("إكتوبر", "October")
    text = text.replace("أكتوبر", "October")

    text = text.replace("إغسطس", "August")
    text = text.replace("أغسطس", "August")

    text = text.replace("إبريل", "April")
    text = text.replace("أبريل", "April")

    return text


def isEvent(text):
    temp = 0
    index = 0
    for i in text:
        temp = i
        print("temp is  ", temp)
        if temp.find("دورة بعنوان") != -1 or temp.find("دورة :") != -1 or temp.find("ورشة عمل بعنوان") != -1 or temp.find("محاضرة بعنوان") != -1 or temp.find("لقاء ريادي بعنوان") != -1 or temp.find("محاضرة") != -1 or temp.find("مخاضرة") != -1 or temp.find("دورة تدريبية بعنوان") != -1 or temp.find("تدريبية بعنوان :") != -1 or temp.find("تدريبية بعنوان") != -1 or temp.find("تدريبية بعنوان ") != -1 or temp.find("لحضور دورة:") != -1 or temp.find("دورة في") != -1 or temp.find("دورة تطوير") != -1 or temp.find("مقدمة في") != -1 or temp.find("Introduction to") != -1 or temp.find("ورش عمل برنامج") != -1 or temp.find("دورة") != -1 or temp.find("تقديم دورة بعنوان:") != -1 or temp.find(" تقديم دورة بعنوان: ") != -1 or temp.find("تقديم دورة بعنوان:") != -1 or temp.find("ندوة بعنوان") != -1 or temp.find("ندوة") != -1 or temp.find("اللقاء") != -1 or temp.find("شهادات حضور") != -1 or temp.find("شهادة حضور") != -1 or temp.find("ساعدك هذا البرنامج") != -1 or temp.find("عن فعالية") != -1 or temp.find("ورشة عمل بعـنـوان") != -1 or temp.find("ورشة عمل") != -1 or temp.find("المدرب")!=-1 or temp.find("فاعلية")!=-1 or temp.find("ونقاط لاصفية")!=-1 or temp.find("نقاط لاصفية")!=-1 or temp.find("المحاور")!=-1 or temp.find("الملتقى")!=-1 or temp.find("دوره")!=-1 or temp.find("الدوره")!=-1 or temp.find("الدوره ")!=-1 or temp.find("دوره ")!=-1 or temp.find("دورة ")!=-1 or temp.find("دورة")!=-1 or temp.find("الدورة")!=-1 or temp.find("الدورة ")!=-1 or temp.find("دورة ")!=-1 or temp.find("دورة ")!=-1:
            return True
        if temp.find("استبيان")!=-1 or  temp.find("إستبيان")!=-1 or temp.find("استبانة")!=-1 or temp.find("إستبانة")!=-1 or temp.find("مسابقة")!=-1 :
            return False
    return False


def processTime(timePattern1, timeText, timeNum, patternNum, time1):
    am = "0"
    pm = "0"
    temp = ""
    time1PM = ""
    time1Temp = ""
    time1AM=""
    copyOfStringT1=""
    print("time  found")
    if(patternNum == 1): 
        time1 = re.search(timePattern1, timeText).group()
    stringT1 = time1
    copyOfStringT1=time1

    timeValue = ""
    counter=0
    splitTime=re.split('(\d+)',copyOfStringT1)
    print("time 1 ",time1)
    while(counter<len(splitTime)):
      print("i am inside loop")
      try :    
       if(time1[counter].isalpha()):
        timeValue=splitTime[counter]
        print("timeValue==",timeValue)
        break
       else:
          break
      except Exception:
       break
       print("time expt")
       timeValue="0"
       
    print("test 123")
    counter=counter+1
    time1 = time1.replace(timeValue,"") 
    am = checkAm(am, timeValue)
    pm = checkPm(pm, timeValue)
    if(pm ==0 and am ==0):
     am = checkAm(am, time1)
     pm = checkPm(pm, time1)
   # amPM = checkTimeValue(timeValue)
    if(am == 0 and pm == 0):  # this means that its written an 24-H  7:40 (no mention to am or pm)
        # am=1]
        print("test")
    print("am : ", am)
    print("pm : ", pm)
    print(time1)
    time1 = time1.replace(" ", "")
    time1 = time1.replace("م", "")
    time1 = time1.replace("ص", "")
    time1 = time1.replace(":", "")
    time1 = os.linesep.join([s for s in time1.splitlines() if s])
    print("after replacing chars ,", time1)
    if "."in time1:
        time1="0"
        return "0","0","0","0","0","0","0"
    time1 = int(time1)
    copyOfStringT1=time1
    time1 = addColon(time1)
    print("len of time is ", len(time1), time1)
    # if
    if(len(time1) == 4):  # it became 4 due to adding :
        time1 = addZeroToTime(time1) #convert 7 ==== 07
        copyOfStringT1= str(copyOfStringT1)
        copyOfStringT1 = copyOfStringT1[:0] + "" + copyOfStringT1[0:]
        copyOfStringT1 = copyOfStringT1[:1] + "" + copyOfStringT1[1:]
        print("copyOfStringT1",copyOfStringT1)



    oldHours = time1[0]+time1[1]
    status24 = is24(oldHours, am, pm)
    if(status24 == False):  # and am ==0
        hours = convertTo24H(time1, am, pm)
        #if(timeNum==1):
         #hours = ChecktimeStatus(time1)
        print("hours after converstion  is ", hours)
        time1 = time1.replace(" ", "")
        remove = oldHours+":"
        print("rem", remove)
        time1 = time1.replace(remove, "")
        time1 = time1[:0] + str(hours) + time1[0:]
        time1 = addColon(time1)
        time1PM = pm
        time1AM=am
        time1Temp = time1
        if(timeNum == 2):
            return time1, time1PM, time1Temp, temp, oldHours,time1AM,copyOfStringT1
    print(" time is ", time1)
    temp = timeText.replace(stringT1, "")

    return time1, time1PM, time1Temp, temp, oldHours,time1AM,copyOfStringT1





def formatTime(time): # for pattern 2 which take 2 numbers
    time = time.replace(" ", "")
    time = time.replace("م", "")
    time = time.replace("ص", "")
    time = time.replace(":", "")
    time = time.replace("من", "")
    time = time.replace("من", "")

    # remove empty lines
    time = os.linesep.join([s for s in time.splitlines() if s])
    timeLen = len(time)
    time1 = ""
    time2 = ""
    if(time[2] == "-"):  # 10-
        time1 = time[0]+time[1]
        time1 = time1[:2] + "00" + time1[2:]
        if(timeLen == 5):  # -11
            time2 = time[3]+time[4]
            time2 = time2[:5] + "00" + time2[5:]
        elif(timeLen == 4):  # -1
            time2 = time[3]
            time2 = time2[:4] + "00" + time2[4:]

    elif(time[1] == "-"):  # 1-
        time1 = time[0]
        time1 = time1[:1] + "00" + time1[1:]
        if(timeLen == 4):  # -11
            time2 = time[2]+time[3]
            time2 = time2[:4] + "00" + time2[4:]
        elif(timeLen == 3):  # -1
            time2 = time[2]
            time2 = time2[:3] + "00" + time2[3:]

    return time1, time2


def checkTimeDifference(t1, t2):
    t1 = t1[0]+t1[1]
    t2 = t2[0]+t2[1]
    t1 = int(t1)
    t2 = int(t1)
    if(t2 > t1 and (t2-t1) < 6):
        t1 = 1

def checkInPerson(text):
    temp = "عمادة شؤون المكتبات"
    if temp in text :
        return "online"
    else : 
        return "in Person"




def ChecktimeStatus (time1):

    if(time1=="23"):
        time1= "11"

    elif(time1=="1"):
       time1= "13"


    elif(time1=="2"):
        time1= "14"


    elif(time1=="3"):
       time1= "15"

    
    elif(time1=="4"):
         time1= "16"


    elif(time1=="5"):
         time1= "17"


    elif(time1=="6"):
        time1= "18"



def insertEvent(jd):
    jsonObject = json.loads(jd)
    # return "test"
    cluster = pymongo.MongoClient("mongodb+srv://Byanati:AAA123321@cluster0.kioeq.mongodb.net/ProjectDB?retryWrites=true&w=majority", connect=False)
    db = cluster["ProjectDB"]
    collection = db["events"]
    post = {

        "Topic": jsonObject["topic"],
        "Instructor":jsonObject["instructor"],
        "Day": jsonObject["day"],
        "Date": jsonObject["date"],
        "Starting": jsonObject["startingTime"],
        "Ending": jsonObject["endingTime"],
        "Link": jsonObject["link"],
        "Technology": jsonObject["intrestTechnology"],
        "SoftSkills":jsonObject["intrestSoftSkills"],
        "Managment":jsonObject["interestManagment"],
        "ImageUrl":jsonObject["image_url"]

    }
    collection.insert_one(post)
    print("event has been added to the database")


def myReg(imageTest, websiteLink,image_url,testing):
   
    index = 0
    topic = ""
    imageName=imageTest
    imageName = imageTest.replace(".jpg", "")
    imageName = imageName.replace(r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\mailsFolder\\", "")
    imageName = imageName.replace(r"C:\Users\3boody\Desktop\test\Image Analysis\images\\","")
    imageName =imageName.replace(r"\\C:\\Users\\3boody\\Desktop\\test\\Image Analysis\\images\\","")
    text = ""
    arrayText = ""
    try:
        text = GoogleAPI(imageTest) 
        print(text)
        arrayText = ocrAPI(imageTest) # return an array, each line in an index
    except (IndexError,requests.exceptions.RequestException,AttributeError,ValueError) :
        print("BAD request from the API")
        myReg(imageTest,websiteLink,image_url)


  
    arrayText = wordCorrection(arrayText,2 )
    text = wordCorrection(text,1)
    copyOfText = text # we need the orginal text to be used later 
    copyOfText2 = text 

    if(isEvent(arrayText) == False):
        return ""

    topic=exteractTopic(arrayText)
    if(topic == "Topic not Found"):
        topic = nanoNetsAPI(imageTest) 

    dates = ""
    datePattern1 = "\s?\d{4}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{1,2}م?\s?"
    datePattern2 = "\s?\d{1,2}\s?[/,-]\s?\d{1,2}\s?[/,-]\s?\d{4}[^٥]م?\s?"


    datePattern3 = "\s?\d{4}\s?(January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{1,2}\s?"
    datePattern4 = "\d{1,2}\s? (?:January|February|March|April|May|June|July|August|September|October|November|December)\s?\d{4}\s?"

    # 1 = days without Hamza
    # 2 = days with an upper Hamza
    # 3 = days with an lower Hamza
    # 4 = days spelled wrong
    dayPattern1 = r'\االاثنين |الثلوث | الثلاثاء: |الربوع |إثنين|الخميس | الجمعة | السبت | الاربعاء|الاحد| الثلاثاء\b'
    dayPattern2 = r'\ الأثنين|الأربعاء|الأحد \b'
    dayPattern3 = r'\ الإربعاء| الإثنين|الإحد \b'
    dayPattern4 = r'\ الثلاداء|الاثنين |الثلاثاء |الثلاثاء :|الحميس |الأجد|الحمعة|الاجد \b'
    weekDays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")

    #namePattern1=r' د.\s+((?:\w+(?:\s+|$)){2})'
    namePattern1 = r'د\\.\s+((?:\w+(?:\s+|$)){2})'
    namePattern2 = r'الدكتورة\s+((?:\w+(?:\s+|$)){2})'
    namePattern3 = r'الدكتور\s+((?:\w+(?:\s+|$)){2})'
    namePattern4 = r'الاستاذ\s+((?:\w+(?:\s+|$)){2})'
    namePattern5 = r'الاستاذة\s+((?:\w+(?:\s+|$)){2})'
    namePattern6 = r'الأستاذ\s+((?:\w+(?:\s+|$)){2})'
    namePattern7 = r'الأستاذة\s+((?:\w+(?:\s+|$)){2})'
    namePattern8 = r'أ\.\s+((?:\w+(?:\s+|$)){2})'
    # namePattern8=r'أ\s?.\s?\s?((?:\w+(?:\s+|$)){2})'
    namePattern9 = r'الأستاذة /\s+((?:\w+(?:\s+|$)){2})'
    #namePattern10=r' الدكتورة/\s+((?:\w+(?:\s+|$)){2})'
    namePattern10 = r'الدكتورة\s?/\s+((?:\w+(?:\s+|$)){2})'
    namePattern11 = r'الدكتور\s?/\s+((?:\w+(?:\s+|$)){2})'
    #namePattern11=r'الدكتور/ /\s+((?:\w+(?:\s+|$)){2})'
    namePattern12 = r'الطالبة:/\s+((?:\w+(?:\s+|$)){2})'
    namePattern13 = r'الطالبة:\s+((?:\w+(?:\s+|$)){2})'
    namePattern14 = r'الأستاذ /\s+((?:\w+(?:\s+|$)){2})'
    namePattern15 = r'المهندس\s?/\s+((?:\w+(?:\s+|$)){2})'
    namePattern16 = r'المهندسة\s?/\s+((?:\w+(?:\s+|$)){2})'
    v1 = "أ"
    v2 = "د"
    v3 = "م"
    namePattern17 = r'\s?'+v1+'\.\s?((?:\w+(?:\s+|$)){2})'
    namePattern18 = r'\s?'+v2+'\.\s?((?:\w+(?:\s+|$)){2})'
    namePattern19 = r'\s?'+v3+'\.\s?((?:\w+(?:\s+|$)){2})'
    namePattern20 = r'المدرب:\s+((?:\w+(?:\s+|$)){2})'
    namePattern21 = r'المدربة:\s+((?:\w+(?:\s+|$)){2})'
    namePattern22 = r'المقدم:\s+((?:\w+(?:\s+|$)){2})'
    namePattern23 = r'المقدمة:\s+((?:\w+(?:\s+|$)){2})'
    namePattern24 = r'تقديم:\s+((?:\w+(?:\s+|$)){2})'
    namePattern25 = r' د\.\s+((?:\w+(?:\s+|$)){2})'
    namePattern26 = r' أ\.\s+((?:\w+(?:\s+|$)){2})'
    namePattern27 = r' م\.\s+((?:\w+(?:\s+|$)){2})'

    namePattern25 = r' د\.\s+((?:\w+(?:\s+|$)){2})'

    namePattern1Bin = r'د\.\s+((?:\w+(?:\s+|$)){3})'
    namePattern2Bin = r'الدكتورة\s+((?:\w+(?:\s+|$)){3})'
    namePattern3Bin = r'الدكتور\s+((?:\w+(?:\s+|$)){3})'
    namePattern4Bin = r'الاستاذ\s+((?:\w+(?:\s+|$)){3})'
    namePattern5Bin = r'الاستاذة\s+((?:\w+(?:\s+|$)){3})'
    namePattern6Bin = r'الأستاذ\s+((?:\w+(?:\s+|$)){3})'
    namePattern7Bin = r'الأستاذة\s+((?:\w+(?:\s+|$)){3})'
    namePattern8Bin = r'أ\.\s+((?:\w+(?:\s+|$)){3})'
    # namePattern8=r'أ\s?.\s?\s?((?:\w+(?:\s+|$)){2})'
    namePattern9Bin = r'الأستاذة /\s+((?:\w+(?:\s+|$)){3})'
    #namePattern10=r' الدكتورة/\s+((?:\w+(?:\s+|$)){2})'
    namePattern10Bin = r'الدكتورة\s?/\s+((?:\w+(?:\s+|$)){3})'
    namePattern11Bin = r'الدكتور\s?/\s+((?:\w+(?:\s+|$)){3})'
    #namePattern11=r'الدكتور/ /\s+((?:\w+(?:\s+|$)){2})'
    namePattern12Bin = r'الطالبة:/\s+((?:\w+(?:\s+|$)){3})'
    namePattern13Bin = r'الطالبة:\s+((?:\w+(?:\s+|$)){3})'
    namePattern14Bin = r'الأستاذ /\s+((?:\w+(?:\s+|$)){3})'
    namePattern15Bin = r'المهندس\s?/\s+((?:\w+(?:\s+|$)){3})'
    namePattern16Bin = r'المهندسة\s?/\s+((?:\w+(?:\s+|$)){3})'
    namePattern17Bin = r'\s?'+v1+'\.\s?((?:\w+(?:\s+|$)){3})'
    namePattern18Bin = r'\s?'+v2+'\.\s?((?:\w+(?:\s+|$)){3})'
    namePattern19Bin = r'\s?'+v3+'\.\s?((?:\w+(?:\s+|$)){3})'
    namePattern20Bin = r'المدرب:\s+((?:\w+(?:\s+|$)){3})'
    namePattern21Bin = r'المدربة:\s+((?:\w+(?:\s+|$)){3})'
    namePattern22Bin = r'المقدم:\s+((?:\w+(?:\s+|$)){3})'
    namePattern23Bin = r'المقدمة:\s+((?:\w+(?:\s+|$)){3})'
    namePattern24Bin = r'تقديم:\s+((?:\w+(?:\s+|$)){3})'

    namePattern25Bin = r' د\.\s+((?:\w+(?:\s+|$)){3})'
    namePattern26Bin = r' أ\.\s+((?:\w+(?:\s+|$)){3})'
    namePattern27Bin = r' م\.\s+((?:\w+(?:\s+|$)){3})'

   

    timePattern1= "\s?(pm|PM|Pm|am|AM|Am|ص|م|صباحا|مساءا|مساء|)?\s?(pm|PM|Pm|am|AM|Am|ص|م|صباحا|مساءا|مساء|)?\d{1,2}\s?(pm|PM|Pm|am|AM|Am|ص|م|صباحا|مساءا|مساء|)?\s?[:,.]\s?(pm|PM|Pm|am|AM|Am|ص|م|صباحا|مساءا|مساء|)?\s?\d{1,2}\s?(pm|PM|Pm|am|AM|Am|ص|م|صباحا|مساءا|مساء|)?\s?"

    timePattern2 = "\s?\ص?\م?\d{1,2}\s?\ص?\م?[-]\s?\ص?\م?\d{1,2}\s?\ص?\م?" #7-12

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

    elif(re.search(dayPattern4, text)): # for mistakes 

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
        elif day == "الاثنين ":
            day = "الاثنين"
        elif day == "الثلاثاء :":
            day = "الثلاثاء"
        elif day == "الثلاثاء ":
            day = "الثلاثاء"

        day = returnDay(day)
        print("d4")
        print(day)

    else:
        day = "no day was found"

    onlineStatus = isOnline(arrayText)
    if(onlineStatus=="in Person"):
      onlineStatus=checkInPerson(copyOfText2)

    technology= interestTechnology(arrayText)
    softSkills=interestSoftSkills(arrayText)
    managment = interestManagment(arrayText)
    datePatternStatus = False  # for 12 march 2020
    regexFound = False
    listobjDates = []
    x = 2
    indian = 0

    while (x != 0):
        text = replaceArabicMonth(text)
        if((re.search(datePattern1, text))):
            regexFound = True
            datePatternStatus = True
            oldDates = re.findall(datePattern1, text, re.MULTILINE) # reutrn an array of dates >>> one or two
            dates = removeSpace(oldDates)
            dates = remove5(oldDates)
            dates = [i.replace("م", "") for i in oldDates]
            dates = [i.replace("ه", "") for i in oldDates]
            x = 0

        elif((re.search(datePattern2, text))):
            regexFound = True
            datePatternStatus = True
            print("date found 2")
            oldDates = re.findall(datePattern2, text, re.MULTILINE)
            print("old date is", oldDates)
            dates = removeSpace(oldDates)
            dates = remove5(oldDates)
            dates = [i.replace("م", "") for i in oldDates]
            dates = [i.replace("ه", "") for i in dates]
            x = 0
            print(2)

        elif((re.search(datePattern3, text))):
            regexFound = True
            print("date found 3")
            oldDates = re.findall(datePattern3, text, re.MULTILINE)
            oldDates = str(oldDates[0])
            print("old date is", oldDates)
            oldDates = oldDates.replace(" ", "")
            day = ""
            year = ""
            monthNum = returnMonthNumber(oldDates)
            month = returnMonth(monthNum)
            print("the month num is ", monthNum)

            oldDates = oldDates.replace(month, monthNum)
            print("old date is now", oldDates)
            print("length is ,", len(oldDates))
            oldDates=oldDates.replace(" ","")
            if(len(oldDates) == 8):  # day consist of two digits
                day = oldDates[6]+oldDates[7]
                year = oldDates[0]+oldDates[1]+oldDates[2]+oldDates[3]

            elif(len(oldDates) == 7):  # day consist of one digits
                day = oldDates[6]
                year = oldDates[0]+oldDates[1]+oldDates[2]+oldDates[3]
                day = day[:6] + "0" + day[6:]

            newDate = day+"/"+monthNum+"/"+year
            newDate = newDate.replace(" ", "")
            newDate = newDate.replace("  ", "")
            if(indian == 1):
                ConvertedDateObject = convert_numbers.hindi_to_english(newDate)
            else:
                ConvertedDateObject = convert_numbers.persian_to_english(
                    newDate)
            newDate = str(ConvertedDateObject)
            newDate = newDate[:4] + "/" + newDate[4:]
            newDate = newDate[:6] + "/" + newDate[6:]
            day = returnWeekDay(objDate, weekDays)
            listobjDates.insert(0, objDate.date())
            x = 0

        elif((re.search(datePattern4, text))):
            regexFound = True
            oldDates = re.findall(datePattern4, text, re.MULTILINE)
            oldDates = str(oldDates[0])
            oldDates = oldDates.replace(" ", "")
            day = ""
            year = ""
            monthNum = returnMonthNumber(oldDates)
            month = returnMonth(monthNum)
            oldDates = oldDates.replace(month, monthNum)
            oldDates = oldDates.replace(" ", "")

            if(len(oldDates) == 8):  # day consist of two digits
                day = oldDates[0]+oldDates[1]
                year = oldDates[4]+oldDates[5]+oldDates[6]+oldDates[7]
              
            elif(len(oldDates) == 7):  # day consist of one digits
                day = oldDates[0]
                year = oldDates[3]+oldDates[4]+oldDates[5]+oldDates[6]
                day = day[:0] + "0" + day[0:]
            newDate = day+"/"+monthNum+"/"+year
            newDate = newDate.replace(" ", "")
            newDate = newDate.replace("  ", "")
            if(indian == 1):
                ConvertedDateObject = convert_numbers.hindi_to_english(newDate)
            else:
                ConvertedDateObject = convert_numbers.persian_to_english(
                    newDate)
            ConvertedDateObject=ConvertedDateObject.replace(" ","")
            ConvertedDateObject = ConvertedDateObject[:2] + "/" + ConvertedDateObject[2:]
            ConvertedDateObject = ConvertedDateObject[:5] + "/" + ConvertedDateObject[5:]

            objDate = ConvertedDateObject
            objDate = datetime.strptime(objDate, '%d/%m/%Y')
            listobjDates.insert(0, objDate)
            day = returnWeekDay(objDate, weekDays)
            print("day is now.", day)
            x = 0
            print(4)

        else:
            print("no date was found")
            break #temp 

        if(datePatternStatus):
            DatesLength = len(dates)
            listobjDates, day = processDate(
                DatesLength, listobjDates, weekDays, dates, day, indian)

        if(x == 1):
            break


    instructor = "not found"

    copyOfText = copyOfText.replace("أ.د عبد الرحمن بن عبيد اليوبي","")

    if((re.search(namePattern1, copyOfText))):
        instructor = re.search(namePattern1, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern1Bin, copyOfText).group()

    elif((re.search(namePattern2, copyOfText))):
        instructor = re.search(namePattern2, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern2Bin, copyOfText).group()

    elif((re.search(namePattern3, copyOfText))):
        instructor = re.search(namePattern3, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern3Bin, copyOfText).group()

    elif((re.search(namePattern4, copyOfText))):
        instructor = re.search(namePattern4, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern4Bin, copyOfText).group()

    elif((re.search(namePattern5, copyOfText))):
        instructor = re.search(namePattern5, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern5Bin, copyOfText).group()

    elif((re.search(namePattern6, copyOfText))):
        instructor = re.search(namePattern6, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern6Bin, copyOfText).group()

    elif((re.search(namePattern7, copyOfText))):
        instructor = re.search(namePattern7, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern7Bin, copyOfText).group()

    elif((re.search(namePattern8, copyOfText))):
        instructor = re.search(namePattern8, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern8Bin, copyOfText).group()

    elif((re.search(namePattern9, copyOfText))):
        instructor = re.search(namePattern9, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern9Bin, copyOfText).group()

    elif((re.search(namePattern10, copyOfText))):
        instructor = re.search(namePattern10, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern10Bin, copyOfText).group()

    elif((re.search(namePattern11, copyOfText))):
        instructor = re.search(namePattern11, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern11Bin, copyOfText).group()

    elif((re.search(namePattern12, copyOfText))):
        instructor = re.search(namePattern12, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern12Bin, copyOfText).group()

    elif((re.search(namePattern13, copyOfText))):
        instructor = re.search(namePattern13, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern13Bin, copyOfText).group()

    elif((re.search(namePattern14, copyOfText))):
        instructor = re.search(namePattern14, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern14Bin, copyOfText).group()

    elif((re.search(namePattern15, copyOfText))):
        instructor = re.search(namePattern15, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern15Bin, copyOfText).group()

    elif((re.search(namePattern16, copyOfText))):
        instructor = re.search(namePattern16, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern16Bin, copyOfText).group()

    elif((re.search(namePattern17, copyOfText))):
        instructor = re.search(namePattern17, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern17Bin, copyOfText).group()

    elif((re.search(namePattern18, copyOfText))):
        instructor = re.search(namePattern18, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern18Bin, copyOfText).group()

    elif((re.search(namePattern19, copyOfText))):
        instructor = re.search(namePattern19, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern19Bin, copyOfText).group()

    elif((re.search(namePattern20, copyOfText))):
        instructor = re.search(namePattern20, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern20Bin, copyOfText).group()

    elif((re.search(namePattern21, copyOfText))):
        instructor = re.search(namePattern21, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern21Bin, copyOfText).group()

    elif((re.search(namePattern22, copyOfText))):
        instructor = re.search(namePattern22, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern22Bin, copyOfText).group()

    elif((re.search(namePattern23, copyOfText))):
        instructor = re.search(namePattern23, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern23Bin, copyOfText).group()

    elif((re.search(namePattern24, copyOfText))):
        instructor = re.search(namePattern24, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern24Bin, copyOfText).group()

    elif((re.search(namePattern25, copyOfText))):
        instructor = re.search(namePattern25, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern25Bin, copyOfText).group()

    elif((re.search(namePattern26, copyOfText))):
        instructor = re.search(namePattern26, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern26Bin, copyOfText).group()

    elif((re.search(namePattern27, copyOfText))):
        instructor = re.search(namePattern27, copyOfText).group()
        if "بن" in instructor:
            instructor = re.search(namePattern27Bin, copyOfText).group()

    if(instructor == "not found"):
        instructor = exteractInstructor(arrayText)

    instructor = nameCorrection(instructor)

    timeText = GoogleAPI(imageTest)
    time1 = ""
    time2 = ""
    time1PM = 0
    time2PM = 0
    time1Temp = ""
    time1AM=""
    time2AM=""
    copyOfStringT1=""
    copyOfStringT2=""

    if(re.search(timePattern1, timeText)):
         
        time1, time1PM, time1Temp, temp, oldHours,time1AM,copyOfStringT1 = processTime(
            timePattern1, timeText, 1, 1, time1)
        tempOldHour = oldHours

        if(re.search(timePattern1, temp)): # for reading the next time
            time2, time2PM, time2Temp, temp, oldHours,time2AM,copyOfStringT2 = processTime(
                timePattern1, temp, 2, 1, time2)


        if(time1PM==0 and time1AM==0):
            if(time2PM==1):
                time1 = convertTo24H(time1,0,1) #this return hours
                #minutes=re.compile('[^:]*$')
                #minutes =  minutes.findall(str(copyOfStringT1))[0]
                copyOfStringT1=str(copyOfStringT1)
                minutes = copyOfStringT1[len(copyOfStringT1)-2]+copyOfStringT1[len(copyOfStringT1)-1]
                time1= str(time1)+str(minutes)
                time1=addColon(time1)
                

            


        
        

    elif(re.search(timePattern2, timeText)):
        time = re.search(timePattern2, timeText).group()
        time1, time2 = formatTime(time)
        time1, time1PM, time1Temp, temp, oldHours,time1AM,copyOfStringT1  = processTime(
            timePattern2, timeText, 1, 2, time1)

        if(re.search(timePattern2, temp)):
            time2, time2PM, time2Temp, temp, oldHours,time2AM,copyOfStringT2  = processTime(
                timePattern2, temp, 2, 2, time2)

  



    instructor = instructor.replace("\n", "")
    topic = topic.replace("\n", "")
    day = day.replace("\n", "")


    if(len(listobjDates) == 0):
        
        event = Event(topic, 0.0, day, instructor, time1, time2,websiteLink,onlineStatus,technology,softSkills,managment,image_url)
        

    else:
        eventDate = str(listobjDates[0])
        eventDate = eventDate.replace("00:00:00","")
        eventDate = eventDate.replace(" ","")
        event = Event(topic,eventDate , day, instructor, time1, time2, websiteLink,onlineStatus,technology,softSkills,managment,image_url)
        #addToGoogleCalendar(listobjDates[0],time1,time2,topic,onlineStatus)
    jd = json.dumps(event.__dict__, ensure_ascii=False,
                    indent=4, sort_keys=True, default=str)
    if(testing !=1):
     insertEvent(jd)

    print(jd)

    return jd
 