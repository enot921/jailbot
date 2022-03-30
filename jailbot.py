import json
import asyncio
from datetime import datetime, timedelta
import a2s


import discord
from discord.ext import commands

from Cybernator import Paginator as pag

client = commands.Bot( command_prefix = ".." )

class server_info1():
    def __init__(self, config):
        self.config = config
        self.ip_address = config.get('server_ip')
        self.server_port = config.get('server_port')
        self.connect_link = 'steam://connect/' + str(self.ip_address) + ':' + str(self.server_port) + '/'
        print('Loaded server config: ' + self.ip_address + ':' + str(self.server_port))

    def get(self):     

        try:
            server_info = a2s.info((self.ip_address, self.server_port ))
            self.player_list = a2s.players((self.ip_address, self.server_port))
            self.server_name = server_info.server_name
            self.curr_map = server_info.map_name.split('/')[-1]
            self.players = str(server_info.player_count) + '/' + str(server_info.max_players)
            self.ping = str(int((server_info.ping* 1000))) + 'ms'

        except:
            print('Server down :(')
            self.server_name = 'Server down :('
            self.curr_map = 'Unknown'
            self.players = '0'
            self.playerstats = 'Unknown'
            self.ping = '999ms'

class mm_player():
    def __init__(self, author):
        self.author = author
        self.init_time = datetime.now()
        self.time_diff = timedelta(seconds=0)


# Refresh server info every n seconds     
async def refresh_server_info():
    while(True):
        server_info.get()
        status = server_info.curr_map + ' | ' + server_info.players
        await asyncio.sleep(config.get('refresh_time'))

# check for inactive matchmaking search status every n minutes, after this, remove player from list
async def check_mm_state():
    while(True):
        for player in mm_player_list:
            player.time_diff = datetime.now() - player.init_time
            if int((player.time_diff.total_seconds() / 60) % 60) > config.get('mm_status_reset_minutes', 30):
                mm_player_list.remove(player)
        await asyncio.sleep(60)


def player_exists(iterable):
    for element in iterable:
        if element:
            return True
    return False

# Load the config file
with open("config1.json") as json_file1:
    config = json.load(json_file1)

with open("strogiy.json") as json_file:
    config1 = json.load(json_file)

with open("peredovoy.json") as json_file:
    config2 = json.load(json_file)

with open("buntovskoy.json") as json_file:
    config3 = json.load(json_file)

with open("izolyator.json") as json_file:
    config4 = json.load(json_file)

with open("blatnaya.json") as json_file:
    config5 = json.load(json_file)

with open("centrovoy.json") as json_file1:
    config6 = json.load(json_file1)

with open("predatel1.json") as json_file1:
    ttth = json.load(json_file1)

with open("hitman.json") as json_file1:
    hitman1 = json.load(json_file1)

with open("iz_kosmosa.json") as json_file1:
    kosmos = json.load(json_file1)

with open("killer_lessons.json") as json_file1:
    killer = json.load(json_file1)

with open("mirage1.json") as json_file1:
    mi1 = json.load(json_file1)

with open("dust2.json") as json_file1:
    du2 = json.load(json_file1)

with open("dust3.json") as json_file1:
    du3 = json.load(json_file1)

with open("dust4.json") as json_file1:
    du4 = json.load(json_file1)

with open("dust5.json") as json_file1:
    du5 = json.load(json_file1)

with open("dust6.json") as json_file1:
    du6 = json.load(json_file1)

with open("mirage2.json") as json_file1:
    mi2 = json.load(json_file1)

with open("mirage3.json") as json_file1:
    mi3 = json.load(json_file1)

with open("mirage4.json") as json_file1:
    mi4 = json.load(json_file1)

with open("mirage5.json") as json_file1:
    mi5 = json.load(json_file1)

with open("mirage6.json") as json_file1:
    mi6 = json.load(json_file1)

with open("mirage7.json") as json_file1:
    mi7 = json.load(json_file1)

