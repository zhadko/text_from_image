from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging

import openai

TOKEN = 'BOT_TOKEN'

openai.api_key = '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'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())