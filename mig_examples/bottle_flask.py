import log
from flask import Flask
app = Flask(__name__)

log.info('init app')

@app.route('/login', 
           methods=['POST'])
def do_login():
  check_login() 
  