from flask import *

app = Flask(__name__)
app.secret_key = "abc"

@app.route('/')
def home():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['res_session'] = 'session#1'
    return res;

@app.route('/get')
def getVariable():
    if 'res_session' in session:
        s = session['res_session']
        return make_response("<h1>session variable [ %s ]<h1>" % s)
    else :
        return 'error!!!'

if __name__ == '__main__':
    app.run(debug=True)
