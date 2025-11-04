from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
 
@app.route("/move_forward", methods=["POST"])
def move_forward():
    if request.method == "POST":
        print(request.form)
        return ('', 204)

@app.route("/move_backward", methods=["POST"])
def move_backward():
    if request.method == "POST":
        print(request.form)
        return ('', 204)

@app.route("/move_left", methods=["POST"])
def move_left():
    if request.method == "POST":
        print(request.form)
        return ('', 204)

@app.route("/move_right", methods=["POST"])
def move_right():
    if request.method == "POST":
        print(request.form)
        return ('', 204)

@app.route("/throttle", methods = ["POST"])
def throttle():
    if request.method == "POST":
        print(request.form)
        return ('', 204)

app.run(host="127.0.0.1", port=5001, debug= True)