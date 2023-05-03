from flask import Flask

app = Flask(__name__)


from views.ppt_creator import *

if __name__ == '__main__':
    app.run(host='192.168.0.192',debug=True)