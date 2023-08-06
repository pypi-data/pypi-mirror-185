import threading
from time import time

from api_analytics.core import log_request
from tornado.web import Application, RequestHandler
from tornado.httputil import HTTPServerRequest


class Analytics(RequestHandler):
    def __init__(self, app: Application, res: HTTPServerRequest, api_key: str):
        super().__init__(app, res)
        self.api_key = api_key
        self.start = time()

    def prepare(self):
        self.start = time()

    def on_finish(self):
        data = {
            'api_key': self.api_key,
            'hostname': self.request.host,
            'ip_address': self.request.remote_ip,
            'path': self.request.path,
            'user_agent': self.request.headers['user-agent'],
            'method': self.request.method,
            'status': self.get_status(),
            'framework': 'Tornado',
            'response_time': int((time() - self.start) * 1000),
        }

        threading.Thread(target=log_request, args=(data,)).start()
        self.start = None
