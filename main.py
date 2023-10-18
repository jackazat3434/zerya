import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

from datetime import datetime

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time

import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from random import randint
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","26177237"))
api_hash = os.environ.get("API_HASH","6929515a9de7f855c81d4e64f6f3a4e9")
bot_token = os.environ.get("TOKEN","6323354353:AAGrgV8-_14fy-bwpxQaF0_fXWKpPQJuU-s") # Botunuzun Tokenini Girin.
sahib = os.environ.get("sahib", "J3llack") # Sahiplik Hesabin Kullanıcı Adını Girin .
komutlar = os.environ.get("komutlar")
BOT_ID = int(os.environ.get("BOT_ID", "6323354353")) # Botunuzun İd'si ( Tokenin Başındaki Rakamları ) Girin .
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://kurdbeats:41213458@cluster0.j9z8lt4.mongodb.net/?retryWrites=true&w=majority") # MongoDB veritabanınızın url'si.
BOT_USERNAME = os.environ.get("BOT_USERNAME","ElitTaggerbot") # Botunuzun kullanıcı adı.
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001603322166")) # Botunuzun eylemleri kaydedeceği kayıt grubunun id'si.
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "ElitTaggerDuyuru") # Botunuzdan yasaklanan kullanıcıların itiraz işlemleri için başvuracağı grup, kanal veya kullanıcı. Boş bırakırsanız otomatik olarak OWNER_ID kimliğine yönlendirecektir.
GONDERME_TURU = os.environ.get("GONDERME_TURU", False) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = int(os.environ.get("OWNER_ID","6596508612")) # Sahip hesabın id'si
LANGAUGE = os.environ.get("LANGAUGE", "TR")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

anlik_calisan = []
gece_tag = []
rxyzdev_tagTot = {}
rxyzdev_initT = {} 
rxyzdev_stopT = {}

ozel_list = [6219267667]
grup_sayi = []
etiketuye = []

# ~~~~~~~~~~~~~~~~~~~~~~~ gece ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

startmesaj = "**ᴍᴇʀʜᴀʙᴀ 👋** __ᴇᴛɪᴋᴇᴛ ᴛᴀɢ ʙᴏᴛᴜɴᴀ ʜᴏs ɢᴇʟᴅɪɴ ,\n\nʙɪʀʙɪʀɪɴᴅᴇɴ ғᴀʀᴋʟɪ ᴇᴛɪᴋᴇᴛ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴠᴇ ʙɪʀʙɪʀɪɴᴅᴇɴ ᴇɢʟᴇɴᴄᴇʟɪ ᴍᴏᴅᴜʟʟᴇʀ ɪʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ʙᴏᴛᴜʏᴜᴍ. 🌜\n\n🤖 Kᴏᴍᴜᴛʟᴀʀɪᴍɪ ɢᴏʀᴍᴇᴋ ɪᴄɪɴ ᴀʟᴛᴛᴀᴋɪ `ᴋᴏᴍᴜᴛʟᴀʀ` ʙᴜᴛᴏɴᴜɴᴀ ᴛɪᴋʟᴀʏɪɴ. 🌜__" 
noadmin = "**➻ 🌜 ᴜᴢɢᴜɴᴜᴍ ᴀᴍᴀ ʏᴏɴᴇᴛɪᴄɪ ᴅᴇɢɪʟsɪɴɪᴢ .**"
nogroup = "**➻ 🌜 ᴋᴏᴍᴜᴛʟᴀʀ sᴀᴅᴇᴄᴇ ɢʀᴜᴘʟᴀʀᴅᴀ ᴋᴜʟʟᴀɴɪʟᴀʙɪʟɪʀ .**"
nomesaj = "**➻ 💬 ʙᴀɴᴀ ʙɪʀ ᴍᴇsᴀᴊ ᴠᴇʀɪɴ .**"

#######################

@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def tag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        
#################
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)




#########################

# tek tek etiketleme modülü

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def tektag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)


#########################

# söz ile etiketleme modülü

