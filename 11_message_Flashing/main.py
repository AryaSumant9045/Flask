from flask import Flask , flash, render_template

app = Flask(__name__)

app.secret_key = "ksldhrp3725owehityopw4eitaseji"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("Hi You just logout", "success")
    return render_template("index.html")

app.run(debug=True)