from command.Command import Command
from utils.Logger import Logger
from utils.LinkUtils import *
import discord

class YoutubeDirectLink(Command):
    def __init__(self):
        super().__init__('youtubedl', self.youtubedl, 'Gets the direct link of a youtube video', 'youtubedl <url>', ['youtubedl', 'ytdl'])
    
    async def youtubedl(self, message, args):
        if len(args) == 0:
            await message.channel.send('Please mention a url')
            return
        try:
            Logger.log('Youtubedl ' + args[0] + ' ' + str(message.author))
            await message.channel.send('Getting.. .')
            await message.channel.send('Got! code: ' + str(youtube_dl(args[0])) + ' ' + str(message.author))
            Logger.log('Got ' + args[0] + ' ' + str(message.author))
        except Exception as e:
            await message.channel.send('error')
            Logger.error(e)