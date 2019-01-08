from gmail import*
sickness_list=["thương hàn", "bại liệt","ốm"]
html='''
<p>Hello sếp</p>
<p>Hôm nay em xin phép <b>nghỉ làm</b> vì em  cảm thấy không khỏe bị <em>{{sickness}}</em></p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>&nbsp;</p>
'''
import random
x=random.choice(sickness_list)
html_content1 = html.replace('{{sickness}}',x)

gmail = GMail('ducha31099@gmail.com>','donguczong99')
msg = Message('Test Message',to='ducha031099@gmail.com',html=html_content)
gmail.send(msg)
print(html_content1)