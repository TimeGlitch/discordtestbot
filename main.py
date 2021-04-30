from keep_alive import keep_alive
import openai
import discord
from discord.ext import commands
import os
import requests
import json
import inspirobot
from replit import db

client = commands.Bot(command_prefix = '$')
openai.api_key = os.environ['OPENAI_API_KEY']


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  channel = client.guilds[0].text_channels[0]
  await channel.send('I am online.')

@client.command()
async def poggers(ctx):
  await ctx.send(":poggers:")

@client.command()
async def inspire(ctx):
  quote = inspirobot.generate()
  await ctx.send(quote)

@client.command()
async def gpt(ctx, *, text):
  role = discord.utils.find(lambda r: r.name == 'tester', ctx.guild.roles)
  if role in ctx.author.roles:
    temp = openai.Completion.create(
      engine = "davinci",
      prompt = text,
      max_tokens= 50
    )
    await ctx.send(text + temp.choices[0].text)
  else:
    await ctx.send("you don't have perms")

@client.command()
async def question(ctx, *, text):
  print("temp")
  


keep_alive()

client.run(os.environ['DISCORD_TOKEN'])