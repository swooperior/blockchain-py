#Not intended behaviour.  addTransaction seems to add to every block in self.chain

from datetime import datetime
import hashlib
class Block:
    hash = ''
    txIndex = 0
    transactions = []
    timeStamp = ''
    previous_hash = ''
    nonce = 0

    def calculateHash(self):
        self.hash = str(hashlib.sha256(repr([self.transactions,self.previous_hash,self.nonce]).encode('utf-8')).hexdigest())

    def getHash(self):
        return self.hash

    


    def addTransaction(self,tx):
        #Validate transaction, then pass to transactions list
        tx.id = self.txIndex
        self.transactions.append(tx)
        self.txIndex += 1

    def printDetails(self):
        print('Block Hash: '+self.getHash())
        print('Nonce: '+str(self.nonce))
        print('Created: '+ str(datetime.fromtimestamp(self.timeStamp)))
        print('Prev_hash: '+str(self.previous_hash))
        print('Transactions ('+str(len(self.transactions))+'):')
        self.printTransactions()
        print('-END OF BLOCK-')

    def printTransactions(self):
        c = 1
        for tx in self.transactions:
            print('Transaction:'+ str(c))
            tx.printDetails()
            c += 1

    def __init__(self,txlist=None,prev_hash=''):
        self.transactions = []
        txlist = txlist or []
        self.txIndex = 0
        self.previous_hash = prev_hash
        for tx in txlist:
            self.addTransaction(tx)
        self.timeStamp = datetime.timestamp(datetime.now())
        self.nonce = 1
        self.calculateHash()
        #print(self.printDetails())
