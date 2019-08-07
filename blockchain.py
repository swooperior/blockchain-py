#CURRENTLY EVERY TRANSACTION APPEARS IN EVERY BLOCK IN THE CHAIN.

import hashlib
from block import Block
from transaction import Transaction

class Blockchain:
    sym = 'BTC'
    chain = []
    difficulty = 1
    miner_reward = 10
    owner = 'Reece'

    def get_last_block(self):
        return self.chain[-1]

    def get_previous_block(self,block):
        block_index = self.chain.index(block,1,len(self.chain))
        return self.chain[block_index - 1]


    def miner_reward_tx(self,owner):
        return Transaction('REWARD',owner,self.miner_reward)

    def create_genesis_block(self):
        print('First block in chain, generating the gensesis block...')
        #gBlock is the Genesis Block (First Block in the chain)
        if len(self.chain) < 1:
            gBlock = Block([],'GENESIS_BLOCK')
            self.chain.append(gBlock)

    def push(self,block):
        print('Adding block to blockchain...')
        self.chain.append(block)

    def mine(self,block):
        mBlock = block
        #Generates a new block to be added to the chain
        #Generats a proof of work hash and nonce for a given block
        ###
        
        #Init and Insert reward transaction into block
        print(self.get_last_block().getHash())
        mBlock.addTransaction(self.miner_reward_tx(self.owner))

        print('Mining Block...')
        while mBlock.getHash().startswith('0' * self.difficulty) != True:
            #print (str(block.getHash()) + ' Nonce: ' + str(block.nonce))
            mBlock.nonce += 1
            mBlock.calculateHash()
        print('Block mined!, Hash: '+block.getHash() + ' Nonce: ' + str(block.nonce))
        self.push(mBlock)
        return True

    def printChain(self):
        for block in self.chain:
            block.printDetails()


    def verifyChain(self):
        valid_block = True
        block_index = -1
        chain_sz = len(self.chain)
        for block in range(1,chain_sz,block_index):
            if self.chain[block_index].getHash() != block.previous_hash:
                valid_block = False
                print('MISMATCH')
                print('Hash of block at index '+str(block_index) +': '+ self.get_last_block().getHash())
                print('Prev hash attrib in current block: '+ block.previous_hash)
            #block_index += 1
        #check the block fits the chain protocols, if it does not it is rejected.
        #hash must match difficulty (to define: dif 1 = 5x0 hash prefix)
        #previous hash must match hash of previous block
            if not valid_block:
                print('INVALID BLOCK')
                break
        print('Blockchain verified and valid.')
        return valid_block
        


    def __init__(self,sym,start_dif=5,start_reward=10):
        self.sym = sym
        self.difficulty = start_dif
        self.miner_reward = start_reward
        self.chain = []
        #Create the genesis block
        self.create_genesis_block()
    
def verifyHash(block,hash):
    blockhash = str(hashlib.sha256(repr([block.transactions,block.previous_hash,block.nonce]).encode('utf-8')).hexdigest())
    if hash == blockhash:
        return True
    return False