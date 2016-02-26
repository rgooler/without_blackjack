# vim:fileencoding=utf8
from flask import Flask

# Flask App
app = Flask(__name__)
app.secret_key = ''

from myapp import views


if __name__ == "__main__":
    pass
