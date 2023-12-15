#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse

def get_soup(url):
    #return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),
    # 'html.parser')
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url)),
        'html.parser')




def scrape_bing(url, category):

    DIR = "images"
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)


    soup = get_soup(
        url
    )
    ActualImages=[]
    for a in soup.find_all("a",{"class":"iusc"}):

        m = json.loads(a["m"])
        murl = m["murl"]
        turl = m["turl"]

        ActualImages.append((turl, murl))

    DIR = os.path.join(DIR, category.replace(" ","_"))
    if not os.path.exists(DIR):
        os.mkdir(DIR)


    for i, ( turl, murl) in enumerate(ActualImages):
        try:
            raw_img = urllib.request.urlopen(turl).read()
            name = category.replace(" ","") +"_bing_"+str(i+1)+".jpg"
            f = open(os.path.join(DIR, name), 'wb')
            f.write(raw_img)
            f.close()
            print(name)
        except Exception as e:
            print("could not load : " + name)
            print(e)


scrape_bing("https://www.bing.com/images/search?q=Darth+Vader", "Darth Vader")