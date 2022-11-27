import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

response = requests.get(YOUTUBE_TRENDING_URL)
print('STATUS_CODE ',response.status_code)

with open('Selenium.html' , 'w') as f:
  f.write(response.text)
doc = BeautifulSoup(response.text,'html.parser')
print('Page title:',doc.title.text)

# finding all divs 
videos_divs = doc.find_all('div', class_= 'ytd-video-renderer')
print(f'Found {len(videos_divs)} videos')