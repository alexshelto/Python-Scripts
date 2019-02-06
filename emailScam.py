# Alex Shelton
# 01/22/19
# Program: Will send requests to a designated email username and password phisher
# How? : Use dev console to botain the request url of the server using a false credential login
# then match the "Form Data" at the bottom to resemble the layout in the dev console.





#########################################################
#                       READ                            #
#                                                       #
# Not intended for malicious use!                       #
# Using this on innocent people is illegal              #
# Read the laws on internet & privacy before using      #
#                                                       #
#########################################################

import json
import os
import requests
import string
import random


def create_pw():
    x = random.randint(6,24)
    pw = ''.join(random.choices(string.ascii_uppercase + string.digits, k=x))
    return pw


REQUEST_URL = " "



#character seed
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))


#working with names json
names = json.loads(open('names.json').read())

#creating email domains:
email_domain = ['@yahoo.com', '@icloud.com', '@gmail.com', '@outlook.com', '@mail.com', '@inbox.com',
'@aol.com', '@comcast.com', '@godaddy.com']



#generating emails and pw:
for name in names:
    nameAdd = ''.join(random.choice(string.digits))
    randomNum = random.randint(1,8)
    email_end = email_domain[randomNum]
    username = name.lower() + nameAdd + email_end
    password = create_pw()

    ##Form Data
    requests.post(REQUEST_URL, allow_redirects=False, data = {
        'user': username,
        'pass': password
})

    print("sending username: " +str(username) + " sending password: " + str(password) )
