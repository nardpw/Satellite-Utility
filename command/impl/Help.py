from ..Command import Command
import discord

class Help(Command):
    def __init__(self, commandmanager):
        super().__init__('help', self.on_command, 'Displays this message', 'help', ['help', '?'])
        self.commandmanager = commandmanager
    
    async def on_command(self, message, args):
        embed = discord.Embed(title='Help', description='', color=0x00ff00)
        embed.add_field(name='Commands', value='\n'.join(['`{}` - {}'.format(c.name, c.desc) for c in self.commandmanager.commands]), inline=False)
        embed.add_field(name='Aliases', value='\n'.join(['`{}` - {}'.format(c.name, ', '.join(c.aliases)) for c in self.commandmanager.commands]), inline=False)
        embed.add_field(name='Usage', value='\n'.join(['`{}` - {}'.format(c.name, c.usage) for c in self.commandmanager.commands]), inline=False)
        embed.set_footer(text='Made by @nardpw#5794')
        await message.channel.send(embed=embed)