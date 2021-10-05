import discord
import os
from dotenv import load_dotenv
from models import ActivityUser
from datetime import datetime

class MyDiscordBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        if "-xp" in message.channel.name:
            print('+15 xp for user to {0.author}! '.format(message))
            
            userActivity = ActivityUser(
                user_id=1, 
                created_at=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
                updated_at=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )

            userActivity.save()
            
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são: {os.linesep} 1 - Não desrespeitar os membros; {os.linesep} 2 - Serão permitidos apenas assuntos relacionados a desenvolvimento;')

        elif message.content == '?level':
            await message.author.send('Level ainda não definido!')

    async def on_member_join(self, member):
        guild = member.guild

        if guild.system_channel is not None:
            message = f'{member.mention} acabou de entrar no {guild.name}, welcome!'
            await guild.system_channel.send(message)

intents = discord.Intents.default()
intents.members = True

client = MyDiscordBot(intents=intents)
load_dotenv()
client.run(os.getenv('DISCORD_KEY'))
