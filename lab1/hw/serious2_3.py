from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#connect to database
client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]

#creat a document
post = {
    'title':'Thông tin tuyển dụng',
    'content':'Trong thời đại công ngiệp hóa hiện đại hóa thì các ngành về công nghệ thông tin càng được nhiều bạn trẻ quan tâm , yêu thích và chọn làm công việc sau này . Nên vì thế càng có nhiều công ty start up về lĩnh vực này nên có rất nhiều cơ hội việc làm',
    'author':'Thuy'
}
#Insert
posts.insert_one(post)

post_list = posts.find()
p = post_list[0]
print(p)

