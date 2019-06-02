#Alexander Shelton



import smtplib, ssl

port = 465  # For SSL
to_email = ''



from_email = ''
password = ''

def send_email(message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message)




send_email('Test 2')