soz = (
'𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış', 
'İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛', 
'𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛',
'𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı', 
'Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚', 
'𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟', 
'𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒', 
'𝑀𝑢𝑡𝑙𝑢𝑦𝑢𝑚 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑒𝑛𝑙𝑒', 
'𝐵𝑒𝑛 ℎ𝑒𝑝 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘 𝑖𝑠𝑡𝑒𝑑𝑖ğ𝑖𝑚 𝑔𝑖𝑏𝑖 𝑠𝑒𝑣𝑖𝑛𝑑𝑖𝑚', 
'𝐵𝑖𝑟𝑖 𝑣𝑎𝑟 𝑛𝑒 ö𝑧𝑙𝑒𝑚𝑒𝑘𝑡𝑒𝑛 𝑦𝑜𝑟𝑢𝑙𝑑𝑢𝑚 𝑛𝑒 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛', 
'Ç𝑜𝑘 𝑧𝑜𝑟 𝑏𝑒 𝑠𝑒𝑛𝑖 𝑠𝑒𝑣𝑚𝑒𝑦𝑒𝑛 𝑏𝑖𝑟𝑖𝑛𝑒 𝑎şı𝑘 𝑜𝑙𝑚𝑎𝑘', 
'Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧', 
'𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖', 
'𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎', 
'𝐴𝑛𝑙𝑎𝑦𝑎𝑛 𝑦𝑜𝑘𝑡𝑢, 𝑆𝑢𝑠𝑚𝑎𝑦ı 𝑡𝑒𝑟𝑐𝑖ℎ 𝑒𝑡𝑡𝑖𝑚', 
'𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛', 
'𝑂 𝑔𝑖𝑡𝑡𝑖𝑘𝑡𝑒𝑛 𝑠𝑜𝑛𝑟𝑎 𝑔𝑒𝑐𝑒𝑚 𝑔ü𝑛𝑑ü𝑧𝑒 ℎ𝑎𝑠𝑟𝑒𝑡 𝑘𝑎𝑙𝑑ı', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚', 
'𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛', 
'İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟', 
'𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖', 
'𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚', 
'Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛', 
'𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟', 
'𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚', 
'𝐾ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛𝑒 𝑔ö𝑛ü𝑙𝑑𝑒 𝑣𝑒𝑟𝑖𝑙𝑖𝑟 ö𝑚ü𝑟𝑑𝑒', 
'𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛', 
'𝑈𝑠𝑙ü𝑝 𝑘𝑎𝑟𝑎𝑘𝑡𝑒𝑟𝑖𝑑𝑖𝑟 𝑖𝑛𝑠𝑎𝑛ı𝑛', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎', 
'𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛', 
'𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟', 
'𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟', 
'𝐻𝑒𝑚 𝑔üç𝑙ü 𝑜𝑙𝑢𝑝 ℎ𝑒𝑚 ℎ𝑎𝑠𝑠𝑎𝑠 𝑘𝑎𝑙𝑝𝑙𝑖 𝑏𝑖𝑟𝑖 𝑜𝑙𝑚𝑎𝑘 ç𝑜𝑘 𝑧𝑜𝑟', 
'𝑀𝑢ℎ𝑡𝑎ç 𝑘𝑎𝑙ı𝑛 𝑦ü𝑟𝑒ğ𝑖 𝑔ü𝑧𝑒𝑙 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟', 
'İ𝑠𝑡𝑒𝑦𝑒𝑛 𝑑𝑎ğ𝑙𝑎𝑟ı 𝑎ş𝑎𝑟 𝑖𝑠𝑡𝑒𝑚𝑒𝑦𝑒𝑛 𝑡ü𝑚𝑠𝑒ğ𝑖 𝑏𝑖𝑙𝑒 𝑔𝑒ç𝑒𝑚𝑒𝑧', 
'İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛', 
'İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟', 
'𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛', 
'𝑌𝑖𝑛𝑒 𝑦ı𝑟𝑡ı𝑘 𝑐𝑒𝑏𝑖𝑚𝑒 𝑘𝑜𝑦𝑚𝑢ş𝑢𝑚 𝑢𝑚𝑢𝑑𝑢', 
'Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç', 
'𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙𝑚𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒', 
'𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢', 
'𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦'
) 



@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def ctag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)





#########################

