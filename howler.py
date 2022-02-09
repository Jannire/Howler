#written in replit initially
#escrito en replit inicialmente

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Buenardas entre como {0.user}'.format(client))

#solo responde mensajes
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hola'):
    await message.channel.send('Holas')
  if message.content.startswith('$sistema'):
    await message.channel.send('https://www.youtube.com/watch?v=SeWc7P4E8uU')
  if message.content.startswith('zzz'):
    await message.channel.send('https://www.youtube.com/watch?v=E2t9jUyra7s')

#tok -> token del bot
secret = os.environ['tok']
client.run(secret)
