import discord
import time
import math
class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        split_message = message.content.split(r'\s+')
        prefix = split_message[0]
        if prefix == "%ping":
            current_time = time.time()
            message_time = message.created_at.timestamp()
            delay = current_time - message_time
            await message.channel.send(f'Pong! It took me {math.floor(delay * 1000)}ms to receive your message!')
        elif prefix == "%jesse":
            await message.channel.send('I hate the Philippines!')

intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run(CLIENT_KEY)