from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from flask import Flask
from config import Config


storage = MemoryStorage()

app = Flask(__name__)
app.config.from_object(Config)

bot = Bot(token=app.config['TELEGRAM_TOKEN'])
dp = Dispatcher(bot, storage=storage)
