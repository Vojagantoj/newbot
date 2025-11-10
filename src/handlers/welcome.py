from main import bot


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет, я Vojagantoj.\nПросто напишите мне что-нибудь, и я это повторю!'
    await bot.reply_to(message, text)
