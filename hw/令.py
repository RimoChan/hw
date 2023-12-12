from . import 送


def t(from_, chat, message_id, 名字='射精'):
    tt = f'{名字}管理员'
    送.授予头衔(chat['id'], from_['id'], tt)
    送.字(chat['id'], f'好，你现在已经是{tt}了！', reply_to_message_id=message_id)


def default(from_, chat, message_id, *li):
    送.字(chat['id'], '不行，那里不行！', reply_to_message_id=message_id)
