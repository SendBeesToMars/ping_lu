import secret
import socket
import time
import discord
import os

hostname = secret.hostname
discord_user_id = int(secret.discord_user_id)

token = os.environ["DOOTDOOT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

starttime = time.time()

@client.event
async def on_ready():
    print(f"Logged on as {client.user}")
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            result = sock.connect_ex((hostname, 80))
		
        if result == 0:
            print("sucess")
        else:
            print("failure")
			# send message
            await send_dm()
            time.sleep(43200.0 - ((time.time() - starttime) %
					   43200.0))  # 43200 sleep for 12h

        time.sleep(3600.0 - ((time.time() - starttime) % 3600.0))  # 3600 sleep 1h

    
async def send_dm():
    member = discord.utils.get(client.get_all_members(), id=discord_user_id)
    # if member found, send dm
    if member:
        channel = await member.create_dm()
        await channel.send("server down ;(")

client.run(token)
