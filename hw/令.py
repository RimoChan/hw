from . import 送


def t(from_, chat):
    tt = '射精管理员'
    送.授予头衔(chat['id'], from_['id'], tt)
    送.字(chat['id'], f'好，你现在已经是{tt}了！')


def default(from_, chat):
    送.字(chat['id'], '不行，那里不行！')
