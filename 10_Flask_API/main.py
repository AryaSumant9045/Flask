from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={
        "Akash": 89,
        "Ravi": 88,
        "Suraj":78,
        "Tejpal":45,
        "Gourav":44
    }
    values=[1, marks,44 ]
    #return jsonify(marks)
    return jsonify(values)


app.run(debug=True)

#Yeh Flask API hai, kyunki yeh data ko JSON format me dusre apps ke liye provide karti hai, HTML page nahi bhejti.