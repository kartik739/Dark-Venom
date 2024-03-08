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

urls = []

def url(file):
    op = open(file, 'r')
    links = op.readlines()
    print(white + "[" + color + "+" + "] " + color + "Total urls: " + green + str(len(links)))
    for link in links:
        link = link.replace("\n", "")
        if link.startswith("http://") is True:
            link = link.replace("http://", "")
            urls.append(link)
        else:
            urls.append(link)



def check(target):
    targetUrl = "http://"+target+".ly"
    try:
        response = requests.get(targetUrl, timeout=3)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find("title").text
        if title == "Darknet TOR / I2P Proxy and Gateway":
            print(white + "[" + red + "-" + white + "] " + color + target + white + " [" + red + "Not Working" + white + "] ")
        else:
            print(white + "[" + green + "+" + white + "] " + color + target + white + " [" + green + "Working" + white + "] ")
            print(white + "[" + green + "+" + white + "] " + color + "Title: " + green + title)
            print(" ")
    except:
        print(white + "[" + red + "-" + white + "] " + color + target + white + " [" + red + "Not Working" + white + "] ")

path = input(white + "[" + color + "+" + "] " + "Enter the file path with links: ")

if os.path.exists(path) is True:
    print(white + "[" + color + "+" + "] " + color + "File Found: " + green + "True")
    print(" ")
    url(path)
    for i in urls:
        try:
            check(i)
        except KeyboardInterrupt as e:
            print(white + "[" + red + "-" + white + "] " + red + "Quiting me? Okk Bye!!")
else:
    print(white + "[" + red + "-" + white + "] " + red + "File not found! Please try again with correct file path!")