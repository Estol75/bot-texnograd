import asyncio
import discord
from discord import utils
import config
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        client.loop.create_task(status_task())
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            member = utils.get(message.guild.members, id=payload.user_id)
            try:
                emoji = str(payload.emoji)
                role = utils.get(message.guild.roles, id=config.ROLES[emoji])
                if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))
            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))
    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=config.ROLES[emoji])
            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))
        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Дайте боту все права пжпжпж'),status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('и на верх меня пжпжжп'),status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('кста ты далбаеб ой'),status=discord.Status.online)
        await asyncio.sleep(3)






client = MyClient()

client.run('Njk4NDk0NTY3MDA3Mzg3Njg5.XqVNgQ.3cxY53qggB49umfXWQNtNuVQ0bM')
