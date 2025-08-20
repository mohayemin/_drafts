import log
from bottle import Bottle
app = Bottle()

log.debug('init app')

@app.route('/login', method='POST')
def do_login():
  check_login()
