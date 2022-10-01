from asyncio.windows_events import NULL
import discord
import datetime
import sys
import os
sys.path.append('/settings')
sys.path.append('/CMD')
sys.path.append('/RPGHelper')
sys.path.append('/Others')

# импорт скриптов PY, в которых описаны функции
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from settings import config
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from CMD import balance # BALANCE HERE
from CMD import farm # FARM HERE
from CMD import hello # HELLO HERE
from CMD import help # HELP HERE
#from CMD import lose UPD -> Archived
from CMD import newcommand # NEW COMMAND HERE
from CMD import prefix # PREFIX HERE
from CMD import roll # ROLL HERE
from CMD import say # SAY HERE
from CMD import send # SEND HERE
from CMD import succ # SUCC HERE
from CMD import test # TEST HERE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from RPGHelper import RPG_areas # RPG AREAS HERE
from RPGHelper import RPG_ascended # RPG ASCENDED HERE
from RPGHelper import RPG_d10 # D10 HERE
from RPGHelper import RPG_help # RPG HELP
from RPGHelper import RPG_pet # RPG PET
from RPGHelper import RPG_trade_d # RPG TRADE HERE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from Others import Others_help # OTHERS HELP HERE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# import time
# UPD -> заброшено, ибо более нет необходимости в импорте

# для более удобного обращения к функциям
client = discord.Client()

client.b = 0 # типо баланс (но глобальный) - типо любой пользователь делает с ним чо хочет
# поэтому нужно сделать БД
# в душе не ебу, как это делается
# придумала, как сделать, но я иду нахуй из-за лени

# UPD -> СДЕЛАНО ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# print('gavno') - вывод в консоль (которая TERMINAL в Visual Studio Code) 
# UPD -> либо в CMD'шку (bat'ник)
# тупо юзаю это, чтобы видеть через терминал, кто что сделал

# + есть команда 'mtf send' - отправляет сообщение пользователя
# в консольку с префиксом 'msg' - так проще искать через CTRL+F 
# UPD -> теперь кидает на мой личный сервер


# собственно, список действий:
#
# [prefix] [some bullshit or/and user#0000]
#
# hhh - hello -> 
# hhh user#0000 checked if bot alive
#
# wsh (want some help) - help -> 
#   wsh user#0000 want some help
#
# +++ - farm (+###) -> 
#   +++ New bal: 10 from user#0000
#
# --- - lose -> 
#   --- New bal: 0 from user#0000
#
# bbb - bal/balance -> 
#   bbb user#0000 checked balance. Balance: 0
#
# sss - succ/suck/sucks -> 
#   sss user#0000 said what bot is suck ;c
#
# msg (message) - send -> 
#   msg from user#0000 :  кто прочитал - тот сдохнет
#
# rrr - roll/dr -> 
#   rrr user#0000 rolled 1
#
# nfc = newcommand ->
#   nfc user#0000 just checked new command
#
# UPD -> заброшено, слишком много функций описывать

