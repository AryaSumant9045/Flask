from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name="sumant"
    token = 3400
    if "name" in request.args.keys():   # matlab site mai agr localhost://3000?name=john&token=39509 toh ye kam krega
        name = request.args['name']
    if "token" in request.args.keys():
        token = request.args['token']
        
    return render_template("index.html", name = name , token = token)
 
app.run(debug=True)