#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MemberCounterMeta Telegram bot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/MemberCounterMeta

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio
from texts.texts_teletips import *

MemberCounterMeta = Client(
    name = "membercountermeta",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
CHANNEL_OR_GROUP_LIST = [i.strip() for i in os.environ.get("CHANNEL_OR_GROUP_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])

print(text_1)
async def main_MemberCounterMeta():
    async with MemberCounterMeta:
        try:
            while True:
                print(text_2)
                edit_message_text_teletips = "**EduMentors | সদস্যতা গণক**"
                for CHANNEL_OR_GROUP in CHANNEL_OR_GROUP_LIST:
                    try:
                        get_chat_teletips = await MemberCounterMeta.get_chat(int(CHANNEL_OR_GROUP))   
                        if get_chat_teletips.type == "channel":
                            edit_message_text_teletips += f"\n\n **{get_chat_teletips.title}**\n ├ <i>{get_chat_teletips.members_count} জন সাবস্ক্রাইবার</i>\n └ <i>[চ্যানেলের লিংক]({get_chat_teletips.invite_link})</i>"
                        else:
                            edit_message_text_teletips += f"\n\n **{get_chat_teletips.title}**\n ├ <i>{get_chat_teletips.members_count} জন মেম্বার</i>\n └ <i>[গ্রুপের লিংক]({get_chat_teletips.invite_link})</i>" 
                        await asyncio.sleep(2)
                    except ValueError:
                        print(f'ID not found: {CHANNEL_OR_GROUP }. Skipping...')                       
                edit_message_text_teletips += f"\n\n<i>৬০ মিনিট বা ১ ঘণ্টা পর পর স্বয়ংক্রিয়ভাবে রিফ্রেশ হবে!</i>"
                try:
                    await MemberCounterMeta.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, edit_message_text_teletips, disable_web_page_preview=True)
                except Exception:
                    pass    
                print(text_3)              
                await asyncio.sleep(3600) # 60 minutes = 3600 seconds
        except FloodWait as e:
            await asyncio.sleep(e.x)

@MemberCounterMeta.on_message(filters.command("status", "!") & filters.me)
async def alive(_, message: Message):
    await message.edit("সদস্য গণক জাগ্রত আছে!")
    await asyncio.sleep(10)
    await message.delete()                   
                        
MemberCounterMeta.run(main_MemberCounterMeta())

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
