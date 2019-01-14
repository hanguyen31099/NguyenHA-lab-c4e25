from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://www.apple.com/itunes/charts/songs/"
conn=urlopen(url)
raw_data=conn.read()
content=raw_data.decode()
soup=BeautifulSoup(content,"html.parser")
section=soup.find("section","section chart-grid")
li_list=section.find_all("li")

for li in li_list:
    name_song=li.h3.a.string
    artist=li.h4.a.string
    option={
        'default_search':'ytsearch',
        'max_downloads' :1,
        'formart':'bestaudio/audio'
    }
    dl=YoutubeDL(option)
    dl.download([ name_song + artist])