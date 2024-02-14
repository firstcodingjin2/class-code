from flask import *  
app = Flask(__name__)  
  
@app.route('/login', methods=['GET'])  
def login():  
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    if uname == "son" and passwrd == "1234":  
        return "Welcome %s" % uname  
    else :
        return 'error!!!'
   
if __name__ == '__main__':  
   app.run(debug=True)
