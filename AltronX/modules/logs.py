import asyncio
import os
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, OWNER_ID, CMD_HNDLR as hl
from telethon import events
from datetime import datetime

# Directory for storing logs
LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# File to store sudo users
SUDO_USERS_FILE = os.path.join(LOGS_DIR, "sudo_users.txt")
sudo_users = set()

def load_sudo_users():
    global sudo_users
    if os.path.exists(SUDO_USERS_FILE):
        with open(SUDO_USERS_FILE, 'r') as f:
            sudo_users = set(int(line.strip()) for line in f if line.strip())
    sudo_users.add(OWNER_ID)  # Always include owner

def save_sudo_users():
    with open(SUDO_USERS_FILE, 'w') as f:
        for user_id in sudo_users:
            f.write(f"{user_id}\n")

load_sudo_users()

def log_action(user_id, username, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = os.path.join(LOGS_DIR, "bot_actions.log")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] User: {username} (ID: {user_id}) - Action: {action}\n")

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%slogs(?: |$)(.*)" % hl))
async def logs(legend):
    if legend.sender_id in sudo_users:
        try:
            start = datetime.now()
            fetch = await legend.reply("» __Fetching Logs...__")
            
            # Read the last 100 lines of logs
            log_file = os.path.join(LOGS_DIR, "bot_actions.log")
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    logs = f.readlines()[-100:]
                logs_text = ''.join(logs)
            else:
                logs_text = "No logs found."

            end = datetime.now()
            ms = (end-start).seconds
            
            # Write logs to temporary file
            temp_file = "temp_logs.txt"
            with open(temp_file, "w") as f:
                f.write(f"⚡ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 ⚡ [ BotSpam Logs ]\n\n{logs_text}")
            
            await asyncio.sleep(1)
            await fetch.delete()
            
            # Send logs file
            await MK1.send_file(
                legend.chat_id,
                temp_file,
                caption=f"⚡ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 ⚡\n  » **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** `{ms} ꜱᴇᴄᴏɴᴅꜱ`"
            )
            
            # Clean up temporary file
            os.remove(temp_file)
            
            # Log this action
            sender = await legend.get_sender()
            username = sender.username or sender.first_name
            log_action(legend.sender_id, username, "Accessed logs")
            
        except Exception as e:
            await legend.reply(f"An error occurred: {str(e)}")
    else:
        await legend.reply("» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴀɴᴅ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def sudo_command(legend):
    if legend.sender_id != OWNER_ID:
        await legend.reply("» ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴅᴅ ᴏʀ ʀᴇᴍᴏᴠᴇ ꜱᴜᴅᴏ ᴜꜱᴇʀꜱ.")
        return

    args = legend.pattern_match.group(1).strip().split()
    if not args:
        # List current sudo users
        sudo_list = []
        for user_id in sudo_users:
            try:
                user = await MK1.get_entity(user_id)
                sudo_list.append(f"• {user.first_name} (ID: {user_id})")
            except:
                sudo_list.append(f"• Unknown User (ID: {user_id})")
        
        await legend.reply("**Current Sudo Users:**\n" + "\n".join(sudo_list))
        return

    action = args[0].lower()
    if len(args) < 2:
        await legend.reply("» Please specify a user ID to add or remove.")
        return

    try:
        user_id = int(args[1])
        if action == "add":
            if user_id in sudo_users:
                await legend.reply("» This user is already a sudo user.")
            else:
                sudo_users.add(user_id)
                save_sudo_users()
                await legend.reply(f"» Successfully added user {user_id} as sudo user.")
        elif action == "remove":
            if user_id == OWNER_ID:
                await legend.reply("» Cannot remove owner from sudo users.")
            elif user_id in sudo_users:
                sudo_users.remove(user_id)
                save_sudo_users()
                await legend.reply(f"» Successfully removed user {user_id} from sudo users.")
            else:
                await legend.reply("» This user is not a sudo user.")
        else:
            await legend.reply("» Invalid action. Use 'add' or 'remove'.")
    except ValueError:
        await legend.reply("» Please provide a valid user ID.")
    except Exception as e:
        await legend.reply(f"» An error occurred: {str(e)}")
