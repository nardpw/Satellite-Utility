from command.Command import Command
from utils.Logger import Logger
import discord
import requests
import json

class CoinRate(Command):
    def __init__(self):
        super().__init__('coinrate', self.coinrate, 'Displays the current coin rate', 'coinrate', ['coinrate', 'cr'])
    
    async def coinrate(self, message, args):
        try:
            Logger.log('Coinrate ' + str(message.author))
            response = requests.get('https://api.coingecko.com/api/v3/coins/')
            if response.status_code != 200:
                await message.channel.send('Error: ' + str(response.status_code))
                return
            coins = json.loads(response.text)
            embed = discord.Embed(title='Coin Rate', description='', color=0x00ff00)
            embed.add_field(name='Coin', value='\n'.join(['`{}` - {}'.format(c['symbol'], c['name']) for c in coins]), inline=False)
            embed.add_field(name='Price', value='\n'.join(['`{}` - {}'.format(c['symbol'], c['market_data']['current_price']['usd']) for c in coins]), inline=False)
            embed.set_footer(text='Made by @nardpw#5794')
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send('Error: ' + str(e))
            Logger.error(e)