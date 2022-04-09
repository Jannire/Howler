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

#gifs
  if message.content.startswith('inception'):
    await message.channel.send('https://tenor.com/view/leonardo-di-caprio-inception-gif-9086835')
  if message.content.startswith('tenet'):
    await message.channel.send('https://tenor.com/view/tenet-gif-18707553')
  if message.content.startswith('dobby'):
    await message.channel.send('https://tenor.com/view/dance-dobbi-harry-potter-meme-gif-16801919')
  if message.content.startswith('harry'):
    await message.channel.send('https://tenor.com/view/harry-potter-harrypotter-ron-hermione-gif-16137638')
  if message.content.startswith('piero'):
    await message.channel.send('https://tenor.com/view/pingu-mad-stare-angry-not-happy-death-glare-gif-23558934')
  if message.content.startswith('midsommar'):
    await message.channel.send('https://tenor.com/view/midsommar-dancing-turning-spinning-gif-15685623')
  if message.content.startswith('mitty'):
    await message.channel.send('https://tenor.com/view/the-secret-life-of-walter-mitty-comedy-drama-adventure-ben-stiller-gif-3454082')

#tok -> token del bot
secret = os.environ['tok']
client.run(secret)
