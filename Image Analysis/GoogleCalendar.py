#from apiclient.discovery import build
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
import pytz
import re
from datetime import datetime, timedelta
import json

def  freeBusy(start,end,service,calendarList):
       tz = pytz.timezone('Asia/Riyadh')
       start_datetime = tz.localize(datetime(2022, 4, 8, 7, 30, 0))
       stop_datetime = tz.localize(datetime(2022, 4, 8, 8, 30, 0))
       body = {
      "timeMin": start_datetime.isoformat(),
      "timeMax": stop_datetime.isoformat(),
      "timeZone": 'Asia/Riyadh',
      "items": [{"id": 'aalbar0029@stu.kau.edu.sa'}]
    }
       print("i am out")
       eventsResult = service.freebusy().query(body=body).execute()
       return eventsResult

     

def addToGoogleCalendar(date,start_time,end_time,topic,online):
 scopes = ['https://www.googleapis.com/auth/calendar']
 flow = InstalledAppFlow.from_client_secrets_file(r"C:\Users\3boody\Documents\GitHub\SeniorProject-1\Image Analysis\client_secret.json", scopes=scopes)
 credentials = flow.run_console()

 service = build("calendar", "v3", credentials=credentials)
 result = service.calendarList().list().execute()
 x = result
 print(result['items'][0])
 print(result)
 calendar_id = result['items'][0]['id']
 if "en-gb.saudiarabian#holiday@group.v.calendar.google.com" in calendar_id:
    calendar_id="aalbar0029@stu.kau.edu.sa"
 result = service.events().list(calendarId=calendar_id, timeZone="GMT+3").execute()
 print(calendar_id)


 print(type(date))
 print(date.year)
 print(date.month)
 hoursStart=start_time[0]+start_time[1]
 minutesStart=start_time[3]+start_time[4]
 hoursEnd=end_time[0]+end_time[1]
 minutesEnd=end_time[3]+end_time[4]
 print(start_time)
 print(end_time)

 start_time = datetime(date.year, date.month, date.day, int(hoursStart), int(minutesStart), 0)
 end_time = datetime(date.year, date.month, date.day, int(hoursEnd), int(minutesEnd), 0)

 timezone = 'GMT+3'
 event = {
  'summary': str(topic),
  'location': str(online),
  'description': str(topic),
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 60*24},
      {'method': 'popup', 'minutes': 45},
    ],
  },
}
 service.events().insert(calendarId=calendar_id, body=event).execute()



