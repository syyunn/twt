from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time

# Set up the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the Twitter profile page
driver.get("https://twitter.com/suyeol_yun")

# Scroll to the bottom of the page to load all the tweets
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all the tweets on the page
tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")

# Print out the text of each tweet
for tweet in tweets:
    print(tweet.text)

# Close the browser
driver.quit()
