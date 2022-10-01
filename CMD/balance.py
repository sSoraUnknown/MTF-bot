import datetime
import os

get = 'balance'
alias = ['bal']
send = '```Balance: %s```'
def CheckBalance(message):
    bal = -1
    if(os.path.exists("DB/bal/%s.txt"%message.author.id)):
        f = open("DB/bal/%s.txt"%message.author.id, "r")
        bal = f.read()
    else:
        f = open("DB/bal/%s.txt"%message.author.id, "w+")
        f.write("0")
        bal = 0
        bal = str(bal)
    
    print('bbb %s checked balance. Balance: %s. DATE: %s' %(message.author, bal, datetime.datetime.now()))
    return bal