#cumlelerle tag
cumle = (
"Asansörde hiç gizlicene osurdun mu? 🙄",
"Bugüne kadar okuduğun en güzel kitap hangisiydi?🤓",
"Çıplak ellerini kullanarak dondurma yiyebilir misin? 🙄",
"Yüzmek zayıflatıyorsa balinaların yağsız, tığ gibi olması gerekmez miydi?😜",
"Hayvanlar konuşabilseydi, en kaba olan hangisi olurdu?🤓",
"Ressam olsaydın ilk gün neyi boyardın?🤩",
"İngilizcede butterfly kelebek anlamına geliyor. “Butter” tereyağı demek, “fly” da uçmak anlamında, o zaman kelebekler uçantereyağları mıdır?😜",
"Oda arkadaşınız olarak hangisini tercih ederdiniz? Keçi mi kuş mu?😵‍💫",
"Uhu iyi bir yapıştırıcıysa içinde bulunduğu tüpün içini neden yapıştıramıyor?🙊",
"Dünya dönüyorsa neden zıpladığımız zaman aynı yere düşüyoruz?🧐",
"Süpermen ve Batman arasındaki bir kavgada kim kazanır?🥸",
"Cenazenizde hangi müziğin çalmasını  istersiniz?🫠",
"Dünya döndüğü halde neden bir helikopter havada sabit durduğunda aynı yerde olur?😵‍💫",
"Duvardaki bir sinek olsaydın, kimi dinlemek isterdin?🤓",
"Bir günlüğüne tanrı olsanız neyi değiştirmek istersiniz?🧐",
"Bir zombi kıyametinde seçeceğiniz silah ne olurdu?😱",
"Hükümet her şeyi yasadışı hale getirmeye karar verirse sonuç ne olur? 🤔",
"Tüp bebek daha mı az yakar?🥸",
"Meyve olsaydın hangi meyve olurdun?🤩",
"Anneannemize “anneanne” diyoruz da neden dedemize “babababa” demiyoruz?🥸",
"Sonsuza kadar yaşayabilseydin ne yapardın?🤔",
"Ellerinizi veya ayaklarınızı kaybetmek zorunda olsaydınız, hangisini seçerdiniz?😬",
"En gereksiz kelime nedir?🫣",
"Gördüğünüz en kötü veya en tuhaf rüya neydi?🤯",
"Tüm dünya borç batağındaysa tüm para nereye gitti?🤔",
"Paraşütle atlamak ister miydin?🥳",
"Hayat bir video oyunuysa, en çok hangi hile kodunu kullanmak istersiniz?😂",
"Yaşadığın şehri aşık olduğun biri için değiştirir misin?🥹",
"Hala hatırlayabiliyorsan, en komik çocukluk anın ne?😄",
"Bir insanda çekici gördüğün en garip şey nedir?😐",
"Evde yalnız kalmaktan korkuyor musunuz?🤔",
"Gerçek anlamda en son ne seni hayal kırıklığına uğrattı?🥲",
"Biri seni aynanın önünde dans ederken yakaladı mı?😁",
"Hayatında denemek istediğin çılgın maceralardan biri ne?🤔",
"Kutudan doğrudan bir pastel boya yemek zorunda kalsaydınız ne renk isterdiniz?🤔",
"Hiç iç çamaşırı giymeden bir gün geçirdin mi?😳",
"Şimdiye kadar yediğin en tuhaf yemek neydi?👀",
"Çocukken hiç kağıttan uçak ya da gemi yaptın mı?🥰",
"Başkaları ile benim hakkımda hiç konuşuyor musun?🤔",
"Çok sevdiğin sevgilin seni aldatsa ama çok pişman olsa onu affeder misin?🙄",
"Zaman yolculuğunu nereye yapmak istersiniz: geçmişe mi yoksa geleceğe mi?🤔",
"Kıyı asla geri sallamadığı için denizin tuzlu olduğunu düşünüyor musunuz?🤨",
"Ölüm listenizdeki ilk kişi kimdir?🙄",
"Gerçekten sarhoş olduktan sonra yaptığınız en çılgınca şey nedir?😅",
"Bir keresinde bir yemek için ödeme yapmayı planlarken cüzdanınızı getirmeyi unuttunuz mu?😯",
"İdam cezasına çarptırıldıysan son yemeğin ne olacağını düşünüyorsun?🤷🏻‍♂️",
"Sahip olduğun en garip alışkanlığın nedir?😵‍💫",
"Kaç defa aşık oldun?🤔",
"Uyurken yürüyüşe çıkma alışkanlığınız var mı?😁",
"İnsanlar çorbayı içer mi yoksa yer mi?😑",
"Sence bir kişinin bir arkadaşlık uygulamasında biyografisine koyabileceği en kötü şey ne?🤮",
"Köpek bulunan eve melek girmezmiş. Azrail de bir melek. Evimizi köpeklerle doldurursak ölümsüz olmaz mıyız?🫣",    
"Su altındayken bir balonu şişirmenin mümkün olduğuna inanıyor musunuz?🤓",
"Kurgusal bir karakter olabilseydin, kim olurdun?😎",
"Hangi Disney prensesi en iyi casusluk yapabilir?🙀", 
"En gereksiz kelime nedir?😒", 
"Hangisini tercih edersiniz: Burnunuz yok ama gerçekten güzel kokan parmaklarınız mı var? Ya da kör ol ama gerçekten güzel bir gülüşün var mı?😵",
"Bir yıl 365 gün 6 saat sürüyor ise neden her yıl yılbaşını gece 12’de kutluyoruz?🎅🏻",
"Vücudunun hangi bölümüne ekleme yapmak isterdin?🙂",
"Köpeğimin adını “Hoşt” koyarsam çağırdığım zaman ne yapar?🐶",
"Eğer uçağın karakutusu kaza anında parçalanmıyorsa neden bütün uçak o maddeden yapılmıyor?✈️",
"Dünya döndüğü halde neden bir helikopter havada sabit durduğunda aynı yerde olur?🚁",
"Bir zombi kıyametinde seçeceğiniz silah ne olurdu?🔫",
"Tüp bebek daha mı az yakar?😵‍💫",
"İngilizcede butterfly kelebek anlamına geliyor. “Butter” tereyağı demek, “fly” da uçmak anlamında, o zaman kelebekler uçantereyağları mıdır?😂",
"Süpermen ve Batman arasındaki bir kavgada kim kazanır?🥵",
"En büyük parti hayvanı hangisidir?😺",
"Dünya dönüyorsa neden zıpladığımız zaman aynı yere düşüyoruz?🙃",
"Yüzmek zayıflatıyorsa balinaların yağsız, tığ gibi olması gerekmez miydi?👀",
"Hayvanlar konuşabilseydi, en kaba olan hangisi olurdu?😃",
"Ressam olsaydın ilk gün neyi boyardın?👨🏻‍🎨",
"Uhu iyi bir yapıştırıcıysa içinde bulunduğu tüpün içini neden yapıştıramıyor?🙊",
"Mağara adamlarının mağara kadınları hakkında kabus gördüğünü düşünüyor musunuz?🫨",
"Özellikle güzel kokmamasına rağmen koklamak istemeye devam ettiğin şey ne?🤪",
"Bir zombi kıyametinde ne kadar hayatta kalabileceğin düşünüyorsun?😱",
"Özellikle güzel kokmamasına rağmen koklamak istemeye devam ettiğin şey ne?🤪",
"En çok hangi ünlüyle hayat değiştirmek istersiniz?😒",
"Gördüğünüz en kötü veya en tuhaf rüya neydi?😪",
"Zaman yolculuğunu nereye yapmak istersiniz: geçmişe mi yoksa geleceğe mi?🤔",
"Kıyı asla geri sallamadığı için denizin tuzlu olduğunu düşünüyor musunuz?🤨",
"Ölüm listenizdeki ilk kişi kimdir?🙄",
"Gerçekten sarhoş olduktan sonra yaptığınız en çılgınca şey nedir?😅",
"Bir keresinde bir yemek için ödeme yapmayı planlarken cüzdanınızı getirmeyi unuttunuz mu?😯",
"İdam cezasına çarptırıldıysan son yemeğin ne olacağını düşünüyorsun?🤷🏻‍♂️",
"Sence bir kişinin bir arkadaşlık uygulamasında biyografisine koyabileceği en kötü şey ne?🤮",
"Köpek bulunan eve melek girmezmiş. Azrail de bir melek. Evimizi köpeklerle doldurursak ölümsüz olmaz mıyız?🫣",
"Korku filmlerinden korkuyor musunuz?😱",
"Vampir ile kurt evlenirse çocukları kumpir mi olur?🤭",
"Başkalarına bildirmek için hangi gizli komployu yapmak istersin?🥶",
"Eğer bugün hava sıcaklığı 0 derece ise ve yarın iki kat daha soğuk olacaksa, yarın hava yine 0 derece olmaz mı?😁",
"Köpeklerin konuşabilseydi imajını tamamen mahvedecek bir şey söyleyebilir mi?🤕",
"Neden sa yazarken as yazılıyoda hi yazılırken ih yazılmıyor?😶‍🌫",
"İnekler ot yiyip süt üretiyorsa sütün hammaddesi ot mudur?🫤",   
"Uçakta uçmaktan korkuyor musunuz? 😁"
)



