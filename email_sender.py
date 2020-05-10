import smtplib  # Creates and smtp (simple mail transfer protocol) server
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Enzo Darío Quesada Rojas'
email['to'] = '#################'  # email
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # stars server
    smtp.starttls()  # encryption mechanism
    smtp.login('#################', '#################')  # email, password
    smtp.send_message(email)
    print('all good boss!')
