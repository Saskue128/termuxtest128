import os
from pyrogram import Client, filters
from pytgcalls import idle
from vc import get_pytgcalls, join_and_play, leave_call

# 🔧 Config (ENV se values le)
API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# 🔧 Bot aur VC client
app = Client("music-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = get_pytgcalls(app)

# ✅ Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    await message.reply_text(
        "🎶 **Music Bot is Alive!**\n\n"
        "Commands:\n"
        "`/play <song name>` - Play song in VC\n"
        "`/leave` - Leave VC"
    )

# ▶️ Play Command
@app.on_message(filters.command("play") & filters.group)
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("❌ Please provide a song name!")
    song = " ".join(message.command[1:])

    await message.reply(f"⏳ Downloading **{song}** ...")

    # 🔽 Download song using yt-dlp
    os.system(f"yt-dlp -x --audio-format mp3 -o song.mp3 'ytsearch1:{song}'")

    # 🔊 Join & Play
    result = await join_and_play(pytgcalls, message.chat.id, "song.mp3")
    if result is True:
        await message.reply(f"🎵 Now Playing: **{song}**")
    else:
        await message.reply(f"⚠️ Error: {result}")

# ⏹ Leave Command
@app.on_message(filters.command("leave") & filters.group)
async def leave(_, message):
    result = await leave_call(pytgcalls, message.chat.id)
    if result is True:
        await message.reply("👋 Left VC successfully.")
    else:
        await message.reply(f"⚠️ Error: {result}")

# 🚀 Run Bot
app.start()
pytgcalls.start()
idle()
