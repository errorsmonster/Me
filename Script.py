class script(object):
    START_TXT = """<b>ʜᴇʟᴏ {}
    
ɪ ᴀᴍ ᴘᴏᴡᴇʀ ғᴜʟʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ʙᴏᴛ
ɪ ᴀᴍ ᴘᴍ sʜᴏʀᴛɴᴇʀ-ʟɪɴᴋ ʙᴏᴛ

ᴍᴀɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/J_shree_ram">ɴᴏᴛʜɪɴɢ ʙʀᴏ</a></b> 😏</b>"""

    
    HELP_TXT = """<b>Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""

    ABOUT_TXT = """<b>
 🤖 ᴍʏ ɴᴀᴍᴇ : {}
 👨‍💻 ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/J_shree_ram'>ɴᴏᴛʜɪɴɢ ʙʀᴏ</a>
 📚 ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
 📝 ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
 ♻️ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
 📡 ʜᴏsᴛᴇᴅ ᴏɴ  : <a href='https://www.heroku.com/'>Heroku</a>
 🥶 ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.0 [sᴛᴀʙʟᴇ​]</b>"""

    SOURCE_TXT = """
<b>Tʜɪꜱ Bᴏᴛ Iꜱ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.
ꜱᴏᴜʀᴄᴇ : <a href='https://github.com/Singhsawan/PM-Shortner-Bot'>ʀᴇᴘᴏ ʟɪɴᴋ</a></b> 🙃</b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonurl:https://t.me/TeamHMT_Bots)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇx</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ᴏɴ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EXTRAMOD_TXT = """ʜᴇʟᴘ: Exᴛʀᴀ Mᴏᴅᴜʟᴇs
<b>ɴᴏᴛᴇ:</b>
my features Stay here new features coming soon...  
 <b>✯ Maintained by : <a href=https://t.me/creatorrio>☢RIO NETWORKS☢</a></b>
  
 <b>✯ Join here : <a href=https://t.me/Teamrioupdates>☢Join my updateds☢</a></b> 
  
 ./id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</ code> 
 ./info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code> 
 ./song - Download any song [<code>example /song vaa vaathi song</code>] 
 ./telegraph - <code>Telegraph generator sen under 5MB video or photo I give telegraph link</code> 
 ./tts - <code>This command usage text to voice converter</code> 
 ./video - This command usage any YouTube video download hd [<code>example /video https://youtu.be/Aiue8PMuD-k</code>]
 ./font - This command usage stylish and cool font generator [<code>example /font hi</code>]"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. Oɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. [Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ Gғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD Fɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>"""

    STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ɪɴ ɢᴏᴏɢʟᴇ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ 😃

ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Uncharted or Uncharted 2022 or Uncharted En

ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 👇

ᴇxᴀᴍᴘʟᴇ : Loki S01 or Loki S01E04 or Lucifer S03E24

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ..."""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ Fᴏʀ Mᴏᴠɪᴇ Iɴ Dᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    SHORTLINK_INFO = """
<b>──────「<a href=https://t.me/> Hᴏᴡ ᴛᴏ Eᴀʀɴ Mᴏɴᴇʏ </a> 」──────

Yᴏᴜ ᴄᴀɴ Eᴀʀɴ Mᴏɴᴇʏ Fʀᴏᴍ Tʜɪs Bᴏᴛ Uɴᴛɪʟ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟɪᴠᴇ.

Wᴀɴᴛ ᴛᴏ Kɴᴏᴡ Hᴏᴡ? Fᴏʟʟᴏᴡ Tʜᴇsᴇ Sᴛᴇᴘs:-

sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 1𝟶𝟶 ᴍᴇᴍʙᴇʀs.

sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ Aɴʏ <a href=https://Omnifly.in.net>Sʜᴏʀᴛᴇɴᴇʀ Wᴇʙsɪᴛᴇ</a>.

sᴛᴇᴘ 𝟹 : ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href=https://t.me/> ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ </a>Tᴏ ᴄᴏɴɴᴇᴄᴛ sʜᴏʀᴛᴇɴᴇʀ.

➣ Yᴏᴜ ᴄᴀɴ ᴄᴏɴɴᴇᴄᴛ ᴀs ᴍᴀɴʏ ɢʀᴏᴜᴘ ʏᴏᴜ ʜᴀᴠᴇ.

Any Doubts or Not Connecting? Contact Me </b>
"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    SELECT = """
MOVIES ➢ Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs"

SERIES ➢ Sᴇʟᴇᴄᴛ "Sᴇᴀsᴏɴs"

Tɪᴘ: Sᴇʟᴇᴄᴛ "Lᴀɴɢᴜᴀɢᴇs" ᴏʀ "Sᴇᴀsᴏɴs" Bᴜᴛᴛᴏɴ ᴀɴᴅ Cʟɪᴄᴋ "Sᴇɴᴅ Aʟʟ" Tᴏ ɢᴇᴛ Aʟʟ Fɪʟᴇ Lɪɴᴋs ɪɴ ᴀ Sɪɴɢʟᴇ ᴄʟɪᴄᴋ"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
 {file_name}

⚙️ sɪᴢᴇ : {file_size}"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
⏱️ Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me this command reply with Picture or Vide Under (5MB) 

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    CARB_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗖𝗔𝗥𝗕𝗢𝗡☽︎
𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝚂 𝙰 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝚃𝙷𝙴 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝚂𝙷𝙾𝚆𝙽 𝙸𝙽 𝚃𝙷𝙴 𝚃𝙾𝙿 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁𝙴 𝚃𝙴𝚇𝚃𝚂.
𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙴 𝙼𝙾𝙳𝚄𝙻𝙴 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝚃𝙴𝚇𝚃 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙸𝚃 𝚆𝙸𝚃𝙷 /carbon 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴 𝙲𝙰𝚁𝙱𝙾𝙽 𝙸𝙼𝙰𝙶𝙴"""

    SHARE_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗦𝗛𝗔𝗥𝗘 𝗧𝗘𝗫𝗧☽︎

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
• /share - 𝚁𝚎𝚙𝚕𝚢 𝚆𝚒𝚝𝚑 𝙰𝚗𝚢 𝚃𝚎𝚡𝚝 𝚃𝚘 𝚂𝚎𝚗𝚍 𝚃𝚑𝚒𝚜 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 """

    YTDL = """<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴</b>

🍁 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘖𝘳 𝘈𝘶𝘥𝘪𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• /song 𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 
• /video or /mp4 𝘈𝘯𝘥 https://youtu.be/*****

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/song Vikram</code>
<code>/mp4 https://youtu.be/*******</code>
<code>/video https://youtu.be/*****</code>  """

    </b>"""

    RULE_TXT = """
    
     𝗚𝗿𝗼𝘂𝗽 𝗥𝘂𝗹𝗲𝘀 

◈ <b>Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ:</b>
• ᴀᴠᴀᴛᴀʀ 𝟸𝟶𝟶𝟿 ✅
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅
• ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌
• ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌

◈ <b>Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛ:</b>
• ᴠɪᴋɪɴɢs S𝟶𝟷 ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷E𝟶𝟷 ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ✅
• ᴠɪᴋɪɴɢs S𝟶𝟷 ʜɪɴᴅɪ ᴅᴜʙʙ... ❌
• ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 𝟷 ❌
• ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs ❌

<b>➙ ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ ꜱᴇʟꜰ ᴘʀᴏᴍᴏᴛɪᴏɴ. 
➙ ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ, ᴅᴏᴄᴜᴍᴇɴᴛꜱ, ᴜʀʟ, ᴇᴛᴄ...
➙ ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇꜱᴛ ᴀɴʏ ᴛʜɪɴɢꜱ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ, ᴀɴɪᴍᴀᴛɪᴏɴ, ᴄᴀʀᴛᴏᴏɴ, ᴀɴɪᴍᴇ, ᴋ-ᴅʀᴀᴍᴀ ᴍᴀɴʏ ᴍᴏʀᴇ.</b>

🔰 <b>Nᴏᴛᴇ :</b> ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ."""



    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    LOGO = """
 __ ____  __    __      _______   ______  ________  ______  
 /      \|  \  /  \    |       \ /      \|        \/      \ 
|  ▓▓▓▓▓▓\ ▓▓ /  ▓▓    | ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\\▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓\
| ▓▓__| ▓▓ ▓▓/  ▓▓     | ▓▓__/ ▓▓ ▓▓  | ▓▓  | ▓▓  | ▓▓___\▓▓
| ▓▓    ▓▓ ▓▓  ▓▓      | ▓▓    ▓▓ ▓▓  | ▓▓  | ▓▓   \▓▓    \ 
| ▓▓▓▓▓▓▓▓ ▓▓▓▓▓\      | ▓▓▓▓▓▓▓\ ▓▓  | ▓▓  | ▓▓   _\▓▓▓▓▓▓\
| ▓▓  | ▓▓ ▓▓ \▓▓\     | ▓▓__/ ▓▓ ▓▓__/ ▓▓  | ▓▓  |  \__| ▓▓
| ▓▓  | ▓▓ ▓▓  \▓▓\    | ▓▓    ▓▓\▓▓    ▓▓  | ▓▓   \▓▓    ▓▓
 \▓▓   \▓▓\▓▓   \▓▓     \▓▓▓▓▓▓▓  \▓▓▓▓▓▓    \▓▓    \▓▓▓▓▓▓ """
