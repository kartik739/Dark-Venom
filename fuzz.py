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
target = input("Enter the target Url: ")
targetUrl = target + ".ly"
try:
    response = requests.get(targetUrl)
    if title == "Darknet TOR / I2P Proxy and Gateway":
        print(white + "[" + red + "-" + white + "] " + color + target + white + " [" + red + "Not Working" + white + "] ")
    else:
        print(white + "[" + green + "+" + white + "] " + color + target + white + " [" + green + "Working" + white + "] ")
        print(" ")
        wordlist = input(white + "[" + color + "+" + "] " + color + "Enter the wordlist path: [for default list press enter] ")
        print(" ")
        if wordlist == "":
            op = open("default.txt", 'r')
            read = op.readlines()
            print(white + "[" + color + "+" + "] " + color + "Total Words: " + green + str(read))
            print(" ")
            for whatever in read:
                domain = targetUrl + "/" + whatever
                status = requests.get(domain).status_code
                if status == 404:
                    pass
                else:
                    print(white + "[" + color + "+" + "] " + green + target + "/" + whatever + white + " [" + green + str(status) + white + "]")
        else:
            if os.path.exists(wordlist) is True:
                print(white + "[" + color + "+" + "] " + color + "File Found: " + green + "True")
                op = open(wordlist, 'r')
                read = op.readlines()
                print(white + "[" + color + "+" + "] " + color + "Total Words: " + green + str(read))
                print(" ")
                for whatever in read:
                    domain = targetUrl + "/" + whatever
                    status = requests.get(domain).status_code
                    if status == 404:
                        pass
                    else:
                        print(white + "[" + color + "+" + "] " + green + target + "/" + whatever + white + " [" + green + str(status) + white + "]")
            else:
                print(white + "[" + red + "-" + "] " + red + "Wordlist not found!!Please try again entering the correct path!!")
except:
    print(white + "[" + red + "-" + white + "] " + color + target + white + " [" + red + "Not Working" + white + "] ")