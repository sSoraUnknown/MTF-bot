import datetime
import os

get = 'farm'
send = (
'''```
Noice, you just got +10 coins!
Balance: %s
```''')
def FarmBalance(message):
  bal = -1
  if(os.path.exists("DB/bal/%s.txt"%message.author.id)):
    f = open("DB/bal/%s.txt"%message.author.id, "r")
    bal = f.read()
    bal = int(bal)+10
    f.close()
    f = open("DB/bal/%s.txt"%message.author.id, "w+")
    bal = str(bal)
    f.write(bal)
  else:
    f = open("DB/bal/%s.txt"%message.author.id, "w+")
    f.write("10")
    bal = 10
    bal = str(bal)

  print('+++ New bal: %s from %s. DATE: %s' % (bal, message.author, datetime.datetime.now()))
  return bal