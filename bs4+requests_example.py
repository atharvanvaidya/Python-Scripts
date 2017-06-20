#This snippet extracts all URLs from the entered Website
from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract the Url:")

r = requests.get('http://' + url)

data = r.text

soup = BeautifulSoup(data , "html.parser")

count = int(0)

for link in soup.find_all('img'):
    print(link.get('alt'))
    count += 1

print('Total Number of Images:' + str(count))
