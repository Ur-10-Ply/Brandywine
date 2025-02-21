# bot/cogs/moderation.py
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """Moderation commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kick a user from the server.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked for: {reason}')

async def setup(bot):
    await bot.add_cog(Moderation(bot))
