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


if __name__ == "__main__":
    bot.run(TOKEN)
