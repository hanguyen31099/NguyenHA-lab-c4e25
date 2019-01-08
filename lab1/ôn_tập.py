def gmail_content():
    reason = {
            'cảm cúm' : 'Em sổ mũi và ho liên tục',
            'tiêu chảy' : 'Em đi ngoài rất nhiều lần',
            'đau dạ dày' : 'Bụng em đau dữ dội',
            'giãn dây chằng' : 'Lưng em rất đau đớn, không ngồi thẳng được'
        }
    html='''
    <p>Hello sếp</p>
    <p>Hôm nay em xin phép <b>nghỉ làm</b> vì em bị <i>{{sickness}}</i>, em cảm thấy không khỏe, <em>{{symptom}}</em></p>
    <p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
    <p>&nbsp;</p>
    '''
    rk = random.choice(list(reason.keys()))
    html_content = html.replace('{{sickness}}',rk).replace('{{symptom}}',reason[rk])
    return html_content

def gmail_send(content,receiver):
    # gmail = GMail('ducha31099@gmail.com>','donguczong99')
    # msg = Message('Test Message',to=receiver,html=content)
    # gmail.send(msg)
    print(content)
#main
import gmail
import random
content=gmail_content()
receiver = 'qhuydtvt@gmail.com'
gmail_send(content,receiver)
