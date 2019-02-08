__author__ = 'Jason'
from discord.ext.commands import Bot
from discord import Game
from itertools import cycle
from discord.utils import get
import random
import asyncio
import datetime
import time
import ReverseImage

TOKEN = 'NTI5NzY1ODkwODk2NDI5MDU2.Dw1mzQ.2z6Z64D4dqM9jXNsoxIKotMkt2c'
BOT_PREFIX = ("?", "!")  # Prefixes you add to call the bot
client = Bot(command_prefix=BOT_PREFIX)
messageCache = {}
@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    attachmentsDict = reaction.message.attachments[0]#dictionary containing information about the message with reaction added
    messageCache[reaction.message] = []
    #print(attachmentsDict)
    print("Reaction added")
    if 'url' in attachmentsDict:
        print('is in"')
        links = ReverseImage.kprofileLookup(attachmentsDict['url'])
        i = 0
        while i< len(links):
            if i<2:
                msg = await client.send_message(channel, 'https://www.kprofiles.com/'+ links[i])
                messageCache[reaction.message].append(msg)
            i+=1
    print("On reaction add done")
@client.event
async def on_reaction_remove(reaction,user):
    channel = reaction.message.channel
    print('Reaction removed')
    if reaction.message in messageCache:
        for x in messageCache[reaction.message]:
            await client.delete_message(x)
    print("On reaction removed done")

@client.event
async def on_ready():
    print('Yuqi is ready.')

@client.command(pass_context=True)
async def kpop(context):
    await client.send_message(context.message.channel, "You can upload a picture and add a reaction to the picture"+
                                                       " if you want their kprofile to appear.")



#deletes the last 10 messages under 14 days old
#can pass in a number to specify how many to delete
@client.command(pass_context=True)
async def clear(context):
        try:
            value = int(context.message)
            print('deleting')
            channel = context.message.channel
            async for message in client.logs_from(channel, value):
                print('deleting')
                await client.delete_message(message)
        except ValueError:
            print('deleting')
            channel = context.message.channel
            async for message in client.logs_from(channel, 10):
                print('deleting')
                await client.delete_message(message)

print("Running Mainboio")
print("Running Mainboio")
client.run(TOKEN)
