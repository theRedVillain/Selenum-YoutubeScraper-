import time
import smtplib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
# this get's you a browser 
# .get loads the url in that browser 
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window() # For maximizing window
  driver.implicitly_wait(50) # gives an implicit wait for 50 seconds
  return driver
# we don't want to open the interface for chrome we just want the javascript lines to run 

def get_videos(driver):
  video_tag = 'ytd-video-renderer'
  print('Getting the Page')
  driver.get(YOUTUBE_TRENDING_URL)
  time.sleep(10)
  video_divs = driver.find_elements(By.TAG_NAME,video_tag)
  return video_divs

def parse_videos(video):
  title_tag = video.find_element(By.ID,'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_url = video.find_element(By.TAG_NAME,'img').get_attribute('src')
  description_tag = video.find_element(By.ID, 'description-text')
  description = description_tag.text
  creator_tag = video.find_element(By.CLASS_NAME,'ytd-channel-name')
  creator = creator_tag.text

  return {
    'title' : title,
    'url' : url,
    'thumbnail_url' : thumbnail_url,
    'description' : description,
    'channel_name' : creator
  }
  

  
if __name__ == '__main__':
  print('Creating Driver')
  driver = get_driver()
  print('Fetching Trending Videos')
  videos = get_videos(driver)
  print('Page Title: ',driver.title)
  print(len(videos))



print('Parsing the videos')
#title,url,thumbnail_url,channel,views,uploaded,description 
# video = videos[0]


# title_tag = video.find_element(By.ID,'video-title')
# title = title_tag.text
# url = title_tag.get_attribute('href')
# thumbnail_url = video.find_element(By.TAG_NAME,'img').get_attribute('src')
# description_tag = video.find_element(By.ID, 'description-text')
# description = description_tag.text
# creator_tag = video.find_element(By.CLASS_NAME,'ytd-channel-name')
# creator = creator_tag.text 

video_data = [parse_videos(video) for video in videos[:10]]



# print('Title :',title)
# print('URL: ',url)
# print('Thumbnail_URL',thumbnail_url)
# print('description :  ',description)
# print('Channel : ',creator)

# print(video_data)

print('Saving Data to CSV ')
top10_df = pd.DataFrame(video_data)
print(top10_df)
top10_df.to_csv('top10_csv')

