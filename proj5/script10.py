from flask import *  

app = Flask(__name__)  
  
@app.route('/cal/<int:num>')  
def message(num):  
      return render_template('message_2.html', num=num)        

if __name__ == '__main__':  
   app.run(debug=True)  
