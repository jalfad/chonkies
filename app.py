from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/our_cookies")

def our_cookies():
    return render_template("our_cookies.html")

@app.route("/hb.html")

def hb():
    return render_template("hb.html")

@app.route("/sl.html")

def sl():
    return render_template("sl.html")

@app.route("/cc.html")

def cc():
    return render_template("cc.html")

@app.route("/ss.html")

def ss():
    return render_template("ss.html")  

@app.route("/contact")

def con():
    return render_template("contacts.html")

@app.route("/bundles")

def bundles():
    return render_template("bundles.html")

if __name__ == "__main__" :
    app.run(debug = True)



