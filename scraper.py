import requests
from bs4 import BeautifulSoup
  
response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
)
print(response.status_code)