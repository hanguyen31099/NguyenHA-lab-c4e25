def gmail_content(reason_dict):
    html='''
    <p>Hello sếp</p>
    <p>Hôm nay em xin phép <b>nghỉ làm</b> vì em bị <i>{{sickness}}</i>, em cảm thấy không khỏe, <em>{{symptom}}</em></p>
    <p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
    <p>&nbsp;</p>
    '''
    rk=random.choice(list(reason_dict.keys()))
    html_content=html.replace('{{sickness}}',rk).replace('{{symptom}}',rk)
    return html_content

def gmail_send(ID_email,password_email,receiver,content):
    gmail = GMail(ID_email,password_email)
    msg = Message('Đơn Xin Nghỉ Phép',to=receiver,html=content)
    gmail.send(msg)

#main
import gmail
import random
import datetime
now = datetime.datetime.now()
time=int(input("Enter hour day do U want to spend the email:"))
ID_email=input("Enter Your email:")
password_email=input("Enter Your password:")
receiver=input("Enter email do you want to send:")

symptom_list = []
sickness_list = []
number_reason = int(input("Enter number reason do U want : "))
for i in range(number_reason):
    print("Enter the sickness",i+1,": ",end='')
    sickness_list.append(input(""))
    print("Enter the symptom",i+1,": ",end='')
    symptom_list.append(input(""))
reason_dict = dict(zip(sickness_list,symptom_list))
gmail_content(reason_dict)

while True:
    run_once=0
    while run_once==0:
        if now.hour==time:
            content= gmail_content()
            gmail_send(ID_email,password_email,receiver,content)
            run_once=1

