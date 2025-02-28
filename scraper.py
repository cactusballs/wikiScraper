import requests
from bs4 import BeautifulSoup
import random

#getting the response from the desired webste 
response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)

#parsing the HTML content of the web page using beut soup making it easier to navigate data as it gives you it structured
soup = BeautifulSoup(response.content, 'html.parser')

#finding element by the IDtag using soup
#this one is finding the first heading
title = soup.find(id="firstHeading")
print(title.content)

#getting all of the links 
allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0 

for link in allLinks:
  if link['href'].find("/wiki/") == -1:
    continue 

  linkToScrape = link
  break

print(linkToScrape)