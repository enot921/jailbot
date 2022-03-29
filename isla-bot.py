#Импорт
from sqlite3.dbapi2 import connect
import discord
import a2s
import random
import json
import requests
import io
import asyncio
import nekos
import sqlite3
from datetime import datetime, timedelta
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands
from discord.ext.commands import errors
from discord import errors as dpy_errors


client = commands.Bot( command_prefix = ".." )
client.remove_command( 'help' )

connection = sqlite3.connect('server.db')
cursor = connection.cursor()


#words
hello_words = [ 'Айла привет', 'айла привет', 'Исла привет', 'исла привет', 'Айла Привет', 'айла Привет', 'Исла Привет', 'исла Привет']
word = [ 'Енот лох?', 'енот лох?', 'Енот лох ?', 'енот лох ?', 'Енот гей?', 'енот гей?', 'Енот гей ?', 'енот гей ?']
Isla = ['айла, кто твой создатель?', 'Айла, кто твой создатель?', 'айла, кто твой создатель ?', 'Айла, кто твой создатель ?', 'Айла, кто тебя создал?', 'айла, кто тебя создал?', 'Айла, кто тебя создал ?', 'айла, кто тебя создал ?']
Night = [ 'Айла, спокойной ночи', 'айла, спокойной ночи', 'Айла спокойной ночи', 'айла спокойной ночи', 'Айла споки ночи', 'Айла, споки ночи', 'айла споки ночи', 'айла, споки ночи' ]
GoodNight = [ 'спокойной ночи, пуська:heart:', 'спокойно ночи, бака:heart:', 'сладких снов:heart:', 'Сладких снов, всё будет хорошо:heart: ' ]
ent = ['Кто половой партнер Енота?', 'кто половой партнер енота?']
mozg = ['Вы заебете с такими вопросами', 'Не ебите мне мозг', 'Тебе  больше спросить нечего?']
prefixx = ['Айла префикс', 'айла префикс']
prefix = '..'
admins = ['айла команды для админов', 'айла, команды для админов', 'айла, команды для администраторов', 'айла команды для администраторов']
info = ['айла информация о сервере', 'айла, помоги разобраться', 'айла помоги']
bad_words = ['даун', 'еблан', 'сука', 'гандон', 'пошел нахуй', 'ебал', 'соси', 'пиздюк', 'ниггер', 'нигер', 'отсталый', 'блять', 'Пошел нахуй', 'мать ебал', 'долбаеб', 'отсоси', 'уебан', 'пидор', 'пидорас', 'сука а', 'сын шлюхи', 'сын собаки', 'шмара', 'блять', 'блядь', 'бля', 'пошла нахуй', 'Пошла нахуй', 'Бля']
random_phrase = ['Зайка, как у тебя дела?', 'ты бака', 'только не внутрь, братик', 'Братик, извращенец!']
random_citate = ['Наша работа разрушать воспоминания, в этом нет ничего весёлого.', 'Добрая рука, как лучик света', 'Если можешь что-то одно — доведи это до совершенства.', 'Надеюсь, однажды, ты сможешь быть с тем, кого любишь...', 'Я надеюсь, что ты когда-нибудь воссоединишься с человеком, которым дорожишь.', 'Радостные и счастливые воспоминания не всегда приносят облегчения. Чем приятнее воспоминание, тем тяжелее на душе. Оно может стать в тягость... и для того, кто уходит... И для того, кто остаётся.', 'Ничто не делает человека счастливее, чем время, проведённое с тем, кого любишь.']
isla_citate = ['Айла цитаты', 'айла цитаты', 'айла, цитаты', 'Айла, цитаты']
ki = ['Нежно поцеловал', 'Сочно засосал', 'Поцеловал', 'Поцеловал в засос', 'Стесняясь поцеловал']
k = random.choice(ki)
hu = ['Обнял', 'Крепко обнял', 'Стесняясь обнимает ', 'Чуть не задушил в объятиях']
h = random.choice(hu)
wi = ['Заигрывающее подмигивает', 'Подмигнул']
w = random.choice(wi)
pa = ['Гладит по головке', 'Ударил по головке', 'Решил погладить по головке']
p = random.choice(pa)
li = ['Облизывает', 'Облизал']
l = random.choice(li)
sl = ['Дал пощечину', 'Ударил', 'Замахнулся и дал лещ']
s = random.choice(sl)
ne = ['Погладил по головке кошкодевочку', 'Нашел у своей двери кошкодевочку', 'Купил кошкодевочку', 'Поцеловал кошкодевочку']
n = random.choice(ne)
ran = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50']
ra = random.choice(ran)
bi = ['Нежно укусил', 'Акуратно откусил головку', 'Сделал кусь', 'Злобно укусил', 'Укусил за ручку']
b = random.choice(bi)
on = ['..filter on']
ba = ['Назвал бакой']
bak = random.choice(ba)
lublu = ['айла я тебя люблю', 'Айла я тебя люблю', 'Айла я тебя лав', 'айла я тебя лав']
otvetlublu = ['Зая, я тебя тоже:heart:', 'Я тоже хотела тебе давно сказать.... вообщем.... \nС нашей первой встречи я думала только об одном.... \nВообщем.... Я тебя тоже люблю...', 'Оууууууу, это так мило) Правда, извини, у меня есть другой..... Надеюсь мы останемся друзьями...', 'Они чан, я знаю что это не правильно, то что ты мой брат, и вообщем... Ты мне нравишься.' ]
aylapomogi = ['айла', 'Айла', 'исла', 'Исла', 'isla', 'Isla']
Pomogau = ['Привет зайка, \nЕсли ты хочешь обратится ко мне, посмотри список ниже. \nАйла привет, Айла, спокойной ночи или Айла споки ночи, Айла префикс, Айла цитаты, Айла я тебя люблю, Айла пока, Айла доброе утро']
Pokaayla = ['айла, пока', 'Айла, пока', 'айла пока', 'Айла пока']
pokaurodebaniy = ['Пока зайка:heart:', 'Ты меня бросаешь, ну ты и бака(', 'Я обиделась (', 'Жду не дождусь твоего возвращения', 'Прощай...']
dobroeutro = ['Айла доброе утро', 'айла доброе утро', 'айла, доброе утро', 'Айла, доброе утро']
dobroeutroisla = ['Доброе утро писечка:heart:', 'Доброе утро', 'Утречко :3', 'Утречко милый', 'Доброго утречка хлопiц',]



