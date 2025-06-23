from flask import Flask

class CQHttp():
  def __init__(self):
    handlers = defaultdict(dict)
    app = Flask(__name__)
    app.route('/', methods=['POST'])(self._handle)
    self._handlers = handlers
    self._app = app
