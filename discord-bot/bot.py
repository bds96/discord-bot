import os

from datetime import datetime
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot("!")

target_channel_id = 724773710996832311

cache = set()

@tasks.loop(hours=1)
async def called_once_a_day():
	today = datetime.today()
	ymd = (today.year, today.month, today.day)
	if ymd not in cache:
		if today.weekday() == 2: # Wednesday 
		    message_channel = bot.get_channel(target_channel_id)
		    print(f"Got channel {message_channel}")
		    await message_channel.send("https://www.youtube.com/watch?v=apANX0_qlr8")
	else
		cache.add(ymd)

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
bot.run(TOKEN)