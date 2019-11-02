import os
import time
import re
import urllib

from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class spider(object):
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_option.add_experimental_option("prefs",prefs)
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--disable-gpu")
        chrome_option.add_argument('user-agent="Mozilla/5.0(X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"')
        self.browser = webdriver.Chrome(options=chrome_option)
        self.browser.implicitly_wait(10)
        self.log_in()
        self.ex()

    def log_in(self):
        print("Logging in...")
        url = "https://forums.e-hentai.org/index.php?s=bcfd0f1dd8b68644c067d7fcd09a92cb&act=Login&CODE=00"
        self.browser.get(url)
        username = self.browser.find_element_by_name("UserName")
        username.send_keys("xhc12321sx")
        password = self.browser.find_element_by_name("PassWord")
        password.send_keys("www2483com")
        login = self.browser.find_element_by_name("submit")
        login.click()

    def ex(self):
        print("Logging to exhentai...")
        url = "https://exhentai.org/"
        self.browser.get(url)

    def ex_url(self, url):
        print("Getting to gallary page...")
        self.browser.get(url)
        
        
        name = self.browser.find_element_by_css_selector("h1#gj").text
        name = validateTitle(name)
        print("In gallary page: {0}".format(name))

        pageblock = self.browser.find_element_by_css_selector("table.ptt").find_element_by_tag_name("tr")
        pages = pageblock.find_elements_by_tag_name("td")

        pages_url = {}
        for page in pages:
            if page.text != '<' and page.text != '>':
                page_num = page.text
                page_url = page.find_element_by_tag_name("a").get_attribute("href")
                pages_url[int(page_num)] = page_url
        pass
        
        pic_urls = []
        for i in range(1, int(page_num)+1):
            print("  Getting to page {0}".format(i))
            if i != 1:
                self.browser.get(pages_url[i])
            print("  In page {0}".format(i))
            self.gallary_page(pic_urls)
        pass
        self.download(pic_urls, name)

    def gallary_page(self, urls):
        # <div style="margin:1px auto 0; width:100px; height:142px; background:transparent url(https://exhentai.org/m/001510/1510460-00.jpg) -300px 0 no-repeat"><a href="https://exhentai.org/s/1daf2389ad/1510460-4"><img alt="004" title="Page 4: Vol.22_0004.jpg" src="https://exhentai.org/img/blank.gif" style="width:100px; height:141px; margin:-1px 0 0 -1px"><br>004</a></div>
        pic_block = self.browser.find_element_by_css_selector("div#gdt")
        pictures = pic_block.find_elements_by_tag_name("a")
        print("    Saving picture urls...")
        for pic in pictures:
            urls.append(pic.get_attribute("href"))
        pass

    def download(self, urls, name):
        try:
            if not os.path.exists("./download/"+name):
                os.mkdir("./download/"+name)
        except:
            name = input("Unvalid path name, need a new one: ")
            os.mkdir("./download/"+name)

        total = str(len(urls)).zfill(3)

        print("Totally: {0} images".format(total))
        print("Start downloding...")
        
        pattern = re.compile(r"-[1-9][0-9]*")
        for img in urls:
            file_name = re.search(pattern, img).group()[1:]
            if len(file_name) == 1:
                file_name = "00" + file_name
            elif len(file_name) == 2:
                file_name = "0" + file_name
            print("Downloading ", file_name, "/", total)

            print("  Getting img url...")
            file_src = self.get_img_src(img)
            prefix = file_src[file_src.rfind("."):]
            print("  Downloading...")
            urllib.request.urlretrieve(file_src, "./download/"+name+"/"+file_name+prefix)

            pass
        print("Done")
        pass
    
    def get_img_src(self, url):
        self.browser.get(url)
        return self.browser.find_element_by_css_selector("img#img").get_attribute("src")


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|\・]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


if __name__ == "__main__":
    if not os.path.exists("./download"):
        os.mkdir("./download")


    url = "https://exhentai.org/g/1478398/0832f2b596/" # short
    # url = "https://exhentai.org/g/1510570/ad704bcce9/" #long
    s = spider()
    s.ex_url(url)

    pass