@client.event
@commands.cooldown(1, 5, commands.BucketType.member)

async def on_message( message ):


	
	
	msg = message.content.lower()

	if msg in hello_words:
		await message.channel.send('Привет пуська, чтобы узнать подробнее о командах, напиши ..help')

	if msg in word:
		await message.channel.send('Однозначно да')

	if msg in Isla:
		await message.channel.send('Меня создал <@404915501727219723>')


	if msg in Night:
		await message.channel.send( random.choice(GoodNight))

	if msg in ent:
		await message.channel.send( random.choice(mozg))
	if msg in prefixx:
		await message.channel.send('Мой префикс ..')

	if msg in admins:
		await message.channel.send( 'Чтобы посмотреть команды для админов пропишите ..ahelp' )

	if msg in info:
		await message.channel.send('Привет заюш, ты потерялся? Напиши ..serverhelp')


	if msg in bad_words:
		await message.delete()

	if msg in isla_citate:
		await message.channel.send( random.choice(random_citate))

	if msg in lublu:
		await message.channel.send( random.choice(otvetlublu) )

	if msg in aylapomogi:
		await message.channel.send( random.choice( Pomogau ) )

	if msg in Pokaayla:
		await message.channel.send( random.choice( pokaurodebaniy ) )

	if msg in dobroeutro:
		await message.channel.send( random.choice( dobroeutroisla ) )


	await client.process_commands( message )


