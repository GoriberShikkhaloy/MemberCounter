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
                edit_message_text_teletips = "**EduMentors | কোর্সকারীর সংখ্যা গণক**\n<i>[দ্যা প্রফেসর **ッ**  কর্তৃক তৈরী ]</i>"
                for CHANNEL_OR_GROUP in CHANNEL_OR_GROUP_LIST:
                    try:
                        get_chat_teletips = await MemberCounterMeta.get_chat(int(CHANNEL_OR_GROUP))   
                        if get_chat_teletips.type == "channel":
                            edit_message_text_teletips += f"\n\n **{get_chat_teletips.title}**\n  👥 কোর্সটিতে যুক্ত আছেন: **{get_chat_teletips.members_count}** জন"
                        else:
                            edit_message_text_teletips += f"\n\n **{get_chat_teletips.title}**\n  👥 কোর্সটিতে যুক্ত আছেন: **{get_chat_teletips.members_count}** জন" 
                        await asyncio.sleep(2)
                    except ValueError:
                        print(f'ID not found: {CHANNEL_OR_GROUP }. Skipping...')                       
                edit_message_text_teletips += f"\n\n**এই মেসেজটি একটি স্বয়ংক্রিয় প্রোগ্রাম দ্বারা পরিবেশিত!**\n<i>মেসেজটি প্রতিদিন দুবার, অর্থাৎ দুপুর ১১ টা এবং রাত ১১ টায় স্বয়ংক্রিয়ভাবে আপডেট হবে!</i>"
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
