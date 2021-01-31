import requests
from bs4 import BeautifulSoup

with open('word.txt', 'w') as file:
    web = requests.get("https://www.englishspeak.com/ko/english-words")
    soup = BeautifulSoup(web.content, "html.parser")

    a = soup.select(".test > a")

    for i in a:
        file.write(i.text.ljust(10))
