from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

d3vil_pic = Config.ALIVE_PIC or "https://telegra.ph/file/5abfcff75e1930dcdfaf3.mp4"
pm_caption = "  __**🔥🔥𝗗3𝗩𝗜𝗟 𝗕𝗢𝗧 𝗜𝗦 𝗔𝗟𝗜𝗩𝗘🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ↼𝗠𝗔𝗦𝗧𝗘𝗥⇀\n  **『 {d3vil_mention} 』**\n\n"
)
pm_caption += f"╔══════════════════╗\n"
pm_caption += f"╠•➳➠ `𝖳𝖾𝗅𝖾𝗍𝗁𝗈𝗇:` `{tel_ver}` \n"
pm_caption += f"╠•➳➠ `𝖵𝖾𝗋𝗌𝗂𝗈𝗇:` `{d3vil_ver}`\n"
pm_caption += f"╠•➳➠ `𝖲𝗎𝖽𝗈:` `{is_sudo}`\n"
pm_caption += f"╠•➳➠ `𝖢𝗁𝖺𝗇𝗇𝖾𝗅:` [𝙹𝗈𝗂𝗇](https://t.me/D3VIL_BOT_OFFICIAL)\n"
pm_caption += f"╠•➳➠ `𝖢𝗋𝖾𝖺𝗍𝗈𝗋:` [𝙳3𝙺𝚁𝙸𝚂𝙷](https://t.me/D3_krish)\n"
pm_caption += f"╠•➳➠ `𝖮𝗐𝗇𝖾𝗋:` [𝙳3𝚅𝙸𝙻𝙶𝚄𝙻𝚂𝙷𝙰𝙽](https://t.me/D3VILGULSHAN)\n"
pm_caption += f"╚══════════════════╝\n"
pm_caption += " [⚡REPO⚡](https://github.com/TEAM-D3VIL/D3vilBot) 🔹 [📜License📜](https://github.com/TEAM-D3VIL/D3vilBot/blob/main/LICENSE)"


#-------------------------------------------------------------------------------

@d3vilbot.on(d3vil_cmd(outgoing=True, pattern="alive$"))
@d3vilbot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(d3vil):
    if d3vil.fwd_from:
        return
    await d3vil.get_chat()
    await d3vil.delete()
    await bot.send_file(d3vil.chat_id, d3vil_pic, caption=pm_caption)
    await d3vil.delete()

msg = f"""
**⚡ 𝐃3𝐕𝐈𝐋𝐁𝐎𝐓 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄 ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**↼𝗠𝗔𝗦𝗧𝗘𝗥⇀   :**  **『{d3vil_mention}』**
**╔══════════════════╗**
**╠➳➠ 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 :**  `{tel_ver}`
**╠➳➠ 𝗗3𝗩𝗜𝗟𝗕𝗢𝗧  :**  **{d3vil_ver}**
**╠➳➠ 𝗨𝗽𝘁𝗶𝗺𝗲   :**  `{uptime}`
**╠➳➠ 𝗔𝗯𝘂𝘀𝗲    :**  **{abuse_m}**
**╠➳➠ 𝗦𝘂𝗱𝗼      :**  **{is_sudo}**
**╚══════════════════╝
"""
botname = Config.BOT_USERNAME

@d3vilbot.on(d3vil_cmd(pattern="d3vil$"))
@d3vilbot.on(sudo_cmd(pattern="d3vil$", allow_sudo=True))
async def d3vil_a(event):
    try:
        d3vil = await bot.inline_query(botname, "alive")
        await d3vil[0].click(event.chat_id)
        if event.sender_id == d3krish:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "d3vil", None, "Shows Inline Alive Menu with more details."
).add()