@client.event
async def on_command_error(ctx, err):
    if isinstance(err, errors.CommandNotFound):
        await ctx.send(embed=discord.Embed( description=f"Данной команды не существует." ))

    elif isinstance(err, errors.BotMissingPermissions):
        await ctx.send(
            embed=discord.Embed( description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для нормальной работы бота") )

    elif isinstance(err, errors.MissingPermissions):
        await ctx.send(embed=discord.Embed( description=f"У вас недостаточно прав для запуска данной команды." ))

    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.message.add_reaction("🕐")

    elif isinstance(err, dpy_errors.Forbidden):
        await ctx.send(embed=discord.Embed(description=f"У бота не достаточно прав на запуск данной команды."))


#clear
@client.command( pass_context = True )
@commands.has_permissions( manage_messages = True )
@commands.cooldown(1, 5, commands.BucketType.member)
async def clear ( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )
 
#kick
@client.command( pass_context = True)
@commands.has_permissions( kick_members = True ) 
@commands.cooldown(1, 5, commands.BucketType.member)
async def kick( ctx, member: discord.Member, *, reason = None):
	author = ctx.message.author
	await ctx.channel.purge( limit = 1 )
	await member.kick( reason = reason )
	await ctx.send(f'{ member } Был кикнут с сервера!')

#ban
@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )
@commands.cooldown(1, 5, commands.BucketType.member)


async def ban( ctx, member: discord.Member, *, reason = None):
	emb = discord.Embed( Color = discord.Color(0xc2487b) )
	await ctx.channel.purge( limit = 1 )

	await member.ban(reason = reason)
	author = ctx.message.author
	emb.set_author( name = member.name, icon_url = member.avatar_url)
	emb.add_field( name = 'Участник успешно забанен', value = 'Чтобы разбанить напишите ..unban')
	emb.set_footer( text = 'Был забанен {}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url)


	await ctx.send( embed = emb )


#unban
@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )
@commands.cooldown(1, 5, commands.BucketType.member)
async def unban ( ctx, *, member ):
	await ctx.channel.purge( limit = 1 ) 

	banned_users = await ctx.guild.bans() #Список забаненных юзеров

	for ban_entry in banned_users: #достаем юзера из списка
		user = ban_entry.user #Находим его

		await ctx.guild.unban( user ) #Разбаниваем
		await ctx.send( f'{ user.mention} Успешно разбанен!' ) #Сообщение

		return

#command help for typical player
@client.command( pass_context = True, aliases = ['h'] )
@commands.cooldown(1, 5, commands.BucketType.member)

async def help( ctx ):
	await ctx.channel.purge( limit = 1 ) 

	embe = discord.Embed( title = 'Modules', description = '``reactions - реакции \nmoderation - модерирование \nvarious - разное``', colour = discord.Colour(0x4910c4) )

	embe.add_field( name = '\nПолезные ссылочки', value = '[``Пригласить на сервер``](https://discord.com/oauth2/authorize?client_id=712676102262227034&scope=bot&permissions=8)     |             [``Тех. Поддержка``](https://discord.gg/usMuEzT)     |             [``Вк разработчика``](https://vk.com/nebegayteslavyane)')
	embe.set_footer( text = '..[Модуль]' )

	await ctx.send(embed = embe)

@client.command( aliases = ['react', 'Reactions', 'React'] )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def reactions( ctx ):

	embe = discord.Embed( title = 'Reactions', description = '``kiss \nhug \nwink \npat \nlick \nslap \ncry \nhappy \nneko \nbite \nbaka``', colour = discord.Colour(0x4910c4) )

	embe.add_field( name = '\nПолезные ссылочки', value = '[``Пригласить на сервер``](https://discord.com/oauth2/authorize?client_id=712676102262227034&scope=bot&permissions=8)     |             [``Тех. Поддержка``](https://discord.gg/usMuEzT)     |             [``Вк разработчика``](https://vk.com/nebegayteslavyane)')

	await ctx.send( embed = embe )

@client.command( aliases = ['var', 'Various', 'Var'] )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def various( ctx ):

	embe = discord.Embed( title = 'Various', description = '``8ball \nuserinfo \navatar \nanimeavatar \nhentai \nsendimage \ncontact``', colour = discord.Colour(0x4910c4) )

	embe.add_field( name = '\nПолезные ссылочки', value = '[``Пригласить на сервер``](https://discord.com/oauth2/authorize?client_id=712676102262227034&scope=bot&permissions=8)     |             [``Тех. Поддержка``](https://discord.gg/usMuEzT)     |             [``Вк разработчика``](https://vk.com/nebegayteslavyane)')

	await ctx.send( embed = embe )

@client.command( aliases = ['moder', 'Moderation', 'Moder'] )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def moderation( ctx ):

	embe = discord.Embed( title = 'Moderation', description = '``ban \nunban \nkick \nclear \nsay``', colour = discord.Colour(0x4910c4) )

	embe.add_field( name = '\nПолезные ссылочки', value = '[``Пригласить на сервер``](https://discord.com/oauth2/authorize?client_id=712676102262227034&scope=bot&permissions=8)     |             [``Тех. Поддержка``](https://discord.gg/usMuEzT     |             [``Вк разработчика``](https://vk.com/nebegayteslavyane)')

	await ctx.send( embed = embe )



#

#Эмоции

@client.command( pass_context = True )
@commands.cooldown(1, 5, commands.BucketType.member)

async def pat( ctx, member: discord.Member, *, reason = None):
    response = requests.get('https://some-random-api.ml/animu/pat')
    json_data = json.loads(response.text)
    emb = discord.Embed( description = (f'{p} {member.mention}'), colour = discord.Colour(0x8e3dcc) ) 

    emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
    emb.set_image(url = json_data['link'])

    await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.cooldown(1, 5, commands.BucketType.member)

async def hug( ctx, member: discord.Member):
	response = requests.get('https://some-random-api.ml/animu/hug')
	json_data = json.loads(response.text)
	emb = discord.Embed( description = (f'{h} { member.mention } '), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image(url = json_data['link'])

	await ctx.send(embed = emb)

@client.command ( pass_context = True )
@commands.cooldown(1, 5, commands.BucketType.member)

async def wink( ctx, member: discord.Member ):
	response = requests.get('https://some-random-api.ml/animu/wink')
	json_data = json.loads(response.text)
	emb = discord.Embed( description = (f'{w} { member.mention }'), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image(url = json_data['link'])

	await ctx.send( embed = emb )


@client.command( pass_context = True )
@commands.cooldown(1, 5, commands.BucketType.member)

async def kiss( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( description = ( f'{k} { member.mention }'), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image( url = nekos.img('kiss')) 

	await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.cooldown(1, 5, commands.BucketType.member)

async def lick( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( description = ( f'{l} { member.mention }' ), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url, )
	emb.set_image( url = random.choice(['https://gifs.gachi.ru/lick/20.gif', 'https://gifs.gachi.ru/lick/21.gif', 'https://gifs.gachi.ru/lick/22.gif', 'https://gifs.gachi.ru/lick/23.gif', 'https://gifs.gachi.ru/lick/24.gif', 'https://gifs.gachi.ru/lick/25.gif', 'https://gifs.gachi.ru/lick/26.gif', 'https://gifs.gachi.ru/lick/27.gif', 'https://gifs.gachi.ru/lick/28.gif', 'https://gifs.gachi.ru/lick/29.gif', 'https://gifs.gachi.ru/lick/30.gif', 'https://gifs.gachi.ru/lick/31.gif', 'https://gifs.gachi.ru/lick/32.gif', 'https://gifs.gachi.ru/lick/33.gif', 'https://gifs.gachi.ru/lick/34.gif', 'https://gifs.gachi.ru/lick/35.gif', 'https://gifs.gachi.ru/lick/36.gif', 'https://gifs.gachi.ru/lick/37.gif', 'https://gifs.gachi.ru/lick/38.gif', 'https://gifs.gachi.ru/lick/39.gif', 'https://gifs.gachi.ru/lick/40.gif']) )

	await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def slap( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( description = (f'{s} { member.mention }'), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url, )
	emb.set_image( url = nekos.img('slap'))

	await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def cry( ctx ):
	emb = discord.Embed( description = ('Не смог скрыть горе, и заплакал'), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = random.choice(['https://gifs.gachi.ru/cry/1.gif', 'https://gifs.gachi.ru/cry/2.gif', 'https://gifs.gachi.ru/cry/3.gif', 'https://gifs.gachi.ru/cry/4.gif', 'https://gifs.gachi.ru/cry/5.gif', 'https://gifs.gachi.ru/cry/6.gif', 'https://gifs.gachi.ru/cry/7.gif', 'https://gifs.gachi.ru/cry/8.gif', 'https://gifs.gachi.ru/cry/9.gif', 'https://gifs.gachi.ru/cry/10.gif', 'https://gifs.gachi.ru/cry/11.gif', 'https://gifs.gachi.ru/cry/12.gif', 'https://gifs.gachi.ru/cry/13.gif', 'https://gifs.gachi.ru/cry/14.gif', 'https://gifs.gachi.ru/cry/15.gif', 'https://gifs.gachi.ru/cry/16.gif', 'https://gifs.gachi.ru/cry/17.gif', 'https://gifs.gachi.ru/cry/18.gif', 'https://gifs.gachi.ru/cry/19.gif', 'https://gifs.gachi.ru/cry/20.gif', 'https://gifs.gachi.ru/cry/21.gif', 'https://gifs.gachi.ru/cry/22.gif', 'https://gifs.gachi.ru/cry/23.gif', 'https://gifs.gachi.ru/cry/25.gif', 'https://gifs.gachi.ru/cry/26.gif', 'https://gifs.gachi.ru/cry/27.gif', 'https://gifs.gachi.ru/cry/28.gif', 'https://gifs.gachi.ru/cry/29.gif', 'https://gifs.gachi.ru/cry/30.gif', 'https://gifs.gachi.ru/cry/24.gif']) )

	await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def happy( ctx ):
	emb = discord.Embed( description = ('Начал прыгать от радости'), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = random.choice(['https://gifs.gachi.ru/happy/1.gif', 'https://gifs.gachi.ru/happy/2.gif', 'https://gifs.gachi.ru/happy/3.gif', 'https://gifs.gachi.ru/happy/4.gif', 'https://gifs.gachi.ru/happy/5.gif', 'https://gifs.gachi.ru/happy/6.gif', 'https://gifs.gachi.ru/happy/7.gif', 'https://gifs.gachi.ru/happy/8.gif', 'https://gifs.gachi.ru/happy/9.gif', 'https://gifs.gachi.ru/happy/10.gif', 'https://gifs.gachi.ru/happy/11.gif', 'https://gifs.gachi.ru/happy/12.gif', 'https://gifs.gachi.ru/happy/13.gif', 'https://gifs.gachi.ru/happy/14.gif', 'https://gifs.gachi.ru/happy/15.gif', 'https://gifs.gachi.ru/happy/16.gif', 'https://gifs.gachi.ru/happy/17.gif', 'https://gifs.gachi.ru/happy/18.gif', 'https://gifs.gachi.ru/happy/19.gif', 'https://gifs.gachi.ru/happy/20.gif', 'https://gifs.gachi.ru/happy/21.gif', 'https://gifs.gachi.ru/happy/22.gif', 'https://gifs.gachi.ru/happy/23.gif', 'https://gifs.gachi.ru/happy/24.gif', 'https://gifs.gachi.ru/happy/25.gif']) )

	await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.cooldown( 1, 5, commands.BucketType.member )
async def neko( ctx ):

	emb = discord.Embed( description = ( f'{ n }' ), colour = discord.Colour(0x8e3dcc) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = random.choice( ['https://gifs.gachi.ru/neko/1.gif', 'https://gifs.gachi.ru/neko/2.gif', 'https://gifs.gachi.ru/neko/3.gif', 'https://gifs.gachi.ru/neko/4.gif', 'https://gifs.gachi.ru/neko/5.gif', 'https://gifs.gachi.ru/neko/6.gif', 'https://gifs.gachi.ru/neko/7.gif', 'https://gifs.gachi.ru/neko/8.gif', 'https://gifs.gachi.ru/neko/9.gif', 'https://gifs.gachi.ru/neko/10.gif', 'https://gifs.gachi.ru/neko/11.gif', 'https://gifs.gachi.ru/neko/12.gif', 'https://gifs.gachi.ru/neko/13.gif', 'https://gifs.gachi.ru/neko/14.gif', 'https://gifs.gachi.ru/neko/15.gif', 'https://gifs.gachi.ru/neko/16.gif', 'https://gifs.gachi.ru/neko/17.gif', 'https://gifs.gachi.ru/neko/18.gif', 'https://gifs.gachi.ru/neko/19.gif' 'https://gifs.gachi.ru/neko/20.gif', 'https://gifs.gachi.ru/neko/21.gif', 'https://gifs.gachi.ru/neko/22.gif', 'https://gifs.gachi.ru/neko/23.gif', 'https://gifs.gachi.ru/neko/24.gif' 'https://gifs.gachi.ru/neko/25.gif'] ) )

	await ctx.send( embed = emb )


@client.command( aliases = ['kusat', 'ukusit', 'Bite'] )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def bite( ctx, member: discord.Member, *, reason = None ):

	emb = discord.Embed( description = ( f'{ b } { member.mention }' ), colour = discord.Colour(0x8e3dcc) )
	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = random.choice(['https://gifs.gachi.ru/bite/20.gif', 'https://gifs.gachi.ru/bite/21.gif', 'https://gifs.gachi.ru/bite/22.gif', 'https://gifs.gachi.ru/bite/23.gif', 'https://gifs.gachi.ru/bite/24.gif', 'https://gifs.gachi.ru/bite/25.gif', 'https://gifs.gachi.ru/bite/26.gif', 'https://gifs.gachi.ru/bite/27.gif', 'https://gifs.gachi.ru/bite/28.gif', 'https://gifs.gachi.ru/bite/29.gif', 'https://gifs.gachi.ru/bite/30.gif', 'https://gifs.gachi.ru/bite/31.gif', 'https://gifs.gachi.ru/bite/32.gif', 'https://gifs.gachi.ru/bite/33.gif', 'https://gifs.gachi.ru/bite/34.gif', 'https://gifs.gachi.ru/bite/35.gif', 'https://gifs.gachi.ru/bite/36.gif', 'https://gifs.gachi.ru/bite/37.gif', 'https://gifs.gachi.ru/bite/38.gif', 'https://gifs.gachi.ru/bite/39.gif', 'https://gifs.gachi.ru/bite/40.gif']) )

	await ctx.send( embed = emb )


@client.command( aliases = ['durak' 'Baka'] )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def baka( ctx, member: discord.Member, *, reason = None ):

	emb = discord.Embed( description = (f'{ bak } { member.mention }'), colour = discord.Colour(0x8e3dcc) )
	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = nekos.img('baka') )

	await ctx.send( embed = emb )

# Mute

#@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '404915501727219723':
        role = discord.utils.get(member.server.roles, name='isla_mute')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

#..serverhelp

@client.command( pass_context = True )

async def serverhelp( ctx ):
	emb = discord.Embed( title = (), color = discord.Color.blue())
	await ctx.channel.purge( limit = 1 )

	emb.add_field( name = 'тута все правила сервера', value = '<#706237749627322490>')
	emb.add_field( name = ('а тут новости сервера')  , value = '<#716878668630327309> ')
	emb.add_field( name = ('здеся ты можешь поиграть в мафию')  , value = '<#707159369875193896> ')
	emb.add_field( name = ('благодарность админам')  , value = '<#720198279199195136> ')
	emb.add_field( name = ('только для тех кому больше 18')  , value = '<#707071129608781907> ')
	emb.add_field( name = ('только тут мы все общаемся')  , value = '<#715222320234496070> ')
	emb.add_field( name = ('обновления сервера')  , value = '<#720205170587336704> ')
	emb.add_field( name = ('Изменить цвет ника')  , value = '<#728321305480528012> ')
	emb.add_field( name = ('ссылочка на приглашение друзей')  , value = 'https://discord.gg/usMuEzT')

	await ctx.send( embed = emb )


#Оповещение в лс (мне) когда бот зашел на новый сервер
@client.event
async def on_guild_join( guild ):


	me = client.get_user(404915501727219723)

	emb = discord.Embed( title = f'Я пришла на новый сервер' )

	for guild in client.guilds:
		category = guild.categories[0]
		try:
			channel = category.text_channels[0]
		except:
			channel = category.voice_channels[0]
		link = await channel.create_invite()
	emb.add_field( name = guild.name, value = f"Участников: {len(guild.members)}\nСсылка: {link}" )

	await me.send( embed = emb )



#не достаточно прав на команду
@clear.error
async def clear_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'Отказано в доступе!')

@ban.error
async def ban_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'Отказано в доступе!')

@kick.error
async def kick_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'Отказано в доступе')

#@mute.error
async def mute_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'Отказано в доступе!')

@unban.error
async def unban_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'Отказано в доступе!')


