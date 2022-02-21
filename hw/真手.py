import re
import requests

from . import 送
from . import 令


def message(from_, chat, text=None, new_chat_members=None, new_chat_title=None, entities=()):
    def 太阳交换(s, 系数=1/50):
        import bnhhsh
        d = re.findall('[a-zA-Z]+', s)
        dp = {x: bnhhsh.yndp(x.lower()) for x in d}
        return {k: a for k, (a, b) in dp.items() if b < len(k)*系数 and k != a and len(k)>1}

    print('from:', from_)
    print('chat:', chat['type'])
    print(text)
    print(new_chat_members)

    实体表 = {}
    if text:
        for i in entities:
            实体表.setdefault(i['type'], []).append(text[i['offset']:i['offset']+i['length']])
    要 = bool(chat['type'] == 'private' or '@childponbot' in 实体表.get('mention', []))
    print('要:', 要)
    print('========\n')

    for cmd in 实体表.get('bot_command', [])[:1]:
        res = re.findall('/(.*?)@(.*?)$', cmd)
        print(res)
        if len(res) != 1:
            continue
        a, b = res[0]
        if b!='childponbot':
            continue
        参数 = text.split()[1:]
        f = {
            't': 令.t,
        }.get(a, 令.default)
        f(from_, chat, *参数)

    if new_chat_members:
        送.字(chat['id'], '新幼女来了！')
        送.上床(chat['id'])
        return
    if new_chat_title:
        送.字(chat['id'], f'{new_chat_title}，好！')
        return

    if 要:
        if text:
            _text = text.replace('@childponbot', '')
            if t:=太阳交换(_text, 9):
                送.纯字(chat['id'], '\n'.join([f'{k}: {v}' for k, v in t.items()]))
        if text and '奸' in text:
            送.字(chat['id'], '奸！')
        else:
            送.字(chat['id'], '好！')
        return
    else:
        if text:
            if t:=太阳交换(text):
                送.纯字(chat['id'], '\n'.join([f'{k}: {v}' for k, v in t.items()]))
                return
