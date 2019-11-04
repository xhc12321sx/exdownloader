import os
from exhentai.spider import spider

if __name__ == "__main__":
    if not os.path.exists("./download"):
        os.mkdir("./download")

    s = spider()

    while True:
        url = input("url(or exit to terminate the process): ")
        if url != "exit":
            s.ex_url(url)
        else:
            break
    
    print("Exit")
