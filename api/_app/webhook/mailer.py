import datetime
import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

BOT_ACCOUNT = os.environ['GMAIL_BOT_ACCOUNT']
APP_PASSWORD = os.environ['GMAIL_APPLICATION_PASSWORD']
DEVELOPER_ADDRESS = os.environ['DEVELOPER_ADDRESS']


def send_mail_with_csv(user, csv: str, target_date: datetime.date):
    subject = target_date.strftime('%m.%d.time')
    from_addr = f'TiM <{BOT_ACCOUNT}>'
    to_addr = user.email
    weekdays_ja = ['月', '火', '水', '木', '金', '土', '日']
    weekday_ja = weekdays_ja[target_date.weekday()]
    body_msg = f"""
お疲れ様です。
{target_date.strftime('%m/%d')}({weekday_ja})の練習のタイムです。
ご確認よろしくお願いします。

{user.gen}期 {user.name}
"""
    body = MIMEText(body_msg, 'plain', 'utf-8')

    attachment = MIMEText(csv, 'plain', 'utf-8-sig')
    csv_filename = target_date.strftime('%Y.%m.%d.csv')
    attachment.add_header('Content-Disposition', 'attachment', filename=csv_filename)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = DEVELOPER_ADDRESS
    msg.attach(body)
    msg.attach(attachment)

    with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
        smtp.login(BOT_ACCOUNT, APP_PASSWORD)
        smtp.send_message(msg)
