import requests
from bs4 import BeautifulSoup

#getting the response from the desired webste 
response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)

#parsing the HTML content of the web page using beut soup making it easier to navigate data as it gives you it structured
soup = BeautifulSoup(response.content, 'html.parser')

#finding element by the IDtag using soup
title = soup.find(id="firstHeading")
print(title.string)

