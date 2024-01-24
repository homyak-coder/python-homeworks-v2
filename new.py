from flask import Flask

app = Flask(__name__)

def get_Word (word):
    return word + 'NEW'

@app.route("/")
def index():
    return "This is a new function"%(get_Word('Lalala'))

if __name__ ==  "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

    