from flask import Flask

app = Flask(__name__)

def get_equal (a, b, c):
    return a == (b + c)

@app.route("/")
def index():
    return "This is a new function"

if __name__ ==  "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

    