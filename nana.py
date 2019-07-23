from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   # a=[100,56,77,33,59,88,90]   
    b=[("1min",100),("2min",56),("3min",77),("4min",90),("5min",89),("6min",70),("7min",65)]
    return  render_template('index.html',data=b)

if __name__ == "__main__":
    app.run(debug=True)



