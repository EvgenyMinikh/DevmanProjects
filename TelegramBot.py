import ptbot
import os
from pytimeparse import parse


def reply(text):
    def notify(message_id):
        bot.update_message(recipient_id, message_id, "Время вышло")

    def notify_progress(secs_left, id):
        message_body = '''Осталось {sec} секунд
{st}
    '''.format(sec=secs_left, st=render_progressbar(delay, delay - secs_left))
        bot.update_message(recipient_id, id, message_body)

    def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
        iteration = min(total, iteration)
        percent = "{0:.1f}"
        percent = percent.format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        pbar = fill * filled_length + zfill * (length - filled_length)
        return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

    delay = parse(text)
    message_id = bot.send_message(recipient_id, "Таймер установлен на {} секунд".format(delay))

    bot.create_timer(delay, notify, message_id)
    bot.create_countdown(delay, notify_progress, id=message_id)


recipient_id = os.getenv("CHAT_ID")
bot_token = os.getenv("TELEGRAM_TOKEN")

bot = ptbot.Bot(bot_token)
bot.send_message(recipient_id, "На сколько запустить таймер?")
bot.wait_for_msg(reply)