from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputStream, AudioPiped

# PyTgCalls client return karega
def get_pytgcalls(app):
    return PyTgCalls(app)

# VC join aur play
async def join_and_play(pytgcalls, chat_id, file_path):
    try:
        await pytgcalls.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(file_path),
            ),
        )
        return True
    except Exception as e:
        return str(e)

# VC leave
async def leave_call(pytgcalls, chat_id):
    try:
        await pytgcalls.leave_group_call(chat_id)
        return True
    except Exception as e:
        return str(e)
