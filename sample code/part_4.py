# Welcome to part 4 to the programming skills validation task!

# This is the fourth part of your program; you will build modify the 'attachement_getter' module from part 4 to create 
# a different functionality: you will create a function called 'link_scraper' that reads-in a folder full of emails (
# just like before), but this time, your module will look at the email body and try to find any URLs inside. This can be
# done with REGEX, but is actually quite difficuly (the internet / stack exchange is full of REGEXs that claim to do this
# but, after, extensive testing, I have found URLs that they all fail to find or non-URLs they incorrectly identify).
# Happily, the Python module URLExtract (https://pypi.org/project/urlextract/) seems to work, so I recommend using that.

# Once your module has found all the URLs, write them into a .txt file (1 URL per line).

import link_scraper
import os

# in order to proceed, the Python interpreter needs to know where the files to chek are. Assuming
# that the test emails are in a folder named 'test_emails' located in the same directory as the this .py
# file, the following lines will figure that out.

# where it the file that we are currently in located?
current_directory = os.path.dirname(__file__)

# add to that path the test_emails directory...
emails_folder = os.path.join(current_directory, 'test_emails/')

link_scraper.scrape_links(emails_folder)
