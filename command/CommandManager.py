from command.impl.Archive import Archive
from command.impl.Help import Help
from command.impl.InviteUser import InviteUser
from command.impl.CoinRate import CoinRate
from command.impl.Shrink import Shrink
from command.impl.ColorPick import ColorPick
from command.impl.YoutubeDirectLink import YoutubeDirectLink

class CommandManager:

    def __init__(self):
        self.commands = []
        self.add_command(Help(self))
        self.add_command(Archive())
        self.add_command(InviteUser())
        self.add_command(CoinRate())
        self.add_command(Shrink())
        self.add_command(ColorPick())
        self.add_command(YoutubeDirectLink())
    
    def add_command(self, command):
        self.commands.append(command)
    
    def get_command(self, name):
        for command in self.commands:
            if command.name == name:
                return command
        return None
    
    def get_commands(self):
        return self.commands
    
    async def handle_message(self, message):
        for command in self.commands:
            await command.on_message(message)
        if message.content.startswith('!'):
            args = message.content.split(' ')
            command = args[0][1:]
            args = args[1:]
            for command_obj in self.commands:
                if command_obj.name == command or command_obj.aliases.__contains__(command):
                    await command_obj.on_command(message, args)
                    break
