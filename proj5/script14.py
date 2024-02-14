from flask import *  
  
app = Flask(__name__)  
 
@app.route('/cookie')  
def cookie():  
    res = make_response("<h1>cookie is set</h1><a href=\"cookie/view\">view</a>")  
    res.set_cookie('foo','test123')  
    return res  
 
@app.route('/cookie/view')  
def cookie_view():      
    return request.cookies.get('foo') 
  
if __name__ == '__main__':  
    app.run(debug = True)  