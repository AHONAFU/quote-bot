from quoters import Quote
import discord

client = discord.Client()

@client.event
async def on_ready():
   print('I have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('+help'):
    channel = client.get_channel(channel_id)
    await message.channel.send('''
    +help
    +a --- anime quotes
    +tv --- tv show quotes
    +x --- random
    ''')
  if message.content.startswith('+a'):
    channel = client.get_channel(channel_id)
    embed = discord.Embed(title="Quote Bot", color=0xff0000)
    embed.add_field(name="Here is a quote for you", value=Quote.print_anime_quote(), inline=False)
    await channel.send(embed=embed)
  if message.content.startswith('+tv'):
    channel = client.get_channel(channel_id)
    embed = discord.Embed(title="Quote Bot", color=0xff0000)
    embed.add_field(name="Here is a quote for you", value=Quote.print_series_quote(), inline=False)
    await channel.send(embed=embed)
  if message.content.startswith('+x'):
    channel = client.get_channel(channel_id)
    embed = discord.Embed(title="Quote Bot", color=0xff0000)
    embed.add_field(name="Here is a quote for you", value=Quote.print(), inline=False)

    await channel.send(embed=embed)

client.run('ODM4MDA1Nzk1MjYxMTIwNTE0.YI0ztg.nd_nQR2j0ywF5fpKP5OxMB-uYW0')