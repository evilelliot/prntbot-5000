# crawling system
import requests
import random, string
from app.database import *
from bs4 import BeautifulSoup

class Crawler:
    def crawling_website():
        database = Database

        def randomString(digitsCount, lettersCount):
            sampleStr = ''.join((random.choice(string.ascii_letters) for i in range(lettersCount)))
            sampleStr += ''.join((random.choice(string.digits) for i in range(digitsCount)))
            
            # Convert string to list and shuffle it to mix letters and digits
            sampleList = list(sampleStr)
            random.shuffle(sampleList)
            finalString = ''.join(sampleList)
            return finalString


        random_id   = randomString(3, 3)
        source_link = "https://prnt.sc/"
        source_link =  source_link + random_id.lower()

        # scrapping the website
        url  = source_link
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'})
        soup = BeautifulSoup(page.content, 'html.parser')
        img_url = soup.find_all('img', {'class': 'no-click screenshot-image'})
        img_url = img_url[0]['src']

        
        # Then download the image
        response = requests.get(img_url)
        image = "images/" + random_id + ".png"
        if response.status_code == 200:
            with open(image, "wb") as f:
                f.write(response.content)

        data = {
            "id": random_id,
            "url": source_link,
            "image": image
        }
        Database.add_entry(data)
        return image