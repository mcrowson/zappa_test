from flask import Flask


app = Flask(__name__)


@app.route('/')
def test(event=None, context=None):
    return 'The server is working'


if __name__ == "__main__":
    app.run(debug=True, port=5151)