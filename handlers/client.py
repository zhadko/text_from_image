from aiogram import types, Dispatcher

import time
import dialogue
import easyocr
import os

from create_bot import bot, dp
from keyboards import client_kb


@dp.message_handler(commands=['start', 'help'])
@dp.message_handler(lambda message: message.text == 'Довідка 🌚')
async def command_start(message : types.Message):

    await bot.send_message(
        message.from_user.id, 
        dialogue.hello_message,
        reply_markup=client_kb.greet_kb,
        parse_mode='HTML', 
    )    


@dp.message_handler(commands=['music'])
@dp.message_handler(lambda message: message.text == 'Музика 🤟')
async def music(message : types.Message):
    await bot.send_audio(message.from_user.id, open('Hava Nagila.mp3', 'rb'))


@dp.message_handler(commands=['team'])
@dp.message_handler(lambda message: message.text == 'Команда 💪')
async def team(message : types.Message):
    
    await bot.send_message(
        message.from_user.id, 
        dialogue.team_message,
        disable_web_page_preview=True, 
        parse_mode='HTML',
    )


async def govnoy_vonyaet(message : types.Message):
    
    from random import choices
    from string import ascii_letters
    
    async def edit_msg(text: str, sleep: float) -> None:
        await bot.edit_message_text(
            chat_id=message.from_user.id,
            message_id=msg.message_id, 
            text=text,
            parse_mode='HTML',
        )
        time.sleep(sleep)
    
    msg = await message.answer(dialogue.fake_progress_bar[0])
    
    dest = ''.join(choices(list(ascii_letters), k=10))
    await message.photo[-1].download(f"temp/{dest}.png")
    
    for d in dialogue.fake_progress_bar[1:-1]:
        await edit_msg(d, 0.15)
    
    text = '\n'.join(await pic_to_text(f'temp/{dest}.png'))
    
    await edit_msg(dialogue.fake_progress_bar[9], 0.15)
    await message.answer(
        f"<i>Результат:</i>\n\n<code>{text}</code>",
        parse_mode='HTML',
    )
        
    await bot.delete_message(message.from_user.id, msg.message_id)
    
    for f in os.listdir('temp'):
        os.remove(os.path.join('temp', f))
    
        
        
async def pic_to_text(file_path):
    try:
        reader = easyocr.Reader(['uk', 'en'])
        result = reader.readtext(file_path, detail=0, paragraph=True)
    except Exception as e:
        raise Exception(f"Text recognition failed: {e}")
    return result


async def none_reply(message: types.Message):
    await bot.send_message(
        message.from_user.id, 
        dialogue.error,
    )

    

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(govnoy_vonyaet, content_types='photo')
    dp.register_message_handler(none_reply, content_types=['text', 'audio', 'document', 'video', 'video_note', 'voice', 'sticker'])