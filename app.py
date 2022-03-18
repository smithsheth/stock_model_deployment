from flask import Flask,render_template,request
import pred as p

app=Flask(__name__)


@app.route("/",methods =["GET","POST"])
def hello():
    predict1=""
    if request.method == "POST":
    
        stockname=request.form["stockname"]
        predict= p.main_prediction(stockname)
        predict1=predict

    return render_template("index.html",prediction = predict1)


"""@app.route("/sub",methods =["POST"])
def submit():
    if request.method == "POST":
       name=request.form["username"]
    return render_template("sub.html",n=name)"""   
if __name__ =="__main__":
    app.run(debug=True)