# On ready says:
@client.event
async def on_ready():
  print('I\'AM ALIFE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# REBUILD THIS FUCKING EVENT PLEASE
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # PREFIX HERE
  pref = prefix.prefix

  # BOT HELP HERE
  if (message.content.startswith(pref+help.get) and len(message.content) == len(pref+help.get)) or (message.content.startswith(pref+help.alias[0]) and len(message.content) == len(pref+help.alias[1])) or (message.content.startswith(pref+help.alias[1]) and len(message.content) == len(pref+help.alias[1])):
    print('wsh %s want some help. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(help.send 
    %(pref+hello.get, pref+roll.get, roll.alias[0], pref+balance.get, balance.alias[0], pref+farm.get, pref+succ.get, succ.alias[0], succ.alias[1], pref+send.get, pref+newcommand.get))

  # RPG HELP HERE
  if (message.content.startswith(pref+RPG_help.get) and len(message.content) == len(pref+RPG_help.get)) or (message.content.startswith(pref+RPG_help.alias[0]) and len(message.content) == len(pref+RPG_help.alias[0])):
    print('rph %s want some help with rpg commands. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(RPG_help.send 
    %(pref+RPG_areas.get, RPG_areas.alias[0], pref+RPG_ascended.get, RPG_ascended.alias[0], pref+RPG_trade_d.get, RPG_trade_d.alias[0], pref+RPG_d10.get, pref+RPG_pet.get))

  # OTHERS HELP HERE
  if (message.content.startswith(pref+Others_help.get) and len(message.content) == len(pref+Others_help.get)) or (message.content.startswith(pref+Others_help.alias[0]) and len(message.content) == len(pref+Others_help.alias[0])) or (message.content.startswith(pref+Others_help.alias[1]) and len(message.content) == len(pref+Others_help.alias[1])):
    print('oth %s want some info about some stuff. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(Others_help.send)

  # FARM HERE
  if message.content.startswith(pref+farm.get) and len(message.content) == len(pref+farm.get):
    bal = farm.FarmBalance(message)
    await message.channel.send(farm.send % bal)

  # LOSE HERE
  # UPD -> Archived
  #if message.content.startswith(pref+lose.get) and len(message.content) == len(pref+lose.get):
  #  client.b = 0
  #  print('--- New bal: %d from %s. DATE: %s' % (client.b, message.author, datetime.datetime.now()))
  #  await message.channel.send(lose.send % client.b)

  # BALANCE HERE <- WORK IN PROGRESS
  if (message.content.startswith(pref+balance.get) and len(message.content) == len(pref+balance.get)) or (message.content.startswith(pref+balance.alias[0]) and len(message.content) == len(pref+balance.alias[0])):
    bal = balance.CheckBalance(message)
    await message.channel.send(balance.send % bal)

  # SLOTS HERE
  # Создать новый PY script под названием slots.py в папке CMD
  # Определить slots.msg как message.content (как в ROLL HERE)
  # Определить функцию slots.roll() и выполнить её (как в ROLL HERE)
  # Определить функцию смены баланса (как в BALANCE HERE или FARM HERE)
  # Определить print(slt [name] slots [num]. New bal: [bal])

  # ROLL HERE
  if message.content.startswith(pref+roll.get) or message.content.startswith(pref+roll.alias[0]):
    roll.msg = message.content
    roll.calc()
    print('rrr %s rolled %s. DATE: %s' % (message.author, roll.msg, datetime.datetime.now()))
    await message.channel.send(roll.send % (message.author, roll.msg))

  # SUCC HERE
  if ((message.content.startswith(pref+succ.get) or message.content.startswith(pref+succ.alias[0])) and len(message.content) == len(pref+succ.get)) or (message.content.startswith(pref+succ.alias[1]) and len(message.content) == len(pref+succ.alias[1])):
    print('sss %s said what bot is succ/suck/sucks ;c DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(succ.send)

  # SAY HERE
  if message.content.startswith(pref+say.get):
    if len(message.content) != len(pref+say.get):
      msg = message.content
      await message.channel.send(say.send % msg[len(pref+say.get)+1:])

  # SEND HERE
  if message.content.startswith(pref+send.get):
    channel = client.get_channel([REDACTED])
    msg = message.content
    msg = msg[len(pref+send.get)+1:]
    msg = '%s: %s' %(message.author, msg) 
    await channel.send(msg)
    await message.channel.send(send.send)

  # TEST HERE
  if message.content.startswith(pref+test.get) and len(message.content) == len(pref+test.get):
    print('tet TEST WAS USED BY %s. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(test.send)

  # NEW COMMAND HERE
  if message.content.startswith(pref+newcommand.get) and len(message.content) == len(pref+newcommand.get):
    print('nfc %s just checked new command. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(newcommand.send)

  #if message.content.startswith('pls porn') and len('pls porn'):
  #  print('prn %s fap again. DATE: %s' %(message.author, datetime.datetime.now()))

  # RPG D10 HERE
  if message.content.startswith(pref+RPG_d10.get) and len(message.content) == len(pref+RPG_d10.get):
    print('d10 %s need help with D10 in Epic RPG Bot. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(RPG_d10.send)

  # RPG PET HERE
  if (message.content.startswith(pref+RPG_pet.get) and len(message.content) == len(pref+RPG_pet.get)):
    print('pet %s need help with pets catching. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(RPG_pet.send)

  # RPG AREAS HERE
  if (message.content.startswith(pref+RPG_areas.get) and len(message.content) == len(pref+RPG_areas.get)) or (message.content.startswith(pref+RPG_areas.alias[0]) and len(message.content) == len(pref+RPG_areas.alias[0])):
    print('ara %s need help with areas commands. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(RPG_areas.send)

  # RPG ASCENDED HERE
  if (message.content.startswith(pref+RPG_ascended.get) and len(message.content) == len(pref+RPG_ascended.get)) or (message.content.startswith(pref+RPG_ascended.alias[0]) and len(message.content) == len(pref+RPG_ascended.alias[0])):
    print('asc %s need help with ascended commands. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(RPG_ascended.send)

  # RPG TRADE HERE
  if (message.content.startswith(pref+RPG_trade_d.get) and len(message.content) == len(pref+RPG_trade_d.get)) or (message.content.startswith(pref+RPG_trade_d.alias[0]) and len(message.content) == len(pref+RPG_trade_d.alias[0])):
    print('trd %s need help with trade commands. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(RPG_trade_d.send)
  
  # HELLO HERE
  if message.content.startswith(pref+hello.get) and len(message.content) == len(pref+hello.get):
    print('hhh %s checked if bot alive. DATE: %s' %(message.author, datetime.datetime.now()))
    await message.channel.send(hello.send)  

# run bot with config.token (in folder settings)
client.run(config.token)

# test functions for "Bot close.bat"
#print('Bye bye')
#async def close():
#  await client.close()
#os.system("pause")
