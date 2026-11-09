## nasa-epic-birthday-earth

It requests the EPIC natural-color photo data for 
that one date and convert the response into a list
of photo dictionaries. It will use the image key for the
chosen photo’s filename and the date key for the year,
month, and day needed to locate the image in the EPIC archive.

## How it works
- get_epic_photos(api_key, date): Requests EPIC photo data for 
one date and turns the response into a list of dictionaries, one per photo.
- get_user_birthday(): Asks for user birthday and makes sure the
date format is valid, and the birthday is after 2015.
- get_random_image(photos): Takes a list of photos from the dictionary
and selects one at random to output the image.
- display_image_url(image): Takes a file name of a photo and then
displays the url for said photo.

## How to run
1. Install requests: pip install requests
2. Run: python birthday_earth.py
3. Uses "DEMO_KEY" by default. My key in place of DEMO_KEY
   from api.nasa.gov for higher rate limits.

## Built with
Python, requests, datetime, random and the NASA EPIC API

<img width="1400" height="1115" alt="EPIC_Function_Diagram (1)" src="https://github.com/user-attachments/assets/dca2475e-d99d-4224-9512-a822df0ff031" />
