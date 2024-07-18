from flask import Flask,render_template,request,session,url_for,flash

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/home')
def home(username=None):
    if username in session:
        return render_template('home.html')
    return render_template('login')

@app.route('/login')
def login():

    return render_template('login.html')



if __name__ == '__main__':
    app.run(port=5001)