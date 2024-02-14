from flask import *  
import os

app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = os.getcwd()+'\\img\\'
print('upload_folder', app.config['UPLOAD_FOLDER'])

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename)) 
        return render_template("success.html", name = f.filename)  

if __name__ == '__main__':      
    app.run(debug = True)  
