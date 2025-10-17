from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "Hi Backend Developer"

@app.route("/home")
def home():
    return "home Page"

@app.route("/about")
def about():
    return "Hi This is the Test Site"

@app.route("/bet")
def bet():
    return "let's bet on your luck"



if __name__=="__main__":
    app.run(debug=True)
