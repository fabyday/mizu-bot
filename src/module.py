import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
import os 


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../privates/token")) as fp :
    token = fp.readline()
client.run(token)