@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def ctag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        


#########################

# renk ile etiketleme modülü
renk = ( 
"🔴",
"🟠",
"🟡",
"🟢", 
"🔵",
"🟣",
"🟤", 
"⚫",
"⚪"
)



@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def rtag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        



#########################

# bayrak ile etiketleme modülü
bayrak = (
"🇦🇨",
"🇧🇬",
"🇧🇭",
"🇧🇮",
"🇧🇯",
"🇧🇱",
"🇧🇲",
"🇧🇳",
"🇧🇶",
"🇧🇷",
"🇧🇸",
"🇧🇹",
"🇧🇻",
"🇧🇼",
"🇧🇾",
"🇧🇿",
"🇨🇦",
"🇨🇨",
"🇨🇩",
"🇨🇫",
"🇨🇬",
"🇨🇭",
"🇿🇼",
"🇿🇲",
"🇿🇦",
"🇾🇹",
"🇾🇪",
"🇽🇰",
"🇼🇸",
"🇼🇫",
"🏴󠁧󠁢󠁷󠁬󠁳󠁿",
"🇻🇺",
"🇻🇳",
"🇻🇮",
"🇻🇬",
"🇻🇪",
"🇻🇨",
"🇻🇦",
"🇺🇿",
"🇺🇾",
"🇺🇸",
"🇺🇳",
"🇺🇬",
"🇺🇦",
"🇹🇿",
"🇹🇼",
"🇹🇻",
"🇹🇹",
"🇹🇷",
"🇹🇴",
"🇹🇳",
"🇹🇲",
"🇹🇱",
"🇹🇰",
"🇹🇭",
"🇹🇫",
"🇹🇨",
"🇹🇦",
"🇸🇿",
"🇸🇾",
"🇸🇽", 
"🇸🇻",
"🇸🇸",
"🇸🇴",
"🇸🇲",
"🇸🇱",
"🇸🇰",
"🇸🇮",
"🇸🇭",
"🇸🇬",
"🇸🇪",
"🇸🇩",
"🏴󠁧󠁢󠁳󠁣󠁴󠁿",
"🇸🇦",
"🇷🇼",
"🇷🇺",
"🇷🇸",
"🇷🇴",
"🇷🇪",
"🇶🇦",
"🇵🇾",
"🇵🇼", 
"🇵🇹", 
"🇵🇸",
"🇵🇷",
"🇵🇳",
"🇵🇲",
"🇵🇱",
"🇵🇰",
"🇵🇭",
"🇵🇫",
"🇵🇪",
"🇦🇿" 
)



