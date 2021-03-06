from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.utils import get_display_name
from telethon import custom, events

from . import *


@bot.on(d3vil_cmd(pattern=r"tag(all|bots|admins)?(.*)"))
@bot.on(sudo_cmd(pattern=r"tag(all|bots|admins)?(.*)", allow_sudo=True))
async def tag(event):
    text = event.text
    d3vil = event.pattern_match.group(2)
    part = 0
    if d3vil:
        users = f"{d3vil}"
    else:
        users = ""
    async for members in event.client.iter_partcipants(event.chat_id, 50):
        part = part + 1
        y = members.participants
        if isinstance(y, admin):
            if "admins" in text:
                if not members.deleted:
                    users+= f"\n[{get_display_name(members)}](tg://user?id={members.id})"
        if "bots" in text:
            if members.bot:
                users+= f"\n[{get_display_name(members)}](tg://user?id={members.id})"
        if "all" in text:
            if not (members.bot or members.deleted):
                users+= f"\n[{get_display_name(members)}](tg://user?id={members.id})"
    await event.client.send_message(event.chat_id)
    await event.delete()       
                  

CmdHelp("tag").add_command(
    "tagall", None, "Tag All The Paticipants Of The Chat"
).add_command(
    "tagbots", None, "Tag All The Bots In The Chat"
).add_command(
    "tagadmins", None, "Tag All The Admins Of The Chat"
).add()
