from bottle import Bottle

class CQHttp():
  def __init__(self):
    handlers = defaultdict(dict)
    app = Bottle()
    app.post('/')(self._handle)
    self._handlers = handlers
    self._app = app
