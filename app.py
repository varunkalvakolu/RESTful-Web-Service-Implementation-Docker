from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./airlines.json').read())
data=jData["Airlines"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return "Welcome! I hope it works!"

# Returns JSON which containes all restaurants
@app.route('/getairlines/')
def restaurants_all():
    return render_template("index.html",items=data)

# Returns restaurants JSON which matches the id
@app.route('/getairlines/<string:id>/')
def restaurants_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the restaurants JSON with particualr food type
@app.route('/getairlines/gate/<string:gate>/')
def restaurants_by_type(gate=''):
    myList=[]
    for element in data:
        if element["gate"].lower() == gate.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