@kiss.error
async def kiss_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument  ):
		emb = discord.Embed( description = ( f'Поцеловал <@712676102262227034>'), colour = discord.Colour(0x710186) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image( url = nekos.img('kiss'))

	await ctx.send( embed = emb )

@hug.error
async def hug_error( ctx, error):
	if isinstance( error, commands.MissingRequiredArgument ):
		response = requests.get('https://some-random-api.ml/animu/hug')
	
	json_data = json.loads(response.text)
	emb = discord.Embed( description = (f'Обнял  свою любимую дакимакуру, и задумался'), colour = discord.Colour(0x710186) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image(url = json_data['link'])

	await ctx.send(embed = emb)

@pat.error
async def pat_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		emb = discord.Embed( description = ( f'Погладил по головке <@712676102262227034>'), colour = discord.Colour(0x710186) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image( url = random.choice(['https://gifs.gachi.ru/pat/1.gif', 'https://gifs.gachi.ru/pat/2.gif', 'https://gifs.gachi.ru/pat/3.gif', 'https://gifs.gachi.ru/pat/4.gif', 'https://gifs.gachi.ru/pat/5.gif', 'https://gifs.gachi.ru/pat/6.gif', 'https://gifs.gachi.ru/pat/7.gif', 'https://gifs.gachi.ru/pat/8.gif', 'https://gifs.gachi.ru/pat/9.gif', 'https://gifs.gachi.ru/pat/10.gif', 'https://gifs.gachi.ru/pat/11.gif', 'https://gifs.gachi.ru/pat/12.gif', 'https://gifs.gachi.ru/pat/13.gif', 'https://gifs.gachi.ru/pat/14.gif', 'https://gifs.gachi.ru/pat/15.gif', 'https://gifs.gachi.ru/pat/16.gif', 'https://gifs.gachi.ru/pat/17.gif', 'https://gifs.gachi.ru/pat/18.gif', 'https://gifs.gachi.ru/pat/19.gif', 'https://gifs.gachi.ru/pat/20.gif', 'https://gifs.gachi.ru/pat/21.gif']) )

	await ctx.send( embed = emb )

@wink.error
async def wink_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		response = requests.get('https://some-random-api.ml/animu/wink')
		
	json_data = json.loads(response.text)
	emb = discord.Embed( description = (f'Подмигнул <@712676102262227034>'), colour = discord.Colour(0x710186) )

	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url,)
	emb.set_image(url = json_data['link'])

	await ctx.send( embed = emb )

@lick.error
async def lick_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		emb = discord.Embed( description = ( f'{l} <@712676102262227034>' ), colour = discord.Colour(0x710186) )

		emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url, )
		emb.set_image( url = random.choice(['https://gifs.gachi.ru/lick/20.gif', 'https://gifs.gachi.ru/lick/21.gif', 'https://gifs.gachi.ru/lick/22.gif', 'https://gifs.gachi.ru/lick/23.gif', 'https://gifs.gachi.ru/lick/24.gif', 'https://gifs.gachi.ru/lick/25.gif', 'https://gifs.gachi.ru/lick/26.gif', 'https://gifs.gachi.ru/lick/27.gif', 'https://gifs.gachi.ru/lick/28.gif', 'https://gifs.gachi.ru/lick/29.gif', 'https://gifs.gachi.ru/lick/30.gif', 'https://gifs.gachi.ru/lick/31.gif', 'https://gifs.gachi.ru/lick/32.gif', 'https://gifs.gachi.ru/lick/33.gif', 'https://gifs.gachi.ru/lick/34.gif', 'https://gifs.gachi.ru/lick/35.gif', 'https://gifs.gachi.ru/lick/36.gif', 'https://gifs.gachi.ru/lick/37.gif', 'https://gifs.gachi.ru/lick/38.gif', 'https://gifs.gachi.ru/lick/39.gif', 'https://gifs.gachi.ru/lick/40.gif']) )

		await ctx.send( embed = emb )

@slap.error
async def slap_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		emb = discord.Embed( description = (f'Ударил и обидел <@712676102262227034>'), colour = discord.Colour(0x710186) )

		emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url, )
		emb.set_image( url = nekos.img('slap') )
		
		await ctx.send( embed = emb )

