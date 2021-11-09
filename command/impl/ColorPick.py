from command.Command import Command
from utils.Logger import Logger
import utils.ImageUtils as ImageUtils
import discord
import requests

class ColorPick(Command):
    def __init__(self):
        super().__init__('colorpick', self.colorpick, 'Picks a random color', 'colorpick', ['colorpick', 'pic'])
    
    async def colorpick(self, message: discord.Message, args):
        try:
            Logger.log('Colorpick ' + str(message.author))
            await message.channel.send('Picking.. .')
            print(message.attachments)
            with open('image.png', 'wb') as f:
                f.write(requests.get(message.attachments[0].url).content)
            colors = ImageUtils.extract_main_color('image.png')
            ImageUtils.colors_to_image(colors, 'image.png')
            await message.channel.send('Picked!', file=discord.File('image.png'))
            Logger.log('Picked ' + str(message.author))
        except Exception as e:
            await message.channel.send('Error: ' + str(e))
            Logger.error(e)