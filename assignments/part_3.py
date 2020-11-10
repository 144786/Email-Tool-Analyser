# Welcome to part 3 to the programming skills validation task!

# This is the third part of your program; we have moved from learning to use API calls to external
# services to finding, reading, and interpreting other people's python modules. In this part, you are
# required to create a module named 'attachment_getter', which will contain a function called 
# "get_attachments". This function will take-in a path to a folder, then scan through all the emai(.msg)
# files in it, and read them into memory as MailParser email objects. You will need to use 
# https://pypi.org/project/mail-parser/ to do this. I recommend installing it using pip.
# 
# Once this has been done, the function should create a folder called 'attachments_found/' 
# and store all the attachments found in these emails there. 

import attachment_getter
import os

# in order to proceed, the Python interpreter needs to know where the files to chek are. Assuming
# that the test emails are in a folder named 'test_emails' located in the same directory as the this .py
# file, the following lines will figure that out.

# where it the file that we are currently in located?
current_directory = os.path.dirname(__file__)

# add to that path the test_emails directory...
emails_folder = os.path.join(current_directory, 'test_emails/')

attachment_getter.get_attachements(emails_folder)


