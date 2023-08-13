from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://youtube.com/playlist?list=PL15B1E77BB5708555&feature=shared") #replace with your needed playlist url

time.sleep(5)

#click on first video in playlist
driver.find_element_by_xpath('//*[@id="thumbnail"]/yt-image/img').click()

time.sleep(3)

while True:
    try:
        
        #pause the video
        driver.find_element(By.CSS_SELECTOR, "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button").click()

        time.sleep(2)
        
        #like the video
        driver.find_element(By.XPATH, '//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()


        time.sleep(2)
        
        #click on next video
        driver.find_element(By.CSS_SELECTOR, "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button").click() 

        time.sleep(3)


    except Exception as e:
        print("An error occurred:", e)
        break 





