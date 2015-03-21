# coding: utf-8
import urllib2
import urllib
import re
import os
# url = "http://tieba.baidu.com/p/2166231880"
url = "http://tieba.baidu.com/p/3640309931"
html_content = urllib2.urlopen(url).read()
# get picture url method 1
r = re.compile('<img src="(.*?)"')
picture_url_list = r.findall(html_content.decode('utf-8'))
# get picture url method 2
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content)
    #print soup
picture_url_list = []

for img in  soup.find_all('img', "BDE_Image"):
    picture_url_list.append(img['src'])
picture_url_list
os.mkdir('pictures')
os.chdir(os.path.join(os.getcwd(), 'pictures'))
for i in range(len(picture_url_list)):
    picture_name = str(i) + '.jpg'
    try:
        urllib.urlretrieve(picture_url_list[i], picture_name)
        print("Success to download " + picture_url_list[i])
    except:
        print("Fail to download " + picture_url_list[i])
