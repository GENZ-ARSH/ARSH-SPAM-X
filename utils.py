import sys
import logging
import importlib
from pathlib import Path
from config import SUDO_USERS


def load_plugins(plugin_name):
    path = Path(f"AltronX/modules/{plugin_name}.py")
    name = "AltronX.modules.{}".format(plugin_name)
    try:
        # First try the newer approach
        if hasattr(importlib, 'util'):
            spec = importlib.util.spec_from_file_location(name, path)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
        else:
            # Fallback to older approach
            load = importlib.machinery.SourceFileLoader(name, str(path)).load_module()
        
        load.logger = logging.getLogger(plugin_name)
        sys.modules["AltronX.modules." + plugin_name] = load
        print("Altron has Imported " + plugin_name)
    except Exception as e:
        print(f"Error loading plugin {plugin_name}: {str(e)}")

async def edit_or_reply(event, text):
    if event.sender_id in SUDO_USERS:
        reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)
