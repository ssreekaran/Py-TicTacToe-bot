import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
P1 = True
pos = ["1","2","3","4","5","6","7","8","9"]
pos_check = [True,True,True,True,True,True,True,True,True]
@client.event
async def on_message(message):
    global P1
    global pos
    global pos_check
    def check_winner():
      if (pos[0] == pos[1] == pos[2] or pos[3] == pos[4] == pos[5] or pos[6] == pos[7] == pos[8] or pos[0] == pos[3] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8] or pos[0] == pos[4] == pos[8] or pos[2] == pos[4] == pos[6]):
        return("Winner, type $reset to reset the board and $t3 if you want a new game.")
      else:
        return("")
    if message.author == client.user:
        return
    if message.content.startswith('$commands'):
        await message.channel.send('$commands -> get commands'+'\n' + '$t3 -> starts a game of tictactoe, type the number for the position you want to play in'+'\n' + '$reset -> resets the board, you must use this before starting a new round')
    if message.content.startswith('$reset'):
      pos = ["1","2","3","4","5","6","7","8","9"]
      pos_check = [True,True,True,True,True,True,True,True,True]
    if message.content.startswith('$t3'):
      await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
  +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'+'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('1')):
      if (pos_check[0]):
        if(P1):
          pos[0] = "X"
          pos_check[0] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[0] = "O"
          pos_check[0] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('2')):
      if (pos_check[1]):
        if(P1):
          pos[1] = "X"
          pos_check[1] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[1] = "O"
          pos_check[1] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('3')):
      if (pos_check[2]):
        if(P1):
          pos[2] = "X"
          pos_check[2] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[2] = "O"
          pos_check[2] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('4')):
      if (pos_check[3]):
        if(P1):
          pos[3] = "X"
          pos_check[3] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[3] = "O"
          pos_check[3] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('5')):
      if (pos_check[4]):
        if(P1):
          pos[4] = "X"
          pos_check[4] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[4] = "O"
          pos_check[4] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('6')):
      if (pos_check[5]):
        if(P1):
          pos[5] = "X"
          pos_check[5] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[5] = "O"
          pos_check[5] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('7')):
      if (pos_check[6]):
        if(P1):
          pos[6] = "X"
          pos_check[6] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[6] = "O"
          pos_check[6] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('8')):
      if (pos_check[7]):
        if(P1):
          pos[7] = "X"
          pos_check[7] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[7] = "O"
          pos_check[7] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
    if (message.content.startswith('9')):
      if (pos_check[8]):
        if(P1):
          pos[8] = "X"
          pos_check[8] = False
          P1 = False
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        elif (not(P1)):
          pos[8] = "O"
          pos_check[8] = False
          P1 = True
          await message.channel.send(pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
            +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
            +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8]+'\n'+check_winner())
        check_winner()
      else:
        await message.channel.send('Can\'t do that, position is already filled' 
          +'\n'+pos[0]+'|'+pos[1]+'|'+pos[2]+'\n'+'-------' 
          +'\n'+pos[3]+'|'+pos[4]+'|'+pos[5]+'\n'+'-------'    
          +'\n'+pos[6]+'|'+pos[7]+'|'+pos[8])
client.run(os.getenv('TOKEN'))