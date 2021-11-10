from command.Command import Command
from utils.Logger import Logger
import discord

class InviteUser(Command):
    def __init__(self):
        super().__init__('invite', self.invite, 'Invites a user to the server', 'invite <user>', ['invite', 'inv'])
        self.invited_users = {}
    
    async def invite(self, message, args):
        if len(args) == 0:
            await message.channel.send('Please mention a user')
            return
        try:
            Logger.log('Inviting ' + args[0] + ' ' + str(message.author))

            if args[0] in self.invited_users:
                if message.channel.id in self.invited_users[args[0]]:
                    await message.channel.send('Already invited')
                    return

            invite = await self.create_invite_onece(message.channel)
            if args[0] not in self.invited_users:
                self.invited_users[args[0]] = list()
            self.invited_users[args[0]].append(message.channel.id)
            Logger.log('Invited ' + invite.url + args[0] + ' ' + str(message.author))
            await message.mentions[0].send('You have been invited to the server!' + invite.url)
            await message.channel.send('Invited ' + args[0] + ' ' + str(message.author))
        except Exception as e:
            await message.channel.send('Error: ' + str(e))
            Logger.error(e)

    @staticmethod
    async def create_invite_onece(channel: discord.abc.GuildChannel, max_uses=1, max_age=0, temporary=False):
        return await channel.create_invite(max_uses=max_uses, max_age=max_age, temporary=temporary)