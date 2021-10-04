from email.mime.text import MIMEText
import smtplib

def send_email(email, temperature,average_temperature,count):
    from_email="fchawala@gmail.com"
    from_password="1987Bernice"
    to_email=email

    subject="Temperature data"
    message="Hey there, your temperature is <strong>%s</strong>. Average temperature of all is<strong>%s</strong> and that is calculated out <strong>%s</strong> of people." % (temperature, average_temperature, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
