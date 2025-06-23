from bottle import Bottle

class CQHttp():
  def __init__(self):
    self._handlers = defaultdict(dict)
    self._app = Bottle()
    self._app.post('/')(self._handle)
