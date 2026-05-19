Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #escape sequences
>>> #There are 2 types
>>> #1]\n-> New line
>>> #2]\t-
>>> #2]\t->tab space
>>> a="name\nmobileno\tmailid"
>>> print(a)
name
mobileno	mailid
>>> b="name:ismail\n\tage:21\n\t\tmobile number:8019807297/n\t\t\tgmailid:ismail@gmail.com"
>>> print(b)
name:ismail
	age:21
		mobile number:8019807297/n			gmailid:ismail@gmail.com
>>> z="name:ismail\n\tage:21\n\t\tmobile number:8019807297\n\t\t\tgmailid:ismail@gmail.com"
>>> print(z)
name:ismail
	age:21
		mobile number:8019807297
			gmailid:ismail@gmail.com
>>> y="name:ismail\n\tage:21\n\t\tmobile number:8019807297/n\t\t\tgmailid:ismail@gmail.com"
... 
>>> y="name:ismail\n\tage:21\n\t\tmobile number:8019807297/n\t\t\tgmailid:ismail@gmail.com"
>>> k="name:ismail\n\tage:21\n\t\tmobile number:8019807297\n\t\t\t\t\tgmailid:ismail@gmail.com"
>>> print(k)
name:ismail
	age:21
		mobile number:8019807297
					gmailid:ismail@gmail.com