@bite.error
async def bite_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		emb = discord.Embed( description = (f'{ b } <@712676102262227034>'), colour = discord.Colour(0x710186) )

		emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
		emb.set_image( url = random.choice(['https://gifs.gachi.ru/bite/20.gif', 'https://gifs.gachi.ru/bite/21.gif', 'https://gifs.gachi.ru/bite/22.gif', 'https://gifs.gachi.ru/bite/23.gif', 'https://gifs.gachi.ru/bite/24.gif', 'https://gifs.gachi.ru/bite/25.gif', 'https://gifs.gachi.ru/bite/26.gif', 'https://gifs.gachi.ru/bite/27.gif', 'https://gifs.gachi.ru/bite/28.gif', 'https://gifs.gachi.ru/bite/29.gif', 'https://gifs.gachi.ru/bite/30.gif', 'https://gifs.gachi.ru/bite/31.gif', 'https://gifs.gachi.ru/bite/32.gif', 'https://gifs.gachi.ru/bite/33.gif', 'https://gifs.gachi.ru/bite/34.gif', 'https://gifs.gachi.ru/bite/35.gif', 'https://gifs.gachi.ru/bite/36.gif', 'https://gifs.gachi.ru/bite/37.gif', 'https://gifs.gachi.ru/bite/38.gif', 'https://gifs.gachi.ru/bite/39.gif', 'https://gifs.gachi.ru/bite/40.gif']) )

		await ctx.send( embed = emb )

