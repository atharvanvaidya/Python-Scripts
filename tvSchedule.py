import requests
from bs4 import BeautifulSoup

channelList = ['Sony Pix', 'WB', 'Movies Now', 'MNX', 'HBO', 'Star Movies']
for channelName in channelList:
    request = requests.get('http://tv.burrp.com/search.html?q='+channelName)
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    movieName = soup.find('strong')
    startTime = soup.find('b', {'class': 'from'})
    endTime = soup.find('b', {'class': 'to'})
    print(channelName+':', end=' ')
    print(movieName.text.strip(), end='  ')
    print(startTime.text.strip()+' to', end=' ')
    print(endTime.text.strip())
