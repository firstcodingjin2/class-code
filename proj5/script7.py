from flask import *  
app = Flask(__name__)  

@app.route('/')  
def message():  
    return """
<html>
    <body>
        <h1>안녕, 웹사이트에 오신 것을 환영합니다</h1>
    </body>
</html>
"""

if __name__ == '__main__':  
   app.run(debug = True)  
