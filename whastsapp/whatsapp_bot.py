import pywhatkit
from datetime import datetime

cur=datetime.now()

time=cur.strftime("%H")
num=input("Enter the recivers mobile number : ")
mes=input("Enter the message : " )
hour=int(input("Enter the hour : "))
min=int(input("Enter the minute : "))

pywhatkit.sendwhatmsg(num,mes,hour,min)