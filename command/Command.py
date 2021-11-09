class Command:
    def __init__(self, name, func, desc, usage, aliases):
        self.name = name
        self.func = func
        self.desc = desc
        self.usage = usage
        self.aliases = aliases
    
    async def on_command(self, message, args):
        await self.func(message, args)
    
    async def on_message(self, message):
        pass