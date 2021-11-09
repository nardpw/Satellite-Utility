from command.Command import Command
from utils.Logger import Logger
import utils.LinkUtils as LinkUtils
import discord

class Shrink(Command):
    def __init__(self):
        super().__init__('shrink', self.shrink, 'Shrinks a url', 'shrink <url>', ['shrink', 'shr'])
    
    async def shrink(self, message, args):
        if len(args) == 0:
            await message.channel.send('Please mention a url')
            return
        try:
            Logger.log('Shrinking ' + args[0] + ' ' + str(message.author))
            await message.channel.send('Shrinking.. .')
            await message.channel.send('Shrinked! code: ' + str(LinkUtils.shrink(args[0])) + ' ' + str(message.author))
            Logger.log('Shrinked ' + args[0] + ' ' + str(message.author))
        except Exception as e:
            await message.channel.send('Error: ' + str(e))
            Logger.error(e)