@baka.error
async def baka_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		emb = discord.Embed( description = (f'Назвал бакой <@712676102262227034>'), colour = discord.Colour(0x710186) )
		
		emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
		emb.set_image( url = nekos.img('baka') )

		await ctx.send( embed = emb )







#Отправка сообщений в лс
@client.command()
@commands.is_owner()
async def send( ctx, member: discord.Member, *, text):
	await ctx.channel.purge( limit = 1 )
	await member.send( text )

#say

@client.command()
@commands.cooldown(1, 5, commands.BucketType.member)
async def say(ctx, *, text):
	await ctx.channel.purge( limit = 1 )
	t = (text)
	emb = discord.Embed(description = f'{t}', colour = discord.Colour(0x710186))
	await ctx.send(embed = emb)


#8ball
 

@client.command(name = "8ball")
@commands.cooldown(1, 5, commands.BucketType.member)
async def ball(ctx, *, arg):

    message = ['Нет','Да','Возможно','Опредленно нет'] 
    s = random.choice( message )
    await ctx.send(embed = discord.Embed(description = f'{s}', colour = discord.Colour(0x4910c4)))
    return

# Работа с ошибками шара

@ball.error 
async def ball_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ): 
        await ctx.send(embed = discord.Embed(description = f'Вы не задали вопрос', colour = discord.Colour(0x4910c4))) 

