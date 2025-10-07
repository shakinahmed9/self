import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = int(os.getenv("APP_ID", 1424547677059809421))

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, application_id=APP_ID)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready and running 24/7!")


@bot.command(name="mrbean")
@commands.has_permissions(manage_guild=True)
async def change_server_name(ctx, *, new_name: str):
    try:
        await ctx.guild.edit(name=new_name)
        await ctx.send(f"✅ Server name changed to **{new_name}** by {ctx.author.mention}")
    except discord.Forbidden:
        await ctx.send("❌ I don’t have permission to change the server name.")
    except Exception as e:
        await ctx.send(f"⚠️ Error: `{e}`")


@change_server_name.error
async def change_server_name_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don’t have permission to use this command.")


if __name__ == "__main__":
    bot.run(TOKEN)
