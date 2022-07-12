import discord
from discord.ext import commands
import json

with open('ayarlar.json') as f:
      ayarlar = json.load(f)
intents = discord.Intents(messages=True, guilds=True, reactions = True, members=True, presences=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
      print(f'{bot.user.name} botu aktif oldu.')
      activity = discord.Game(name="Yaşa Gazi Léon Paşaa", type=2)
      await bot.change_presence(status=discord.Status.dnd, activity=activity)

      modules = ['yardım']
      try:
            for module in modules:
                  bot.load_extension('cogs.' + module)
            print(f'yüklendi: {module}.')
      except Exception as e:
            print(f'Hata Yükleniyor {module}: {e}')

            print('Bot aktif oldu')


@bot.event
async def on_member_join(member):
      channel = discord.utils.get(member.guild.text_channels, name='welcome') #ODA ADI
      await channel.send(f'{member} Hoşgeldin')
      print(f"{member} Hoşgeldin.")
      
@bot.event 
async def on_member_remove(member):
      channel = discord.utils.get(member.guild.text_channels, name='welcome') #ODA ADI
      await channel.send(f'{member} Ayrıldı.')
      print(f"{member} Aramızdan ayrıldı")

@bot.command()
async def Hello(ctx):
      embed=discord.Embed(title="Test",  
      description="Hello my creator!", 
      color=discord.Color.red())
      await ctx.send(embed=embed)
bot.run(ayarlar["token"])
