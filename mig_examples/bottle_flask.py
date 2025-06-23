from flask import Flask

class CQHttp():
  def __init__(self):
    self._handlers = defaultdict(dict)
    self._app = Flask(__name__)
    self._app.route('/', methods=['POST'])(self._handle)
