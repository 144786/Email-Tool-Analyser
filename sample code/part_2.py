# Welcome to part 2 to the programming skills validation task!

# This is the second part of your program. In it, you are required to create a module named "hash_check_api".
# This module will contain a function called 'file_is_malicious()' which returns 'True' if a file's SHA256 hash
# is flagged as malicious by VirusTotal, and False otherwise. This fuction will take in a file's location,
# hash it (SHA256), report the hash to the user on standard output (i.e. console), send the hash to VT, and 
# return 'True' if a file's SHA256 hash is flagged as malicious by VirusTotal, and False otherwise.

# Once complete, use this code to verify your module. If your module is working correctly, the
# following should be printed to the standard output (i.e. the console):

#   Checking file: /home/CPT member/Documents/code/dev/Python Task 2/test files/wordDoc.docx
#   SHA256 hash: ee88ff66874d15a3837334d3affc93cd85c569e312913310510b4215083d0d6a
#   Does not flag as malicious.

#   Checking file: /home/CPT member/Documents/code/dev/Python Task 2/test files/eicar.com
#   SHA256 hash: 131f95c51cc819465fa1

import hash_check_api
import os

# in order to proceed, the Python interpreter needs to know where the files to chek are. Assuming
# that the test_files are in a folder named 'test files' located in the same directory as the this .py
# file, the following lines will figure that out.

# where it the file that we are currently in located?
current_directory = os.path.dirname(__file__)

# to that, add the path to the 'test files' directory and the files to test.
file_1 = os.path.join(current_directory, 'test files/wordDoc.docx')
file_2 = os.path.join(current_directory, 'test files/eicar.com')

files = [file_1, file_2]

for file in files:
    print('\nChecking file: ' + file)
    if hash_check_api.file_is_malicious(file):
        print('Flags as malicious.')
    else:
        print('Does not flag as malicious.')
