import requests
import time
import datetime
import os

from playsound import playsound

script_dir = os.path.dirname(__file__)
rel_path = "cowin-slot-script.mp3"
sound_path = os.path.join(script_dir, rel_path)

#edit this date as per your convenience
today = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow = today .strftime('%d-%m-%Y')

#City code
dist=363

URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, tomorrow)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
flag=1
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
                playsound(sound_path)

        if(counter == 0):
            return False


while(findAvailability() != True):
    if(flag==1):
        print("The script is now running as soon as the slots will open you will get notified")
        flag=0
    time.sleep(5)
    findAvailability()