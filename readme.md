Termail
====

	Termail is an evolution of PyMail. It is a full command line e-mail
client. Termail is a lot more friendly than your normal e-mail client,
faster, and a great alternative to using a browser based solution.

Features:

Send personalized emails by changing how your recipent sees your name:

	From: John Doe <johndoe@gmail.com>
	From: Jane Doe <johndoe@gmail.com>

Change how the recipient sees their own name:

	To: Jack Sprat <person@live.com>
	To: Jack, our valued customer <person@live.com>
	
Attach files easily on the command line:
	
	- ~/pictures/thumb_cat_picture.png

Attach all top level files in a directory:
	
	- ~/c/my_project/

Keeps your password (we all know it is ********) hidden with getpass!

Termail was written with Python's core libraries in mind. This means no
hunting down additional libraries or mucking about with a config file!

Usage
====

        Usage: termail.py [options]

        Options:
        
            -h, --help            Show this help message and exit.
            
            -f username, --from=username
                        Sender E-mail address.
                        
            -s subject, --subject=subject
                        Subject of E-mail.
                        
            -r recipient, --recipient=recipient
						Recipient E-mail address.
            
            -d from_name, --from_name=from_name
                        Display name to send.
                        
            -n recipient_name, --recipient_name=recipient_name
                        Name of recipient.
                        
            -m message, --message=message
						Message of E-mail
			
			-p file_path, --path=file_path
						Attach file or top level directory


Dependencies
====

`python` version 2.6 or greater, may work on Python 3.
Internet connection.


License
====

        Copyright (C) 2012, Spencer Wood <spencer.wood25@gmail.com>

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
