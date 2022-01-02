from flask import Flask,jsonify, request

# __name__ is a built-in variable which evaluates to the name of the current module
# Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

# File is being run directly. Hence this check. If the file is imported, this evaluates to false.
if (__name__ == "__main__"):
    app.run(debug=True)
