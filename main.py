import discord
import json
import os
from command.CommandManager import CommandManager
from utils.Logger import Logger

botowner = '786906605987037224'

class Main(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_manager = CommandManager() 

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        if message.content.startswith('!'):
            try:
                await self.command_manager.handle_message(message)
            except Exception as e:
                await message.channel.send('Error: ' + str(e))
                Logger.error(e)

if __name__ == '__main__':
    print('Starting...')
    global config
    # config = json.load(open('config.json'))
    client = Main()
    print(os.environ.get('TOKEN'))
    client.run(os.environ.get('TOKEN'))