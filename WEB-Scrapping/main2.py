import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Content
navBarSupportedContent = BeautifulSoup.find(id="navbarSupportedContent")

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
# elem = soup.select('#loginModal')[0] 
# print(elem)