@client.command(aliases=['юзер', 'юзеринфо', 'user'])
async def userinfo(ctx, member: discord.Member):
    roles = member.roles
    role_list = ""
    for role in roles:
        role_list += f"<@&{role.id}> "
    emb = discord.Embed(title=f'Информация о пользователе {member}', colour = discord.Colour(0x4910c4) )
    emb.set_thumbnail(url=member.avatar_url)
    emb.add_field(name='ID', value=member.id)
    emb.add_field(name='Имя', value=member.name)
    emb.add_field(name='Высшая роль', value=member.top_role)
    emb.add_field(name='Дискриминатор', value=member.discriminator)
    emb.add_field(name='Присоеденился к серверу', value=member.joined_at.strftime('%Y.%m.%d \n %H:%M:%S'))
    emb.add_field(name='Присоеденился к Discord', value=member.created_at.strftime("%Y.%m.%d %H:%M:%S"))

    await ctx.send( embed = emb )

@userinfo.error
async def userinfo_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		
		roles = ctx.author.roles
		role_list = ""
		for role in roles:
			role_list += f"<@&{role.id}>"
		emb = discord.Embed(title=f'Информация о пользователе { ctx.author }', colour = discord.Colour(0x4910c4) )
		emb.set_thumbnail(url=ctx.author.avatar_url)
		emb.add_field(name='ID', value=ctx.author.id)
		emb.add_field(name='Имя', value=ctx.author.name)
		emb.add_field(name='Высшая роль', value=ctx.author.top_role)
		emb.add_field(name='Дискриминатор', value=ctx.author.discriminator)
		emb.add_field(name='Присоеденился к серверу', value=ctx.author.joined_at.strftime('%Y.%m.%d \n %H:%M:%S'))
		emb.add_field(name='Присоеденился к Discord', value=ctx.author.created_at.strftime("%Y.%m.%d %H:%M:%S"))

		await ctx.send( embed = emb )



@client.command( pass_context = True )
@commands.cooldown(1, 5, commands.BucketType.member)
async def avatar( ctx, member: discord.Member, *, reason = None ):
	emb = discord.Embed( description = f'Аватарка { member.mention }', colour = discord.Colour(0x4910c4) )

	emb.set_image( url = member.avatar_url )

	await ctx.send( embed = emb )

@avatar.error
async def avatar_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		emb = discord.Embed( description = f'Аватарка <@712676102262227034>', colour = discord.Colour(0x4910c4) )

	emb.set_image( url = 'https://cdn.discordapp.com/avatars/712676102262227034/97bc4179ad12c1e70fa425a91e2dfef9.webp?size=1024' )

	await ctx.send( embed = emb )



@client.command()
async def animeavatar(ctx):
    emb = discord.Embed( description= 'Ваша аватарка', colour = discord.Colour(0x4910c4) )
    emb.set_image(url=nekos.img('avatar'))
    await ctx.send(embed=emb)


#Hentai
@client.command( aliases = [' hentai '] )
@commands.cooldown( 1, 5, commands.BucketType.member )

async def hentai( ctx, text ):
    if ctx.channel.is_nsfw():
        rnek = nekos.img( text )
        emb = discord.Embed( colour = discord.Colour( 0xc2487b ) )
        emb.set_image( url = rnek )
        await ctx.send( embed = emb )
    else:
        msg = await ctx.send( embed=discord.Embed( description='Я бы с радостью, но тут не NSFW канал....', colour = discord.Colour.blue() ) )
        await ctx.message.add_reaction( '🔞' )
        await asyncio.sleep( 5 )
        await msg.delete()

#Hentai error
@hentai.error
async def hentai_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
			emb = discord.Embed( colour = discord.Colour( 0xc2487b ) )

			emb.add_field( name = 'Укажите аргумент.', value = '**feet, yuri, trap, futanari, solog, feetg, cum, lewdkemo, erokemo, hololewd, eroyuri, solo, bj, eron, nsfw_avatar, anal, hentai, erofeet, blowjob, pussy, tits, holoero, pwankg, classic, kuni, femdom, spank, erok, boobs, random_hentai_gif, smallboobs, ero, lewd, keta. ** ' )


			await ctx.send( embed = emb )




#nekos image
@client.command( aliases = ['sendimg', 'image', 'img'] )
@commands.cooldown( 1,5, commands.BucketType.member )

async def sendimage( ctx, text ):
	sneko = nekos.img( text )
	emb = discord.Embed( colour = discord.Colour(0x8e3dcc) )
	emb.set_image( url = sneko )
	await ctx.send( embed = emb )

#nekos image error
@sendimage.error
async def sendimage_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
			emb = discord.Embed( colour = discord.Colour(0x8e3dcc) )

			emb.add_field( name = 'Укажите аргумент.', value = '**kemonomimi, gasm, lizard, fox_girl, neko, waifu, holo.** ' )


			await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.is_owner()

async def bot( ctx ):
	emb = discord.Embed( description = f'Я присутствую на {len(client.guilds)} серверах' )

	await ctx.send( embed = emb )



@client.command( aliases = ['cs', 'status'] )
@commands.is_owner()
async def changestatus( ctx, statustype:str = None, *, arg:str = None):
    if statustype is None: # Type Check
        await ctx.send( 'Вы не указали тип Статуса' )
    elif arg is None: # Arg Check
        await ctx.send( 'Вы не указали нужный аргумент' )
    else:
        if statustype.lower() == 'game': # Game
            await client.change_presence (activity=discord.Game( name = arg) )
        elif statustype.lower() == 'listen': # Listen
            await client.change_presence( activity=discord.Activity( type=discord.ActivityType.listening, name = arg) )
        elif statustype.lower() == 'watch': # Watch
            await client.change_presence( activity=discord.Activity( type=discord.ActivityType.watching, name = arg) )



