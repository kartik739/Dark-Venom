import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import random

urls = []
target_links = []
url = []

target = input("[+] " + "Enter the url: ")


def extract(tar):
    try:
        response = requests.get(target)
        soup = BeautifulSoup(response.content, 'html.parser')
        return re.findall('(?:href=")(.*?)"', str(soup))
    except:
        pass


def crawl(path):
    links = extract(path)
    for link in links:
        url = urljoin(path, link)
        if "#" in url:
            url = url.split("#")[0]
        if link in url and url not in target_links:
            target_links.append(url)
            urls.append(target_links)
            try:
                res = requests.get(url)
                sou = BeautifulSoup(res.content, 'html.parser')
            except:
                pass
            print("[+] " + url)
            crawl(url)


crawl(target)
