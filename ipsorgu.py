from bs4 import BeautifulSoup
import requests
import sys

try:
    ipaddr = sys.argv[1]
    print("Please wait..")
except IndexError:
    print("Please Entered IP Adress")
try:
    req = requests.get("http://www.ipsorgu.com/?ip=" + str(ipaddr) + "#sorgu")
    
    soup = BeautifulSoup(req.text, 'html.parser')
    
    googlemaps = soup.find("iframe")
    googlemaps = str(googlemaps).split("src=")
    googlemaps = str(googlemaps[1]).split("&")
    googlemaps = str(googlemaps[0]).replace('"', "")
    googlemaps = str(googlemaps).split("=")
    
    info = soup.find_all("em")
    info1 = str(info).replace('<em style="color:#666">', '')
    info1 = str(info1).replace('</em>', '')
    info1 = info1.split(", ")
    
    print("Location : " + str(googlemaps[1]))
    print("Country : " + str(info1[0]).replace("[", ""))
    print("Region : " + str(info1[1]))
    print("Host : " + str(info1[3]))
    
    req = requests.get("https://whatismyipaddress.com/ip/" + str(ipaddr))
    
    soup = BeautifulSoup(req.text, 'html.parser')
    
    info2 = soup.find_all("td")
    info3 = str(info2).replace('<td>', '')
    info3 = str(info3).replace('</td>', '')
    info3 = str(info3).replace('[', '')
    info3 = info3.split(", ")
    
    print("Decimal : " + str(info3[1]))
    print("ASN : " + str(info3[3]))
    print("ISP : " + str(info3[4]))
    print("Postal Code : " + str(info3[16]).replace("]", ""))
    print("continent : " + str(info3[10]))
except SyntaxError:
    print("Please enter a correct IP")
except (NameError, IndexError) as e:
    if e == NameError or e == IndexError:
        print("Please Entered IP Adress")
