# Welcome to part 2 to the programming skills validation task!
# In this task, you will be demonstrating yout ability to use others' code and APIs to 'stitch together'
# existing tools to create an automated pipeline. In the end, you will have created an application that
# can rapidly tear through an arbirtary number of .msg emails and scan them for malicious links and
# attachments.

# This is the first part of your program. In it, you are required to create a module named "url_api".
# This module will contain a function called 'url_is_malicious()' which returns 'True' if a URL
# is flagged as malicious by VirusTotal, and False otherwise.

# Skeleton code can be found in the folder titled "starter modules" to get you started.

# Once complete, use this code to verify your module. If your module is working correctly, the
# following should be printed to the standard output (i.e. the console):

#   Checking www.google.com
#   Does not flag as malicious.

#   Checking www.haveibeenpwned.com
#   Does not flag as malicious.

#   Checking http://malware.wicar.org/data/ms14_064_ole_not_xp.html
#   Flags as malicious.

#   Checking https://www.wikipedia.com
#   Does not flag as malicious.

#   Checking http://www.csm-testcenter.org/download/malicious/index.html
#   Flags as malicious.

#   Checking http://malware.wicar.org/data/java_jre17_exec.html
#   Flags as malicious.

#   Checking https://xkcd.com/1694/
#   Does not flag as malicious.

#   Checking http://malware.wicar.org/data/ms10_090_ie_css_clip_ie6.html
#   Flags as malicious.

import url_api

links_to_check = [
    'www.google.com',
    'www.haveibeenpwned.com',
    'http://malware.wicar.org/data/ms14_064_ole_not_xp.html',
    'https://www.wikipedia.com',
    'http://www.csm-testcenter.org/download/malicious/index.html',
    'http://malware.wicar.org/data/java_jre17_exec.html',
    'https://xkcd.com/1694/',
    'http://malware.wicar.org/data/ms10_090_ie_css_clip_ie6.html'
]

for link in links_to_check:
    print('\nChecking '+link)
    if url_api.url_is_malicious(link):
        print('Flags as malicious.')
    else:
        print('Does not flag as malicious.')
