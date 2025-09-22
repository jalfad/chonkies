from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/our_cookies")

def our_cookies():
    return render_template("our_cookies.html")

if __name__ == "__main__" :
    app.run(debug = True)

