import requests
from colorama import Fore
import os
import random
from bs4 import BeautifulSoup
from urllib.parse import urlparse

white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.CYAN
cyan = Fore.CYAN

colors = [white, green, yellow, cyan]
color = random.choice(colors)

urls = []

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
print(" ")
target = input(white + "[" + color + "+" + "] " + color + "Enter the Url: ")
try:
    targetUrl = target.replace("http://", "")
except:
    pass
fuck = targetUrl.replace(".onion", ".onion.ly")
print(" ")
try:
    response = requests.get("http://" + fuck).content
    soup = BeautifulSoup(response, 'html.parser')
    for links in soup.findAll("a"):
        link = links.get("href")
        parsed = urlparse(link)
        url = parsed.netloc
        final = url.replace(".ly", "")
        urls.append(final)
except:
    print(white + "[" + red + "-" + white + "] " + red + "Site not working!!")

for url in urls:
    if url == "twitter.com" or url == "target":
        pass
    elif url.endswith(".com") or url.endswith(".ru") or url.endswith("org"):
        pass
    else:
        try:
            response = requests.get("http://" + url + ".ly").content
            soup = BeautifulSoup(response, 'html.parser')
            title = soup.find("title").text
            if title == "Darknet TOR / I2P Proxy and Gateway":
                print(
                    white + "[" + red + "-" + white + "] " + color + url + white + " [" + red + "Not Working" + white + "] ")
                print(" ")
            else:
                print(
                    white + "[" + green + "+" + white + "] " + color + target + white + " [" + green + "Working" + white + "] ")
                print(white + "[" + green + "+" + white + "] " + color + "Title: " + green + title)
                print(" ")
        except:
            print(white + "[" + red + "-" + white + "] " + color + url + white + " [" + red + "Not working" + white + "]")
            print(" ")