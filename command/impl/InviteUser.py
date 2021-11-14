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
            user = message.mentions[0] if len(message.mentions) > 0 else message.guild.get_member(int(args[0]))
            if user in self.invited_users:
                if message.channel.id in self.invited_users[args[0]]:
                    await message.channel.send('Already invited')
                    return

            invite = await self.create_invite_onece(message.channel)
            if user not in self.invited_users:
                self.invited_users[user] = list()
            self.invited_users[user].append(message.channel.id)
            Logger.log('Invited ' + invite.url + user + ' ' + str(message.author))
            await message.mentions[0].send('You have been invited to the server!' + invite.url)
            await message.channel.send('Invited ' + user + ' ' + str(message.author))
        except Exception as e:
            await message.channel.send('Error: ' + str(e))
            Logger.error(e)

    @staticmethod
    async def create_invite_onece(channel: discord.abc.GuildChannel, max_uses=1, max_age=0, temporary=False):
        return await channel.create_invite(max_uses=max_uses, max_age=max_age, temporary=temporary)