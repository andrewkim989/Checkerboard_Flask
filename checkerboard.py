from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def check():
    return render_template("cindex.html", row = 8, column = 8)

@app.route('/<x>/<y>')
def checktwo(x, y):
    return render_template("cindex.html", row = int(x), column = int(y))

if __name__=="__main__":
    app.run(debug = True)