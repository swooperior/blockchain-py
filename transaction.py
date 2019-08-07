import hashlib
from datetime import datetime
class Transaction:
    id = 0
    sender = ''
    recipient = ''
    amount = ''
    signature = ''
    timeStamp = ''

    def getSig(self):
        return str(hashlib.sha256(repr([self.sender,self.recipient,self.amount,self.timeStamp]).encode('utf-8')).hexdigest())
    
    def verifyTx(self):
        pass

    def printDetails(self):
        print(self.id) 
        print(datetime.fromtimestamp(self.timeStamp))
        print(self.sender)
        print(self.recipient)
        print(self.amount)
        print(self.signature)


    def __init__(self,sender,recipient,amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timeStamp = datetime.timestamp(datetime.now())
        self.signature = self.getSig()
        #self.printDetails()

