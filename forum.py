import requests
from bs4 import BeautifulSoup
from colorama import Fore
import os
import random

white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.CYAN
cyan = Fore.CYAN

colors = [white, green, yellow, cyan]
color = random.choice(colors)

banner = """
██████╗  █████╗ ██████╗ ██╗  ██╗      ██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝      ██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║
██║  ██║███████║██████╔╝█████╔╝ █████╗██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════╝╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██████╔╝██║  ██║██║  ██║██║  ██╗       ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝        ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝   

"""
author = "VenomGrills (Gaurav Chaudhary)"
forum = "https://venomgrills.com"
instagram = "Instagram: https://instagram.com/venomgrills"
twitter = "https://twitter.com/venomgrills"
github = "https://github.com/venomgrills"

def ban():
    print(color + banner)
    print(white + "     [" + color + "+" + "] " + color + "Author: " + author)
    print(white + "     [" + color + "+" + "] " + color + "Forum: " + forum)
    print(white + "     [" + color + "+" + "] " + color + "Instagram: " + instagram)
    print(white + "     [" + color + "+" + "] " + color + "Twitter: " + twitter)
    print(white + "     [" + color + "+" + "] " + color + "Github: " + github)
    print(" ")
ban()
try:
    ip = requests.get("https://api.ipify.org").text
    print(white + "[" + color + "+" + "] " + color + "Your IP: " + ip)
except:
    print(white + "[" + red + "-" + "] " + red + "Please connect Yourself to internet")
    exit()


titles = []
links = []
response = requests.get("http://bestteermb42clir6ux7xm76d4jjodh3fpahjqgbddbmfrgp4skg2wqd.onion.ly/index.php?sid=305052d37a0466de3d097997a0622d8c").content
soup = BeautifulSoup(response, 'html.parser')
for rows in soup.findAll("a", class_="forumtitle"):
    titles.append(rows.text)
    link = rows.get("href")
    links.append("http:"+link)
x = 0
print(" ")
for venom in titles:
    print(white + "[" + color + str(x) + white + "] " + green + venom)
    x += 1
print(" ")
choice = int(input(white + "[" + color + "+" + white + "] " + color +"Enter the section number you want to continue with: "))
print(" ")

urls = []

url = links[choice]
newtitles = []
print(white + "[" + color + "+" + white + "] " + white + "============== " + green + titles[choice] + white + " ==============" + white + "[" + color + "+" + white + "] ")
print(" ")
response_ = requests.get(url).content
soup_ = BeautifulSoup(response_, "html.parser")
y = 0
for titles in soup_.findAll("a", class_="topictitle"):
    print(white + "[" + color + str(y) + white + "] " + green + titles.text)
    newtitles.append(titles.text)
    link = titles.get("href")
    urls.append("http:"+link)
    y += 1
print(" ")
choose = int(input(white + "[" + color + "+" + white + "] " + color + "Enter the section number you want to continue with: "))
print(" ")
print(white + "[" + color + "+" + white + "] " + white + "============== " + green + newtitles[choose] + white + " ==============" + white + "[" + color + "+" + white + "] ")
print(" ")
newUrl = urls[choose]
venom = requests.get(newUrl).content
newSoup = BeautifulSoup(venom, "html.parser")
for br in newSoup('br'):
    br.replace_with('\n')

content = newSoup.find("div", class_="content")
print(green + content.text)
try:
    print(" ")
    for find in content.findAll("a", class_="postlink"):
        link = find.get("href")
        print(white + "[" + color + "+" + white + "] " + color + "Link in thread:" + green + link)
except:
    pass