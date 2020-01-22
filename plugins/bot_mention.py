# -*- coding: utf-8 -*-
from slackbot.bot import respond_to

@respond_to('test')
def say_bot(message):
    message.reply('testのお返事成功です')