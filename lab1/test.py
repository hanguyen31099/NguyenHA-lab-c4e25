from gmail import*
sickness_list=["thương hàn", "bại liệt"]
html='''
<p>Hello sếp</p>
<p>TO day I <strong>{{sickness}}</strong> because <em>{{symptom}}</em></p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>&nbsp;</p>
'''
import random
x=random.choice(sickness_list)
html_content = html.replace('{{sickness}}','thương hàn')
gmail = GMail('ducha31099@gmail.com>','donguczong99')
msg = Message('Test Message',to='quydtvt@gmail.com',html=html_content)
gmail.send(msg)
print(html_content)