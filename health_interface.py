from googlesearch import search
from bs4 import BeautifulSoup
import requests
import geocoder
from geopy.geocoders import Nominatim
import sys

#location
g = geocoder.ip('me')
print(g.latlng)

geolocator = Nominatim(user_agent="geoapiExercises")

latlng = g.latlng

lat = latlng[0]

lng = latlng[1]

lat = str(lat)
lng = str(lng)
  
location = geolocator.reverse(lat + "," + lng)
  
address = location.raw['address']

city = address.get('city', '')

state = address.get('state', '')

#main
child = False
adult = False
male = False
female = False
unknown_gender = False

age = int(input("What is your age? [6 and up] "))
gender = input("What is your gender [male, female] ")

sbp = int(input("Please Enter your SBP Blood Pressure Reading: "))
dbp = int(input("Please Enter your DBP Blood Pressure Reading: "))

bpm = int(input("Please Enter your Resting Heart Rate (BPM): "))

if age >= 6 and age <= 18:
          child = True
elif age >= 18:
          adult = True

if gender == 'male':
          male = True

elif gender == 'female':
          female = True

elif gender == 'prefer not to specify':
          unknown_gender = True

elif gender == 'other':
          unknown_gender = True

if sbp >= 150 or dbp >= 100 or bpm >= 160 or sbp <= 85 or dbp <= 55 or bpm <= 45:
    print("*Please seek immediate medical assistance*")
    query = ("Hospitals near" + city + state)
    print("Please refer to these links about the nearest hospitals to your current location")

    for i in search(query, tld="com", num=3, stop=10, pause=0):
              print(i)

    sys.exit()

#

if adult == True and male == True and sbp >= 114 and dbp <= 125:
          print("Your blood pressure levels are normal for your age and gender")

elif adult == True and male == True and sbp >= 114 and dbp <= 143:
          print("Your blood pressure levels are a little high for your age and gender")
          print("Here is a link to a website that might be of assistance to you: https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/high-blood-pressure/art-20046974")

elif adult == True and male == True and sbp >= 90 and dbp < 114:
          print("Your blood pressure levels are a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might of assistance to you: https://www.healthline.com/health/how-to-raise-blood-pressure")

#

if adult == True and female == True and sbp >= 114 and dbp <= 125:
          print("Your blood pressure levels are normal for your age and gender")

elif adult == True and female == True and sbp >= 114 and dbp <= 143:
          print("Your blood pressure levels are a little high for your age and gender")
          print('')  
          print("Here is a link to a website that might be of assistance to you: https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/high-blood-pressure/art-20046974")

elif adult == True and female == True and sbp >= 90 and dbp < 114:
          print("Your blood pressure levels are a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might of assistance to you: https://www.healthline.com/health/how-to-raise-blood-pressure")

#

if child == True and male == True and sbp >= 114 and dbp <= 125:
          print("Your blood pressure levels are normal for your age and gender")

elif child == True and male == True and sbp >= 114 and dbp <= 143:
          print("Your blood pressure levels are a little high for your age and gender")
          print('')  
          print("Here is a link to a website that might be of assistance to you: https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/high-blood-pressure/art-20046974")

elif child == True and male == True and sbp >= 90 and dbp < 114:
          print("Your blood pressure levels are a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might of assistance to you: https://www.healthline.com/health/how-to-raise-blood-pressure")

#

if child == True and female == True and sbp >= 114 and dbp <= 125:
          print("Your blood pressure levels are normal for your age and gender")

elif child == True and female == True and sbp >= 114 and dbp <= 143:
          print("Your blood pressure levels are a little high for your age and gender")
          print('')  
          print("Here is a link to a website that might be of assistance to you: https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/high-blood-pressure/art-20046974")

elif child == True and female == True and sbp >= 90 and dbp < 114:
          print("Your blood pressure levels are a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might of assistance to you: https://www.healthline.com/health/how-to-raise-blood-pressure")


#


if adult == True and male == True and bpm >= 46 and bpm <= 70:
          print("Your heart rate is a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might be of assistance to you: https://www.paihealth.com/post/3-activities-to-increase-your-heart-rate")

elif adult == True and male == True and bpm >= 46 and bpm <= 120:
          print("Your heart rate is normal for your age and gender")

elif adult == True and male == True and bpm >= 46 and bpm <= 159:
                print("Your heart rate is a little high for your age and gender")
                print('')    
                print("Here is a link to a website that might be assistance to you: https://www.healthline.com/health/how-to-lower-heart-rate")

#

if child == True and male == True and bpm >= 46 and bpm <= 70:
          print("Your heart rate is a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might be of assistance to you: https://www.paihealth.com/post/3-activities-to-increase-your-heart-rate")

elif child == True and male == True and bpm >= 46 and bpm <= 120:
          print("Your heart rate is normal for your age and gender")

elif child == True and male == True and bpm >= 46 and bpm <= 159:
                print("Your heart rate is a little high for your age and gender")
                print('')    
                print("Here is a link to a website that might be assistance to you: https://www.healthline.com/health/how-to-lower-heart-rate")

#


if child == True and female == True and bpm >= 46 and bpm <= 70:
          print("Your heart rate is a little low for your age and gender")
          print('')  
          print("Here is a link to a website that might be of assistance to you: https://www.paihealth.com/post/3-activities-to-increase-your-heart-rate")

elif child == True and female == True and bpm >= 46 and bpm <= 120:
          print("Your heart rate is normal for your age and gender")

elif child == True and female == True and bpm >= 46 and bpm <= 159:
                print("Your heart rate is a little high for your age and gender")
                print('')    
                print("Here is a link to a website that might be assistance to you: https://www.healthline.com/health/how-to-lower-heart-rate")

                
          
