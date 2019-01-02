import smtplib

fadd = ' # senders Email address'
tadd = '# receivers Email address'
msg = 'Mail sent through Python!'
username = '# Your username(Email ID)'
password = '# Your password for above Email ID'
server = smtplib.SMTP('SMTP.GMAIL.COM', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fadd, tadd, msg)




# So Simple :)




