from flask import *  

app = Flask(__name__)  

student_data = {
    1:{"name":"손흥민","score": {"국어": 80, "수학" : 100}},
    2:{"name":"이강인","score": {"국어" :90, "수학" : 80}}
}

@app.route('/')
def index():
    return render_template("index.html", template_students = student_data)
  
@app.route('/students/<int:id>')  
def message(id):  
      return render_template('students.html', 
                             s_name = student_data[id]["name"],
                             s_score = student_data[id]["score"])        

if __name__ == '__main__':  
   app.run(debug=True)  