with open("mirage8.json") as json_file1:
    mi8 = json.load(json_file1)

with open("awp.json") as json_file1:
    aw = json.load(json_file1)

with open("awp.json") as json_file1:
    aw = json.load(json_file1)

with open("awp1.json") as json_file1:
    aw1 = json.load(json_file1)

with open("awp2.json") as json_file1:
    aw2 = json.load(json_file1)

with open("awp3.json") as json_file1:
    aw3 = json.load(json_file1)

with open("awp4.json") as json_file1:
    aw4 = json.load(json_file1)

with open("awp5.json") as json_file1:
    aw5 = json.load(json_file1)

with open("awp6.json") as json_file1:
    aw6 = json.load(json_file1)

with open("awp7.json") as json_file1:
    aw7 = json.load(json_file1)

server_info = server_info1(config)
si = server_info1(config1)
sip = server_info1(config2)
sipb = server_info1(config3)
sipbz = server_info1(config4)
sipbzb = server_info1(config5)
sipbzbc = server_info1(config6)
ttt1 = server_info1(ttth)
ht = server_info1(hitman1)
kms = server_info1(kosmos)
kl = server_info1(killer)
m = server_info1(mi1)
d = server_info1(du2)
d2 = server_info1(du3)
d3 = server_info1(du4)
d4 = server_info1(du5)
d5 = server_info1(du6)
m1 = server_info1(mi2)
m2 = server_info1(mi3)
m3 = server_info1(mi4)
m4 = server_info1(mi5)
m5 = server_info1(mi6)
m6 = server_info1(mi7)
m7 = server_info1(mi8)
a = server_info1(aw)
a1 = server_info1(aw1)
a2 = server_info1(aw2)
a3 = server_info1(aw3)
a4 = server_info1(aw4)
a5 = server_info1(aw5)
a6 = server_info1(aw6)
a7 = server_info1(aw7)

mm_player_list = []


@client.event
async def on_ready():
    client.loop.create_task(refresh_server_info())
    client.loop.create_task(check_mm_state())
    print('Bot logged in as {0.user}'.format(client))

# !server - show server info embed
@client.command(aliases = ['j', 'tyurma', 'jails'])
async def jail(ctx):  
    server_info.get()
    si.get()
    sip.get()
    sipb.get()
    sipbz.get()
    sipbzb.get()
    sipbzbc.get()
    status = server_info.curr_map + ' | ' + server_info.players  
    emb = discord.Embed(title='Jail', color=0x37393d ) 
    emb1 = discord.Embed(title='Jail', color=0x37393d )
    if(len(config.get('custom_thumb')) > 0):
        emb.set_thumbnail(url=config.get('custom_thumb'))
    map_banner = config['map_banner'].get(server_info.curr_map, None)
    if(map_banner):
        if(len(map_banner) > 0):
            emb.set_image(url=map_banner)
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field(name='**Name**', value=server_info.server_name, inline=True)
    emb.add_field(name='Map', value=server_info.curr_map, inline=True)
    emb.add_field(name='Players', value=server_info.players, inline=True)
    emb.add_field(name='\u200b', value=server_info.connect_link, inline=False)
    emb.add_field(name='**Name**', value=si.server_name, inline=True)
    emb.add_field(name='Map', value=si.curr_map, inline=True)
    emb.add_field(name='Players', value=si.players, inline=True)
    emb.add_field(name='\u200b', value=si.connect_link, inline=False)
    emb.add_field(name='**Name**', value=sip.server_name, inline=True)
    emb.add_field(name='Map', value=sip.curr_map, inline=True)
    emb.add_field(name='Players', value=sip.players, inline=True)
    emb.add_field(name='\u200b', value=sip.connect_link, inline=False)
    emb.add_field(name='**Name**', value=sipb.server_name, inline=True)
    emb.add_field(name='Map', value=sipb.curr_map, inline=True)
    emb.add_field(name='Players', value=sipb.players, inline=True)
    emb.add_field(name='\u200b', value=sipb.connect_link, inline=False)
    emb.add_field(name='**Name**', value=sipbz.server_name, inline=True)
    emb.add_field(name='Map', value=sipbz.curr_map, inline=True)
    emb.add_field(name='Players', value=sipbz.players, inline=True)
    emb.add_field(name='\u200b', value=sipbzb.connect_link, inline=False)
    emb.add_field(name='**Name**', value=sipbzb.server_name, inline=True)
    emb.add_field(name='Map', value=sipbzb.curr_map, inline=True)
    emb.add_field(name='Players', value=sipbzb.players, inline=True)
    emb.add_field(name='\u200b', value=sipbzb.connect_link, inline=False)
    emb1.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb1.add_field(name='**Name**', value=sipbzbc.server_name, inline=True)
    emb1.add_field(name='Map', value=sipbzbc.curr_map, inline=True)
    emb1.add_field(name='Players', value=sipbzbc.players, inline=True)
    emb1.add_field(name='\u200b', value=sipbzb.connect_link, inline=False)
    embeds = [emb, emb1]

    message = await ctx.send(embed = emb1)
    page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds, timeout = 30 )




    await page.start()


