from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/preview/<name>')
def success(name):
    return f"<h1>Hello {name}, your Order has been recorded. You shall receive a bill shortly.</h1>"

@app.route('/order',methods = ['POST','GET'])
def total():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success',name = user))

    else:
        user = request.args.get('name')
        return redirect(url_for('success',name = user))
            
            




if __name__ == "__main__":
    app.run(debug = True)	