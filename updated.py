import requests
from colorama import Fore
import os
import random
from bs4 import BeautifulSoup

white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.CYAN
cyan = Fore.CYAN
blue = Fore.BLUE

colors = [white, blue, yellow, cyan]
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

links = []
titles = []
names = []
about = []
print(" ")
print(white + "[" + color + "1" + "] " + color + "DarkNetLive News")
print(white + "[" + color + "2" + "] " + color + "Arrests (Arrested Darknet Vendors)")
print(white + "[" + color + "3" + "] " + color + "Markets (Darknet Market List)")
print(white + "[" + color + "4" + "] " + color + "Forums (Darkweb Forums)")
print(white + "[" + color + "5" + "] " + color + "Onions (Daily Updated Onion Links)")
print(white + "[" + color + "X" + "] " + color + "X for exit")
print(" ")
choice = input(white + "[" + color + "+" + white + "] " + color + "Enter your choice: ")
print(" ")
num = 0
if choice == "1":
    response = requests.get("http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion.ly").content
    soup = BeautifulSoup(response, 'html.parser')
    for content in soup.findAll("a", class_="a5"):
        link = content.get("href")
        links.append(link)
        title = content.get("title")
        titles.append(title)
        print(white + "[" + color + str(num) + white + "] " + green + title)
        num += 1
        print(" ")
    number = int(input(white + "[" + color + "+" + white + "] " + color + "Enter your choice: "))
    url = "http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion.ly" + links[number]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(" ")
    print(white + "[" + color + "+" + white + "] " + white + "---------------------------" + green + titles[number] + white + "---------------------------" + white + " [" + color + "+" + white + "]")
    article = soup.find("article").text
    final_Article = article.splitlines()
    new_article = final_Article[8:]
    print(" ")
    for i in new_article:
        print(i)
elif choice == "2":
    response = requests.get("http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion.ly/arrested-darknet-vendors/").content
    soup = BeautifulSoup(response, 'html.parser')
    for i in soup.findAll("h3"):
        names.append(i.text)
    content = soup.find("div", class_="a2r")
    for i in content.findAll("ul"):
        lis = i.findAll("li")
        about.append(lis)
    fuck = 0
    for name in names:
        print(white + "[" + color + "-" + white + "] " + color + "Name: "+ name)
        for i in about[fuck]:
            print(white + "[" + color + "*" + white + "] " + green + i.text)
        print(" ")
        fuck += 1
elif choice == "3":
    response = requests.get("http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion.ly/markets/").content
    soup = BeautifulSoup(response, 'html.parser')
    content = soup.find("ul", class_="a6u n__d")
    for i in content.findAll("article"):
        title = i.find("a").text
        link = i.find("span", class_="s__a").text
        print(white + "[" + color + "+" + white + "] " + color + "Title: " + green + title)
        print(white + "[" + color + "+" + white + "] " + color + "Link: " + green + link)
        print(" ")
elif choice == "4":
    response = requests.get("http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion.ly/forums/").content
    soup = BeautifulSoup(response, 'html.parser')
    content = soup.find("ul", class_="a6u n__d")
    for i in content.findAll("article"):
        title = i.find("a").text
        link = i.find("span", class_="s__a").text
        print(white + "[" + color + "+" + white + "] " + color + "Title: " + green + title)
        print(white + "[" + color + "+" + white + "] " + color + "Link: " + green + link)
        print(" ")
elif choice == "5":
    response = requests.get("http://darkzzx4avcsuofgfez5zq75cqc4mprjvfqywo45dfcaxrwqg6qrlfid.onion.ly/onions/").content
    soup = BeautifulSoup(response, 'html.parser')
    for i in soup.findAll("ul", class_="a9r"):
        title = i.find("a").text
        link = i.find("span", class_="s__a").text
        print(white + "[" + color + "+" + white + "] " + color + "Title: " + green + title)
        print(white + "[" + color + "+" + white + "] " + color + "Link: " + green + link)
        print(" ")
elif choice == "6":
    pass
else:
    print(white + "[" + color + "-" + white + "] " + red + "Is there any option like this!? I don't understand you! Please try again!")
    os.system("cls")
    os.system("python updated.py")