@client.command(aliases = ['t', 'traitor', 'hitman', 'h', 'killer'])
async def ttt(ctx):  
    ttt1.get()
    ht.get()
    kms.get()
    kl.get()
    status = server_info.curr_map + ' | ' + server_info.players  
    emb = discord.Embed(title='TTTH', color=0x37393d) 
    if(len(config.get('custom_thumb')) > 0):
        emb.set_thumbnail(url=config.get('custom_thumb'))
    map_banner = config['map_banner'].get(server_info.curr_map, None)
    if(map_banner):
        if(len(map_banner) > 0):
            emb.set_image(url=map_banner)
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field(name='**Name**', value=ttt1.server_name, inline=True)
    emb.add_field(name='Map', value=ttt1.curr_map, inline=True)
    emb.add_field(name='Players', value=ttt1.players, inline=True)
    emb.add_field(name='\u200b', value=ttt1.connect_link, inline=False)
    emb.add_field(name='**Name**', value=ht.server_name, inline=True)
    emb.add_field(name='Map', value=ht.curr_map, inline=True)
    emb.add_field(name='Players', value=ht.players, inline=True)
    emb.add_field(name='\u200b', value=ht.connect_link, inline=False)
    emb.add_field(name='**Name**', value=kms.server_name, inline=True)
    emb.add_field(name='Map', value=kms.curr_map, inline=True)
    emb.add_field(name='Players', value=kms.players, inline=True)
    emb.add_field(name='\u200b', value=kms.connect_link, inline=False)
    emb.add_field(name='**Name**', value=kl.server_name, inline=True)
    emb.add_field(name='Map', value=kl.curr_map, inline=True)
    emb.add_field(name='Players', value=kl.players, inline=True)
    emb.add_field(name='\u200b', value=kl.connect_link, inline=False)


    await ctx.send(embed = emb)

