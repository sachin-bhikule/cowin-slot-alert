import requests
import time
import datetime

from playsound import playsound

#By default this checks the slots for next day edit this date as per your convenience
date1 = datetime.datetime.now() + datetime.timedelta(days=1)
date = date1 .strftime('%d-%m-%Y')

#path for the sound
path='D:/Vaccine Script/cowin-slot-script.mp3'

#City code
dist=363

URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, date)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


def findAvailability():
        counter = 0
        result = requests.get(URL, headers=header)
        response_json = result.json()
        data = response_json["sessions"]
        for parameter in data:
		#you can change the available_capacity for multiple bookings
            if((parameter["available_capacity"] > 0) & (parameter["min_age_limit"] == 18)):
                counter += 1
                print(parameter["name"])
                print(parameter["pincode"])
                print(parameter["vaccine"])
                print(parameter["available_capacity"])
                print(datetime.datetime.now())
                playsound(path)

        if(counter == 0):
            return False


while(findAvailability() != True):
    time.sleep(5)
    findAvailability()