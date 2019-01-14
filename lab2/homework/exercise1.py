from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
# 1 download trang
url ="https://www.apple.com/itunes/charts/songs/"

# 1.1 Open a connection to sever
conn=urlopen(url)
# 1.2 Read data 
raw_data=conn.read()
# 1.3 decode data
content=raw_data.decode("utf8")

f=open("exercise1.html","wb")
f.write(raw_data)
f.close()
# 2 ROI
soup =  BeautifulSoup(content,"html.parser")
section = soup.find("section","section chart-grid")
li_list= section.find_all("li")
# 3 Extract data
song_list=[]
for li in li_list:
    number=li.strong.string
    name_song=li.h3.a.string
    artists=li.h4.a.string
    song={
        "Number" : number,
        "Name song": name_song,
        "Artists":artists
    }
    song_list.append(OrderedDict(song))
# 4 Save Data to excel
pyexcel.save_as(records=song_list,dest_file_name="excercise1.xlsx")