@client.command( aliases = ['c'] )
async def contact( ctx ):
	emb = discord.Embed ( colour  = discord.Colour(0x4910c4))

	emb.add_field( name = 'Контакты разработчика', value = '[``Вк разработчика``](https://vk.com/nebegayteslavyane)     |             [``Стим разработчика``](https://steamcommunity.com/id/Enot2017/)     |             [``Дискорд сервер``](https://discord.gg/usMuEzT)' )

	await ctx.send( embed = emb )

@client.command()
async def prefix(ctx, arg: str = None):
    if arg is None:
        emb = discord.Embed(title = "Изменение префикса", description = "Введите префикс, на какой хотите поменять?", colour = discord.Color.red())
        emb.add_field(name = "Пример использования комманды", value = f"{ctx.prefix}prefix <ваш префикс>")
        await ctx.send(embed = emb)
    elif len(str(arg)) > 5:
        emb = discord.Embed(title = "Изменение префикса", description = "Введите префикс не больше 5-ти символов", colour = discord.Color.red())
        emb.add_field(name = "Пример использования комманды", value = f"{ctx.prefix}prefix <ваш префикс>")
        await ctx.send(embed = emb)
    else:
        prefix.update_one({"_guild_id": ctx.guild.id}, {"$set": {"prefix": arg}})
        
        emb = discord.Embed(title = "Изменение префикса", description = f"Префикс сервера был обновлён на: {arg}", colour = discord.Color.green())
        await ctx.send(embed = emb)

#@client.command(aliases = ['информация', 'моя карта', 'я'])
async def usercard(ctx):
	img = Image.new('RGBA', (400, 200), '#228921')
	url = str(ctx.author.avatar_url)

	response = requests.get(url, stream = True)
	response = Image.open(io.BytesIO(response.content))
	response = response.convert('RGBA')
	response = response.resize((100, 100), Image.ANTIALIAS)

	img.paste(response, (15, 15, 115, 115))

	idraw = ImageDraw.Draw(img)
	name = ctx.author.name
	tag = ctx.author.descriminator

	headline = ImageFont.truetype('arial.ttf', size = 20)
	undertext = ImageFont.truetype('arial.ttf', size = 12)
	idraw.text((145, 15), f'{name}#{tag}', font = headline)

	img.save('usercard.png')

	await ctx.send(file = discord.File(fp = 'usercard.png'))

@client.command()
async def profile(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    image = Image.open("file.jpg")
    img = image.resize((1024, 576))
    idraw = ImageDraw.Draw(img)
    title = ImageFont.truetype('21028.ttf', size = 80)

    name = user.name
    idraw.text((400, 10), name, font = title, fill = "black")
    
    avatar = user.avatar_url_as(size = 128)
    avt = io.BytesIO(await avatar.read())
    imga = Image.open(avt)
    imguser = imga.resize((250, 250))

    img.paste(imguser, (10, 10))
    img.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg"))

@client.event
async def on_member_join(member):
	if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
		cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 0)")
		connection.commit()

	else:
		pass

@client.command(aliases = ['cash'])
async def balance(ctx, member: discord.Member = None):
	if member is None:
		await ctx.send(embed = discord.Embed( 
			description = f"""Баланс пользователя **{ctx.author}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} :leaves:**""")
		)
	else:
		await ctx.send(embed = discord.Embed( 
			description = f"""Баланс пользователя **{member}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0]} :leaves:**""")
		)


class server_info():
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

class server_info1():
    def __init__(self, config):
        self.config1 = config
        self.ip_address = config.get('server_ip')
        self.server_port = config.get('server_port')
        self.connect_link = 'steam://connect/' + str(self.ip_address) + ':' + str(self.server_port) + '/'
        print('Loaded server config: ' + self.ip_address + ':' + str(self.server_port))

    def get(self):     

        try:
            server_info1 = a2s.info((self.ip_address, self.server_port ))
            self.player_list = a2s.players((self.ip_address, self.server_port))
            self.server_name = server_info1.server_name
            self.curr_map = server_info1.map_name.split('/')[-1]
            self.players = str(server_info1.player_count) + '/' + str(server_info1.max_players)
            self.ping = str(int((server_info1.ping* 1000))) + 'ms'

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
        await client.change_presence(activity=discord.Game(name=status))
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
with open("config.json", "strogiy.json") as json_file:
    config = json.load(json_file)

server_info = server_info(config)	

mm_player_list = []

@client.event
async def on_ready():
    client.loop.create_task(refresh_server_info())
    client.loop.create_task(check_mm_state())

    print('Bot connect')
# !server - show server info embed
@client.command()
async def server(ctx):  
	server_info.get()
	status = server_info.curr_map + ' | ' + server_info.players  
	emb = discord.Embed(title='Jail', color=0x00ff00) 
	if(len(config.get('custom_thumb')) > 0):
		emb.set_thumbnail(url=config.get('custom_thumb'))
	map_banner = config['map_banner'].get(server_info.curr_map, None)
	if(map_banner):
		if(len(map_banner) > 0):
			emb.set_image(url=map_banner)
	emb.add_field(name='Name', value=server_info.server_name, inline=True)
	emb.add_field(name='Map', value=server_info.curr_map, inline=True)
	emb.add_field(name='Players', value=server_info.players, inline=True)
	emb.add_field(name='Ping', value=server_info.ping, inline=True)
	emb.add_field(name='\u200b', value=server_info.connect_link, inline=False)
	await ctx.send(embed=emb)






# Connect

token = open( 'token.txt', 'r' ).readline()

client.run(token)