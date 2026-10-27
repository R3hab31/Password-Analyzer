from flask import Flask, render_template, request
from analyzer import analyze

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["POST"])
def check():
    pwd=request.form["password"]
    strength,sugg=analyze(pwd)
    if strength=="Weak":
        color="red"
    elif strength=="Medium":
        color="orange"
    else:
        color="limegreen"
        
    return render_template(
        "index.html",
        strength=strength,
        sugg=sugg,
        color=color)

if __name__=="__main__":
    app.run(debug=True)
