from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "Hi Backend Developer"

@app.route("/home")
def home():
    return "home Page"


if __name__=="__main__":
    app.run(debug=True)
