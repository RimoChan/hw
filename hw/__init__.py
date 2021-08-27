import json
import logging

import azure.functions as func

from . import 手


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.warning(repr([req.url, req.method, dict(req.headers), req.get_body(), req.params]))
        手.手(json.loads(req.get_body()))
        return func.HttpResponse(
            '233',
            headers={},
            status_code=200,
        )
    except Exception as e:
        logging.exception(e)
        logging.warning(repr([req.url, req.method, req.headers, req.params]) + '坏了')
        return response(f'运行错误: {repr(e)}', status_code=500)


def response(x, status_code=200, headers={}) -> func.HttpResponse:
    新x = json.dumps(x, ensure_ascii=False)
    return func.HttpResponse(新x, status_code=status_code, headers=headers)
