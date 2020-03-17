from bs4 import BeautifulSoup
from glob import glob
from random import choice
import requests
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import json
from telegram import ParseMode
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utility import get_keyboard



def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?') #вывод сообщения в консоль при отправке команды /start
    bot.message.reply_text('Здравствуйте, {}! \nНажмите ?'
                           .format(bot.message.chat.first_name), reply_markup=get_keyboard()) # отправим ответ
    print(bot.message)