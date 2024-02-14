from flask import Flask

app = Flask(__name__)

@app.route('/home/<int:age>')
def home(age):
    return "나이 = %d" % age

if __name__ == "__main__":
    app.run(debug=True)