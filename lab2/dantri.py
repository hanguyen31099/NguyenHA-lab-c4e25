from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel #as p
from collections import OrderedDict

#1. download trang
url = "https://dantri.com.vn"
#1.1 Open a connection to server
conn = urlopen(url)
#1.2 Read data
raw_data = conn.read()
#1.3 Decode data
page_content = raw_data.decode("utf8")

# print(page_content)

# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()



#2. Extract ROI (Region of Interest)
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew") #.find(ten the, nhan dang them) class thi k can them. #neu k phai la class thi phai them
#id="uli ulnew"
print(ul.prettify()) #.prettify: lam dep
#la 1 soup thi moi' prettify duoc 


#3. Extract data
li_list = ul.find_all("li")

# for li in li_list:
#     print(li.prettify())

news_list = []
for li in li_list:
    h4 = li.h4
    a = li.h4.a
    title = a.string #truy cap vao content cua a tag.
    link = url + a["href"] #dictionary  :)
    # print(title)
    # print(link)
    news = OrderedDict({ 
        "Title": title,
        "Link": link
    })
    news_list.append(news)


#4. Save data to excel
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
