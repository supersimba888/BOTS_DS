#
# discord_image_spam_dm.py
# @author Merubokkusu
# @created Fri Jan 04 2019 00:58:07 GMT-0500 (Eastern Standard Time)
# @copyright 2018 - 2019
# @license CC BY-NC-ND 3.0 US | https://creativecommons.org/licenses/by-nc-nd/3.0/us/
# @website https://github.com/Merubokkusu/discord-spam-bots/
# @email liam@merubokkusu.com
# @last-modified Tue Mar 05 2019 02:15:49 GMT-0500 (Eastern Standard Time)
#

import discord
import asyncio
import random
import os
import sys
import subprocess
import aiohttp
sys.path.append("./.")
from config import *

if(os.path.exists("proxies.txt")):
    conn = aiohttp.ProxyConnector(proxy="http://"+sys.argv[2])
    client = discord.Client(connector=conn)
else:
    client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
    for server in client.servers:
        if ScanAllServers == False:
            if(server.id == DiscordServer):
                UserList = list(server.members)
        else:
            UserList = list(server.members)
            
    if HeavyScrape == False:                  
        for member in UserList:
            if(member.id != client.user.id):
                userNames = open('dm_spam_image.txt');
                text = userNames.read().strip().split()
                if member.id in text: 
                    print(member.name + ' was already messaged')
                else:
                    try:
                        UpImage = random.choice(os.listdir(DirPictures)) 
                        await client.send_file(member, DirPictures + UpImage)
                        print('Sent '+UpImage +' To '+ member.name)
                        file = open('dm_spam_image.txt','a')
                        file.writelines(member.id + '\n')
                        file.close()
                        for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                            sys.stdout.flush()
                            await asyncio.sleep(1)
                        sys.stdout.write("\rComplete!                    \n")
                    except Exception:
                        print('Something went wrong (;3;) relaunching...')
    else:
        while not client.is_closed:
            member = random.choice(UserList)   
            if(member.id != client.user.id):
                userNames = open('dm_spam_image.txt');
                text = userNames.read().strip().split()
                if member.id in text: 
                    print(member.name + ' was already messaged')
                else:
                    try:
                        UpImage = random.choice(os.listdir(DirPictures)) 
                        await client.send_file(member, DirPictures + UpImage)
                        print('Sent '+UpImage +' To '+ member.name)
                        file = open('dm_spam_image.txt','a')
                        file.writelines(member.id + '\n')
                        file.close()
                        for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                            sys.stdout.write("\r")
                            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                            sys.stdout.flush()
                            await asyncio.sleep(1)
                        sys.stdout.write("\rComplete!                    \n")
                    except Exception:
                        print('Something went wrong (;3;) relaunching...')     

if ':' in token: 
    enp = token.split(':')
    if autojoinServer == True:
        if sys.platform == "win32":
            p = subprocess.Popen(['python','bots/misc/joinServer.py',enp[0],enp[1],inviteLink,useBrowser],shell=True)
            p.wait()
        else:
            p = subprocess.Popen(['python','bots\misc\joinServer.py',enp[0],enp[1],inviteLink,useBrowser],shell=False)
            p.wait() 
    client.run(enp[0],enp[1], bot=False) 
else:
    if autojoinServer == True:
		if sys.platform == "win32":
			p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=True)
			p.wait()
		else:
			p = subprocess.Popen([pythonCommand,'bots\misc\joinServer2.0.py',token,inviteLink,sys.argv[3]],shell=False)
			p.wait()
    client.run(token, bot=False)
