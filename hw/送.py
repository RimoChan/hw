import random

import requests

from . import 全局
from . import unvcode


def 上床(chat_id):
    resp = requests.get(全局.地址 + 'sendSticker', params={'chat_id': chat_id, 'sticker': 'CAACAgUAAxkBAAMSYRkYC6d7rgeSouJ7OMKvnXuq5YEAAscCAAJbiYFUPPJUAsGvBMkgBA'})
    assert resp.status_code==200


def 纯字(chat_id, text):
    text = unvcode.simple_unvcode(text)
    resp = requests.get(全局.地址 + 'sendMessage', params={'chat_id': chat_id, 'text': text})
    assert resp.status_code==200


def 字(chat_id, text):
    if random.random()<0.1:
        import yinglish
        text = yinglish.chs2yin(text)
    纯字(chat_id, text)
