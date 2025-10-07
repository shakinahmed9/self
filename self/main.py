import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = int(os.getenv("APP_ID")
CHANNEL_ID = int(os.getenv("FIX_CHANNEL_ID", 0))  

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents, application_id=APP_ID)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready to change nicknames!")


@bot.command(name="mrbean")
async def change_nick(ctx, *, new_nick: str):
    """Change the member's nickname in the server"""
    # ✅ Check if command is used in the fixed channel
    if CHANNEL_ID != 0 and ctx.channel.id != CHANNEL_ID:
        return await ctx.send("❌ I don’t have permission to change the server nick name !")

    member = ctx.author  # command ব্যবহারকারী
    try:
        await member.edit(nick=new_nick)
        await ctx.send(f"✅ {member.mention}, ✅ Server name changed to **{new_nick}**")
    except discord.Forbidden:
        await ctx.send("❌ I don’t have permission to change the server name.")
    except Exception as e:
        await ctx.send(f"⚠️ Error: `{e}`")


def joiner(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
    vc = {"op": 4,"d": {"guild_id": GUILD_ID,"channel_id": CHANNEL_ID,"self_mute": SELF_MUTE,"self_deaf": SELF_DEAF}}
    ws.send(json.dumps(auth))
    ws.send(json.dumps(vc))
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps({"op": 1,"d": None}))

def run_joiner():
  os.system("clear")
  print(f"Logged in as {username}#{discriminator} ({userid}).")
  while True:
    joiner(usertoken, status)
    time.sleep(30)



if __name__ == "__main__":
    bot.run(TOKEN)
