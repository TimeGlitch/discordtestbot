from keep_alive import keep_alive
import openai
import discord
import os
import requests
import json
import inspirobot
from replit import db

client = discord.Client()
openai.api_key = os.environ['OPENAI_API_KEY']




@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  channel = client.guilds[0].text_channels[0]
  await channel.send('gday')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send("hello")
  
  if message.content.startswith('$inspire'):
    quote = inspirobot.generate()
    await message.channel.send(quote)

  if message.content.startswith('$userinfo'):
    await message.channel.send(message.author.name)

  if message.content.startswith('$openai'):
    await message.channel.send

  """
  if message.content.startswith('$regSag'):
    await message.channel.send(message.content.split(' '))
    #temp = message.content.split(' ')[1]
    #print(temp)
    #if temp in db:

    
    #if int(len(message.content.split(' '))) <= 2:

     # await message.channel.send('add true or false as an argument dumbass')
     # return
    #db.update({str(message.author): str(message.content.split(' ')[1])})
  if message.content.startswith('$checkSag'):
    if message.author in db:
      await message.channel.send(db[message.author])
  """






  



keep_alive()

client.run(os.getenv('TOKEN'))