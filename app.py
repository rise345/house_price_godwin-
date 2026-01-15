from flask import Flask, request, render_template
from model import model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        size = float(request.form["size"])
        result = model.predict([[size]])[0]
    return render_template("index.html", result=result)

app.run(debug=True)
