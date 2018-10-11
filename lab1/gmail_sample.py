from gmail import GMail,Message
from random import choice
#    thư viện       hàm trong thư viện đó
gmail = GMail('vuthuyfptk11@gmail.com','20091997')
#msg = Message('Vu Thi Thuy',to='vuthuyfptk11@gmail.com',text='Hello')

#msg = Message("Tiêu đề",to="gmail của người nhận",text="nội dung")

#msg = Message('Test Message',to='vuthuyfptk11@gmail.com',text="Hello",html="<b>Hello</b>",attachments=['flag.png'])

#nếu nội dung dài thì html='biến'  chỗ biến đấy sẽ ghi nội dung
html_template = '''
<p>ch&agrave;o sếp</p>     
                           #placeholder
<p>hôm nay em bị <strong>{{symptom}}</strong> em phai đi khám bác sĩ , sau khi khám xong em bị <strong>symptom</strong>nên em phải nghỉ làm</p>
<p>Th&uacute;y<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-undecided.gif" alt="undecided" /></p>
'''
symptom_list = ["đau chân","đau đầu","đau bụng"]

x = choice(symptom_list)
y = choice(symptom_list)
print(x)
print(y)
html_content = html_template.replace("{{symptom}}",x)
html_content = html_template.replace("symptom",y)
#html_content = html_template.replace("{{symptom1}}","bệnh")
#replace : thay thế 1 đoạn string này thành string khác 
#          hoặc xóa 1 string bằng cách : html_content = html_template.replace("{{symptom}}","")
msg = Message('Test Message',to='vuthuyfptk11@gmail.com',text="Hello",html=html_content,attachments=['flag.png'])

gmail.send(msg)
