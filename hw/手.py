import inspect
import logging
import traceback
from . import 真手
from . import 送


def 手(u):
    try:
        try:
            try:
                assert len(u) == 2
                u.pop('update_id')
                (k, d), = u.items()
                if not hasattr(真手, k):
                    return
                f = 真手.__getattribute__(k)
                d['from_'] = d['from']
                a = inspect.getfullargspec(f).args
                d = {k: v for k, v in d.items() if k in a}
                f(**d)
            except 送.TG坏 as e:
                送.字(d['chat']['id'], f'不行！{e.args[0]}！')
        except Exception as e:
            logging.exception(e)
            s = traceback.format_exc()
            送.字(d['chat']['id'], s)
    except Exception:
        logging.exception('23333')