@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def btag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 2:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        














###################

#etiket işlemini iptal
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")

  global gece_tag
  gece_tag.remove(event.chat_id)

  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**⛔ ɪsʟᴇᴍ ɪᴘᴛᴀʟ ᴇᴅɪʟᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪᴘᴛᴀʟ ᴇᴅᴇɴ : {rxyzdev_stopT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")

  global anlik_calisan
  anlik_calisan.remove(event.chat_id)

  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**⛔ ɪsʟᴇᴍ ɪᴘᴛᴀʟ ᴇᴅɪʟᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪᴘᴛᴀʟ ᴇᴅᴇɴ : {rxyzdev_stopT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)




#########################

# Emoji ile etiketleme modülü

anlik_calisan = []

tekli_calisan = []




emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")



@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        



#İsim Etiket Modülü


gisim = ['Üzümlü kek ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu panda 🐼', 'Ay pare ✨', 'Ballı lokma ✨', 'Lale 🌷', 'Zambak ⚜', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare ✨', 'Reyhan 🌷', 'Kaktüs ⚜️', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği ✨', 'Tweety 🐥', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨',]

#güzel isimler @goktuResmi tarafından.




@client.on(events.NewMessage(pattern="^/itag ?(.*)"))
async def itag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ!__")
  else:
    return await event.respond(f"{nomesaj}\n**veya** /utag ⬅️ **ᴛɪᴋʟᴀʏɪɴ**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**🌜 ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ʙᴀsʟᴀᴛɪʟᴅɪ .**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{random.choice(gisim)}](tg://user?id={usr.id})  "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**➻ {msg}\n{usrtxt}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**🌜 ɪsʟᴇᴍ ᴛᴀᴍᴀᴍʟᴀɴᴅɪ .\n\n👤 ᴇᴛɪᴋᴇᴛʟᴇʀɪɴ sᴀʏɪsɪ : {rxyzdev_tagTot[event.chat_id]}\n🗣 ɪsʟᴇᴍɪ ʙᴀsʟᴀᴛᴀɴ : {rxyzdev_initT}**", buttons=(
                      [
                      Button.url('🌜 ʀᴇsᴍɪ ᴋᴀɴᴀʟ ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        







#Slap Modülü


tokat_mesaj = (
"{}, {}  Sana Domates Fırlattı! Suratı kıp kırmızı oldu 😁", 
"{}, {}  Senin Saçını Çekti!", 
"{}, {}  Sana Yumruk attı ! Buz koy morarmasın 🤕", 
"{}, {}  Sana Kafa Attı! Burnu kırıldı sanırım 😱", 
"{}, {}  Sana Uçan Tekme Attı! Jetli misin mübarek 👀", 
"{}, {}  Sana Kanepeyi Fırlattı! Öyle ölmez füze atsaydın 😱", 
"{}, {}  Sana İğne sapladı! Bu acıtmıştır sanırım 🥲", 
"{}, {}  Sana Yumurta Fırlattı! Tam isabet 🎯", 
"{}, {}  Sana Omuz attı! Ne bakıyon birader", 
"{}, {}  Sana Çelme taktı!", 
"{}, {}  Sana Damacana Fırlattı! Damacanaya bişey olmamıştır umarım 👀", 
"{}, {}  Senin Üstüne Çay Döktü! Yanıyorsun Fuat Abii 🔥", 
"{}, {}  Senin Kafanda Şişe Kırdı! Acımış olmalı 🥲",
"{}, {}  Senin Yüzüne Tükürdü! İşte bunu yapmayacaktın 🤬", 
"{}, {}  Sana Taş Attı! Aha kafası yarıldı 🤭", 
"{}, {}  Sana Osmanlı Tokatı Attı! Resmen şamar oğlana çevirdi 😱", 
"{}, {}  Sana Kavanoz Fırlattı! Başka bişey bulamadı sanırım 🙄",
"{}, {}  Senin Ayağının Önüne Muz Fırlattı! Basıp Kaydı 😂",
"{}, {}  Sana Çöp Kovası Fırlattı! Üstü Başı Hep Çöp Oldu 😥",
"{}, {}  Senin Üzerine Kamyon Sürdü! Kamyon'un Altında Kalmaktan Son Anda Kurtuldu 😱",
"{}, {}  Senin Gözüne Parmağını Soktu! Bu Gerçekten Acımış Olmalı 😭", 
"{}, {}  Sana Yolda Yürürken Ensene Tokat Attı ! Ve Kaçmaya Başladı🤣",
"{}, {}  Senin Yüzüne Kezzap Attı! Ah Be Bergenim🥹" ,   
"{}, {}  Seni Kıyma Makinesine Attı! Yenir Omega5😋" ,  
"{}, {}  Sana F35 Fırlattıı!! Savaş Başlasın🫣" ,   
"{}, {}  Sana Pasta Attı!! Duş Almak Şart Oldu.😝",
"{}, {}  Sana Terlik Fırlattı!! Tam İsabet Anne Adayı mısın Beee😱🤣" 
    
) 



@client.on(events.NewMessage(pattern="^/slap ?(.*)"))
async def tokatla(event):
  if not event.is_reply:
       await event.reply("✘ ʟᴜ‌ᴛғᴇɴ ᴛᴏᴋᴀᴛʟᴀᴍᴀᴋ ɪsᴛᴇᴅɪɢ‌ɪɴ ᴋᴜʟʟᴀɴıᴄıɴıɴ ᴍᴇsᴀᴊıɴı ʏᴀɴıᴛʟᴀ 🤗")
       return
  atan = await event.get_sender()
  mesaj = event.message

  yiyen_mesaj = await mesaj.get_reply_message()
  yiyen = yiyen_mesaj.sender

  vuran = f"[{atan.first_name}](tg://user?id={atan.id})"
  atilan = f"[{yiyen.first_name}](tg://user?id={yiyen.id})"

  memom = random.choice(tokat_mesaj)
  await event.reply(memom.format(vuran, atilan))
















#Bot kontrol
#@goktuResmi Tarafından eklenmiştir.

@client.on(events.NewMessage(pattern='^/botcum'))
async def event(ups):
  if ups.sender_id == 6695730144:
   await ups.reply("**Göktuğ Abi Şuan Çalışmaktayım 🇹🇷🤍**")
  elif ups.sender_id == 6695730144:
    await ups.reply("**Seni ne kadar seviyorum bilsen tamam tamam uzatmıyorum. Aktifim !**")
  elif ups.sender_id == 5979903647:
    await ups.reply("** Sayın Berf hanım Şuan Çalışmaktayım 🇹🇷🤍**")
  elif ups.sender_id == 6604549799:
    await ups.reply("__Poyrazcım Şuan Çalışıyorum Merak Etme🥺👉👈__")
  elif ups.sender_id == 6303442651:
    await ups.reply("__En Sevdiğim Yengem Şuan Çalışmaktayım👉👈🌹🌺__")
  else:
    await ups.reply("**Sen benim sahibim değilsin! **")








  
# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("💫 ᴋᴏᴍᴜᴛʟᴀʀ", data="help")
                      ],
                      [Button.url('➕ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ', f'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [
                      Button.url("🏷️ ʀᴇsᴍɪ ᴋᴀɴᴀʟ", f'https://t.me/{GROUP_SUPPORT}')
                      ],[
                      Button.url('👨🏻‍💻 ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ', f'https://t.me/{sahib}')
                      ]
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"{startmesaj}", buttons=( 
                                                    [
                                                     Button.inline("💫 ᴋᴏᴍᴜᴛʟᴀʀ", data="help")
                                                    ],
                                                    [Button.url('➕ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ', f'https://t.me/{BOT_USERNAME}?startgroup=a')],
                                                    [
                                                    Button.url("🏷️ ʀᴇsᴍɪ ᴋᴀɴᴀʟ", f'https://t.me/{GROUP_SUPPORT}')
                                                    ],[
                                                    Button.url('👨🏻‍💻 ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ', f'https://t.me/{sahib}')
                                                    ]
                                                  ),
                                                  link_preview=False)


# gece kusu
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"{komutlar}", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)






# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("💫 ᴋᴏᴍᴜᴛʟᴀʀ", data="help")
                      ],
                      [Button.url('➕ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ', f'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [Button.url('🏷️ ʀᴇsᴍɪ ᴋᴀɴᴀʟ', f'https://t.me/{GROUP_SUPPORT}')],
                       [Button.url('👨🏻‍💻 ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)

#########################

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**📖 Hey , {msg.from_user.mention}\nBeni Gruba Eklediğin İçin Teşekkürler .**''', 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚙️ Daha Fazla Bilgi", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply('🇹🇷 ⚙️ ʙᴏᴛᴜɴ sᴀʜɪʙɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴋᴀᴛɪʟᴅɪ !')


# Eros oku

@app.on_message(filters.command(["eros"],["/", ""]) & ~filters.private & ~filters.channel)
async def ship(c:Client, m:Message):
    users = await c.get_chat_members(m.chat.id, limit=200)
    
    users_l = []
    for user in users:
        if user.user.is_bot or user.user.is_deleted:
            pass
        else:
            users_l.append(user.user)
    count = len(users_l)
    
    ilk = users_l[randint(0,count)]
    iki = users_l[randint(0,count)]
    
    if ilk.id==1550788256 or ilk.id==5576614947 or iki.id==5375589992 or iki.id==5576614947:
        await m.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜ ᴀᴛɪʟᴅɪ.\n• ᴀsɪᴋʟᴀʀ  :\n\n[ ✍🏻 ](tg://user?id=5053767281) 💞 [ . ](tg://user?id=5533927130)**")
        
    else:
        await m.reply(f"**💘 ᴇʀᴏs'ᴜɴ ᴏᴋᴜ ᴀᴛɪʟᴅɪ.\n• ᴀsɪᴋʟᴀʀ  :\n\n{ilk.mention}  💞  {iki.mention}\n\n`ᴜʏᴜᴍʟᴜʟᴜᴋ ᴏʀᴀɴɪ: %{random.randint(0, 100)}`**")







################### VERİTABANI VERİ GİRİŞ ÇIKIŞI #########################
class Database: 
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id): # Veritabanına yeni kullanıcı ekler
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            ),
        )

    async def add_user(self, id): # Veritabına yeni kullanıcı eklemek için ön def
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id): # Bir kullanıcının veritabında olup olmadığını kontrol eder.
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self): # Veritabanındaki toplam kullanıcıları sayar.
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self): # Veritabındaki tüm kullanıcıların listesini verir.
        return self.col.find({})

    async def delete_user(self, user_id): # Veritabından bir kullanıcıyı siler.
        await self.col.delete_many({"id": int(user_id)})

    async def ban_user(self, user_id, ban_duration, ban_reason): # Veritabanınızdaki bir kullanıcıyı yasaklılar listesine ekler.
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason,
        )
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def remove_ban(self, id): # Veritabanınızdaki yasaklılar listesinde bulunan bir kullanıcın yasağını kaldırır.
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id): # Bir kullanıcın veritabanınızda yasaklılar listesinde olup olmadığını kontrol eder.
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        user = await self.col.find_one({"id": int(id)})
        return user.get("ban_status", default)

    async def get_all_banned_users(self): # Veritabınızdaki yasaklı kullanıcılar listesini verir.
        return self.col.find({"ban_status.is_banned": True})


db = Database(DATABASE_URL, BOT_USERNAME)
mongo_db_veritabani = MongoClient(DATABASE_URL)
dcmdb = mongo_db_veritabani.handlers



################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()

############### Broadcast araçları ###########
broadcast_ids = {}


async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-goktug.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-goktug.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-goktug.txt")



# Genelde müzik botlarının mesaj silme özelliği olur. Bu özelliği ReadMe.md dosyasındaki örnekteki gibi kullanabilirsiniz.
delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool: # Grup için mesaj silme özeliğinin açık olup olmadığını kontrol eder.
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int): # Grup için mesaj silme özeliğini açar.
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int): # Grup için mesaj silme özeliğini kapatır.
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})

################# SAHİP KOMUTLARI #############
# Verileri listeleme komutu
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")



# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)



# Broadcast komutu
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)



# Bir kullanıcı yasaklama komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def ban(c: Client, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        if len(m.command) <= 1:
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 2:
            ban_duration = 9999
            ban_reason = " ".join(m.command[1:])
    else:
        if len(m.command) <= 1:
            return await m.reply(LAN.NEED_USER)
        elif len(m.command) == 2:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 3:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = " ".join(m.command[2:])
    
        if str(user_id).startswith("-"):
            try:    
                ban_log_text = LAN.BANNED_GROUP.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_GROUP.format(ban_reason))
                await c.leave_chat(user_id)
                ban_log_text += LAN.GROUP_BILGILENDIRILDI
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.GRUP_BILGILENDIRILEMEDI.format(traceback.format_exc())
        else:
            try:    
                ban_log_text = LAN.USER_BANNED.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_USER.format(ban_reason))
                ban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.ban_user(user_id, ban_duration, ban_reason)
        await c.send_message(LOG_CHANNEL, ban_log_text)
        await m.reply_text(ban_log_text, quote=True)


# Bir kullanıcın yasağını kaldırmak komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unban(c: Client, m: Message):
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        else:
            if len(m.command) <= 1:
                return await m.reply(LAN.NEED_USER)
            else:
                user_id = int(m.command[1])
        unban_log_text = LAN.UNBANNED_USER.format(m.from_user.mention, user_id)
        if not str(user_id).startswith("-"):
            try:
                await c.send_message(user_id, LAN.USER_UNBAN_NOTIFY)
                unban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                unban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.remove_ban(user_id)
        await c.send_message(LOG_CHANNEL, unban_log_text)
        await m.reply_text(unban_log_text, quote=True)



# Yasaklı listesini görme komutu
@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BLOCKS.format(user_id, ban_duration, banned_on, ban_reason)
    reply_text = LAN.TOTAL_BLOCK.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)



############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"



########### ÇOKLU DİL ##############
class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})**"
        GRUP_BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})\n💬 Grub : {}\n🌟 Grub ID: {}\n🎲 Mesaj Linki : [Buraya Tıkla](https://t.me/c/{}/{})**"
        SAHIBIME = "sahibime"
        PRIVATE_BAN = "Üzgünüm, yasaklandınız! Bunun bir hata olduğunu düşünyorsanız {} yazın."
        GROUP_BAN = "Üzgünüm, grubunuz karalisteye alındı! Burada daha fazla kalamam. Bunun bir hata olduğunu düşünyorsanız {} yazın.'"
        NOT_ONLINE = "aktif değil"
        BOT_BLOCKED = "botu engellemiş"
        USER_ID_FALSE = "kullanıcı kimliği yanlış"
        BROADCAST_STARTED = "```📤 BroadCast başlatıldı! Bittiği zaman mesaj alacaksınız!"
        BROADCAST_STOPPED = "✅ ```Broadcast başarıyla tamamlandı.``` \n\n**Şu Kadar Sürede Tamamlandı:** `{}` \n\n**Kayıtlı Toplam Kullanıcı:** `{}` \n\n**Toplam Gönderme Denemesi:** `{}` \n\n**Başarıyla Gönderilen:** `{}` \n\n**Toplam Hata:** `{}`"
        STATS_STARTED = "{} **Lütfen bekleyiniz verileri getiriyorum!**"
        STATS = """**@{} Verileri**\n\n**Kullanıcılar;**\n» **Toplam Sohbetler:** `{}`\n» **Toplam Gruplar: `{}`\n» **Toplam PM's: `{}`"""
        BAN_REASON = "Bu sebep yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur"
        NEED_USER = "**Lütfen Kullanıcı kimliği verin.**"
        BANNED_GROUP = "🚷 **Yasaklandı!\n\nTarafından:** {}\n**Grup ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_GROUP = "**Üzgünüm grubunuz kara listeye alındı! \n\nSebep:** `{}`\n\n**Daha fazla burada kalamam. Bunun bir hata olduğunu düşünüyorsanız destek grubuna gelin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Grubu bilgilendirdim ve gruptan ayrıldım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Grubu bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        USER_BANNED = "🚷 **Yasaklandı! \n\nTarafından:** {}\n **Kullanıcı ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_USER = "**Üzgünüm kara listeye alındınız! \n\nSebep:** `{}`\n\n**Bundan sonra size hizmet veremeyeceğim.**"
        KULLANICI_BILGILENDIRME = "\n\n✅ Kişiyi bilgilendirdim."
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **Kişiyi bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        UNBANNED_USER = "🆓 **Kullanıcının Yasağı Kaldırıldı !** \nTarafından: {} \n**Kullanıcı ID:**{}"
        USER_UNBAN_NOTIFY = "🎊 Müjde! Yasağınız kaldırıldı!"
        BLOCKS = "🆔 **Kullanıcı ID**: `{}`\n⏱ **Süre**: `{}`\n🗓 **Yasaklanan Tarih**: `{}`\n💬 **Sebep**: `{}`\n\n"
        TOTAL_BLOCK = "🚷 **Toplam Yasaklanan:** `{}`\n\n{}"

        
app.run()
print(" Bot çalışıyor :)")
client.run_until_disconnected()
