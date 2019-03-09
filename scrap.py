from bs4 import BeautifulSoup
import requests


print("enter search term:")
search = input()
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)


soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol",{"id": "b_results"})
links = results.findAll("li",{"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("summary:", item.find("a").parent.parent.find("p").text)

'''
        children = item.children
        for child in children:
            print("child:", child)
'''

'''
image scrapper
'''

from PIL import Image
from io import BytesIO


search = input("search for:")
params = {"q":search}
r = requests.get("https://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text,"html.parser")
links = soup.findAll("a",{"class":"thumb"})

for item in links:
    img_obj = requests.get(item.attrs["href"])
    title = item .attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped_images/" + title, img.format)
