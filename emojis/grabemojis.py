from emojipedia import Emojipedia
from bs4 import BeautifulSoup

sunglasses = Emojipedia.search("sunglasses")
print(sunglasses.title)
print(sunglasses.aliases)
# print(sunglasses._soup)

# Get all image divs and the images inside them, find the one ending with with "on Microsoft Teams 1.0"
image_divs = sunglasses._soup.find_all("div", class_="vendor-image")
for image_div in image_divs:
    images = image_div.find_all("img")
    for image in images:
        if image["alt"].endswith("on Microsoft Teams 1.0"):
            print(image["alt"], image["src"])
            break