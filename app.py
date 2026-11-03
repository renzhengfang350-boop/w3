from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/", methods=["POST","GET"])
def home():
    if request.method =="POST":
        topic = request.form.get("topic","")
        print("我選擇的主題:",topic)

    return render_template("index.html",topic=topic)
if __name__ =="__main__":
    app.run(debug=True,port=5001)
