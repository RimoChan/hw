import json
import time
import random

import requests

from . import 全局
from . import unvcode


class TG坏(Exception): ...


class 器类:
    def __getattr__(self, x):
        def f(**d):
            resp = requests.get(全局.地址 + x, params=d)
            if resp.status_code!=200:
                raise TG坏(json.loads(resp.content)['description'])
        return f
器 = 器类()


def 上床(chat_id):
    器.sendSticker(chat_id=chat_id, sticker='CAACAgUAAxkBAAMSYRkYC6d7rgeSouJ7OMKvnXuq5YEAAscCAAJbiYFUPPJUAsGvBMkgBA')


def 纯字(chat_id, text, reply_to_message_id=None):
    text = unvcode.simple_unvcode(text)
    器.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=reply_to_message_id)


def 字(chat_id, text, reply_to_message_id=None):
    if random.random()<0.1:
        import yinglish
        text = yinglish.chs2yin(text)
    纯字(chat_id, text, reply_to_message_id=reply_to_message_id)


def 授予头衔(chat_id, user_id, custom_title):
    器.promoteChatMember(chat_id=chat_id, user_id=user_id, can_manage_chat=True)
    for _ in range(3):
        try:
            器.setChatAdministratorCustomTitle(chat_id=chat_id, user_id=user_id, custom_title=custom_title)
        except TG坏 as e:
            time.sleep(2)
        else:
            break
