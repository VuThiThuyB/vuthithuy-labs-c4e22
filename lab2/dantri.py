#1.download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup  #để cho python biết đây là html chứ k phải là 1 string
import pyexcel


url = "https://dantri.com.vn/"
    # 1.1 Connect to webpaga
conn = urlopen(url)  # mo 1 ket noi
    # 1.2 Download raw data (Raw data laf du lieu tho)
raw_data = conn.read()
    # 1.3 Decode data(giair max guiwx lieeuj)
webpage_text = raw_data.decode("utf-8")   # utf-8 : unicode
#print(len(webpage_text))
    # 1.4 Save text
    #w : write
    #b : binary
# f = open("dantri.html","wb") # mở 
# #f.write(webpage_text) #lưu 
# f.write(raw_data) #lưu
# f.close() #đóng





#2.extract ROI
    # 2.1 Convert text to soup
soup = BeautifulSoup(webpage_text,"html.parser") # file text thanh html cos ten laf soup
#print(soup)
#print(soup.prettify())
ul = soup.find("ul","ul1 ulnew")  #id = "ul1 ulnew"  : tìm theo id
#print(ul.prettify())
li_list=ul.find_all("li")
#print(type(li_list))
#print(li_list)
# for li in li_list:
#     print(li.prettify)
#     print("*   *   *   *   *")

# li = li_list[0]
# # h4 = li.h4
# # a = h4.a
# a = li.h4.a
# # print(h4.prettify())
# #print(a.prettify())
# title = a.string
# #print(title)
# #link = a["href"]
# link = url + a["href"]
# print(title)
# print(link)

news_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]
    # print(title)
    # print(link)
    news ={
        "Title":title,
        "Link":link,
    }
    news_list.append(news)
    #print("*"*20)
print(*news_list,sep="\n* * *\n") 



#3.Extract data


#4.Save data
pyexcel.save_as(records=news_list,dest_file_name="dantri.xlsx")