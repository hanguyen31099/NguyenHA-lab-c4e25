from gmail import*
sickness_list=["thương hàn", "bại liệt","ốm","viêm khớp"]
html='''
<p>Hello sếp</p>
<p>Hôm nay em xin phép <b>nghỉ làm</b> vì em  cảm thấy không khỏe có thể em bị <em>{{sickness}}</em> em phải đi khám</p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>&nbsp;</p>
'''
import datetime
now = datetime.datetime.now()
import random
while True:
    run_once=0
    while run_once==1:
        if now.hour==7:
            x=random.choice(sickness_list)
            run_once=1
            html_content = html.replace('{{sickness}}',x)
            gmail = GMail('ducha31099@gmail.com>','donguczong99')
            msg = Message('Test Message',to='qhuydtvt@gmail.com',html=html_content)
            gmail.send(msg)