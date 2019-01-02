import smtplib

fadd = ' # senders email address'
tadd = '# receivers email address'
msg = 'Mail sent through Python!'
username = '# Your username(email ID)'
password = '# Your password for above Email ID'
server = smtplib.SMTP('SMTP.GMAIL.COM', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fadd, tadd, msg)