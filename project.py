from flask import Flask , request , jsonify


app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'contact': '3053602936',
        'name' : 'Raed'
    },
    {
        'id': 2,
        'contact': '9886533678',
        'name' : 'Ankita'
    }
]


@app.route("/")
def hello():
    return "Hello World!!"



@app.route("/add-data" , methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error", 
            "message": "please provide task"
        })

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['Name'],
        'contact': request.json.get('Contact', ""),
    }

    tasks.append(task)
    return jsonify({
        "status": "success", 
        "message" : "Contact added success"
    })


@app.route("/get-data")

def getTask():
    return jsonify({
        "data": tasks, 
    })





if(__name__) == "__main__":
    app.run(debug=True)







