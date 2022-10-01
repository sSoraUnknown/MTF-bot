import sys
import random

get = 'roll'
alias = ['dr']
send = (
'''```
Name:  %s 
His roll: %s
```''' 
)

msg = 'типо сообщение'

def calc():
    global msg
    str = msg
    num = [int(s) for s in str.split() if s.isdigit()][0]
    msg = random.randint(1, num)



#str = message.content
#num = [int(s) for s in str.split() if s.isdigit()][0]
#num = random.randint(1, num)
#msg = message.author + str(num)

#print('%s %s %d' % (message.author, '\n' ,num))
#await message.channel.send(msg)
#await message.channel.send(message.author)
#await message.channel.send(num)