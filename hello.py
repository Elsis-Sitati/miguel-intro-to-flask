from flask import Flask,render_template

# creating an instance of class Flask and storing it in a global variable app
app = Flask(__name__)

# route for index
@app.route('/')
def index():
    return render_template('index.html')

# rout for user
@app.route('user/<name>')
def user(name):
    return render_template('user.html',name=name)

# starting the web server
if __name__ == 'main':
    app.run(debug=True)