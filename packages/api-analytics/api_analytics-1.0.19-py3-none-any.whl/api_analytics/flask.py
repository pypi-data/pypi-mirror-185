import threading
from time import time
from typing import Callable

from api_analytics.core import log_request
from flask import Flask, Request, Response
from flask_http_middleware import BaseHTTPMiddleware, MiddlewareManager


def add_middleware(app: Flask, api_key: str):
    app.wsgi_app = MiddlewareManager(app)
    app.wsgi_app.add_middleware(Analytics, api_key=api_key)


class Analytics(BaseHTTPMiddleware):
    def __init__(self, api_key: str):
        super().__init__()
        self.api_key = api_key

    def dispatch(self, request: Request, call_next: Callable[[Request], Response]):
        start = time()
        response = call_next(request)

        data = {
            'api_key': self.api_key,
            'hostname': request.host,
            'ip_address': request.remote_addr,
            'path': request.path,
            'user_agent': request.headers['user-agent'],
            'method': request.method,
            'status': response.status_code,
            'framework': 'Flask',
            'response_time': int((time() - start) * 1000),
        }
        
        threading.Thread(target=log_request, args=(data,)).start()
        return response
