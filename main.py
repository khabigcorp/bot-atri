import discord
import time
import math
import os
from mistralai import Mistral
class Client(discord.Client):
    async def on_ready(self):
        self.delusional = False
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user and self.delusional:
            time.sleep(5)
            api_key = os.environ["MISTRAL_API_KEY"]

            client = Mistral(api_key=api_key)

            response = client.beta.conversations.start(
                agent_id="ag_068602445d8b7e9980004e12b933eea0",
                inputs=message.content,
                #store=False
            )

            reply = ""
            for item in response.outputs:
                if (type(item).__name__ == "MessageOutputEntry"):
                    reply = item.content

            await message.channel.send(reply)
        elif message.author == self.user and not self.delusional:
            return
        
        split_message = message.content.split()
        prefix = split_message[0]
        print(split_message)
        if prefix == "%ping":
            current_time = time.time()
            message_time = message.created_at.timestamp()
            delay = current_time - message_time
            await message.channel.send(f'Pong! It took me {math.floor(delay * 1000)}ms to receive your message!')
        elif prefix == "%jesse":
            await message.channel.send('I hate the Philippines!')
        elif prefix == "%say":
            self.delusional = True
            await message.channel.send(" ".join(split_message[1:]))
        elif prefix == "%stop":
            self.delusional = False
            await message.channel.send("Time to stop...")

intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
CLIENT_KEY = os.getenv("CLIENT_KEY")
client.run(CLIENT_KEY)