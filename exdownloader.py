import os
from exhentai.spider import spider

if __name__ == "__main__":
    if not os.path.exists("./download"):
        os.mkdir("./download")

    s = spider()

    while True:
        url = input("url: ")
        s.ex_url(url)
