from flask import Flask

app = Flask(__name__)


from views.ppt_creator import *

if __name__ == '__main__':
    app.run(debug=True)