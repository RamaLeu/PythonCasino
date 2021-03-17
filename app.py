from flask import Flask

from views.Index import Index

app = Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'))

if __name__ == '__main__':
    app.run()
