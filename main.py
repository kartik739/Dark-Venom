import os
import random
try:
    import requests
    from colorama import Fore
    from bs4 import BeautifulSoup
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install bs4")
    print("Now restart the tool!!!")

titles = []
links = []

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
keyword = input(white + "[" + color + "+" + "] " + "Enter the keyword you want to search: ")

x = 0
while True:
    url = "https://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion.ws/?q=" + keyword + "&offset=" + str(x)
    x += 20
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.findAll('div', class_="result")
    if results == []:
        print("Sorry no more results on this!!")
        break
    else:
        for result in results:
            link = result.find("i")
            title = result.find("a").text
            titles.append(title)
            links.append(link.text)
            title_ = title.replace("\t", "")
            print(white + "[" + color + "+" + "] " + color + "Title: " + green + title_)
            print(white + "[" + color + "+" + "] " + color + "Url: " + green + link.text)
        continue
"""save = input(white + "[" + color + "+" + "] " + color + "Do you want to save the output? [y/n] ")
if save == "y" or save == "Y":
    output = input(white + "[" + color + "+" + "] " + color + "Enter the output filename: ")
    op = open(output, 'a')"""
