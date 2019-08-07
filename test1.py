from blockchain import Blockchain
from transaction import Transaction
from block import Block
#Create a new blockchain currency 'Ecoin', init difficulty 3, 'init Mining reward 10'


evilCoin = Blockchain('EC',3,10)


#although each block has its own transactions, all of them appear in every block...

#block1 = Block([Transaction('Reece','Caryn',5)],evilCoin.get_last_block().getHash())
#block2 = Block([Transaction('Reece','Caryn',10),Transaction('Caryn','Reece',5)],evilCoin.get_last_block().getHash())
#block3 = Block([],evilCoin.get_last_block().getHash())

#evilCoin.mine(block1)
#evilCoin.mine(block2)
#evilCoin.mine(block3)

while True:
    inp = input('Mine?')
    if inp:
        evilCoin.mine(Block([],evilCoin.get_last_block().getHash()))
        evilCoin.printChain()
        evilCoin.verifyChain()