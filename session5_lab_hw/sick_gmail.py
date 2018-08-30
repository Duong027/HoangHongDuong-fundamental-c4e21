from gmail import GMail, Message
import datetime 
mail = GMail("duong1995027@gmail.com","Duonggre027")

body = '''

Sếp ơi, hôm qua em bị sốt cao. Ngày hôm nay em không đi làm được, sếp cho em nghỉ 1 hôm nhé.

Hôm sau em sẽ bù lại công việc ngày hôm nay :D

Kính thư,

Nôbita

'''

msg = Message("HHD-Đơn xin nghỉ ốm",to = 'duong027@gmail.com',html = body) 

now = datetime.datetime.now()

while True:

    now = datetime.datetime.now().hour
    if now == 7: 
        mail.send(msg)
    break
print('Done')


