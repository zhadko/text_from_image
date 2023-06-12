from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging

import openai

TOKEN = 'BOT_TOKEN'

openai.api_key = 'OPENAI_API_KEY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())