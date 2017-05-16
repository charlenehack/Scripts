#!/bin/env python
# coding:utf8


import poplib
import email
import mimetypes
import os


pop = poplib.POP3(host)
pop.user(user)
pop.pass_(passwd)
_, msg, _ = pop.retr(29) 
email_msg = email.message_from_string('\n'.join(msg))
#Get the email header
email_msg.get('Subject')
email_msg.get('To')
email_msg.get('From')
#parse the email body and attach file
counter = 1
for part in email_msg.walk():
    if part.is_multipart():
	continue
    filename = part.get_filename()
    if not filename:
	ext = mimetypes.guess_extension(part.get_content_type())
	if not ext:
	    ext = '.bin'
	filename = 'part-%03d%s' % (counter,ext)
    counter += 1
    fp = open(os.path.join(os.getcwd(), filename),'wb')
    fp.write(part.get_payload(decode=True))
    fp.close()


	


