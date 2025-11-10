#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import asyncio
import os
from telebot.async_telebot import AsyncTeleBot
from src import handlers # NoQa


bot = AsyncTeleBot(os.environ["TELEGRAM_TOKEN"])


# Handle '/start' and '/help'


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

if __name__ == '__main__':
    asyncio.run(bot.polling())