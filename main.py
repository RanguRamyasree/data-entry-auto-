from bs4 import BeautifulSoup
import lxml
import requests
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

responce = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(responce.content,"lxml")

# ----------------------------- data collection ------------------------------- #
# prices
all_prices = soup.find_all(class_="PropertyCardWrapper")
prices = []

for price in all_prices:
    number = price.get_text().split("$")[1].split("/mo")[0].split("+ 1 bd")[0].split("+")[0]
    prices.append(number)

# links
all_links = soup.find_all("a",class_="property-card-link")
links = []

for link in all_links:
    href = link.get("href")
    links.append(href)

# addresses
all_addresses = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
addr = []

for address in all_addresses:
    place = address.get_text("address").split("address")[1].strip().replace("|", "")
    addr.append(place)

# ------------------------filling the form----------------------------------#

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/4C2PyuHsmve8yCkv8")

for i, j, k in zip(addr,prices,links):
    time.sleep(2)
    addr_blank = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr_blank.send_keys(f"{i}")
    addr_blank.send_keys(Keys.ENTER)
    pri_blank = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pri_blank.send_keys(f"{j}")
    pri_blank.send_keys(Keys.ENTER)
    link_blank = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_blank.send_keys(f"{k}")
    link_blank.send_keys(Keys.ENTER)
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    submit_another = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
