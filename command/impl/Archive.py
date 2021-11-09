from command.Command import Command
from utils.Logger import Logger
from utils.Archive import *

class Archive(Command):
    def __init__(self):
        super().__init__('archive', self.archive, 'Archives a web page', 'archive <url>', ['archive', 'arc'])
    
    async def archive(self, message, args):
        if len(args) == 0:
            await message.channel.send('Please Valid Url')
            return
        try:
            Logger.log('Archiving ' + args[0] + ' ' + str(message.author))
            await message.channel.send('Archiving.. .')
            await message.channel.send('Archived! code: ' + str(save_archive(args[0])) + ' ' + str(message.author))
            Logger.log('Archived ' + args[0] + ' ' + str(message.author))
        except Exception as e:
            await message.channel.send('Error: ' + str(e))
            Logger.error(e)