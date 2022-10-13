# Author: Snehashish Laskar
# Date: 13-10-2022

from bs4 import BeautifulSoup
import requests

url = "https://www.hindustantimes.com/latest-news"
html = BeautifulSoup(requests.get(url).text, "html.parser")
var = html.find_all("a")
print(requests.get(url).text)



