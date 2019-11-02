import os
import time
import re
import urllib
import lxml

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


if __name__ == "__main__":
    if not os.path.exists("./download"):
        os.mkdir("./download")

    url = "https://exhentai.org/g/1509379/87011470ad/"

    chrome_option = webdriver.ChromeOptions()
    # chrome_option.add_argument("--headless")
    chrome_option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(options=chrome_option)
    browser.implicitly_wait(10)

    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "lmxl")
    print(soup.pretty())
    
    pass