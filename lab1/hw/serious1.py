from gmail import GMail,Message
import datetime

t = datetime.datetime.now()

print(t.hour)

gmail = GMail('vuthuyfptk11@gmail.com','20091997')

html_content='''
<p>Em chào thầy ạ:)))</p>     
                           #placeholder
<p>hôm nay em bị sốt phát bang em phai đi khám bác sĩ , sau khi khám xong em bác sĩ bảo em phải nằm viện mấy ngày nên em phải nghỉ học.Em mong thầy cho em nghỉ mấy buổi học</p>
<p>Th&uacute;y<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-undecided.gif" alt="undecided" /></p>
'''

msg = Message('ĐƠN XIN NGHỈ HỌC',to='vuthuyfptk11@gmail.com',html=html_content)

while True:
    if t.hour:
        gmail.send(msg)
        break


