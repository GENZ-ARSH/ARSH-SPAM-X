import os
import sys
import heroku3
from datetime import datetime
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
from .sudo_manager import add_sudo_user, remove_sudo_user, is_sudo_user
from utils import edit_or_reply


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"»⚡️𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥⚡️_ᴏᴘ_ʙᴏʟᴛᴀ", parse_mode=None, link_preview=None)
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"_⚡️𝗞𝗜𝗦𝗞𝗜 𝗚𝗔𝗔𝗡𝗗 𝗠𝗔𝗥𝗡𝗜 𝗕𝗢𝗦𝗦⚡️_\n» `{mp} ms`")


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"😖ʀᴇʙᴏᴏᴛ ᴋᴀʀᴋᴇ ᴛᴜɴᴇ ᴀᴘɴɪ ᴀᴜᴋᴀᴀᴛ ᴅɪᴋʜᴀ ᴅɪ...!😪😒")
        try:
            await MK1.disconnect()
        except Exception:
            pass
        try:
            await MK2.disconnect()
        except Exception:
            pass
        try:
            await MK3.disconnect()
        except Exception:
            pass
        try:
            await MK4.disconnect()
        except Exception:
            pass
        try:
            await MK5.disconnect()
        except Exception:
            pass
        try:
            await MK6.disconnect()
        except Exception:
            pass
        try:
            await MK7.disconnect()
        except Exception:
            pass
        try:
            await MK8.disconnect()
        except Exception:
            pass
        try:
            await MK9.disconnect()
        except Exception:
            pass
        try:
            await MK10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
sudousers = os.environ.get("SUDO_USER", None)

@MK1.on(events.NewMessage(pattern=r"\.addsudo"))
@MK2.on(events.NewMessage(pattern=r"\.addsudo"))
@MK3.on(events.NewMessage(pattern=r"\.addsudo"))
@MK4.on(events.NewMessage(pattern=r"\.addsudo"))
@MK5.on(events.NewMessage(pattern=r"\.addsudo"))
@MK6.on(events.NewMessage(pattern=r"\.addsudo"))
@MK7.on(events.NewMessage(pattern=r"\.addsudo"))
@MK8.on(events.NewMessage(pattern=r"\.addsudo"))
@MK9.on(events.NewMessage(pattern=r"\.addsudo"))
@MK10.on(events.NewMessage(pattern=r"\.addsudo"))
async def add_sudo(event):
    if event.sender_id != OWNER_ID:
        return await edit_or_reply(event, "⚠️ Only owner can add sudo users!")
    
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
    else:
        # Try to get user ID from command arguments
        try:
            user_id = int(event.pattern_match.group(1))
        except:
            return await edit_or_reply(event, "⚠️ Please reply to a user or provide user ID!")
    
    if add_sudo_user(user_id):
        await edit_or_reply(event, f"✅ Successfully added user {user_id} as sudo!")
    else:
        await edit_or_reply(event, f"⚠️ User {user_id} is already a sudo user!")

@MK1.on(events.NewMessage(pattern=r"\.delsudo"))
@MK2.on(events.NewMessage(pattern=r"\.delsudo"))
@MK3.on(events.NewMessage(pattern=r"\.delsudo"))
@MK4.on(events.NewMessage(pattern=r"\.delsudo"))
@MK5.on(events.NewMessage(pattern=r"\.delsudo"))
@MK6.on(events.NewMessage(pattern=r"\.delsudo"))
@MK7.on(events.NewMessage(pattern=r"\.delsudo"))
@MK8.on(events.NewMessage(pattern=r"\.delsudo"))
@MK9.on(events.NewMessage(pattern=r"\.delsudo"))
@MK10.on(events.NewMessage(pattern=r"\.delsudo"))
async def del_sudo(event):
    if event.sender_id != OWNER_ID:
        return await edit_or_reply(event, "⚠️ Only owner can remove sudo users!")
    
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id
    else:
        # Try to get user ID from command arguments
        try:
            user_id = int(event.pattern_match.group(1))
        except:
            return await edit_or_reply(event, "⚠️ Please reply to a user or provide user ID!")
    
    if remove_sudo_user(user_id):
        await edit_or_reply(event, f"✅ Successfully removed user {user_id} from sudo!")
    else:
        await edit_or_reply(event, f"⚠️ User {user_id} is not a sudo user!")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(GetFullUserRequest(previous_message.forward.sender_id))
        else:
            replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    return replied_user.user.id
