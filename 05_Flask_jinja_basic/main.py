from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "john":34,
        "Mohan":89,
        "Surbhi":67,
        "Gnni":35
    }
    return render_template("index.html",marks = marks)

app.run(debug=True)

# this is the way to pass variable to a templates in flask
#download jinja snippit flask extension