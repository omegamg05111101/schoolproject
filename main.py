import discord
from discord.ext import commands ,tasks
from discord import Member

#client(bot)
client = commands.Bot(command_prefix='!')
#version of bot
   
@client.command(name='ver')

async def ver(context):
    
    myEmbed1=discord.Embed(title="title1", description="description 1",color=0xe91e63)
    myEmbed1.add_field(name="Version1", value="1.4",inline=False)
    myEmbed1.add_field(name="Version Number", value="1.4.5",inline=False)
    
    await context.message.reply(embed=myEmbed1)
@client.command(name='cmd')
async def cmd(context):

    myEmbed2 = discord.Embed(title="title2", description="description 2",color=0x1abc9c)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version Number", value="2.4.5",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)
    myEmbed2.add_field(name="Version2", value="2.4",inline=False)

    await context.message.reply(embed=myEmbed2)
client.run('ODQyMDYwNTc3ODE0NjA5OTIw.YJv0Bg.gAbxF10kdBLjkW3YTv6Bp5xtcxs')