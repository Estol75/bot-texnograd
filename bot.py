#all import for work
import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix = '!')

#the console write when the bot start
@client.event
async def on_ready():
    print('The bot is ready to work')
    client.loop.create_task(status_task())

@client.event
async def on_member_join(member):
    print(f'{member}has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'The member has left the server')


@client.command()
async def корды(ctx):
    await ctx.send('**Вот тебе полезные координаты:**\r\n'
                      '```Ферма скелетов (По метро): -7844 -5753```'
                      '```Ферма гвардов (по метро): -8000 -6435```'
                      '```Ферма золота и яма: -7777 -6460```'
                      '```Ферма зомби и пауков (По метро): -7430 -5895```'
                      '```Городская ферма ифритов (В аду): -1200 -630```'
                      '```Портал в энд (В аду): -1100 -950```'
                      '```Портал в Техноград (В аду): -918 -750```'
                      '```Портал в хаб Технограда: -7400 -6085```'
                      '```Склад: -7470 -6015```')

#status for bot
@client.event

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Дайте боту все права пжпжпж'),status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('и на верх меня пжпжжп'),status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('кста ты далбаеб ой'),status=discord.Status.online)
        await asyncio.sleep(3)

token = os.environ.get('BOT_TOKEN')
client.run(str(token))