@client.command( aliases = ['p', 'dust', 'dust2', 'mirage'] )
async def public(ctx):  
    m.get()
    d.get()
    d2.get()
    d3.get()
    d4.get()
    d5.get()
    m1.get()
    m2.get()
    m3.get()
    m4.get()
    m5.get()
    m6.get()
    m7.get()
    status = server_info.curr_map + ' | ' + server_info.players  
    emb = discord.Embed(title='DUST2', color=0x37393d) 
    emb1 = discord.Embed(title='MIRAGE', color=0x37393d)
    emb2 = discord.Embed(title='MIRAGE', color=0x37393d) 
    if(len(config.get('custom_thumb')) > 0):
        emb.set_thumbnail(url=config.get('custom_thumb'))
    map_banner = config['map_banner'].get(server_info.curr_map, None)
    if(map_banner):
        if(len(map_banner) > 0):
            emb.set_image(url=map_banner)
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field(name='**Name**', value=m.server_name, inline=True)
    emb.add_field(name='Map', value=m.curr_map, inline=True)
    emb.add_field(name='Players', value=m.players, inline=True)
    emb.add_field(name='\u200b', value=m.connect_link, inline=False)
    emb.add_field(name='**Name**', value=d.server_name, inline=True)
    emb.add_field(name='Map', value=d.curr_map, inline=True)
    emb.add_field(name='Players', value=d.players, inline=True)
    emb.add_field(name='\u200b', value=d.connect_link, inline=False)
    emb.add_field(name='**Name**', value=d2.server_name, inline=True)
    emb.add_field(name='Map', value=d2.curr_map, inline=True)
    emb.add_field(name='Players', value=d2.players, inline=True)
    emb.add_field(name='\u200b', value=d2.connect_link, inline=False)
    emb.add_field(name='**Name**', value=d3.server_name, inline=True)
    emb.add_field(name='Map', value=d3.curr_map, inline=True)
    emb.add_field(name='Players', value=d3.players, inline=True)
    emb.add_field(name='\u200b', value=d3.connect_link, inline=False)
    emb.add_field(name='**Name**', value=d4.server_name, inline=True)
    emb.add_field(name='Map', value=d4.curr_map, inline=True)
    emb.add_field(name='Players', value=d4.players, inline=True)
    emb.add_field(name='\u200b', value=d4.connect_link, inline=False)
    emb.add_field(name='**Name**', value=d5.server_name, inline=True)
    emb.add_field(name='Map', value=d5.curr_map, inline=True)
    emb.add_field(name='Players', value=d5.players, inline=True)
    emb.add_field(name='\u200b', value=d5.connect_link, inline=False)
    emb1.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb1.add_field(name='**Name**', value=m1.server_name, inline=True)
    emb1.add_field(name='Map', value=m1.curr_map, inline=True)
    emb1.add_field(name='Players', value=m1.players, inline=True)
    emb1.add_field(name='\u200b', value=m1.connect_link, inline=False)
    emb1.add_field(name='**Name**', value=m2.server_name, inline=True)
    emb1.add_field(name='Map', value=m2.curr_map, inline=True)
    emb1.add_field(name='Players', value=m2.players, inline=True)
    emb1.add_field(name='\u200b', value=m2.connect_link, inline=False)
    emb1.add_field(name='**Name**', value=m3.server_name, inline=True)
    emb1.add_field(name='Map', value=m3.curr_map, inline=True)
    emb1.add_field(name='Players', value=m3.players, inline=True)
    emb1.add_field(name='\u200b', value=m3.connect_link, inline=False)
    emb1.add_field(name='**Name**', value=m4.server_name, inline=True)
    emb1.add_field(name='Map', value=m4.curr_map, inline=True)
    emb1.add_field(name='Players', value=m4.players, inline=True)
    emb1.add_field(name='\u200b', value=m4.connect_link, inline=False)
    emb1.add_field(name='**Name**', value=m5.server_name, inline=True)
    emb1.add_field(name='Map', value=m5.curr_map, inline=True)
    emb1.add_field(name='Players', value=m5.players, inline=True)
    emb1.add_field(name='\u200b', value=m5.connect_link, inline=False)
    emb1.add_field(name='**Name**', value=m6.server_name, inline=True)
    emb1.add_field(name='Map', value=m6.curr_map, inline=True)
    emb1.add_field(name='Players', value=m6.players, inline=True)
    emb1.add_field(name='\u200b', value=m6.connect_link, inline=False)
    emb2.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb2.add_field(name='**Name**', value=m7.server_name, inline=True)
    emb2.add_field(name='Map', value=m7.curr_map, inline=True)
    emb2.add_field(name='Players', value=m7.players, inline=True)
    emb2.add_field(name='\u200b', value=m7.connect_link, inline=False)
    embeds = [emb, emb1, emb2]

    message = await ctx.send(embed = emb1)
    page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds, timeout = 30 )




    await page.start()

