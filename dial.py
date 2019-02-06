#!/usr/bin/python
from twilio.rest import TwilioRestClient
import time

#CONSTANTS Calls
#use +1 for numbers
FROM ="+1 " ##user number
CALLED ="+1 " ##number to call
#SID & Token found in menu
ACCOUNT_SID = ""
AUTH_TOKEN = ""
#Constants Mail


class System:
    def __init__(self):
        self.FROM = FROM
        self.CALLED = CALLED
        self.ACCOUNT_SID = ACCOUNT_SID
        self.AUTH_TOKEN = AUTH_TOKEN
        self.callCount = 0
        self.LIMIT = 20

    def makeCall(self):
        client = TwilioRestClient(self.ACCOUNT_SID,self.AUTH_TOKEN)
        while self.callCount < self.LIMIT:
            call = client.calls.create(
                to =self.CALLED,from_ =self.FROM,
                url =" ") ##find an xml server for a sound on phone
            self.callCount = self.callCount + 1
            print("Call #" + str(self.callCount)+" Calling Number :" + self.CALLED)##output:
            time.sleep(10) ##secconds between calls

def main():
    bot1 = System()
    bot1.makeCall()

##Running program:
if __name__ == '__main__':
    main()
