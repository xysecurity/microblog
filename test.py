from flask_mail import Message
from app import app, mail
msg=Message('test subject',sender=app.config['ADMINS'][0],recipients=['@qq.com'])
msg.body='text body'
msg.html='<b>HTML</b> body'
with app.app_context():
    mail.send(msg)