@client.command(aliases = ['a', 'sniper'])
async def awp(ctx):  
    a.get()
    a1.get()
    a2.get()
    a3.get()
    a4.get()
    a5.get()
    a6.get()
    a7.get()
    status = server_info.curr_map + ' | ' + server_info.players  
    emb = discord.Embed(title='AWP', color=0x37393d) 
    emb1 = discord.Embed(title='AWP', color=0x37393d) 
    if(len(config.get('custom_thumb')) > 0):
        emb.set_thumbnail(url=config.get('custom_thumb'))
    map_banner = config['map_banner'].get(server_info.curr_map, None)
    if(map_banner):
        if(len(map_banner) > 0):
            emb.set_image(url=map_banner)
    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field(name='**Name**', value=a.server_name, inline=True)
    emb.add_field(name='Map', value=a.curr_map, inline=True)
    emb.add_field(name='Players', value=a.players, inline=True)
    emb.add_field(name='\u200b', value=a.connect_link, inline=False)
    emb.add_field(name='**Name**', value=a1.server_name, inline=True)
    emb.add_field(name='Map', value=a1.curr_map, inline=True)
    emb.add_field(name='Players', value=a1.players, inline=True)
    emb.add_field(name='\u200b', value=a1.connect_link, inline=False)
    emb.add_field(name='**Name**', value=a2.server_name, inline=True)
    emb.add_field(name='Map', value=a2.curr_map, inline=True)
    emb.add_field(name='Players', value=a2.players, inline=True)
    emb.add_field(name='\u200b', value=a2.connect_link, inline=False)
    emb.add_field(name='**Name**', value=a3.server_name, inline=True)
    emb.add_field(name='Map', value=a3.curr_map, inline=True)
    emb.add_field(name='Players', value=a3.players, inline=True)
    emb.add_field(name='\u200b', value=a3.connect_link, inline=False)
    emb.add_field(name='**Name**', value=a4.server_name, inline=True)
    emb.add_field(name='Map', value=a4.curr_map, inline=True)
    emb.add_field(name='Players', value=a4.players, inline=True)
    emb.add_field(name='\u200b', value=a4.connect_link, inline=False)
    emb.add_field(name='**Name**', value=a6.server_name, inline=True)
    emb.add_field(name='Map', value=a6.curr_map, inline=True)
    emb.add_field(name='Players', value=a6.players, inline=True)
    emb.add_field(name='\u200b', value=a6.connect_link, inline=False)
    emb1.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url)
    emb1.add_field(name='**Name**', value=a7.server_name, inline=True)
    emb1.add_field(name='Map', value=a7.curr_map, inline=True)
    emb1.add_field(name='Players', value=a7.players, inline=True)
    emb1.add_field(name='\u200b', value=a7.connect_link, inline=False)

    embeds = [emb, emb1]

    message = await ctx.send(embed = emb1)
    page = pag(client, message, only=ctx.author, use_more=False, embeds=embeds, timeout = 30 )




    await page.start()

@client.command( aliases = ['cs', 'status'] )
@commands.is_owner()
async def changestatus( ctx, statustype:str = None, *, arg:str = None):
    if statustype is None: # Type Check
        await ctx.send( 'Please select status' )
    elif arg is None: # Arg Check
        await ctx.send( 'Write argument please' )
    else:
        if statustype.lower() == 'game': # Game
            await client.change_presence (activity=discord.Game( name = arg) )
        elif statustype.lower() == 'listen': # Listen
            await client.change_presence( activity=discord.Activity( type=discord.ActivityType.listening, name = arg) )
        elif statustype.lower() == 'watch': # Watch
            await client.change_presence( activity=discord.Activity( type=discord.ActivityType.watching, name = arg) )

@client.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def say(ctx, *, text):
	await ctx.channel.purge( limit = 1 )
	t = (text)
	emb = discord.Embed(description = f'{t}', colour = discord.Colour(0x37393d))
	await ctx.send(embed = emb)




token = open( 'token.txt', 'r' ).readline()

client.run(token)
