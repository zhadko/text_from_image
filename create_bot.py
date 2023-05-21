from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import logging

TOKEN = '5863641670:AAGQ_2Nl87ROAFkPf6Ql1oJjotcT5OM_zto'
storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=storage)