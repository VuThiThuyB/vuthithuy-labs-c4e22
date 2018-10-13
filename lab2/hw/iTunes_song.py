from urllib.request import urlopen
from bs4 import BeautifulSoup 
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8") 
soup = BeautifulSoup(webpage_text,"html.parser")
section = soup.find("section","section chart-grid")
div = section.find("div","section-content")
ul = div.find("ul")
li_list = ul.find_all("li")

news_list=[]

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)

for li in li_list:
    a1 = li.h3.a
    names = a1.string
    a2 = li.h4.a
    artists = a2.string
    dl.download([names,artists])
    news = {
        "Name":names,
        "Artists":artists,
    }
    news_list.append(news)
#print(*news_list,sep="\n* * *\n")
pyexcel.save_as(records=news_list,dest_file_name="iTunes.xlsx")




