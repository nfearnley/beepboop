from discord.ext import commands

__version__ = "1.0.0"


class BeepBoopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.lower() == "beep":
            await message.channel.send("boop")
        elif message.content.lower() == "boop":
            await message.channel.send("beep")


def setup(bot):
    bot.add_cog(BeepBoopCog(bot))
