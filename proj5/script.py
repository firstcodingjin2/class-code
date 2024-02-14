from flask import Flask  
  
app = Flask(__name__)  # Flask 클래스 객체 생성   
 
@app.route('/')  # 데코레이터는 URL 매핑 정의   
def home():  
    return "first flask website";  
  
if __name__ =='__main__':  
    app.run(debug=True)  