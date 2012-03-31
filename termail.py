#!/usr/bin/python
##############################-TERMAIL-#################################
#Copyright (C) 2011-2012, Spencer Wood <spencer.wood25@gmail.com>      #
#This program is free software: you can redistribute it and/or modify  #
#it under the terms of the Lesser GNU General Public License as        #
#published by the Free Software Foundation, either version 3 of the    #
#License, or (at your option) any later version.                       #
#                                                                      #
#This program is distributed in the hope that it will be useful,       #
#but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#GNU General Public License for more details.                          #
#                                                                      #
#You should have received a copy of the GNU General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                      #
#For your convience, the LGPL license can be found on the GNU website, #
#or read http://www.gnu.org/licenses/lgpl.txt.                         #
########################################################################

import time, getpass, getopt, optparse, os, sys, smtplib, email.utils
import glob
import zipfile
from email.mime.text import MIMEText
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

def send_mail(username, recipient, subject, body, sender_name,
				recipient_name, file_path):
#function that sends mail.
	
	message = MIMEMultipart()
	message['To'] = email.utils.formataddr((recipient_name, recipient))
	message['From'] = email.utils.formataddr((sender_name, username))
	message['Subject'] = subject
	
	if file_path != None:
		#if no file this will skip
		#try to send file normally, if directory will hit the except
		try:
			part = MIMEBase('application', "octet-stream")
			part.set_payload(open(file_path, "rb").read())
			Encoders.encode_base64(part)
			part.add_header('Content-Disposition', 
			'attachment; filename="{}"'.format(os.path.basename(
			file_path)))
			message.attach(part)
			#add the file to the message as attachment
		except:
			for infile in glob.glob(os.path.join(file_path, '*')):
				#find the path to the directory and add an
				#asterisk to ensure files in the top level of the dir
				#are sent properly.	
				part = MIMEBase('application', "octet-stream")
				part.set_payload(open(infile, "rb").read())
				Encoders.encode_base64(part)
				part.add_header('Content-Disposition', 
				'attachment; filename="{}"'.format(os.path.basename(
				infile)))
				message.attach(part)
	
	host = username.find('@')
	#use the @ symbol as a seed for parsing to find the host server
	server = smtplib.SMTP(('smtp.{}:587').format(username[host+1:]))
	#insert the host site: example.com for instance
	server.starttls()
	server.login(username, getpass.getpass(prompt= 'Enter Password: '))
	server.sendmail(username, recipient, message.as_string())
	server.quit()
	#close connection to the server
	print 'Email sent: {}'.format(time.ctime())

if __name__=='__main__':
	#main, starts up the parser
	parser = optparse.OptionParser()
	
	parser.add_option('-f',
					  '--from',
					  dest ='username',
					  default = False,
					  type ='string',
					  help ='Sender E-mail address')
	parser.add_option('-s',
					  '--subject',
					  dest ='subject',
					  default = "",
					  type ='string',
					  help ='Subject of E-mail')
	parser.add_option('-r',
					  '--recipient',
					  dest ='recipient',
					  default = '',
					  type ='string',
					  help ='Recipient of E-mail address')
	parser.add_option('-d',
					  '--from_name',
					  dest ='from_name',
					  default = '',
					  type ='string',
					  help ='Display name to send')
	parser.add_option('-n',
					  '--recipient_name',
					  dest ='recipient_name',
					  default = '',
					  type ='string',
					  help ="Recipient of E-mail's name")
	parser.add_option('-m',
					  '--message',
					  dest ='body',
					  default = "",
					  type ='string',
					  help ='Message of E-mail')
	parser.add_option('-p',
					  '--path',
					  dest ='file_path',
					  default = None,
					  type ='string',
					  help ='Attach file or top level directory')

	(options, args) = parser.parse_args()
	if len(sys.argv) < 1:
		parse.error('Incorrect number of arguments. See help -h')
	if options.recipient == '':
		options.recipient = options.username
	send_mail(options.username, options.recipient, options.subject,
				options.body, options.from_name, options.recipient_name,
				options.file_path)
	#if everything goes okay, send mail with command line settings
