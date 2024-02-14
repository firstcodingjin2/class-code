from flask import *  
app = Flask(__name__)  
  
@app.route('/login', methods=['POST'])  
def login():  
    uname = request.form['uname']  
    passwrd = request.form['pass']  
    if uname == "son" and passwrd == "1234":  
        return "Welcome %s" % uname  
    else :
        return 'error!!!'
   
if __name__ == '__main__':  
   app.run(debug=True)
