import requests
from datetime import date
from random import randint

def get_epic_photos(api_key, date):
    endpoint_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    params = {"api_key": api_key}

    response = requests.get(endpoint_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Data not received. Status code: {response.status_code}")
        return None

def get_user_birthday():
    while True:
        user_birthday = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            iso_date = date.fromisoformat(user_birthday)
            if iso_date.year < 2015:
              print("Enter a year from 2015 onwards")
              continue
            else:
              return iso_date.isoformat()
        except ValueError:
            print("Invalid format or date. Please use YYYY-MM-DD")

def get_random_image(photos):
  count = len(photos)
  random_index = randint(0, count - 1)
  filename = photos[random_index]["image"]
  return filename

def display_image_url(date, filename):
  year = date[0:4]
  month = date[5:7]
  day = date[8:10]
  return f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{filename}.png"

if __name__ == "__main__":
  user_birthday = get_user_birthday()
  photos = get_epic_photos("DEMO_KEY", user_birthday)
  if photos:
        print(f"Photos on this date: {len(photos)}")
        print()
        filename = get_random_image(photos)
        print(display_image_url(user_birthday, filename))
  else:
    print("No photos for this date.")
  
