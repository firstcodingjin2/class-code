from flask import *  
app = Flask(__name__)  
app.secret_key = "test123"  
 
@app.route('/')  
def home():  
    return render_template("login/home.html")  
 
@app.route('/login',methods = ["GET", "POST"])  
def login():  
    if request.method == "GET":
        return render_template("login/login_form.html")  
    elif request.method == "POST":  
        session['login_info']=request.form['email']  
        return redirect(url_for('profile'))
    else :
        return redirect(url_for('home'))
 
@app.route('/logout')  
def logout():  
    if 'login_info' in session:  
        session.pop('login_info',None)  
        return render_template('login/logout.html');  
    else:  
        return '<p>user already logged out</p>'  
 
@app.route('/profile')  
def profile():  
    if 'login_info' in session:  
        email = session['login_info']  
        return render_template('login/profile.html',name=email)  
    else:  
        return '<p>Please login first</p>'  
  
if __name__ == '__main__':  
    app.run(debug = True)  