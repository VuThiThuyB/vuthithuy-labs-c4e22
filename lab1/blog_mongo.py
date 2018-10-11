from pymongo import MongoClient
uri = "mongodb://admin:Thuy200997@ds245022.mlab.com:45022/c4e22"

#connect to database
client = MongoClient(uri)
db = client.get_default_database()  # lấy database mặc định

#collection  : nơi chứa các hồ sơ cùng loại, tập hợp data giống nhau
posts = db['posts'] #lấy posts #insert_one() thêm   #đọc find()

post_list = posts.find()

#sử lí từng phần tử
# p = post_list[0]
# print(p)
# print(p['author'])
# print(p['title'])
# print(p['content'])

#sử lí nhiều phần tử
for p in post_list:
    print(p['author'])
    print(p['title'])
    print(p['content'])

#document: 
 # 1.create a document
# post = {
#     'title':'Thứ 2 phải nộp assm',
#     'content':'Tôi vẫn chưa làm được bài',
#     'author':'Thuy'
# }
 # 2.Insert created document
# posts.insert_one(post)



