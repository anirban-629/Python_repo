# If you want to scrape a website:
# 1. Use the Api
# 2. HTML Web Scrapping using some tools like bs4

# Requirements
# pip install requests
# pip install bs4
# pip install html5lib

from xml.etree.ElementTree import Comment
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTMl

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)


# Step 2: Parse the HTML
# soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())


# Step 3: HTML Tree Traversal
# title = soup.title

# print(title)
# print(title.text)

# print(type(soup))  # BeautifulSoup
# print(type(title))  # Element Tag
# print(type(title.string))  # NavigableString


# Get Various Tags

# paras = soup.find_all('p')
# anchors = soup.find_all('a')
# print(paras)
# print(anchors)

# print(soup.find('p'))  # First Para
# print(soup.find('p')['class'])  # First para's class
# print(soup.find('p')['id'])  # First Para's id
# print(soup.find('a')['class'])  # First Div


# find element using class name
# print(soup.find_all('p', class_="mt-2"))

# Get Text
# print(soup.find('p').get_text())

# Get Links
# linkSet = set()
# for link in anchors:
#     linkSet.add("https://codewithharry.com"+(link.get('href')))

# for item in linkSet:
#     print(item)

# 4. Comment
markup = '<p><!--Comment--></p>'
soup2 = BeautifulSoup(markup)

# print(soup2.p)
# print(soup2.p.string)
# print(type(soup2.p.string))
