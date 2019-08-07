from blockchain import Blockchain
from transaction import Transaction
from block import Block
#Create a new blockchain currency 'Ecoin', init difficulty 3, 'init Mining reward 10'


evilCoin = Blockchain('EC',3,10)

while True:
    print('Welcome to the blockchain.')
    print('1 - Create a transaction')
    print('2 - Mine block')
    print('3 - View Entire blockchain')
    print('4 - View Current block details')
    print('q - Quit')

    usr_in = input('-> ')

    block = Block(None,evilCoin.get_last_block().getHash())
    if usr_in == '1':
        print('Creating a new transaction Record.')
        sender = input('Sending Address: ')
        reciever = input('Recieving Address: ')
        amount = input('Amount: ')
        tx = Transaction(sender,reciever,float(amount))
        block.addTransaction(tx)
        print('Transaction '+ tx.signature +' added to block.') 
    elif usr_in == '2':
        evilCoin.mine(block)
    elif usr_in == '3':
        evilCoin.printChain()
    elif usr_in == '4':
        block.printDetails()
    elif usr_in == 'q':
        break
    else:
        print('Invalid option.')
        continue
    evilCoin.verifyChain()
else:     
    print('Goodbye!')
