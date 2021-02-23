from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is my first flask page <h1>Hola!</h1>"


if __name__=="__main__":
    app.run()
