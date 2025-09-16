from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "john":91,
        "Mohan":89,
        "Surbhi":67,
        "Gnni":35,
        "harry":100
    }
    return render_template("index.html",marks = marks)

app.run(debug=True)