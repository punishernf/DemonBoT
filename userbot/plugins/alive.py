""".admin Plugin for @thedemonhub"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`I AM ALIVE MASTER!!!!`**\n\n"
                     "`My Great Developer`: @demonhub\nDatabase Status: Databases functioning Normally!\n\n`Always with you, My Master!!!`\n"
                     f"`My Master`: {DEFAULTUSER}\n")
                     
